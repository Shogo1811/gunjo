# osライブラリ
import os

# ファイルの存在チェック
print(os.path.exists("xxx.txt"))  # 結果: True or False

# ディレクトリの作成
os.mkdir("new_directory")

file_path = "example.txt"
directory, file_name = os.path.split(file_path)
print(f"Directory: {directory}, File name: {file_name}")

# datetimeライブラリ
import datetime

# 現在の日付と時刻を取得
now = datetime.datetime.now()
print(now)  # 結果: 2024-12-06 10:00:00.000000

# 日付のフォーマット
formatted_date = now.strftime("%Y-%m-%d")
print(formatted_date)  # 結果: 2024-12-06

# 日付の加算
future_date = now + datetime.timedelta(days=7)
print(future_date)  # 結果: 2024-12-13

# ランダムライブラリ
import random

# 0〜9のランダムな整数を生成
random_number = random.randint(0, 9)
print(random_number)

# リストからランダムに要素を選択
fruits = ["apple", "banana", "cherry"]
random_fruit = random.choice(fruits)
print(random_fruit)

# ランダムに並べ替え
random.shuffle(fruits)
print(fruits)

# mathライブラリ
import math

# 平方根
print(math.sqrt(25))  # 結果: 5.0

# 三角関数
print(math.sin(math.pi / 2))  # 結果: 1.0

# 定数pi
print(math.pi)  # 結果: 3.141592653589793

# sysライブラリ
import sys

# コマンドライン引数の取得
print(sys.argv)  # 実行時に渡された引数リストを表示

# Pythonのバージョン情報
print(sys.version)

# requestsライブラリ
import requests

# Webページを取得
response = requests.get('https://www.yahoo.com')
print(response.status_code)  # 結果: 200
print(response.text)  # 結果: ページのHTML

# JSONデータをPOSTする
"""
以下はサンプル例
# data = {"key": "value"}
# response = requests.post('https://api.example.com/data', json=data)
# print(response.json())  # レスポンスのJSONデータを表示
"""

# # numpyライブラリ
import numpy as np

# 配列の作成
arr = np.array([1, 2, 3, 4])
print(arr)

# 配列の演算
arr2 = np.array([5, 6, 7, 8])
print(arr + arr2)  # 結果: [6 8 10 12]

# 行列の掛け算
matrix = np.array([[1, 2], [3, 4]])
result = np.dot(matrix, matrix)
print(result)

# pandasライブラリ
import pandas as pd

# データフレームの作成
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# データフレームの表示
print(df)

# 特定の列にアクセス
print(df['Name'])

# matplotlibライブラリ

import matplotlib.pyplot as plt

# グラフの描画
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.title("Simple Plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()
