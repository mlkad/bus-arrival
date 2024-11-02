import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Загрузка данных
stops_data = pd.read_csv('stops_data.csv')  # Укажите путь к вашему файлу
stops_data['latitude'] = pd.to_numeric(stops_data['latitude'], errors='coerce')
stops_data['longitude'] = pd.to_numeric(stops_data['longitude'], errors='coerce')

# Преобразование категорий в числа
stops_data['route_id'] = stops_data['route_id'].astype('category').cat.codes

# Задайте реальные данные о времени прибытия (это просто пример)
# Убедитесь, что длина массива arrival_times соответствует количеству остановок
arrival_times = [10, 15, 5, 20, 13]  # Пример данных
# Генерация значения времени прибытия для каждой остановки (например, случайные значения, если данные отсутствуют)
stops_data['arrival_time'] = np.random.choice(arrival_times, len(stops_data))

# Разделение данных на признаки (X) и цель (y)
X = stops_data[['latitude', 'longitude', 'route_id']]
y = stops_data['arrival_time']

# Разделение на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Проверка точности модели
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print("Средняя ошибка предсказания:", mae)

# Пример предсказания
example = pd.DataFrame([[7.292462226, 80.6349778, 101]], columns=['latitude', 'longitude', 'route_id'])
predicted_arrival = model.predict(example)
print("Прогноз времени прибытия (минут):", predicted_arrival[0])
