---
title: "Instalación del Nodo Nano v28.1"
translationKey: nano-node-v28-1
date: 2025-06-04
draft: false
tags: 
    - Nano
    - Criptomonedas
    - Nodo
    - Docker
    - Seguridad
categories: 
    - Blockchain
    - Infraestructura
description: "Guía completa para instalar un nodo Nano versión 28.1 con Docker, configurar una wallet e integrarse a la red."
---

# 🪙 Instalación y Configuración de Nodo Nano (V28.1) en Docker

Este documento detalla el proceso completo de instalación, configuración y activación de un nodo Nano como representative, incluyendo importación de una wallet externa con seed.

---

## ✅ Información general

- **Versión del nodo:** `V28.1`
- **Contenedor:** Docker (`docker compose`)
- **Sistema base:** Ubuntu 24.04 (Noble)
- **Puerto P2P abierto:** `7075 TCP/UDP`
- **Cuenta representativa:**  
  `nano_ie9a...`
- **Wallet ID:**  
  `5D59...`
- **Seed:**  
  `B9D32...`
- **Mnemonic (24 palabras):**  
  `crash rabbit disease then daring nice park salad lamp bridge point human found tortoise paper nerve simple enjoy device add decorate trouble sister vast`

---

## 🐳 Instalación de Docker y Docker Compose

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release

# Clave GPG
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Repositorio para Ubuntu 24.04 (noble)
echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  noble stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalación final
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

---

## 📦 Configuración del contenedor Nano

```bash
mkdir -p ~/nano-node-docker
cd ~/nano-node-docker
```

### `docker-compose.yml`

```yaml
services:
  nano_node:
    image: nanocurrency/nano:V28.1
    container_name: nano_node
    restart: unless-stopped
    ports:
      - "7075:7075/tcp"
      - "7075:7075/udp"
    volumes:
      - ./data:/root/Nano
```

```bash
sudo docker compose up -d
```

---

## 🔐 Importación de wallet y cuenta

### 1. Acceder al contenedor

```bash
sudo docker exec -it nano_node bash
```

### 2. Crear wallet

```bash
nano_node --wallet_create
# Resultado:
# 4D...
```

### 3. Importar seed

```bash
nano_node --wallet_change_seed \
  --wallet=4D... \
  --seed=P6AD...
```

### 4. Crear cuenta derivada (desde el seed)

```bash
nano_node --account_create \
  --wallet=4D...

# Resultado:
# nano_7...
```

---

## 🗳️ Establecer cuenta como Representative

```bash
nano_node --wallet_representative_set \
  --wallet=4D... \
  --account=nano_7...
```

```bash
nano_node --account_representative_set \
  --account=nano_7... \
  --representative=nano_7...
```

---

## 💾 Respaldo manual del archivo `wallets.ldb`

```bash
cp ~/nano-node-docker/data/Nano/wallets.ldb ~/wallets-respaldo.ldb
```

---

## 🧪 Verificación del nodo

```bash
sudo docker logs -f nano_node
sudo docker exec -it nano_node bash
nano_node --diagnostics
```

---

## 📌 Notas

- La wallet importada es completamente funcional dentro del nodo.
- La cuenta ya está registrada como representative.
- El archivo `wallets.ldb` contiene todas las claves derivadas del seed.

---

## Apéndice: Verificación manual del nodo Nano (sin scripts)

### ✅ 1. Verificar que el contenedor está corriendo

```bash
sudo docker ps
```

Debe mostrar una línea como:

```
nanocurrency/nano:V28.1   ...   Up XX minutes ...   nano_node
```

---

### ✅ 2. Ver logs en tiempo real

```bash
sudo docker logs -f nano_node
```

Deberías ver:

```
[monitor] [info] Blocks confirmed: ...
[monitor] [info] Peers: ...
```

---

### ✅ 3. Comprobar conectividad y diagnóstico

```bash
sudo docker exec -it nano_node bash
nano_node --diagnostics
```

---

### ✅ 4. Ver número de bloques

```bash
nano_node --debug_block_count
```

---

### ✅ 5. Ver lista de peers conectados

```bash
nano_node --debug_peers
```

Salida esperada:

```
[::ffff:178.33.122.56]:7075
[::ffff:51.81.243.15]:7075
```

# 🧭 Verificación Manual del Nodo Nano
Última actualización: 2025-06-05 03:37:44

Verifica manualmente que el nodo esté activo, sin scripts ni monitoreo externo.

| Nº | Comando                                                                 | Qué verifica                                                | Resultado esperado                                |
|----|-------------------------------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------|
| 1  | `sudo docker ps`                                                        | Que el contenedor esté corriendo                            | Línea con `nano_node` y estado `Up`              |
| 2  | `sudo docker exec -it nano_node tail -n 20 /root/Nano/log/node.log`    | Que el nodo esté generando logs recientes                   | Líneas recientes con actividad (`monitor`, etc.) |
| 3  | `sudo docker exec -it nano_node grep Peers /root/Nano/log/node.log \| tail -n 1` | Que el nodo esté conectado a otros nodos                     | Algo como `Peers: 166 (inbound: 72 ...)`         |

---

## 📝 Recomendación

Realiza esta revisión al menos **una vez al día** si no tienes supervisión automática.


---

Estas verificaciones aseguran que el nodo está:
- ✅ Sincronizado
- ✅ Conectado
- ✅ Operativo
- ✅ Activo en la red Nano

## ⚠️ Aviso de responsabilidad

Esta guía ha sido elaborada con el objetivo de documentar comandos prácticos para interactuar con un nodo Nano autoalojado mediante su API JSON-RPC. Aunque se ha verificado cuidadosamente su contenido, **no se garantiza su funcionamiento en todos los entornos** o configuraciones particulares.

**El uso de estos comandos es responsabilidad del usuario.** Se recomienda realizar copias de seguridad antes de modificar configuraciones sensibles o manipular claves privadas.

Para dudas o problemas, consulta la [documentación oficial de Nano](https://docs.nano.org/) o los foros de soporte de la comunidad.
