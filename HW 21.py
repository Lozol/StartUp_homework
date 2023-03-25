#1.Напишіть клас для роботи з матрицями. Клас повинен створювати об'єкт матриць з вкладених
# списків, виводити на друк, виконувати операції додавання, віднімання, множння на число ,
# множення на матрицю, транспонування. Передбачте можливість приведення матриць для операції
# додавання і віднімання, та обробку виключних ситуацій для операцій множення матриці на матрицю.
from copy import deepcopy

class MyMatrix:
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def print_matrix(self):
        for i in range(len(self)):
            for j in range(len(self[i])):
                print(self[i][j], end=' ')
            print()

    def sum_matrix(self, A, B ):
        if isinstance(A, int) and isinstance(B, float):
            print("У матриць різні типи даних")
        elif len(A)!= len(B) and len(A[0])!= len(B[0]) :
            return 'Неможна додавати матриці різних розмірностей'
        else:
            result_matrix = [[A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
            return result_matrix


    def div_matrix(self,A, B ):
        if isinstance(A, int) and isinstance(B, float):
            print("У матриць різні типи даних")
        elif len(A)!= len(B) and len(A[0])!= len(B[0]) :
            return 'Неможна віднімати матриці різних розмірностей'
        else:
            result_matrix= [[A[i][j] - B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
            return result_matrix

    def mult_matrix_on_number(self, A, scalar):
        result_matrix = [[A[i][j]* scalar for j in range(len(A[0]))] for i in range(len(A))]
        return result_matrix

    def mult_matrixies(self,A,B):
        rows_A = len(A)
        cols_A = len(A[0])
        rows_B = len(B)
        cols_B = len(B[0])
        if isinstance(A, int) and isinstance(B, float):
            print("У матриць різні типи даних")
        elif len(A)!= len(B[0]):
            return 'Неможна помножити матриці таких розмірностей'
        else:
            result = [[0 for row in range(cols_B)] for col in range(rows_A)]

            for s in range(rows_A):
                for j in range(cols_B):
                    for k in range(cols_A):
                        result[s][j] += A[s][k] * B[k][j]
            return result

    def get_trans_matrix(self, A):
        n = len(A)
        for i in range(n - 1):
            for j in range(i + 1, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        return A


#2. напишіть код, який здійснює процес перетворення матриці, наведений у прикладі з презентації.


matrix1 =[[4, 2, 0], [1, 3, 2], [-1, 3, 10]]
matrix1[0], matrix1[1] = matrix1[1], matrix1[0]
matrix1[0]=[(matrix1[0][j] + matrix1[1][j])*(-4) for j in range(len(matrix1[0]))]
matrix1[1]=[matrix1[1][j]/(-2) for j in range(len(matrix1[1]))]
matrix1[2]=[matrix1[2][j]/6 for j in range(len(matrix1[2]))]
matrix1[1], matrix1[2] = matrix1[2], matrix1[1]
matrix1[2]=[(matrix1[2][j] + matrix1[1][j])*(-5) for j in range(len(matrix1[2]))]

