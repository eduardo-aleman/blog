---
title: "Origen y evolución de las funciones primitivas recursivas"
description: "Un recorrido histórico desde Skolem hasta Kleene sobre las funciones primitivas recursivas, su definición formal y su importancia en la teoría de la computación."
date: 2025-04-16
categories:
  - computación
  - lógica
  - historia
  - matemáticas
cover:
  image: "portada_funciones_primitivas.webp"
  alt: "Ilustración de bloques apilados junto a notación matemática básica"
  relative: false
  hidden: false
---

Las **funciones primitivas recursivas** son funciones total y computables que se construyen a partir de funciones básicas mediante dos operaciones: composición y recursión primitiva. Son fundamentales en la teoría de la computabilidad y fueron objeto de estudio mucho antes del desarrollo de las máquinas de Turing.

## 🧠 Los inicios: 1923 - Skolem

**Thoralf Skolem** fue el primero en definir formalmente la recursión primitiva en 1923. Lo hizo en el contexto de funciones aritméticas mecánicamente computables, aunque sin usar las funciones "cero", "sucesora" y "proyección" como base explícita.

## ✨ Funciones más allá de lo primitivo: 1928 - Ackermann y Sudan

**Wilhelm Ackermann** y **Gabriel Sudan** demostraron que existen funciones total y computables que **no** pueden ser definidas mediante recursión primitiva. El ejemplo clásico es la **función de Ackermann**, que crece más rápido que cualquier función primitiva recursiva.

## 📚 Sistematización: 1930s-40s - Rózsa Péter

**Rózsa Péter** desarrolló una teoría completa de funciones recursivas y destacó el papel de la recursión primitiva. Escribió el influyente libro *Recursive Functions* en 1951, donde se establece el uso sistemático de funciones iniciales.

## 🔄 Formalización moderna: 1936-1943 - Stephen Kleene

**Stephen Kleene** es el autor clave en la formalización moderna. Introdujo los términos "funciones primitivas recursivas" y definió rigurosamente que pueden ser construidas a partir de:

- La función **cero**: \( Z(n) = 0 \)
- La función **sucesora**: \( S(n) = n + 1 \)
- Las funciones de **proyección**: \( P^n_k(x_1, \dots, x_n) = x_k \)

Usando solo **composición** y **recursión primitiva**, estas tres funciones permiten generar toda la clase de funciones primitivas recursivas.

---

## 📊 Línea del tiempo visual

![Línea del tiempo: funciones primitivas recursivas](linea_tiempo_funciones_primitivas.webp)

Esta línea del tiempo resume el desarrollo histórico:

- **1923**: Skolem introduce la recursión primitiva
- **1928**: Ackermann define una función no primitiva recursiva
- **1930s-40s**: Rózsa Péter sistematiza el estudio
- **1936-43**: Kleene formaliza completamente el concepto

---

Las funciones primitivas recursivas son una piedra angular de la computación formal. Aunque no abarcan todas las funciones computables (como lo demuestra la función de Ackermann), sí representan el subconjunto de funciones que son **totalmente deterministas, acotadas y siempre terminan**.


## 🧱 Las 3 funciones primitivas iniciales

| Función           | Definición                                  | ¿Qué representa?                            |
|-------------------|----------------------------------------------|---------------------------------------------|
| **Cero** \( Z(n) \)      | Siempre devuelve \( 0 \)                         | El concepto de *cero constante*             |
| **Sucesora** \( S(n) \)  | Devuelve \( n + 1 \)                             | El acto de *contar*: sumar uno              |
| **Proyección** \( P^n_k \) | Devuelve el \( k \)-ésimo de \( n \) argumentos | *Seleccionar* datos de entrada               |

---

## 🧠 ¿Por qué son las “reglas más básicas”?

### 1. **Cero: el comienzo absoluto**
Es el **origen numérico**: toda aritmética empieza en algún punto, y ese punto es 0.  
En lógica, representa la **constante más elemental**.

### 2. **Sucesora: el paso mínimo**
Es la **regla para pasar de un número al siguiente**.  
Toda la aritmética natural puede construirse repitiendo esta operación.

### 3. **Proyección: elegir lo que importa**
Permite **elegir un dato de entrada** entre varios.  
Es esencial para combinar funciones y reutilizar argumentos.

---

## 🔄 ¿Qué podemos construir a partir de estas tres?

| Función derivada     | Cómo se construye                                       |
|----------------------|----------------------------------------------------------|
| Suma \( x + y \)      | Por recursión sobre \( y \), usando la sucesora         |
| Multiplicación \( x \cdot y \) | Por recursión sobre \( y \), usando la suma         |
| Potencia \( x^y \)     | Por recursión sobre \( y \), usando la multiplicación  |
| Factorial \( n! \)     | Por recursión sobre \( n \), usando multiplicación     |

Cada una de estas operaciones más complejas se define a partir de las tres funciones iniciales mediante **composición** y **recursión primitiva**.

---

## 🧠 Analogía

> Es como decir que en una lengua natural, todo se puede expresar usando solo:
> - Palabras simples (como “yo”, “uno”, “tú”)
> - Reglas de combinación (“y”, “luego”)
> - Y repeticiones ordenadas

Así también, la aritmética completa puede construirse desde una base **mínima pero suficiente**.

---

## ✅ Conclusión

> Las tres funciones primitivas iniciales son efectivamente los **bloques elementales** de la aritmética computable.  
> Son a la computación lo que los **átomos** son a la materia: todo lo demás se construye a partir de ellos.
