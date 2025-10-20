# Sistema de Recomendación, Filtrado Colaborativo

Este proyecto implementa un sistema de recomendación basado en diferentes métricas de similitud y técnicas de predicción. Utiliza una matriz de utilidad para calcular similitudes entre usuarios y predecir valores faltantes en la matriz.

## Características

- **Cálculo de similitudes**:
  - Correlación de Pearson
  - Similitud de coseno
  - Similitud euclidiana
- **Técnicas de predicción**:
  - Predicción simple
  - Predicción basada en la media del usuario
- **Soporte para valores faltantes** en la matriz de utilidad.

## Requisitos

- Python 3.7 o superior
- Bibliotecas:
  - `numpy`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <https://github.com/ArunDaswaniLakhani/GCO-Sistemas-de-Recomendacion.git>
   cd <GCO-Sistemas-de-Recomendacion>

2. Asegúrate de tener instaladas las dependencias:
   ```bash
   pip install numpy

3. Ejecuta el script principal con el siguiente formato:
   ```bash
   python3 main.py <archivo> <metrica> <num_vecinos> <tipo_prediccion>