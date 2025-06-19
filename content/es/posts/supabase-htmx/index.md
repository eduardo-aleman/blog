---
title: "Integración de Supabase Edge Functions con HTMX"
date: 2025-06-19T11:00:00-04:00
draft: false
tags:
  - Supabase
  - HTMX
  - Edge Functions
  - Tutorial
categories:
  - Desarrollo Web
---

**Partimos de que ya existen las tablas** `authors`, `texts` y `texts_contents` **con sus triggers de** `updated_at`.

## Prerrequisitos

- **Node.js** (>=14) con `npm` y `npx`.
- **Docker Desktop** en macOS (o Docker Engine en Linux/Windows).
- **Cuenta y proyecto** activos en Supabase.

## Pasos detallados

### 1. Crear la función RPC en la base de datos

1. Accede al **SQL Editor** en Supabase.
2. Ejecuta este script (ajusta los XPaths a tu TEI):

    ```sql
    create or replace function public.rpc_get_text_chapter(
      p_text_id   uuid,
      p_chapter_n text
    )
    returns table (
      original_text       text,
      translation_text    text,
      original_notes      text,
      translator_notes    text,
      translator_name     text,
      original_edition    text,
      translation_edition text
    )
    language sql stable as
    $$
    with 
      ns as (
        select array[
          array['tei','http://www.tei-c.org/ns/1.0'],
          array['xml','http://www.w3.org/XML/1998/namespace']
        ] as xmlns
      ),
      tc as (
        select tei_xml
        from public.texts_contents
        where text_id = p_text_id
      )
    select
      array_to_string(
        xpath(
          format(
            '//tei:div[@type="section" and @n="%s"]/tei:seg[@xml:lang="gr"]/text()',
            p_chapter_n
          ),
          tc.tei_xml,
          ns.xmlns
        ), ''
      ) as original_text,
      array_to_string(
        xpath(
          format(
            '//tei:div[@type="section" and @n="%s"]/tei:seg[@xml:lang="es"]/text()',
            p_chapter_n
          ),
          tc.tei_xml,
          ns.xmlns
        ), ''
      ) as translation_text,
      array_to_string(
        xpath(
          format(
            '//tei:div[@type="section" and @n="%s"]//tei:app/tei:rdg//text()',
            p_chapter_n
          ),
          tc.tei_xml,
          ns.xmlns
        ), E'\n'
      ) as original_notes,
      array_to_string(
        xpath(
          format(
            '//tei:div[@type="section" and @n="%s"]//tei:note[@resp="translator"]/text()',
            p_chapter_n
          ),
          tc.tei_xml,
          ns.xmlns
        ), E'\n'
      ) as translator_notes,
      (xpath(
         '//tei:respStmt[@resp="translator"]/tei:name/text()',
         tc.tei_xml,
         ns.xmlns
       ))[1]::text as translator_name,
      (xpath(
         '//tei:editionStmt/tei:edition/text()',
         tc.tei_xml,
         ns.xmlns
       ))[1]::text as original_edition,
      (xpath(
         '//tei:extent[../@unit="translation"]/text()',
         tc.tei_xml,
         ns.xmlns
       ))[1]::text as translation_edition
    from tc, ns;
    $$;

    grant execute on function public.rpc_get_text_chapter(uuid, text) to authenticated;
    ```

### 2. Instalar y configurar Supabase CLI

Puedes usar **npx** o instalar globalmente:

```bash
# Con npx
npx supabase@latest login
npx supabase@latest link --project-ref <TU_PROJECT_REF>

# Ó globalmente
npm install -g supabase
supabase login
supabase link --project-ref <TU_PROJECT_REF>
```

Para pruebas locales con Docker Desktop:

```bash
supabase start
```

### 3. Crear la Edge Function

1. Crea el directorio local:

    ```
    supabase/functions/text-chapter/index.ts
    ```
2. En `index.ts` pega:

```ts
import { serve } from "https://deno.land/std@0.177.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const sb = createClient(
  Deno.env.get("SUPABASE_URL")!,
  Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!
);

serve(async (req) => {
  const url = new URL(req.url);
  const textId  = url.searchParams.get("textId");
  const chapter = url.searchParams.get("chapter");
  if (!textId || !chapter) {
    return new Response("Missing params", { status: 400 });
  }

  const { data, error } = await sb
    .rpc("rpc_get_text_chapter", { p_text_id: textId, p_chapter_n: chapter })
    .single();

  if (error || !data) {
    return new Response("Error loading chapter", { status: 500 });
  }

  const html = `
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <section>
        <h3 class="text-xl font-semibold mb-2">Original (Griego)</h3>
        <p>${data.original_text}</p>
        <h4 class="mt-4 font-medium">Notas Críticas</h4>
        <pre class="text-sm whitespace-pre-wrap">${data.original_notes}</pre>
        <p class="mt-2 text-xs italic">Edición: ${data.original_edition}</p>
      </section>
      <section>
        <h3 class="text-xl font-semibold mb-2">Traducción (Español)</h3>
        <p>${data.translation_text}</p>
        <h4 class="mt-4 font-medium">Notas del Traductor</h4>
        <pre class="text-sm whitespace-pre-wrap">${data.translator_notes}</pre>
        <p class="mt-2 text-xs italic">Traducido por: ${data.translator_name}</p>
        <p class="text-xs italic">Edición: ${data.translation_edition}</p>
      </section>
    </div>
  `;

  return new Response(html, {
    headers: { "Content-Type": "text/html; charset=utf-8" },
  });
});
```

### 4. Configurar variables de entorno

```bash
export SUPABASE_URL="https://<tu-proyecto>.supabase.co"
export SUPABASE_SERVICE_ROLE_KEY="<tu-service-role-key>"
```

### 5. Desplegar la función

```bash
cd supabase/functions/text-chapter
supabase functions deploy text-chapter
```

Al terminar verás la URL de la función.

### 6. Consumir desde HTMX

En tu HTML, agrega:

```html
<div
  id="chapter-container"
  hx-get="https://<project>.functions.supabase.co/text-chapter?textId={{textId}}&chapter={{chapterN}}"
  hx-trigger="load"
  hx-target="#chapter-container"
  hx-swap="innerHTML"
>
  Cargando capítulo…
</div>
```

### 7. Pruebas y ajustes

- Verifica `textId` y `chapter`.
- Ajusta XPaths.
- Instala Docker Desktop si no lo tenías.

---

**Descargo de responsabilidad**: este tutorial se ofrece “tal cual” sin garantías. Adapta comandos y rutas a tu entorno.
