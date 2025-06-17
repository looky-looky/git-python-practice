# main.py
# 他のモジュールやクラスを使用するメインプログラム

# 標準ライブラリのインポート
import random
import datetime

# 自作モジュールのインポート
import math_functions
from student import Student
from calculator import Calculator

def main():
    """メイン関数"""
    print("=== Pythonモジュール・クラス学習プログラム ===")
    print(f"実行日時: {datetime.datetime.now()}")
    print()
    
    # 1. 関数モジュールの使用例
    print("1. math_functions モジュールの使用")
    print("-" * 40)
    a, b = 15, 3
    print(f"数値: a = {a}, b = {b}")
    print(f"足し算: {math_functions.add(a, b)}")
    print(f"引き算: {math_functions.subtract(a, b)}")
    print(f"掛け算: {math_functions.multiply(a, b)}")
    print(f"割り算: {math_functions.divide(a, b)}")
    print(f"べき乗: {math_functions.power(a, b)}")
    print()
    
    # 2. Studentクラスの使用例
    print("2. Student クラスの使用")
    print("-" * 40)
    # 複数の学生インスタンスを作成
    students = [
        Student("山田太郎", "S2024001"),
        Student("鈴木花子", "S2024002"),
        Student("田中次郎", "S2024003")
    ]
    
    # 各学生に情報を設定
    students[0].set_grade(random.randint(70, 100))
    students[0].add_subject("Python基礎")
    students[0].add_subject("データサイエンス")
    
    students[1].set_grade(random.randint(70, 100))
    students[1].add_subject("Python基礎")
    students[1].add_subject("機械学習")
    students[1].add_subject("統計学")
    
    students[2].set_grade(random.randint(70, 100))
    students[2].add_subject("Python基礎")
    
    # 全学生の情報を表示
    for student in students:
        print(student.introduce())
        student.show_info()
    
    # 3. Calculatorクラスの使用例
    print("3. Calculator クラスの使用")
    print("-" * 40)
    calc = Calculator()
    
    # いくつかの計算を実行
    operations = [
        (25, 8, 'add'),
        (50, 15, 'subtract'),
        (7, 6, 'multiply'),
        (100, 4, 'divide'),
        (10, 0, 'divide')  # エラーケース
    ]
    
    for x, y, operation in operations:
        if operation == 'add':
            calc.add(x, y)
        elif operation == 'subtract':
            calc.subtract(x, y)
        elif operation == 'multiply':
            calc.multiply(x, y)
        elif operation == 'divide':
            calc.divide(x, y)
    
    calc.show_history()
    print()
    
    # 4. 外部ライブラリの使用例（標準ライブラリ）
    print("4. 標準ライブラリの使用例")
    print("-" * 40)
    
    # randomライブラリの使用
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    print(f"ランダムな数値: {random_numbers}")
    
    # math_functionsを使って合計を計算
    total = 0
    for num in random_numbers:
        total = math_functions.add(total, num)
    print(f"合計: {total}")
    
    # 平均を計算
    average = math_functions.divide(total, len(random_numbers))
    print(f"平均: {average}")
    
    print()
    print("=== プログラム終了 ===")

def demonstrate_import_methods():
    """様々なimport方法のデモンストレーション"""
    print("=== 様々なimport方法 ===")
    
    # 方法1: import モジュール名
    import math_functions
    result1 = math_functions.add(10, 5)
    print(f"方法1 - import math_functions: {result1}")
    
    # 方法2: from モジュール名 import 関数名
    from math_functions import multiply, divide
    result2 = multiply(4, 3)
    result3 = divide(20, 4)
    print(f"方法2 - from import: {result2}, {result3}")
    
    # 方法3: import モジュール名 as 別名
    import math_functions as mf
    result4 = mf.power(2, 8)
    print(f"方法3 - import as: {result4}")
    
    # 方法4: from モジュール名 import * (非推奨だが説明用)
    # from math_functions import *
    # result5 = subtract(15, 7)  # 直接関数名で呼び出し可能
    
    print()

if __name__ == "__main__":
    main()
    # demonstrate_import_methods()