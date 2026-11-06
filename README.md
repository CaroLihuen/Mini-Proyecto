# Generador de Códigos QR

Genera códigos QR a partir de texto o URLs y los guarda como imágenes PNG.

## Requisitos

- Python 3.8+

## Instalación

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd Mini-Proyecto

# 2. Crear y activar el entorno virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

El programa pedirá:
1. El texto o URL a codificar
2. El nombre del archivo de salida (se guarda como `.png`)

## Ejemplo

```
=== Generador de Códigos QR ===

Ingresá el texto o URL a codificar: https://github.com
Nombre del archivo de salida (sin extensión): mi_qr

✓ Código QR guardado como 'mi_qr.png'
  Ubicación: C:\Users\...\Mini-Proyecto\mi_qr.png
```
