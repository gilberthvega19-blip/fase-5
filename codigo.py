# =========================================================
# PROBLEMA 3 - AUDITORÍA DE INVENTARIO
# Curso: Fundamentos de Programación
# Autor: Gilberth Andres Segura Vega
# =========================================================
inventario = [
    ["A101", "Teclado", 5, 10],
    ["A102", "Mouse", 12, 8],
    ["A103", "Monitor", 3, 7],
    ["A104", "Impresora", 9, 9],
    ["A105", "Memoria USB", 2, 6]
]


# ---------------------------------------------------------
# Función para calcular la cantidad a solicitar
# ---------------------------------------------------------
def calcular_reabastecimiento(stock_actual, stock_minimo):
    
    # Verificar si el stock es menor al mínimo requerido
    if stock_actual < stock_minimo:
        
        # Calcular diferencia
        cantidad_pedir = stock_minimo - stock_actual
        
        return cantidad_pedir
    
    else:
        return 0


# ---------------------------------------------------------
# Mostrar reporte de pedidos
# ---------------------------------------------------------
print("======================================")
print("     REPORTE DE REABASTECIMIENTO")
print("======================================\n")


# Recorrer matriz del inventario
for articulo in inventario:
    
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Llamar función
    cantidad_solicitar = calcular_reabastecimiento(
        stock_actual,
        stock_minimo
    )

    # Mostrar información
    print(f"Código: {codigo}")
    print(f"Artículo: {nombre}")
    print(f"Stock Actual: {stock_actual}")
    print(f"Stock Mínimo: {stock_minimo}")
    print(f"Cantidad a Solicitar: {cantidad_solicitar}")
    print("--------------------------------------")
  
