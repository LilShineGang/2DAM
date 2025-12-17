import matplotlib.pyplot as plt
import numpy as np

# Datos del problema
CF = 13300
Pv = 25
Cv = 18
Q_equilibrio = 1900

# Rango de cantidades para el gráfico (de 0 a 3500 libros)
q = np.linspace(0, 3500, 100)

# Ecuaciones
IT = Pv * q  # Ingresos Totales
CT = CF + (Cv * q)  # Costes Totales
C_Fijos = [CF for _ in q]  # Costes Fijos (línea recta)

# Configuración del gráfico
plt.figure(figsize=(10, 6))

# Dibujar líneas
plt.plot(q, IT, label='Ingresos Totales (IT)', color='green', linewidth=2)
plt.plot(q, CT, label='Costes Totales (CT)', color='red', linewidth=2)
plt.plot(q, C_Fijos, label='Costes Fijos (CF)', color='blue', linestyle='--', alpha=0.7)

# Marcar el Punto Muerto
plt.scatter(Q_equilibrio, Pv * Q_equilibrio, color='black', zorder=5)
plt.annotate(f'Punto Muerto\n(1.900 libros, 47.500€)',
            xy=(Q_equilibrio, Pv * Q_equilibrio),
            xytext=(Q_equilibrio + 200, Pv * Q_equilibrio - 10000),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Sombreado de zonas
plt.fill_between(q, IT, CT, where=(q > Q_equilibrio), interpolate=True, color='green', alpha=0.1, label='Zona de Beneficios')
plt.fill_between(q, IT, CT, where=(q < Q_equilibrio), interpolate=True, color='red', alpha=0.1, label='Zona de Pérdidas')

# Etiquetas y Título
plt.title('Gráfico del Umbral de Rentabilidad (Punto Muerto)')
plt.xlabel('Cantidad de libros vendidos (Q)')
plt.ylabel('Importe en Euros (€)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Guardar imagen para mostrar
plt.tight_layout()
plt.savefig('punto_muerto.png')