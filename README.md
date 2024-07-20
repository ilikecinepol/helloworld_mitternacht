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

![Схема подключения ADXL345](https://github.com/ilikecinepol/helloworld_mitternacht/issues/1#issue-2420808455)


## 5. Создание скрипта для чтения данных с ADXL345

Скрипт находится в репозитории

```bash
python3 adxl345_test.py
```
