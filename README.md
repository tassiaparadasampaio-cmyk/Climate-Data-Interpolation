# Climate Data Interpolation

## Descrição do Projeto

Este projeto aborda a **interpolação espacial de dados climáticos**, especificamente temperatura e precipitação. O objetivo é estimar valores em locais não amostrados a partir de dados de estações meteorológicas, utilizando métodos como Kriging e Inverse Distance Weighting (IDW). As análises são realizadas com uma combinação de **QGIS** para processamento geoespacial e **Python** para implementação dos algoritmos de interpolação e análise de dados.

## Objetivos

- Aplicar e comparar métodos de interpolação espacial (Kriging e IDW) para dados climáticos.
- Gerar mapas contínuos de temperatura e precipitação a partir de dados pontuais.
- Avaliar a precisão e a adequação de diferentes métodos de interpolação para dados climáticos.

## Metodologia

1. **Coleta de Dados**: Aquisição de dados pontuais de temperatura e precipitação de estações meteorológicas.
2. **Pré-processamento**: Limpeza e organização dos dados para análise espacial.
3. **Interpolação no QGIS**: Utilização de ferramentas de geoprocessamento do QGIS para aplicar IDW e Kriging.
4. **Interpolação em Python**: Implementação de algoritmos de interpolação (ex: `scipy.interpolate`, `pykrige`) para maior flexibilidade e automação.
5. **Validação e Análise**: Comparação dos resultados dos diferentes métodos e avaliação da precisão.

## Tecnologias Utilizadas

- **QGIS**: Software de Sistema de Informação Geográfica (SIG) para visualização, análise e geoprocessamento.
- **Python**: Linguagem de programação para manipulação de dados e implementação de algoritmos.
- **Bibliotecas Python**: `pandas` para manipulação de dados, `numpy` para computação numérica, `scipy` (para interpolação), `pykrige` (para Kriging), `matplotlib` e `seaborn` para visualização.

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/tassiaparadasampaio-cmyk/Climate-Data-Interpolation.git
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install pandas numpy scipy matplotlib seaborn pykrige
   ```
3. Execute o script principal (exemplo):
   ```bash
   python climate_interpolation.py
   ```

## Exemplo de Código (climate_interpolation.py)

```python
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
lon_grid = np.linspace(df['lon'].min() - 0.05, df['lon'].max() + 0.05, 50)
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
```

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
