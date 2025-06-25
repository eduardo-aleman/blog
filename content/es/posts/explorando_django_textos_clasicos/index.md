---
title: "Explorando Django y Python para sitios de textos clásicos"
date: 2025-06-13
draft: true
categories:
- Desarrollo web
- Humanidades digitales
- Django
- Python
- Textos clásicos
- Corpus Abierto
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

### Ventajas principales

- **Seguridad**: Django incluye protecciones integradas contra ataques comunes como XSS, CSRF y SQL injection.
- **Escalabilidad y estabilidad**: Diseñado para aplicaciones grandes y de largo plazo, utilizado por sitios como Instagram y la NASA.
- **Despliegue profesional**: Integra bien con servidores como Nginx y Gunicorn.
- **Gestor de base de datos robusto**: Compatible con PostgreSQL, SQLite y otros.
- **Sistema de plantillas**: Permite separar lógica y presentación con facilidad.

A continuación una breve lista del software que utilizo en mi servidor Ubuntu.

---

## 1. Servidor Web y Aplicaciones

Este es el software principal que sirve mi aplicación Django.

* **nginx**: Un servidor web de alto rendimiento y proxy inverso. Se utiliza para recibir las peticiones de los visitantes y servirlas directamente (para archivos estáticos como CSS y imágenes) o pasarlas a tu aplicación Django (a través de Gunicorn).
* **gunicorn**: (Green Unicorn) Es un servidor WSGI (Web Server Gateway Interface) para Python. Actúa como intermediario entre Nginx y tu aplicación Django. Gunicorn gestiona los procesos de la aplicación para que pueda manejar múltiples peticiones simultáneamente.
* **certbot**: Una herramienta esencial para obtener e instalar automáticamente certificados SSL/TLS de Let's Encrypt. Esto permite que tu sitio funcione con HTTPS, cifrando el tráfico entre los usuarios y tu servidor.
* **postgresql / postgresql-14**: Un potente sistema de gestión de bases de datos relacionales de código abierto. Tu aplicación Django probablemente utiliza esta base de datos para almacenar y recuperar datos (usuarios, publicaciones, etc.).
* **python3**: La versión principal del intérprete de Python instalada en el sistema, que es el lenguaje en el que está escrito Django.
    * `python3-pip`: El gestor de paquetes para Python. Se usa para instalar librerías y dependencias que tu proyecto Django necesita (como Django, Psycopg2, etc.).
    * `python3-venv`: Herramienta para crear entornos virtuales aislados. Es una buena práctica usarla para que las dependencias de tu proyecto no entren en conflicto con las del sistema.
    * `python3-psycopg2`: Un adaptador de base de datos de PostgreSQL para Python. Permite que tu aplicación Django se comunique con la base de datos PostgreSQL.
    * El resto de paquetes `python3-*` son librerías y dependencias, muchas de ellas necesarias para que `certbot` y otras herramientas de Python funcionen correctamente.

---

## 2. Gestión del Sistema y Core Utilities

Estos son los componentes fundamentales que hacen que el sistema operativo en mi servidor funcione.

* **apt / dpkg**: El sistema de gestión de paquetes de Debian/Ubuntu. `apt` es la herramienta de alto nivel que usas para instalar, actualizar y eliminar software (`sudo apt install ...`), mientras que `dpkg` es el backend que gestiona los paquetes `.deb`.
* **systemd**: El sistema de inicio y gestor de servicios para Linux. Es responsable de iniciar el sistema, gestionar los servicios (como Nginx, Gunicorn, PostgreSQL) y registrar los eventos del sistema.
* **sudo**: Permite a los usuarios autorizados ejecutar comandos como superusuario (root), lo cual es necesario para tareas administrativas.
* **bash**: El intérprete de comandos por defecto. Es la terminal que usas para interactuar con el servidor.
* **coreutils / util-linux**: Colecciones de herramientas básicas de línea de comandos de GNU/Linux, como `ls`, `cp`, `mv`, `rm`, `mount`, `fdisk`, etc.
* **cron**: Un demonio para ejecutar tareas programadas. Se usa para automatizar tareas repetitivas, como copias de seguridad o la renovación de certificados SSL.
* **build-essential / gcc / g++ / make**: Herramientas de compilación. Son necesarias para construir software desde su código fuente. A menudo, las librerías de Python con extensiones en C las necesitan durante la instalación.
* **git**: Sistema de control de versiones distribuido. Esencial para gestionar el código fuente de tu aplicación.

---

## 3. Red y Seguridad

Herramientas para la conectividad de red, la seguridad y el acceso remoto.

* **openssh-server**: Permite la conexión remota segura a tu servidor a través del protocolo SSH (Secure Shell). Así es como te conectas con `ssh eduardo@...`.
* **ufw (Uncomplicated Firewall)**: Una interfaz fácil de usar para gestionar el firewall de Linux (`iptables`). Te permite controlar qué tráfico de red está permitido entrar o salir del servidor.
* **apparmor**: Un módulo de seguridad del kernel de Linux que restringe las capacidades de los programas, limitando el daño potencial en caso de una vulnerabilidad.
* **openssl**: Una biblioteca de criptografía que proporciona funciones de SSL/TLS. Es fundamental para casi toda la comunicación segura en el servidor, incluyendo HTTPS y SSH.
* **fail2ban** (No instalado, pero relacionado): Aunque no está en tu lista, es una herramienta comúnmente usada junto a UFW para bloquear automáticamente direcciones IP que intentan ataques de fuerza bruta.
* **netplan.io**: La herramienta estándar en Ubuntu Server para configurar la red.
* **curl / wget**: Herramientas de línea de comandos para transferir datos desde o hacia un servidor, comúnmente usadas para descargar archivos o probar APIs.

---

## 4. Agentes del Proveedor Cloud y Monitorización

Estos paquetes son específicos de mi proveedor de alojamiento (DigitalOcean).

* **cloud-init**: Se ejecuta durante el primer arranque de una máquina virtual en la nube para configurarla automáticamente (por ejemplo, establecer el nombre de host, añadir claves SSH, etc.).
* **do-agent / droplet-agent**: Agentes de monitorización de DigitalOcean. Recopilan métricas sobre el uso de CPU, memoria y disco de tu Droplet para que puedas ver gráficos en el panel de control de DigitalOcean.
* **htop**: Un visor interactivo de procesos. Es una versión mejorada del comando `top` y es muy útil para ver en tiempo real qué procesos están consumiendo más CPU o memoria.
* **logrotate**: Rota, comprime y elimina los archivos de registro del sistema y de las aplicaciones para evitar que ocupen todo el espacio en disco.
* **sysstat**: Recopila y muestra estadísticas de rendimiento del sistema, como la actividad de la CPU, el disco y la red a lo largo del tiempo.

---

## 5. Kernel de Linux y Módulos

El núcleo del sistema operativo.

* **linux-image-5.15...**: La imagen del kernel de Linux, que es el núcleo del sistema operativo. Gestiona el hardware, los procesos y los recursos del sistema.
* **linux-headers-...**: Los archivos de cabecera del kernel. Son necesarios para compilar módulos del kernel o software que interactúa directamente con él.
* **linux-modules-...**: Módulos que añaden funcionalidades al kernel, como controladores para hardware específico o sistemas de archivos.

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

Este es solo el comienzo de un proyecto mayor para difundir y trabajar textos clásicos con tecnologías modernas. Al combinar **seguridad, escalabilidad y libertad de diseño**, Django me permite construir un entorno robusto y personalizable para *[Corpus Abierto](https://corpusabierto.com)*.

---

> **Disclaimer**: Este proyecto se encuentra en fase exploratoria y educativa. Las configuraciones descritas reflejan decisiones de aprendizaje, no necesariamente recomendaciones definitivas de producción. El sitio *[Corpus Abierto](https://corpusabierto.com)* puede evolucionar conforme se desarrollen nuevas herramientas o se adquieran nuevas competencias.
