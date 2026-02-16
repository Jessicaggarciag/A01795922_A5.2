# pylint: disable=invalid-name
"""
Programa para calcular el total de ventas desde archivos JSON.
"""

import sys
import json
import time


def load_json_file(file_path):
    """Carga un archivo JSON y maneja errores de lectura."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error al procesar el archivo {file_path}: {e}")
        return None


def calculate_total(catalogue, sales):
    """Calcula el costo total cruzando catálogo y ventas."""
    total_cost = 0
    # E501: Línea acortada para cumplir con el límite de 79 caracteres
    prices = {item['title']: item['price']
              for item in catalogue if 'title' in item}

    for sale in sales:
        product = sale.get('Product')
        quantity = sale.get('Quantity', 0)

        if product in prices:
            total_cost += prices[product] * quantity
        else:
            print(f"Error: Producto '{product}' no encontrado.")

    return total_cost


def main():
    """Función principal para la ejecución."""
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Uso: python computeSales.py cat.json sales.json")
        return

    catalogue = load_json_file(sys.argv[1])
    sales = load_json_file(sys.argv[2])

    if catalogue is None or sales is None:
        return

    total = calculate_total(catalogue, sales)
    elapsed_time = time.time() - start_time

    # Formateo de resultados sin espacios al final (W291 corregido)
    result_output = (
        f"{'-'*30}\n"
        f"REPORTE DE VENTAS\n"
        f"{'-'*30}\n"
        f"Total de Ventas: ${total:,.2f}\n"
        f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n"
        f"{'-'*30}\n"
    )

    print(result_output)
    with open("SalesResults.txt", "w", encoding='utf-8') as f:
        f.write(result_output)


if __name__ == "__main__":
    main()
