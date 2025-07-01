from student import Student

class GradeManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, student_id) -> bool:
        if self.find_student(student_id):
            print(f"エラー: 学生ID {student_id} は既に使用されています。")
            return False

        new_student = Student(name, student_id)
        self.students.append(new_student)
        print(f"学生「{name}」(ID: {student_id}) を追加しました。")
        return True
    
    def find_student(self, student_id) -> Student | None:
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def add_grade_to_student(self, student_id, grade):
        student = self.find_student(student_id)
        if student:
            student.add_grade(grade)
        else:
            print(f"エラー: 学生ID {student_id} が見つかりません。")
    
    def show_all_students(self):
        print("\n--- 全ての学生情報 ---")
        if not self.students:
            print("学生が登録されていません。")
        else:
            for student in self.students:
                print(student.get_info())
        print("---------------------\n")
    
    def show_top_student(self):
        print("\n--- 最高成績の学生 ---")
        if not self.students:
            print("学生が登録されていません。")
            print("----------------------\n")
            return

        students_with_grades = [s for s in self.students if s.grades]

        if not students_with_grades:
            print("成績が登録されている学生がいません。")
            print("----------------------\n")
            return

        top_student = max(students_with_grades, key=lambda student: student.get_average())
        print(top_student.get_info())
        print("----------------------\n")