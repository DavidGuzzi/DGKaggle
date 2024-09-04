import pandas as pd

#Read train.csv
df = pd.read_csv('train.csv').sample(frac=0.03, random_state=7)

#Get a sample, and save it
sample = df.to_csv(r'C:\Users\HP\OneDrive\Escritorio\David Guzzi\Github\DGKaggle\New York City Taxi Fare Prediction\train_s.csv')

#%%
import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
n_simulations = 10000  # Número de simulaciones de Montecarlo
n_loans = 1000  # Número de préstamos en la cartera
default_probability = 0.05  # Probabilidad de mora individual
loan_amount = 10000  # Monto promedio del préstamo

# Array para almacenar los resultados de las simulaciones
losses = np.zeros(n_simulations)

# Simulación de Montecarlo
for i in range(n_simulations):
    # Simular si cada préstamo entra en mora (1) o no (0)
    defaults = np.random.binomial(1, default_probability, n_loans)
    # Calcular la pérdida total para esta simulación
    loss = np.sum(defaults * loan_amount)
    # Almacenar la pérdida en el array de resultados
    losses[i] = loss

# Análisis de los resultados
expected_loss = np.mean(losses)
percentile_95_loss = np.percentile(losses, 95)

print(f"Pérdida esperada: ${expected_loss:,.2f}")
print(f"Pérdida en el percentil 95 (VaR 95%): ${percentile_95_loss:,.2f}")

# Visualización de la distribución de las pérdidas
plt.hist(losses, bins=50, color='blue', alpha=0.7)
plt.title("Distribución de las pérdidas totales de la cartera")
plt.xlabel("Pérdida total ($)")
plt.ylabel("Frecuencia")
plt.show()

# %%
