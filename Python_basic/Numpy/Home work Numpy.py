# Домашнее задание по лекции "Библиотека numpy. Вычислительные задачи."
# Преподаватель: Константин Башевой
# Домашнее задание
import numpy as np

# Задание 1
# Создайте numpy array с элементами от числа N до 0 (например, для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])).
N = 10
nu_lsat_test = np.arange(0, N)
print(nu_lsat_test)
nu_lsat_test = np.arange(0, N)[::-1]
print(nu_lsat_test, type(nu_lsat_test))



# Задание 2
# Создайте диагональную матрицу с элементами от N до 0. Посчитайте сумму ее значений на диагонали.
N = 20
test_arr = np.arange(0, N)
diag_arr = np.diag(test_arr)
print(diag_arr)
print(sum(np.diag(diag_arr)))



# Задание 3
# Решите систему уравнений:
# 4x + 2y + z = 4
# x + 3y = 12
# 5y + 4z = -3
a = np.array([[4., 2., 1.], [1., 3., 0.], [0., 5., 4.]])
b = np.array([4., 12., -3.])
result = np.linalg.solve(a, b)
print(result)



M2 = np.array([[1., 0., 1., 0.], [-1., 1., -2., 1.], [4., 0., 1., -2.], [-4., 4., 0., 1.]]) # Матрица (левая часть системы)
v2 = np.array([2., -2., 0., 5.]) # Вектор (правая часть системы)
result_test = np.linalg.solve(M2, v2)
print(result_test)
