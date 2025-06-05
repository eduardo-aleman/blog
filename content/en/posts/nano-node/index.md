---
title: "Useful RPC Commands for a Nano Node"
description: "Overview of available actions through the JSON-RPC API on a self-hosted Nano node."
date: 2025-05-27
categories:
- Technology
- Reference
- Blockchain
- Infrastructure
draft: false
tags:
- Nano
- Blockchain
- RPC
- Cryptocurrency
- Node
- Docker
- Ubuntu
- Security
draft: false
translationKey: nano-node
---

Once the Nano node is running and port `7076` is enabled, you can interact with it using HTTP POST requests via the JSON-RPC protocol. Below is a collection of useful commands organized by topic, with inline comments and ready to copy.

---

## 🔍 Node Status

### 🔹 Node version

```bash
# Get node and protocol version
curl -d '{ "action": "version" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Basic telemetry

```bash
# Get general health status of the node
curl -d '{ "action": "telemetry" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Block count

```bash
# Check total number of blocks on the network
curl -d '{ "action": "block_count" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🧭 Network and Peers

### 🔹 List connected peers

```bash
# View all peers currently connected to the node
curl -d '{ "action": "peers" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Add a peer manually

```bash
# Manually add a peer to the node's connection list
curl -d '{ "action": "peer_add", "address": "peering.nano.org", "port": "7075" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🔐 Accounts and Wallets

### 🔹 List existing wallets

```bash
# Show all wallets in the local node
curl -d '{ "action": "wallet_list" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Create a new wallet

```bash
# Generate a new empty wallet
curl -d '{ "action": "wallet_create" }' -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Create an account in a wallet

```bash
# Create a new account from the given wallet
curl -d '{ "action": "account_create", "wallet": "<WALLET_ID>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Add a private key to a wallet

```bash
# Import a private key into an existing wallet
curl -d '{ "action": "wallet_add", "wallet": "<WALLET_ID>", "key": "<PRIVATE_KEY>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 💬 Account Information

### 🔹 Check balance

```bash
# Get the available balance of an account
curl -d '{ "action": "account_balance", "account": "<ACCOUNT_ID>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Account details

```bash
# Get general account info (open block, representative, etc.)
curl -d '{ "action": "account_info", "account": "<ACCOUNT_ID>" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🛠 Administration

### 🔹 Online representatives

```bash
# View list of connected and online representatives
curl -d '{ "action": "representatives_online" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

### 🔹 Manual bootstrap

```bash
# Start a bootstrap from any available source
curl -d '{ "action": "bootstrap_any" }' \
     -H "Content-Type: application/json" http://127.0.0.1:7076
```

---

## 🗂 Resources

- [Official RPC Documentation](https://docs.nano.org/commands/rpc-protocol/)
- [NanoLooker Explorer](https://nanolooker.com/)
- [Public Node Directory](https://nanonodes.io/)

---

_Last updated: 2025-05-27_

---

## ⚠️ Disclaimer

This guide was created to document practical commands to interact with a self-hosted Nano node via its JSON-RPC API. While its content has been carefully verified, **its behavior is not guaranteed in all environments** or custom configurations.

**Use these commands at your own risk.** Always make backups before changing sensitive settings or handling private keys.

For issues or help, refer to the [official Nano documentation](https://docs.nano.org/commands/rpc-protocol/) or the community forums.
