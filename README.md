# Установка и использование библиотеки ADXL345 на Raspberry Pi

Проверено для датчика ADXL345 на Raspberry Pi под управлением Ubuntu.

## 1. Установка зависимостей

Обновите список пакетов и установите нужные зависимости::

```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-smbus i2c-tools
pip3 install adafruit-circuitpython-adxl34x
pip3 install RPi.GPIO
```

## 2. Добавление пользователя в группу "i2c"

Для доступа к шине I2C вашему пользователю нужно быть членом группы i2c. Выполните команду:

```bash
sudo usermod -aG i2c $USER
```

## 3. Перезагрузка системы

Для применения изменений необходимо перезагрузить систему или выйти из текущей сессии и войти снова.

```bash
sudo reboot
```

## 4. Проверка файла /dev/i2c-1

Убедитесь, что файл /dev/i2c-1 существует и имеет правильные права доступа:

```bash
ls -l /dev/i2c-1
```

## 5. Сборка схемы:


Сборка схемы:

![Схема подключения ADXL345](https://private-user-images.githubusercontent.com/47589206/350685343-caf6b787-fc8f-4429-b92f-759f14359b6a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE0NzIwMjMsIm5iZiI6MTcyMTQ3MTcyMywicGF0aCI6Ii80NzU4OTIwNi8zNTA2ODUzNDMtY2FmNmI3ODctZmM4Zi00NDI5LWI5MmYtNzU5ZjE0MzU5YjZhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzIwVDEwMzUyM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTRkODdkMGVlNWY3YTBlMzAyNmFjY2IyMmE0MDU4NGJhYTA5N2NhZGY3NjViYjEyODg5YzE0YjNkOWY2ZmY3NTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.CoMqM4I1LPA1AFWpiLjt5UCeHzz_9SXjtyHetZwalnE.png)


## 5. Создание скрипта для чтения данных с ADXL345

Скрипт находится в репозитории

```bash
python3 adxl345_test.py
```

# Установка и использование NFC модуля pn532 на Raspberry Pi

## 1. Сборка схемы:


Сборка схемы:

![image](https://github.com/user-attachments/assets/486d33c8-c7db-4a40-9a96-5dad6423f504)



