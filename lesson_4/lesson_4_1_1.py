import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# モジュール　外部ファイルからインポートする
from util.module import add

result = add(10, 5)
print(result)  # 結果: 15

# パッケージ
from util.package.package_1 import add
from util.package.package_2 import subtract

print(add(10, 5))       # 結果: 15
print(subtract(10, 5))  # 結果: 5
