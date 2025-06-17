# student.py
# 学生を表すクラスを定義

class Student:
    """学生クラス"""
    
    def __init__(self, name, student_id, grade=0):
        """コンストラクタ - インスタンス生成時に呼ばれる"""
        self.name = name          # 属性：名前
        self.student_id = student_id  # 属性：学生ID
        self.grade = grade        # 属性：成績
        self.subjects = []        # 属性：履修科目リスト
    
    def introduce(self):
        """メソッド：自己紹介"""
        return f"こんにちは、{self.name}です。学生IDは{self.student_id}です。"
    
    def set_grade(self, grade):
        """メソッド：成績を設定"""
        if 0 <= grade <= 100:
            self.grade = grade
            print(f"{self.name}の成績を{grade}点に設定しました")
        else:
            print("成績は0-100の範囲で入力してください")
    
    def add_subject(self, subject):
        """メソッド：履修科目を追加"""
        self.subjects.append(subject)
        print(f"{self.name}が{subject}を履修しました")
    
    def show_info(self):
        """メソッド：学生情報を表示"""
        print(f"名前: {self.name}")
        print(f"学生ID: {self.student_id}")
        print(f"成績: {self.grade}点")
        print(f"履修科目: {', '.join(self.subjects) if self.subjects else 'なし'}")
        print("-" * 30)

# クラスのテスト用
if __name__ == "__main__":
    # インスタンス生成
    student1 = Student("田中太郎", "S001")
    student2 = Student("佐藤花子", "S002", 85)
    
    # メソッドの呼び出し
    print(student1.introduce())
    student1.set_grade(92)
    student1.add_subject("Python基礎")
    student1.add_subject("データサイエンス")
    student1.show_info()