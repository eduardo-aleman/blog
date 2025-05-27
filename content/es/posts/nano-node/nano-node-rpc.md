---
title: "Comandos útiles con RPC para un nodo Nano"
description: "Resumen de acciones disponibles mediante la API JSON-RPC en un nodo Nano autoalojado."
date: 2025-05-27
categories:
  - nano
  - blockchain
  - rpc
  - administración
draft: false
---

Una vez que el nodo Nano está en ejecución y el puerto `7076` habilitado, es posible interactuar con él mediante peticiones HTTP POST usando el protocolo JSON-RPC. A continuación, se presenta una colección de comandos útiles organizados por temática.

---

## 🔍 Estado general del nodo

```bash
curl -d '{ "action": "version" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

```bash
curl -d '{ "action": "telemetry" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

```bash
curl -d '{ "action": "block_count" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🧭 Red y Peers

```bash
curl -d '{ "action": "peers" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

```bash
curl -d '{ "action": "peer_add", "address": "peering.nano.org", "port": "7075" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🔐 Cuentas y Wallets

```bash
curl -d '{ "action": "wallet_list" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

```bash
curl -d '{ "action": "wallet_create" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

```bash
curl -d '{ "action": "account_create", "wallet": "<WALLET_ID>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

```bash
curl -d '{ "action": "wallet_add", "wallet": "<WALLET_ID>", "key": "<PRIVATE_KEY>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 💬 Información de cuentas

```bash
curl -d '{ "action": "account_balance", "account": "<ACCOUNT_ID>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

```bash
curl -d '{ "action": "account_info", "account": "<ACCOUNT_ID>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🛠 Administración

```bash
curl -d '{ "action": "representatives_online" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

```bash
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
