class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"{self.name}の成績を{grade}点に設定しました")
        else:
            print("成績は0-100の範囲で入力してください")
    
    def get_average(self):
        if not self.grades:
            print(f"{self.name}の成績が入力されていません")
        else:
            print(f"平均点は{sum(self.grades) / len(self.grades)}点です")
    
    def get_info(self):
        print(f"ID: {self.student_id}")
        print(f"名前: {self.name}")
        print(f"平均点:{sum(self.grades) / len(self.grades)}")