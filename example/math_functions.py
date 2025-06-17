# math_functions.py
# 基本的な数学関数を含むモジュール

def add(x, y):
    """2つの数を足し算する関数"""
    return x + y

def subtract(x, y):
    """2つの数を引き算する関数"""
    return x - y

def multiply(x, y):
    """2つの数を掛け算する関数"""
    return x * y

def divide(x, y):
    """2つの数を割り算する関数（ゼロ除算チェック付き）"""
    if y == 0:
        return "エラー: ゼロで割ることはできません"
    return x / y

def power(x, y):
    """xのy乗を計算する関数"""
    return x ** y

# モジュール内で実行される部分（テスト用）
if __name__ == "__main__":
    print("math_functions.py が直接実行されました")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")