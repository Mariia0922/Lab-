def multiply_matrices(A, B):
    if not A or not B:
        raise ValueError("Матриці не можуть бути порожніми")

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


def sum_max_elements_in_rows(matrix):
    total = 0.0

    for row in matrix:
        total += max(row)

    return total


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:8.2f}", end=" ")
        print()


def main():
    try:
        A = [
            [1.0, 2.0],
            [3.0, 4.0]
        ]

        B = [
            [5.0, 6.0],
            [7.0, 8.0]
        ]

        C = multiply_matrices(A, B)
        result = sum_max_elements_in_rows(C)

        print("Матриця A:")
        print_matrix(A)

        print("\nМатриця B:")
        print_matrix(B)

        print("\nМатриця C = A × B:")
        print_matrix(C)

        print("\nСума найбільших елементів кожного рядка матриці C =", result)

    except ValueError as e:
        print("Помилка:", e)


if __name__ == "__main__":
    main()
