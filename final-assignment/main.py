import numpy as np
from score_analyzer import ScoreAnalyzer

def main():
    sample_scores = np.array([
        [85, 92, 78],
        [90, 88, 94],
        [76, 80, 85],
        [98, 95, 99],
        [68, 75, 70]
    ])

    print("--------- サンプルスコアデータ ---------")
    print(sample_scores)
    print("-" * 40)

    analyzer = ScoreAnalyzer(sample_scores)

    student_averages = analyzer.calculate_student_averages()
    print("各学生の平均点:")
    for i, avg in enumerate(student_averages):
        print(f"  学生{i} の平均点：{avg:.2f}")
    print("-" * 40)


    subject_averages = analyzer.calculate_subject_averages()
    print("各科目の平均点:")
    for i, avg in enumerate(subject_averages):
        print(f"  科目{i} の平均点：{avg:.2f}")
    print("-" * 40)


    top_student_index = analyzer.get_top_student_index()
    print(f"合計点が最も高い学生：学生{top_student_index}")
    print("-" * 40)

if __name__ == "__main__":
    main()