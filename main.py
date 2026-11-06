"""Generador de códigos QR desde la terminal."""

import os
import qrcode
from PIL import Image


def validar_datos(datos: str) -> None:
    """Valida que los datos no estén vacíos.

    Args:
        datos: Texto o URL a codificar en el QR.

    Raises:
        ValueError: Si los datos están vacíos o son solo espacios.
    """
    if not datos.strip():
        raise ValueError("Los datos no pueden estar vacíos.")


def validar_nombre_archivo(nombre: str) -> str:
    """Valida y normaliza el nombre del archivo de salida.

    Args:
        nombre: Nombre del archivo ingresado por el usuario.

    Returns:
        Nombre del archivo con extensión .png.

    Raises:
        ValueError: Si el nombre contiene caracteres inválidos.
    """
    nombre = nombre.strip()
    if not nombre:
        raise ValueError("El nombre del archivo no puede estar vacío.")

    caracteres_invalidos = r'\/:*?"<>|'
    for caracter in caracteres_invalidos:
        if caracter in nombre:
            raise ValueError(f"El nombre contiene un carácter inválido: '{caracter}'")

    if not nombre.endswith(".png"):
        nombre += ".png"

    return nombre


def generar_qr(datos: str, nombre_archivo: str) -> None:
    """Genera un código QR y lo guarda como imagen PNG.

    Args:
        datos: Texto o URL a codificar.
        nombre_archivo: Ruta del archivo de salida.

    Raises:
        OSError: Si no se puede guardar el archivo.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(datos)
    qr.make(fit=True)

    imagen: Image.Image = qr.make_image(fill_color="black", back_color="white")
    imagen.save(nombre_archivo)


def main() -> None:
    """Punto de entrada principal del generador de QR."""
    print("=== Generador de Códigos QR ===\n")

    try:
        datos = input("Ingresá el texto o URL a codificar: ")
        validar_datos(datos)

        nombre = input("Nombre del archivo de salida (sin extensión): ")
        nombre_archivo = validar_nombre_archivo(nombre)

        generar_qr(datos, nombre_archivo)

        print(f"\n✓ Código QR guardado como '{nombre_archivo}'")
        print(f"  Ubicación: {os.path.abspath(nombre_archivo)}")

    except ValueError as e:
        print(f"\n✗ Error de validación: {e}")
    except OSError as e:
        print(f"\n✗ Error al guardar el archivo: {e}")


if __name__ == "__main__":
    main()
