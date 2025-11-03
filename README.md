# TODO List - Sistema de Gestión de Tareas (TDD & Testing)

## 🧩 Descripción del Proyecto

**TODO List Testing** es un sistema completo de gestión de tareas desarrollado en **Python** aplicando **principios SOLID**, **Clean Code** y el flujo de trabajo **TDD (Test Driven Development)**.
El objetivo es demostrar buenas prácticas de desarrollo y testing, garantizando una **cobertura superior al 80%** y una arquitectura modular mantenible.

### 🎯 Objetivos del Proyecto

* Implementar un sistema de tareas con modelo inmutable y repositorio desacoplado.
* Aplicar **TDD** en cada feature (Red → Green → Refactor).
* Diseñar una arquitectura limpia aplicando los principios **SOLID**.
* Asegurar alta cobertura de tests unitarios e integración.

---

## ⚙️ Tecnologías Utilizadas

* **Python 3.8+**
* **pytest** y **coverage** para testing y métricas.
* **Git / GitHub** para control de versiones.
* **GitHub Actions** para integración continua (CI).
* **VSCode** como entorno recomendado.

---

## 🧱 Estructura del Proyecto

```
todo-list-testing/
├── .github/
│   └── workflows/
│       └── ci.yml        #
├── src/                  # Código fuente del sistema
│   ├── __init__.py
│   ├── task.py           # Modelo Task con validaciones e inmutabilidad
│   └── task_manager.py   # Lógica de gestión de tareas y repositorio
│
├── tests/                # Suite de pruebas unitarias e integración
│   ├── test_task.py
│   └── test_manager.py
│
├── docs/                 # Documentación técnica y diseño
│   └── design.md
│
├── .github/workflows/    # CI/CD con GitHub Actions
│   └── ci.yml
│
├── requirements.txt      # Dependencias del proyecto
├── .gitignore
└── README.md             # Documentación principal
```

---

## 🧠 Arquitectura y Principios SOLID

| Principio                     | Aplicación                                                                   |
| ----------------------------- | ---------------------------------------------------------------------------- |
| **S** (Single Responsibility) | `Task` solo modela y valida datos, `TaskManager` maneja la lógica.           |
| **O** (Open/Closed)           | Enums `Priority` y `Status` pueden ampliarse sin modificar código existente. |
| **L** (Liskov Substitution)   | `TaskRepository` es una interfaz reemplazable por otras implementaciones.    |
| **I** (Interface Segregation) | Cada clase tiene responsabilidades bien definidas.                           |
| **D** (Dependency Inversion)  | `TaskManager` depende de la abstracción `TaskRepository`.                    |

---

## 🚀 Instalación y Configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/xKior/todo-list-testing.git
cd todo-list-testing
```

### 2️⃣ Crear entorno virtual y activar

```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Linux/Mac
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🧪 Ejecución de Tests

### Ejecutar toda la suite de tests

```bash
pytest -v
```

### Ver cobertura de código

```bash
coverage run -m pytest
coverage report -m
```

### Generar reporte HTML de cobertura

```bash
coverage html
# Abre htmlcov/index.html en el navegador
```

---

## 🧰 Flujo de Trabajo TDD

| Fase            | Descripción                                             |
| --------------- | ------------------------------------------------------- |
| 🔴 **Red**      | Escribir un test que falle inicialmente.                |
| 🟢 **Green**    | Escribir el código mínimo necesario para pasar el test. |
| 🔵 **Refactor** | Mejorar el código sin romper los tests existentes.      |

Ejemplo:

```bash
# Escribir test
pytest -v
# Implementar código hasta que pase
# Refactorizar y volver a probar
```

---

## 🧬 Integración Continua (CI)

El proyecto incluye un workflow automatizado en `.github/workflows/ci.yml` que ejecuta **pytest** y **coverage** en cada *push* o *pull request*.

### CI Workflow Simplificado

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: |
          pip install -r requirements.txt
          coverage run -m pytest
          coverage report -m
```

---

## 📸 Evidencias


### Ejemplo: Resultados de los Tests


<img width="1528" height="215" alt="image" src="https://github.com/user-attachments/assets/e7ff7cb6-ac9e-4c1d-bb38-10ec20f8f03c" />


### Ejemplo: Reporte de Coverage

<img width="548" height="200" alt="image" src="https://github.com/user-attachments/assets/6ac35fa4-08fe-4ecb-ae2d-be57f924ac90" />


---

## 📊 Métricas esperadas

* ✅ Cobertura mínima: **> 80%**
* 🧩 Tests unitarios: Validaciones, creación, actualización y filtrado.
* 🔗 Tests de integración: Repositorio + Manager.

---
