---
title: "Installing Nano Node v28.1"
translationKey: nano-node-v28-1
date: 2025-06-04
draft: false
tags:
   - nano
   - cryptocurrencies
   - node
   - docker
   - security
categories:
   - blockchain
   - infrastructure
description: "A complete guide to installing a Nano node version 28.1 with Docker, setting up a wallet, and integrating into the network."
---


# 🪙 Installing and Configuring Nano Node (V28.1) in Docker


This document details the complete process of installing, configuring, and activating a Nano node as a representative, including importing an external wallet with seed.


---


## ✅ General information


- **Node version:** `V28.1`
- **Container:** Docker (`docker compose`)
- **Basic system:** Ubuntu 24.04 (Noble)
- **P2P port open:** `7075 TCP/UDP`
- **Representative account:** 
 `nano_ie9a...`
- **Wallet ID:** 
 `5D59...`
- **Seed:** 
 `B9D32...`
- **Mnemonic (24 words):** 
 `crash rabbit disease then daring nice park salad lamp bridge point human found tortoise paper nerve simple enjoy device add decorate trouble sister vast`


---


## 🐳 Installing Docker and Docker Compose


```bash
sudo apt update
sudo apt install -and ca-certificates curl gnupg lsb-release


# Clave GPG
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
 sudo gpg --dearmor -the /etc/apt/keyrings/docker.gpg


# Repository for Ubuntu 24.04 (noble)
echo \
 "deb [arch=$(dpkg --print-architecture) \
 signed-by=/etc/apt/keyrings/docker.gpg] \
 https://download.docker.com/linux/ubuntu \
 noble stable" | \
 sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


# Final installation
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```


---


## 📦 Nano Container Configuration


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


## 🔐 Wallet and account import


### 1. Access the container


```bash
sudo docker exec -it nano_node bash
```


### 2. Create wallet


```bash
nano_node --wallet_create
# Result:
# 4D...
```


### 3. Import seed


```bash
nano_node --wallet_change_seed \
 --wallet=4D... \
 --seed=P6AD...
```


### 4. Create a derivative account (from the seed)


```bash
nano_node --account_create \
 --wallet=4D...


# Result:
# nano_7...
```


---


## 🗳️ Set up an account as a Representative


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


## 💾 Manual backup of the `wallets.ldb` file


```bash
cp ~/nano-node-docker/data/Nano/wallets.ldb ~/wallets-backup.ldb
```


---


## 🧪 Node Verification


```bash
sudo docker logs -f nano_node
sudo docker exec -it nano_node bash
nano_node --diagnostics
```


---


## 📌 Notes


-The imported wallet is fully functional within the node.
-The account is already registered as a representative.
-The file`wallets.ldb`contains all the keys derived from the seed.

---


## Appendix: Manual verification of the Nano node (without scripts)


### ✅ 1. Verify that the container is running


```bash
sudo docker ps
```


It should display a line like:


```
nanocurrency/nano:V28.1   ...   Up XX minutes ...   nano_node
```


---


### ✅ 2. View logs in real time


```bash
sudo docker logs -f nano_node
```


You should see:


```
[monitor] [info] Blocks confirmed: ...
[monitor] [info] Peers: ...
```


---


### ✅ 3. Check connectivity and diagnostics


```bash
sudo docker exec -it nano_node bash
nano_node --diagnostics
```


---


### ✅ 4. View number of blocks


```bash
nano_node --debug_block_count
```


---


### ✅ 5. View list of connected peers


```bash
nano_node --debug_peers
```


Expected output:


```
[::ffff:178.33.122.56]:7075
[::ffff:51.81.243.15]:7075
```


# 🧭 Manual Verification of the Nano Node
Last updated: 2025-06-05 03:37:44


Manually verify that the node is up, without scripts or external monitoring.


| No. | Command | What it checks | Expected result |
|----|-------------------------------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------|
| 1  | `sudo docker ps`| That the container is running | Line with`nano_node`and state`Up`              |
| 2  | `sudo docker exec -it nano_node tail -n 20 /root/Nano/log/node.log`| That the node is generating recent logs | Recent lines with activity (`monitor`, etc.) |
| 3  | `sudo docker exec -it nano_node grep Peers /root/Nano/log/node.log \| tail -n 1`| That the node is connected to other nodes | Something like`Peers: 166 (inbound: 72 ...)`         |


---


## 📝 Recommendation


Perform this review at least **once a day** if you don't have automatic supervision.




---


These checks ensure that the node is:
-✅ Synchronized
-✅ Connected
-✅ Operational
-✅ Active on the Nano network





