import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import NearestNDInterpolator, LinearNDInterpolator
# from pykrige.ok import OrdinaryKriging # Descomente se pykrige estiver instalado

print("Script de exemplo para interpolação de dados climáticos.")

# Exemplo de dados fictícios de estações meteorológicas
# latitude, longitude, temperatura, precipitacao
data = {
    'lat': [ -23.55, -23.45, -23.60, -23.50, -23.40],
    'lon': [ -46.63, -46.55, -46.70, -46.60, -46.50],
    'temp': [20.5, 21.0, 19.8, 20.7, 21.2],
    'precip': [10.2, 11.5, 9.5, 10.8, 12.0]
}
df = pd.DataFrame(data)

# Criar uma grade para interpolação
lat_grid = np.linspace(df['lat'].min() - 0.05, df['lat'].max() + 0.05, 50)
lon_grid = np.linspace(df['lon'].min() - 0_05, df['lon'].max() + 0.05, 50)
lon_mesh, lat_mesh = np.meshgrid(lon_grid, lat_grid)

# Interpolação IDW (usando NearestNDInterpolator como proxy para demonstração simples)
# Para IDW real, seria necessário implementar o algoritmo ou usar uma biblioteca específica.
points = df[['lat', 'lon']].values
values_temp = df['temp'].values
values_precip = df['precip'].values

interp_temp = NearestNDInterpolator(points, values_temp)
interp_precip = NearestNDInterpolator(points, values_precip)

interpolated_temp = interp_temp((lat_mesh, lon_mesh))
interpolated_precip = interp_precip((lat_mesh, lon_mesh))

# Visualização (exemplo para temperatura)
plt.figure(figsize=(12, 6))
plt.imshow(interpolated_temp, extent=[lon_grid.min(), lon_grid.max(), lat_grid.min(), lat_grid.max()],
           origin='lower', cmap='coolwarm', alpha=0.8)
plt.scatter(df['lon'], df['lat'], c=df['temp'], cmap='coolwarm', edgecolors='k', s=100, label='Estações')
plt.colorbar(label='Temperatura (°C)')
plt.title('Interpolação de Temperatura (Exemplo Simples)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()

print("Para interpolação Kriging, considere usar a biblioteca pykrige.")
print("Para integração com QGIS, o processo geralmente envolve a exportação de dados e o uso de ferramentas nativas do QGIS.")
