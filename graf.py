# # Импорт необходимых библиотек
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas
#
# import pandas as pd
#
# # фактический путь к вашему CSV файлу
# file_path = "bitkoin_quotes.csv"
# # Прочитайте CSV файл
# df = pd.read_csv(file_path, delimiter=';')
#
# date = []
# price = []
#
# for i in range(100, 0, -1):
#     date.append(df['дата'][i][0:10])
#     price.append(df['закрытый'][i])
#
# print(f"Самая высока цена {max(price)}$ была {date[price.index(max(price))]}")
# print(f"А самая низкая цена {min(price)}$ была {date[price.index(min(price))]}")
#
#
#
# # Создайте график
# plt.plot(date, price)
#
# # Поворот меток по горизонтали для дат
# plt.xticks(rotation=270)
#
# # Добавьте подписи к осям
# plt.xlabel('Дата')
# plt.ylabel('Цена')
#
# # Добавьте заголовок
# plt.title('График цен по датам')
#
# # Отобразите график
# plt.show()
#
# # # Данные для первого графика (годы и население)
# # year = [1950, 1975, 2000, 2018]
# # population = [2.13, 3.681, 5.312, 6.981]
# #
# # # Создание графика линии и точечного графика с использованием данных
# # plt.scatter(year, population)  # Точечный график по точкам
# # plt.yticks([0, 2, 4, 6, 8, 10])  # Установка делений на оси Y
# #
# # # Создание графика косинуса и синуса
# # X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# # cos, sin = np.cos(X), np.sin(X)
# # plt.plot(X, cos, color='blue', label='cos')  # График косинуса с синей линией и меткой
# # plt.plot(X, sin, color='red', label='sin')   # График синуса с красной линией и меткой
# # plt.legend(loc='upper left', frameon=False)  # Добавление легенды в верхний левый угол без рамки
# #
# # # Данные для гистограммы (имена и скорость)
# # names = ('Tom', 'Dick', 'Harry', 'Jill', 'Meredith', 'George')
# # y_pos = np.arange(len(names))
# # speed = [8, 7, 12, 4, 3, 2]
# #
# # # Создание гистограммы с использованием данных
# # plt.bar(y_pos, speed, align='center', alpha=0.5)  # Гистограмма с прозрачностью
# # plt.xticks(y_pos, names)  # Установка имен на оси X
# # plt.ylabel('Speed')  # Название оси Y
# # plt.title('Person')  # Заголовок графика
# #
# # # Отображение всех созданных графиков





# Import libraries
import json
import requests

# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# requesting data from url
data = requests.get(key)
data = data.json()
print(f"{data['symbol']} price is {data['price'][0:5]}")
