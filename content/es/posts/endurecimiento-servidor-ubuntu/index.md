---
translationKey: ubuntu-hardening
title: "Endurecimiento de un servidor Ubuntu: pasos esenciales"
date: 2025-05-29
draft: false
categories:
  - Seguridad
  - Tecnología 
  - Referencia
tags: 
  - SSH
  - UFW 
  - Fail2Ban
  - Linux 
  - Servidores
  - Ubuntu
description: "Guía práctica para asegurar un servidor Ubuntu: desde deshabilitar el acceso root hasta configurar un ProxyJump reverso y autenticación en dos pasos."
translationKey: ubuntu-hardening
---

El endurecimiento de un servidor Ubuntu es una práctica esencial para asegurar cualquier infraestructura expuesta a Internet. A continuación se detallan los pasos fundamentales para aumentar la seguridad, con una tabla-resumen de efectos por cada configuración aplicada.

## 🔐 Paso 1: Crear un usuario seguro y usar llaves SSH

Deshabilitar el acceso directo del usuario `root` y utilizar un usuario limitado con llaves SSH mejora la trazabilidad y elimina uno de los vectores de ataque más comunes.

```bash
# Crear y asignar usuario al grupo sudo
adduser secureuser
usermod -aG sudo secureuser
```

Luego, copiar tu llave pública al servidor:

```bash
# SSH command
ssh-copy-id secureuser@tu-servidor
```

## 🔐 Paso 2: Deshabilitar el acceso SSH para root

Editar el archivo `/etc/ssh/sshd_config`:

```bash
# Comando
PermitRootLogin no
```

## 🔐 Paso 3: Deshabilitar autenticación por contraseña

Para forzar el uso de llaves SSH:

```bash
# Comando
PasswordAuthentication no
```

Recuerda reiniciar el servicio:

```bash
# SSH command
sudo systemctl restart ssh
```

## 🔁 Paso 4: Configurar actualizaciones automáticas de seguridad

Instala y configura:

```bash
# Instalar actualizaciones automáticas de seguridad
sudo apt install unattended-upgrades
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

Esto garantiza que tu sistema reciba parches de seguridad sin intervención manual.

## 📦 Paso 5: Instalar fail2ban

Fail2ban bloquea IPs que realizan intentos de fuerza bruta contra servicios como SSH:

```bash
# Configurar fail2ban para proteger el servicio SSH
sudo apt install fail2ban
sudo systemctl enable --now fail2ban
```

Para un jail básico de SSH:

```ini
# /etc/fail2ban/jail.local
[sshd]
enabled = true
```

## 🔄 Paso 6: Configurar SSH ProxyJump reverso (bastión)

Desde tu máquina local (por ejemplo, tu Mac), puedes configurar `~/.ssh/config` para acceder al servidor privado a través de un bastión:

```ssh
Host nodo-privado
    HostName 10.0.0.3
    User secureuser
    ProxyJump bastion

Host bastion
    HostName 123.456.789.000
    User secureuser
```

## 📊 Paso 7: Monitoreo con Uptime Kuma

Uptime Kuma es una herramienta moderna de monitoreo de disponibilidad con dashboard web:

```bash
# Ejecutar contenedor de Uptime Kuma
docker run -d --restart=always -p 3001:3001 \
-v uptime-kuma:/app/data --name uptime kuma uptimekuma/uptime-kuma
```

Accede a `http://tu-ip:3001` para configurarlo.

## 📜 Paso 8: Script para rotar llaves SSH

Crea un script en `/usr/local/bin/rotate_ssh.sh`:

```bash
#!/bin/bash
USER="secureuser"
KEY_DIR="/home/$USER/.ssh"
NEW_KEY="$KEY_DIR/id_ed25519_new"
ssh-keygen -t ed25519 -f "$NEW_KEY" -N ""
cat "$NEW_KEY.pub" >> "$KEY_DIR/authorized_keys"
echo "Llave nueva agregada. Borra manualmente la anterior tras verificar acceso."
```

## 🔐 Paso 9: Activar autenticación en dos pasos (2FA) con Google Authenticator

```bash
# Configurar autenticación 2FA con Google Authenticator
sudo apt install libpam-google-authenticator
google-authenticator
```

Luego, edita `/etc/pam.d/sshd` y agrega al principio:

```
auth required pam_google_authenticator.so
```

Y en `/etc/ssh/sshd_config`:

```bash
# Comando
ChallengeResponseAuthentication yes
```

Reinicia el servicio:

```bash
# SSH command
sudo systemctl restart ssh
```

---

## Resumen

| Paso                            | Efecto                                                     |
|---------------------------------|------------------------------------------------------------|
| `secureuser` + llaves SSH       | Reemplaza acceso root directo                              |
| `PermitRootLogin no`            | Evita ataques a la cuenta root                             |
| `PasswordAuthentication no`     | Solo autenticación por llave                               |
| UFW                             | Limita los puertos accesibles                              |
| Timeout & retries en SSH        | Evita fuerza bruta lenta                                   |
| Fail2ban                        | Bloqueo automático por intentos fallidos                   |
| ProxyJump                       | SSH seguro y restringido desde bastión                     |
| Actualizaciones automáticas     | Cierra vulnerabilidades sin intervención manual            |
| Uptime Kuma                     | Supervisión visual de servicios                            |
| Rotación de llaves SSH          | Mejora la higiene de claves de acceso                      |
| Google Authenticator            | Añade segundo factor de autenticación                      |

---

Con estos pasos tendrás una base robusta para un servidor seguro y mantenible. Para aumentar la protección aún más, puedes integrar herramientas de auditoría como `Lynis`, escaneos de puertos internos, y segmentación de red.