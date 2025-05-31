---
title: "Hardening an Ubuntu Server: Essential Steps"
date: 2025-05-31
draft: false
categories: ["security", "servers", "ubuntu"]
tags: ["ssh", "ufw", "fail2ban", "security", "linux"]
description: "A practical guide to securing your Ubuntu server: from disabling root access to configuring ProxyJump and two-factor authentication."
---

Hardening an Ubuntu server is a key step to protect any infrastructure exposed to the internet. Below are essential actions you can take to significantly improve security, with a summary table of each configuration's effects.

## 🔐 Step 1: Create a secure user and use SSH keys

Disable direct root access and use a limited user with SSH keys to enhance traceability and eliminate a common attack vector.

```bash
adduser secureuser
usermod -aG sudo secureuser
```

Then copy your public key to the server:

```bash
ssh-copy-id secureuser@your-server
```

## 🔐 Step 2: Disable SSH access for root

Edit `/etc/ssh/sshd_config`:

```bash
PermitRootLogin no
```

## 🔐 Step 3: Disable password authentication

To enforce key-based login only:

```bash
PasswordAuthentication no
```

Restart SSH:

```bash
sudo systemctl restart ssh
```

## 🔁 Step 4: Enable automatic security updates

Install and configure:

```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

This ensures timely patching without manual intervention.

## 📦 Step 5: Install fail2ban

Fail2ban automatically blocks brute-force login attempts:

```bash
sudo apt install fail2ban
sudo systemctl enable --now fail2ban
```

Basic jail for SSH:

```ini
# /etc/fail2ban/jail.local
[sshd]
enabled = true
```

## 🔄 Step 6: Configure reverse ProxyJump (bastion)

From your local machine (e.g., a Mac), set up `~/.ssh/config`:

```ssh
Host private-node
    HostName 10.0.0.3
    User secureuser
    ProxyJump bastion

Host bastion
    HostName 123.456.789.000
    User secureuser
```

## 📊 Step 7: Monitor with Uptime Kuma

Uptime Kuma is a sleek status monitoring tool with a web dashboard:

```bash
docker run -d --restart=always -p 3001:3001 \
-v uptime-kuma:/app/data --name uptime kuma uptimekuma/uptime-kuma
```

Access it at `http://your-ip:3001`.

## 📜 Step 8: Script to rotate SSH keys

Create a script at `/usr/local/bin/rotate_ssh.sh`:

```bash
#!/bin/bash
USER="secureuser"
KEY_DIR="/home/$USER/.ssh"
NEW_KEY="$KEY_DIR/id_ed25519_new"

ssh-keygen -t ed25519 -f "$NEW_KEY" -N ""
cat "$NEW_KEY.pub" >> "$KEY_DIR/authorized_keys"
echo "New key added. Manually remove the old one after verifying access."
```

## 🔐 Step 9: Enable 2FA with Google Authenticator

```bash
sudo apt install libpam-google-authenticator
google-authenticator
```

Then edit `/etc/pam.d/sshd` and add at the top:

```
auth required pam_google_authenticator.so
```

And in `/etc/ssh/sshd_config`:

```bash
ChallengeResponseAuthentication yes
```

Restart SSH:

```bash
sudo systemctl restart ssh
```

---

## Summary

| Step                           | Effect                                                      |
|--------------------------------|--------------------------------------------------------------|
| `secureuser` + SSH keys        | Replaces direct root access                                  |
| `PermitRootLogin no`           | Blocks root login brute force attempts                       |
| `PasswordAuthentication no`    | Enforces key-only login                                      |
| UFW                            | Restricts open ports                                         |
| SSH timeout & retry limits     | Prevents slow brute-force attempts                           |
| Fail2ban                       | Auto-bans after failed logins                                |
| ProxyJump                      | Enables safe SSH from bastion                                |
| Unattended upgrades            | Keeps system patched                                         |
| Uptime Kuma                    | Visual monitoring                                            |
| SSH key rotation               | Enhances access hygiene                                      |
| Google Authenticator           | Adds two-factor authentication                               |

---

With these steps, you’ll have a solid foundation for a secure and maintainable server. For even stronger security, consider audit tools like `Lynis`, internal port scans, and network segmentation.
