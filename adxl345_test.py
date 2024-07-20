import time
import board
import busio
import adafruit_adxl34x

# Коэффициент чувствительности
sensitivity_threshold = 0.5
# Параметры для скользящего среднего
window_size = 10
acceleration_buffer = []


def calculate_moving_average(values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


try:
    # Инициализация I2C
    i2c = busio.I2C(board.SCL, board.SDA)
    # Создание объекта акселерометра
    accelerometer = adafruit_adxl34x.ADXL345(i2c)

    # Начальные значения ускорений
    prev_x, prev_y, prev_z = accelerometer.acceleration

    while True:
        # Получаем текущие значения ускорений по осям X, Y и Z
        x, y, z = accelerometer.acceleration

        # Добавляем новые значения в буфер и сохраняем только последние window_size значений
        acceleration_buffer.append((x, y, z))
        if len(acceleration_buffer) > window_size:
            acceleration_buffer.pop(0)

        # Вычисляем средние значения для скользящего окна
        avg_x = calculate_moving_average([val[0] for val in acceleration_buffer])
        avg_y = calculate_moving_average([val[1] for val in acceleration_buffer])
        avg_z = calculate_moving_average([val[2] for val in acceleration_buffer])

        # Вычисляем изменения ускорений относительно скользящего среднего
        delta_x = abs(x - avg_x)
        delta_y = abs(y - avg_y)
        delta_z = abs(z - avg_z)

        # Проверяем, превышает ли изменение ускорения по какой-либо оси коэффициент чувствительности
        if delta_x > sensitivity_threshold or delta_y > sensitivity_threshold or delta_z > sensitivity_threshold:
            print(f"ПРЕДУПРЕЖДЕНИЕ: X: {x:.2f}, Y: {y:.2f}, Z: {z:.2f}")

        # Задержка перед следующим чтением данных
        time.sleep(0.5)

except Exception as e:
    print(f"Произошла ошибка: {e}")
