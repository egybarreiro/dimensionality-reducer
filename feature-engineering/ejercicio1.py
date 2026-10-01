"""
Feature Engineering Function for a Weather file
Author: Edgar Barreiro
Date Created: 2024-06-10
Date Modified: 2024-06-10
"""

import pandas as pd

weather_df = pd.read_csv('/Users/User/OneDrive/Desktop/Terminal34_Bootcamp/feature-engineering/unit_1_feature_engineering_exercise_data.csv')
#print(weather_df)

print(weather_df['datetime'])

weather_df['datetime'] = pd.to_datetime(weather_df['datetime'], format='%Y-%m-%d %H:%M:%S')

# Exercise #1: hour, day, month and year.
weather_df['hour'] = weather_df['datetime'].dt.hour
weather_df['day'] = weather_df['datetime'].dt.day
weather_df['month'] = weather_df['datetime'].dt.month
weather_df['year'] = weather_df['datetime'].dt.year

# Exercise #2: seasons 1=spring, 2=summer, 3=fall, 4=winter
weather_df['season_name'] = weather_df['season'].map({1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'})
print(weather_df['season_name'])

# Exercise #3: Combine weather and temp columns into a new feature called feels_like.
def calculate_feels_like(row):

    temp = row['temp']
    weather = row['weather']

    if weather == 1:  # Despejado
        feels_like = temp
    elif weather == 2:  # Neblina + Nublado
        feels_like = temp - 2
    elif weather == 3:  # Nieve ligera, lluvia ligera + tormenta eléctrica + nubes dispersas
        feels_like = temp - 5
    elif weather == 4:  # Lluvia intensa + granizo + tormenta eléctrica + neblina, nieve + niebla
        feels_like = temp -8
    else:
        feels_like = temp  # Default case if weather code is not recognized

    return feels_like

weather_df['feels_like'] = weather_df.apply(calculate_feels_like, axis=1)
print(weather_df[['temp', 'weather', 'feels_like']].head(10))

# Exercise 4: Crea una característica binaria 'peak_hours' que tome el 
# valor 1 si la hora está entre las 7 y 9 de la mañana o entre las 4 y 6 
# de la tarde; en caso contrario, 0 (asumiendo que son horas de mayor tráfico).
weather_df['peak_hours'] = (weather_df['hour'].between(7, 9) | weather_df['hour'].between(16, 18)).astype(int)
weather_df['peak_hours'] = weather_df['hour'].apply(lambda x: 1 if (7 <= x <= 9) or (16 <= x <= 18) else 0)
print(weather_df[['hour', 'peak_hours']].head(10))

# Exercise 5: Estandariza las características temp, humidity y windspeed 
# para que tengan una media de 0 y una desviación estándar de 1.
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
weather_df[['temp_scaled']] = scaler.fit_transform(weather_df[['temp']])
weather_df[['humidity_scaled', 'windspeed_scaled']] = scaler.fit_transform(weather_df[['humidity', 'windspeed']])
print(weather_df[['temp', 'temp_scaled', 'humidity', 'humidity_scaled', 'windspeed', 'windspeed_scaled']].head(10))