---
title: "Explorando Django y Python para sitios de textos clásicos"
date: 2025-06-13
categories:
- Desarrollo web
- Humanidades digitales
- Django
- Python
- Textos clásicos
tags:
- XML
- HTML
- Markdown
- TXT
- Deployment
- Nginx
- Gunicorn
- Postgres
- Certbot
- Seguridad
---

Recientemente he comenzado a aprender **Python 3** y **Django**, explorando su potencial para construir sitios web donde puedan consultarse y descargarse **textos clásicos** en diversos formatos: XML (para anotaciones estructuradas), HTML (para navegación web), Markdown (para edición flexible) y TXT (para portabilidad). Esta iniciativa forma parte de mis proyectos en *Humanidades Digitales*, enfocados en la edición, difusión y preservación del patrimonio textual.

## ¿Por qué Django?

> "Django es un framework web Python de alto nivel que fomenta el desarrollo rápido y un diseño limpio y pragmático. Desarrollado por desarrolladores experimentados, se encarga de gran parte de las complicaciones del desarrollo web, para que puedas concentrarte en escribir tu aplicación sin tener que reinventar la rueda. Es gratuito y de código abierto." — *Documentación oficial*

### Ventajas principales:

- **Seguridad**: Django incluye protecciones integradas contra ataques comunes como XSS, CSRF y SQL injection.
- **Escalabilidad y estabilidad**: Diseñado para aplicaciones grandes y de largo plazo, utilizado por sitios como Instagram y la NASA.
- **Despliegue profesional**: Integra bien con servidores como Nginx y Gunicorn.
- **Gestor de base de datos robusto**: Compatible con PostgreSQL, SQLite y otros.
- **Sistema de plantillas**: Permite separar lógica y presentación con facilidad.

---

## Arquitectura del sitio `corpusabierto`

| Paquete  | Versión | Licencia y origen  | Función principal                                      |
| -------- | ------- | ------------------ | ------------------------------------------------------ |
| Django   | 5.0     | Custom (GitHub)    | Framework web y gestor de base de datos                |
| Nginx    | 1.18.0  | Custom             | Servidor HTTP y proxy inverso                          |
| Gunicorn | 20.1.0  | MIT (GitHub)       | WSGI server para servir Django con eficiencia          |
| Certbot  | 1.21.0  | Apache 2 (GitHub)  | Certificados SSL automáticos de Let's Encrypt          |
| Postgres | 14.18   | PostgreSQL License | Base de datos robusta y escalable                      |
| Postfix  | 3.6.4   | IBM Public License | Agente de transferencia de correo (para alertas, etc.) |

---

## Primeros pasos para editar el sitio

1. **Editar la vista principal**:
   - Archivo: `main/views.py`
   - Funciones como `home()` definen la lógica de cada página.

2. **Editar la plantilla HTML**:
   - Archivo: `main/templates/main/home.html`
   - Ahí puedes incluir texto, enlaces o contenido en HTML, Markdown o JS.

3. **Agregar nuevas rutas**:
   - Archivo: `corpusabierto/urls.py`
   - Cada nueva vista requiere un `path()` registrado.

4. **Gestionar archivos estáticos**:
   - CSS, JS e imágenes van en la carpeta `static/`
   - Comando para recopilar estáticos: `python manage.py collectstatic`

5. **Migraciones y base de datos**:
   - Aplicar migraciones: `python manage.py migrate`
   - Crear nuevas apps: `python manage.py startapp nueva_app`

6. **Subir cambios al servidor**:
   - Usar `git add . && git commit -m "Cambios" && git push`
   - Luego reiniciar Gunicorn y Nginx en el servidor.

7. **Desarrollo local**:
   - Ejecutar `python manage.py runserver` para pruebas.
   - Asegurarse de incluir `127.0.0.1` en `ALLOWED_HOSTS` para evitar errores 400.

---

## Próximos pasos

- Crear una sección para explorar corpus por autor, época o formato.
- Agregar motores de búsqueda textual o por lema.
- Integrar visualizaciones (mapas, gráficos) usando JS o bibliotecas de Python.
- Automatizar los despliegues desde GitHub con WebHooks.
- Incluir validación de TEI/XML con esquemas personalizados.

---
## Lecturas recomendadas

- **[Documentación oficial de Django](https://docs.djangoproject.com/es/5.0/)**  
  Guía completa para aprender y profundizar en Django, desde lo básico hasta temas avanzados como seguridad, despliegue y rendimiento.

- **[Two Scoops of Django](https://www.twoscoopspress.com/collections/books/products/two-scoops-of-django-3-x)**  
  Libro práctico sobre buenas prácticas de diseño con Django, muy recomendado para desarrolladores que buscan mantener sus proyectos escalables.

- **[Deploying Django with Gunicorn and Nginx](https://testdriven.io/blog/django-nginx-gunicorn/)**  
  Tutorial paso a paso sobre cómo configurar un servidor de producción usando Gunicorn y Nginx. Muy útil para entender los componentes involucrados.

- **[Let's Encrypt + Certbot](https://certbot.eff.org/)**  
  Página oficial del proyecto Certbot, con guías para instalar certificados SSL gratuitos en servidores con Nginx o Apache.

- **[PostgreSQL Documentation](https://www.postgresql.org/docs/)**  
  Manual oficial del sistema de base de datos PostgreSQL, ideal si planeas escalar tu aplicación o trabajar con datos estructurados complejos.

- **[Digital Humanities and the Web](https://dhdebates.gc.cuny.edu/read/untitled/section/6b7b7c4d-e7ba-41f1-9c7f-91c8f2b4d0e3)**  
  Artículo de *Debates in the Digital Humanities* que explora el potencial de las tecnologías web para proyectos académicos en humanidades.

---

Este es solo el comienzo de un proyecto mayor para difundir y trabajar textos clásicos con tecnologías modernas. Al combinar **seguridad, escalabilidad y libertad de diseño**, Django me permite construir un entorno robusto y personalizable para *corpusabierto.com*.

---

> **Disclaimer**: Este proyecto se encuentra en fase exploratoria y educativa. Las configuraciones descritas reflejan decisiones de aprendizaje, no necesariamente recomendaciones definitivas de producción. El sitio *corpusabierto.com* puede evolucionar conforme se desarrollen nuevas herramientas o se adquieran nuevas competencias.
