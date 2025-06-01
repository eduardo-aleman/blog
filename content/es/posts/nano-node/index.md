---
title: Comandos útiles con RPC para un nodo Nano
description: Resumen de acciones disponibles mediante la API JSON-RPC en un nodo Nano
  autoalojado.
date: 2025-05-27
categories:
- nano
- blockchain
draft: false
tags:
- nano
- blockchain
- rpc
- criptomonedas
- nodo
- docker
---

Una vez que el nodo Nano está en ejecución y el puerto `7076` habilitado, es posible interactuar con él mediante peticiones HTTP POST usando el protocolo JSON-RPC. A continuación, se presenta una colección de comandos útiles organizados por temática, con ejemplos comentados y listos para copiar.

---

## 🔍 Estado general del nodo

### 🔹 Versión del nodo

```bash
# Obtener la versión del nodo y del protocolo
curl -d '{ "action": "version" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Telemetría básica

```bash
# Obtener datos generales del estado de salud del nodo
curl -d '{ "action": "telemetry" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Conteo de bloques

```bash
# Ver el número total de bloques en la red
curl -d '{ "action": "block_count" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🧭 Red y Peers

### 🔹 Listar peers conectados

```bash
# Ver todos los peers a los que está conectado el nodo
curl -d '{ "action": "peers" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Agregar manualmente un peer

```bash
# Agregar un peer manualmente a la lista de conexiones
curl -d '{ "action": "peer_add", "address": "peering.nano.org", "port": "7075" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🔐 Cuentas y Wallets

### 🔹 Listar wallets existentes

```bash
# Mostrar todos los wallets en el nodo
curl -d '{ "action": "wallet_list" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Crear un nuevo wallet

```bash
# Generar un nuevo wallet vacío
curl -d '{ "action": "wallet_create" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Crear una cuenta dentro de un wallet

```bash
# Crear una nueva cuenta a partir del wallet especificado
curl -d '{ "action": "account_create", "wallet": "<WALLET_ID>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Agregar clave privada a un wallet

```bash
# Importar una clave privada en un wallet existente
curl -d '{ "action": "wallet_add", "wallet": "<WALLET_ID>", "key": "<PRIVATE_KEY>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 💬 Información de cuentas

### 🔹 Consultar saldo

```bash
# Obtener el saldo disponible de una cuenta
curl -d '{ "action": "account_balance", "account": "<ACCOUNT_ID>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Información detallada de la cuenta

```bash
# Obtener información general de la cuenta (bloque abierto, representante, etc.)
curl -d '{ "action": "account_info", "account": "<ACCOUNT_ID>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🛠 Administración

### 🔹 Representantes activos

```bash
# Ver la lista de representantes conectados y activos
curl -d '{ "action": "representatives_online" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Bootstrap manual

```bash
# Iniciar bootstrap manual desde cualquier fuente disponible
curl -d '{ "action": "bootstrap_any" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🗂 Recursos

- [Documentación oficial de RPC Nano](https://docs.nano.org/commands/rpc-protocol/)
- [Explorador de red NanoLooker](https://nanolooker.com/)
- [Directorio de nodos públicos](https://nanonodes.io/)

---

*Última revisión: 2025-05-27*

---

## ⚠️ Aviso de responsabilidad

Esta guía ha sido elaborada con el objetivo de documentar comandos prácticos para interactuar con un nodo Nano autoalojado mediante su API JSON-RPC. Aunque se ha verificado cuidadosamente su contenido, **no se garantiza su funcionamiento en todos los entornos** o configuraciones particulares.

**El uso de estos comandos es responsabilidad del usuario.** Se recomienda realizar copias de seguridad antes de modificar configuraciones sensibles o manipular claves privadas.

Para dudas o problemas, consulta la [documentación oficial de Nano](https://docs.nano.org/commands/rpc-protocol/) o los foros de soporte de la comunidad.
