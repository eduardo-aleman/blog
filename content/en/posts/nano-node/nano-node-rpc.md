---
title: "Useful RPC Commands for a Nano Node"
description: "Summary of common actions available through the JSON-RPC API for a self-hosted Nano node."
date: 2025-05-27
categories:
  - nano
  - blockchain
  - rpc
  - administration
draft: false
---

# Useful RPC Commands for a Nano Node

Once your Nano node is running and port `7076` is open, you can interact with it using HTTP POST requests to the JSON-RPC API. Below is a collection of useful commands organized by category.

---

## 🔍 Node Status

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

## 🧭 Network & Peers

```bash
curl -d '{ "action": "peers" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

```bash
curl -d '{ "action": "peer_add", "address": "peering.nano.org", "port": "7075" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🔐 Wallets & Accounts

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

## 💬 Account Information

```bash
curl -d '{ "action": "account_balance", "account": "<ACCOUNT_ID>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

```bash
curl -d '{ "action": "account_info", "account": "<ACCOUNT_ID>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🛠 Administration

```bash
curl -d '{ "action": "representatives_online" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

```bash
curl -d '{ "action": "bootstrap_any" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🗂 References

- [Official Nano RPC Documentation](https://docs.nano.org/commands/rpc-protocol/)
- [NanoLooker Explorer](https://nanolooker.com/)
- [Nano Node Directory](https://nanonodes.io/)

---

## ⚠️ Disclaimer

This guide is intended to document practical JSON-RPC commands for interacting with a self-hosted Nano node. While its contents have been carefully reviewed, it **may not function identically across all environments** or configurations.

**Use at your own risk.** Always make backups before altering configurations or handling private keys.

For support or questions, refer to the [Nano documentation](https://docs.nano.org/commands/rpc-protocol/) or the Nano community forums.
