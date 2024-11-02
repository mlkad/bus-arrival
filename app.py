import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)

# Загружаем данные из CSV файла
stops_data = pd.read_csv('stops_data.csv')

# Здесь создаем искусственные данные для времени прибытия
arrival_times = np.random.randint(1, 30, size=len(stops_data))
stops_data['arrival_time'] = arrival_times

# Обучаем модель
model = LinearRegression()
X = stops_data[['latitude', 'longitude']]
y = stops_data['arrival_time']
model.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not data:
        return jsonify({'error': 'Нет данных'}), 400

    example = [
        data.get('latitude'),
        data.get('longitude')
    ]

    predicted_arrival = model.predict([example])
    return jsonify({'predicted_arrival_time': predicted_arrival[0]})

if __name__ == '__main__':
    app.run(debug=True)
