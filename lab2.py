class MatrixCalculator:
    def multiply_matrices(self, A, B):
        if not A or not B or not A[0] or not B[0]:
            raise ValueError("Матриці не можуть бути порожніми або мати порожні рядки")

        if len(A[0]) != len(B):
            raise ValueError("Матриці неможливо перемножити")

        C = []

        for i in range(len(A)):
            row = []

            for j in range(len(B[0])):
                element = 0.0

                for k in range(len(B)):
                    element += A[i][k] * B[k][j]

                row.append(element)

            C.append(row)

        return C

    def sum_max_elements_in_rows(self, matrix):
        total = 0.0

        for row in matrix:
            if not row:
                raise ValueError("Рядок матриці C не може бути порожнім")

            total += max(row)

        return total

    def print_matrix(self, matrix):
        for row in matrix:
            for element in row:
                print(f"{element:8.2f}", end=" ")
            print()

    def main(self):
        try:
            A = [
                [1.0, 2.0],
                [3.0, 4.0]
            ]

            B = [
                [5.0, 6.0],
                [7.0, 8.0]
            ]

            C = self.multiply_matrices(A, B)

            result = self.sum_max_elements_in_rows(C)

            print("Матриця A:")
            self.print_matrix(A)

            print("\nМатриця B:")
            self.print_matrix(B)

            print("\nМатриця C = A × B:")
            self.print_matrix(C)

            print("\nСума найбільших елементів кожного рядка матриці C =", result)

        except ValueError as e:
            print("Помилка:", e)


if __name__ == "__main__":
    calculator = MatrixCalculator()
    calculator.main()
