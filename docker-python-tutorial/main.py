import numpy as np

# numpyで配列を作成
numbers = np.array([1, 2, 3, 4, 5])
print("作成した配列:", numbers)

# 配列の計算
print("配列の合計:", np.sum(numbers))
print("配列の平均:", np.mean(numbers))
print("配列の最大値:", np.max(numbers))

# 2次元配列の作成と表示
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2次元配列:")
print(matrix)
print("行列の形状:", matrix.shape)
