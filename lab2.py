"""a це i та b j"""
def main():
    try:
        a = int(input("Введіть число від -128 до 127 a: ")) 
        b = int(input("Введіть число від -128 до 127 b: "))
        n = int(input("Введіть число від -128 до 127 n: "))
        m = int(input("Введіть число від -128 до 127 m: "))

        C = 2
        S = 0

        if a > n or b > m:
            print("Помилка: неправильні межі")
            return

        for i in range(a, n + 1):
            for j in range(b, m + 1):
                if i + C == 0:
                    print("Помилка: ділення на нуль")
                    return

                S += (i - j) / (i + C)

        print("Результат S =", S)

    except ValueError:
        print("Помилка: потрібно вводити цілі числа")


if __name__ == "__main__":
    main()
