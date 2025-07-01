from grade_manager import GradeManager

def print_menu():
    print("-"*30)
    print("1. 学生を追加")
    print("2. 成績を追加")
    print("3. 全ての学生を表示")
    print("4. 最高成績の学生を表示")
    print("5. 終了")
    print("-"*30)

def setup_sample_data(manager: GradeManager):
    manager.add_student("緑谷 出久", "S001")
    manager.add_student("麗日 お茶子", "S002")
    manager.add_student("八百万 百", "S003")

    manager.add_grade_to_student("S001", 85)
    manager.add_grade_to_student("S001", 92)
    manager.add_grade_to_student("S002", 78)
    manager.add_grade_to_student("S002", 88)
    manager.add_grade_to_student("S003", 95)
    manager.add_grade_to_student("S003", 100)
    print("\nサンプルデータを追加しました。\n")

def main():
    manager = GradeManager()
    setup_sample_data(manager)

    while True:
        print_menu()
        choice = input("メニューを選択してください (1-5): ")

        if choice == '1':
            name = input("追加する学生の名前を入力してください: ")
            student_id = input("追加する学生のIDを入力してください: ")
            manager.add_student(name, student_id)

        elif choice == '2':
            student_id = input("成績を追加する学生のIDを入力してください: ")
            while True:
                try:
                    grade_str = input("追加する成績 (0-100) を入力してください: ")
                    grade = int(grade_str)
                    manager.add_grade_to_student(student_id, grade)
                    break
                except ValueError:
                    print("エラー: 数値を入力してください。")

        elif choice == '3':
            manager.show_all_students()

        elif choice == '4':
            manager.show_top_student()

        elif choice == '5':
            print("システムを終了します。")
            break

        else:
            print("1-5の数字を入力してください。")

        input("\n続けるにはEnterキーを押してください")


if __name__ == "__main__":
    main()