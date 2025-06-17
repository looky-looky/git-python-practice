# calculator.py
# 計算機クラスの定義

class Calculator:
    """計算機クラス - 計算履歴を保持する"""
    
    def __init__(self):
        """コンストラクタ"""
        self.history = []  # 属性：計算履歴
        self.result = 0    # 属性：現在の結果
    
    def add(self, x, y):
        """足し算メソッド"""
        self.result = x + y
        self.history.append(f"{x} + {y} = {self.result}")
        return self.result
    
    def subtract(self, x, y):
        """引き算メソッド"""
        self.result = x - y
        self.history.append(f"{x} - {y} = {self.result}")
        return self.result
    
    def multiply(self, x, y):
        """掛け算メソッド"""
        self.result = x * y
        self.history.append(f"{x} × {y} = {self.result}")
        return self.result
    
    def divide(self, x, y):
        """割り算メソッド"""
        if y == 0:
            error_msg = "エラー: ゼロで割ることはできません"
            self.history.append(f"{x} ÷ {y} = {error_msg}")
            return error_msg
        
        self.result = x / y
        self.history.append(f"{x} ÷ {y} = {self.result}")
        return self.result
    
    def show_history(self):
        """計算履歴を表示"""
        print("=== 計算履歴 ===")
        if not self.history:
            print("履歴がありません")
        else:
            for i, record in enumerate(self.history, 1):
                print(f"{i}. {record}")
    
    def clear_history(self):
        """履歴をクリア"""
        self.history = []
        self.result = 0
        print("履歴をクリアしました")
    
    def get_last_result(self):
        """最後の計算結果を取得"""
        return self.result

# テスト用
if __name__ == "__main__":
    calc = Calculator()
    
    calc.add(10, 5)
    calc.multiply(3, 4)
    calc.divide(20, 4)
    calc.subtract(15, 7)
    
    calc.show_history()
    print(f"最後の結果: {calc.get_last_result()}")