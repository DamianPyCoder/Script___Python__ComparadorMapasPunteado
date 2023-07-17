import cv2
import numpy as np

def comparar_mapas(mapa1, mapa2):
    # Cargar mapas
    img1 = cv2.imread(mapa1)
    img2 = cv2.imread(mapa2)

    # Convertirlos a escala de grises
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Detectar los contornos en la imagen
    _, contours1, _ = cv2.findContours(img1_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    _, contours2, _ = cv2.findContours(img2_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calcular calles sin puntear
    lineas_sin_puntos = 0

    for contour in contours2:
        # Coordenadas del contorno en la segunda imagen
        x, y, w, h = cv2.boundingRect(contour)
        punto_central = (x + w // 2, y + h // 2)

        # Verificar si el punto central está contenido en algún contorno de la primera imagen
        punto_contenido = False

        for contour in contours1:
            if cv2.pointPolygonTest(contour, punto_central, False) >= 0:
                punto_contenido = True
                break

        # Contador si el punto no está contenido en ningún contorno de la primera imagen
        if not punto_contenido:
            lineas_sin_puntos += 1

    # Calcular porcentaje de líneas con puntos correspondientes
    total_lineas = len(contours2)
    lineas_con_puntos = total_lineas - lineas_sin_puntos
    porcentaje = (lineas_con_puntos / total_lineas) * 100

    return lineas_sin_puntos, porcentaje

# Rutas de los mapas
mapa1 = "mapa1.jpg"
mapa2 = "mapa2.jpg"

# Comparar los mapas
lineas_sin_puntos, porcentaje = comparar_mapas(mapa1, mapa2)

# Imprimir el resultado
print(f"El número de líneas sin puntos correspondientes es: {lineas_sin_puntos}")
print(f"Porcentaje de líneas con puntos correspondientes: {porcentaje}%")
