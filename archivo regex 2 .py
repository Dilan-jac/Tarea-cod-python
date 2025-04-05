import re
regex_contrasena = r"(?i)contraseña:\s*([a-zA-Z0-9!@#$%^&*()_+=\-]+)"
regex_curp = r"\b[A-Z]{4}\d{6}[HM][A-Z]{5}\d{2}\b"
regex_telefono = r"\b(?:\+?\d{1,3}[\s-]?)?(?:\(?\d{2,4}\)?[\s-]?)*\d{2,4}[\s-]?\d{2,4}\b"
regex_tarjeta = r"(?:\d{4}[\s-]?){4}"
regex_liga = r"https?://[^\s]+|www\.[^\s]+"
def buscar_patrones(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    contrasena = re.findall(regex_contrasena, contenido)
    curp = re.findall(regex_curp, contenido)
    telefono = re.findall(regex_telefono, contenido)
    tarjeta = re.findall(regex_tarjeta, contenido)
    liga = re.findall(regex_liga, contenido)

    if contrasena:
        print(f"Contraseña encontrada en {archivo}: {contrasena}")
    if curp:
        print(f"CURP encontrada en {archivo}: {curp}")
    if telefono:
        print(f"Teléfono encontrado en {archivo}: {telefono}")
    if tarjeta:
        print(f"Tarjeta encontrada en {archivo}: {tarjeta}")
    if liga:
        print(f"Liga encontrada en {archivo}: {liga}")

archivos = ["archivo 1", "archivo 2", "archivo 3"]

for archivo in archivos:
    buscar_patrones(archivo)
