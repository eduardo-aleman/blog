---
translationKey: ubuntu-hardening
title: "Hardening an Ubuntu Server: Essential Steps"
date: 2025-05-29
draft: false
categories: ["security", "servers", "ubuntu"]
tags: ["ssh", "ufw", "fail2ban", "security", "linux"]
description: "Practical guide to securing an Ubuntu server: from disabling root access to setting up reverse ProxyJump and two-factor authentication."
---

Hardening an Ubuntu server is a critical practice to protect any infrastructure exposed to the internet. Below are key steps to strengthen security, including a summary table of each configuration and its effect.

## 🔐 Step 1: Create a secure user and use SSH keys

Disabling direct access to the `root` user and using a limited user with SSH keys improves traceability and removes one of the most common attack vectors.

```bash
adduser secureuser
usermod -aG sudo secureuser
```

Then, copy your public key to the server:

```bash
ssh-copy-id secureuser@your-server
```

## 🔐 Step 2: Disable SSH access for root

Edit the file `/etc/ssh/sshd_config`:

```bash
PermitRootLogin no
```

## 🔐 Step 3: Disable password authentication

To enforce the use of SSH keys:

```bash
PasswordAuthentication no
```

Remember to restart the service:

```bash
sudo systemctl restart ssh
```

## 🔁 Step 4: Set up automatic security updates

Install and configure:

```bash
sudo apt install unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

This ensures your system receives security patches without manual intervention.

## 📦 Step 5: Install fail2ban

Fail2ban blocks IPs that perform brute-force attacks on services like SSH:

```bash
sudo apt install fail2ban
sudo systemctl enable --now fail2ban
```

For a basic SSH jail:

```ini
# /etc/fail2ban/jail.local
[sshd]
enabled = true
```

## 🔄 Step 6: Configure reverse SSH ProxyJump (bastion)

From your local machine (e.g., your Mac), configure `~/.ssh/config` to access a private server through a bastion host:

```ssh
Host private-node
    HostName 10.0.0.3
    User secureuser
    ProxyJump bastion

Host bastion
    HostName 123.456.789.000
    User secureuser
```

## 📊 Step 7: Monitoring with Uptime Kuma

Uptime Kuma is a modern web-based uptime monitoring tool:

```bash
docker run -d --restart=always -p 3001:3001 \
-v uptime-kuma:/app/data --name uptime kuma uptimekuma/uptime-kuma
```

Access it via `http://your-ip:3001` to configure.

## 📜 Step 8: SSH key rotation script

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

## 🔐 Step 9: Enable Two-Factor Authentication (2FA) with Google Authenticator

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

Restart the service:

```bash
sudo systemctl restart ssh
```

---

## Summary

| Step                          | Effect                                                     |
|-------------------------------|-------------------------------------------------------------|
| `secureuser` + SSH keys       | Replaces direct root access                                |
| `PermitRootLogin no`          | Prevents attacks on the root account                       |
| `PasswordAuthentication no`   | Enforces key-based authentication only                     |
| UFW                           | Restricts accessible ports                                 |
| SSH timeout & retries         | Mitigates slow brute-force attacks                         |
| Fail2ban                      | Auto-blocks failed login attempts                          |
| ProxyJump                     | Secure SSH via restricted bastion access                   |
| Automatic updates             | Patches vulnerabilities without manual effort              |
| Uptime Kuma                   | Visual monitoring of services                              |
| SSH key rotation              | Improves credential hygiene                                |
| Google Authenticator          | Adds a second authentication factor                        |

---

With these steps, you'll have a solid baseline for a secure and maintainable server. For even greater protection, consider integrating audit tools like `Lynis`, internal port scanning, and network segmentation.