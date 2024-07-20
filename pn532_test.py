# SPDX-FileCopyrightText: 2021 ladyada для Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Этот пример демонстрирует подключение к PN532 через I2C (требуется поддержка растяжения тактового сигнала),
SPI или UART. SPI лучше всего, он использует больше выводов, но является самым надежным и универсально поддерживаемым.
После инициализации попробуйте поднести различные RFID-карты на 13,56 МГц!
"""

import board
import busio
from digitalio import DigitalInOut
import binascii
import time

from adafruit_pn532.i2c import PN532_I2C

# Подключение по I2C:
i2c = busio.I2C(board.SCL, board.SDA)

# С подключением I2C, мы рекомендуем подключить RSTPD_N (сброс) к цифровому пину для ручного сброса аппаратуры
reset_pin = DigitalInOut(board.D6)
# На Raspberry Pi вы также должны подключить пин к P32 "H_Request" для аппаратного пробуждения
req_pin = DigitalInOut(board.D12)
pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

CARD_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]  # Ключ для аутентификации карты
HEADER = b'BG'  # Заголовок, который используется для записи данных на карту

# Инициализация PN532 и получение версии прошивки
ic, ver, rev, support = pn532.firmware_version
print("Найден PN532 с версией прошивки: {0}.{1}".format(ver, rev))

# Конфигурация PN532 для работы с картами MiFare
pn532.SAM_configuration()

def read_from_card():
    """
    Читает данные с карты NFC/RFID.
    """
    print("Ожидание RFID/NFC карты...")
    while True:
        # Проверка, доступна ли карта для чтения
        uid = pn532.read_passive_target(timeout=0.5)
        if uid is None:
            print(".", end="")
            continue
        
        print("\nНайдена карта с UID:", [hex(i) for i in uid])
        
        # Аутентификация и чтение блока 4
        if not pn532.mifare_classic_authenticate_block(uid, 4, 0x60, CARD_KEY):
            print("Не удалось аутентифицировать карту!")
            continue
        
        data = pn532.mifare_classic_read_block(4)
        if data is None:
            print("Не удалось прочитать данные с карты!")
            continue
        
        print("Данные, считанные с карты:", data)
        
        if data[:2] != HEADER:
            print("Карта не записана с правильными данными блока!")
            continue

        try:
            # Извлечение данных пользователя из считанных данных
            user_data = data[2:2+14].decode("utf-8").strip()
            print("Данные пользователя: {0}".format(user_data))
        except ValueError:
            print("Не удалось разобрать данные пользователя с карты.")
        break

def write_to_card(data):
    """
    Записывает данные на карту NFC/RFID.
    
    :param data: Данные для записи (до 14 байт)
    """
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is None:
        print("Не удалось найти карту для записи.")
        return
    
    print("Найдена карта с UID:", [hex(i) for i in uid])
    
    # Аутентификация перед записью
    if not pn532.mifare_classic_authenticate_block(uid, 4, 0x60, CARD_KEY):
        print("Не удалось аутентифицировать карту!")
        return
    
    # Убедитесь, что данные имеют длину 14 байт
    data = data[:14].ljust(14, b'\0')
    full_data = HEADER + data
    if not pn532.mifare_classic_write_block(4, full_data):
        print("Не удалось записать данные на карту!")
    else:
        print("Данные успешно записаны на карту!")

if __name__ == "__main__":
    while True:
        print("\n1. Прочитать данные с карты")
        print("2. Записать данные на карту")
        print("3. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            read_from_card()
        elif choice == '2':
            data = input("Введите данные для записи (до 14 байт): ").encode('utf-8')
            write_to_card(data)
        elif choice == '3':
            break
        else:
            print("Неверный выбор, пожалуйста, попробуйте снова.")
