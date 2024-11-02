document.getElementById('predictButton').addEventListener('click', function() {
    const latitude = parseFloat(document.getElementById('latitude').value);
    const longitude = parseFloat(document.getElementById('longitude').value);

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            latitude: latitude,
            longitude: longitude
        })
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.getElementById('result');

        if (data.error) {
            resultElement.textContent = 'Ошибка: ' + data.error;
        } else {
            resultElement.textContent = 'Предсказанное время прибытия: ' + data.predicted_arrival_time;
        }
    })
    .catch(error => {
        const resultElement = document.getElementById('result');
        resultElement.textContent = 'Ошибка: ' + error;
    });
});
