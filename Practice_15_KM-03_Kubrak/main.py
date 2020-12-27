from factorial import factorial
from exp_root import exponentiation, root
from logarithm import logarithm

if __name__ == '__main__':
    print("________________________________")
    print("   Список можливих функцій:     ")
    print("________________________________")
    print("|| 1. Факторіал числа         ||")
    print("|| 2. Піднесення до квадрату  ||")
    print("|| 3. Піднесення до кубу      ||")
    print("|| 4. Квадратний корінь       ||")
    print("|| 5. Кубічний корінь         ||")
    print("|| 6. Логарифм числа          ||")
    print("|| 7. Натуральний логарифм    ||")
    print("|| 8. Десятковий логарифм     ||")
    print("________________________________")

    lst = ['1','2','3','4','5','6','7','8']
    while True:
        x = input("Виберіть номер функції: ")
        if x not in lst:
            print("Такого номеру не існує")
            continue
        if x == "1":
            try:
                n = int(input("Введіть довільне ціле додатнє число: "))
                if n <= 0:
                    print("Ви ввели недопустиме значення")
                    continue
            except ValueError:
                print('Ви ввели недопустиме значення')
                continue
            print(f"Факторіл числа {n} = {factorial.fact(n)}")
        elif x == "2":
            try:
                n = float(input("Введіть довільне число: "))
            except ValueError:
                print('Ви ввели недопустиме значення')
                continue
            print(f"Квадрат числа {n} = {exponentiation.exp2(n)}")
        elif x == "3":
            try:
                n = float(input("Введіть довільне число: "))
            except ValueError:
                print('Ви ввели недопустиме значення')
                continue
            print(f"Куб числа {n} = {exponentiation.exp3(n)}")
        elif x == "4":
            try:
                n = float(input("Введіть довільне додатнє число: "))
                if n <= 0:
                    print("Ви ввели недопустиме значення")
                    continue
            except ValueError:
                print('Ви ввели недопустиме значення')
                continue
            print(f"Корінь квадратний з числа {n} = {root.root2(n)}")
        elif x == "5":
            try:
                n = float(input("Введіть довільне додатнє число: "))
                if n <= 0:
                    print("Ви ввели недопустиме значення")
                    continue
            except ValueError:
                print('Ви ввели недопустиме значення')
                continue
            print(f"Корінь кубічний з числа {n} = {root.root3(n)}")
        elif x == "6":
            try:
                a = int(input("Введіть додатнє ціле значення основи а (окрім 1): "))
                if a <= 0 or a == 1:
                    print("Ви ввели недопустиме значення")
                    continue
            except ValueError:
                print('Ви ввели недопустиме значення')
                continue
            try:
                b = int(input("Введіть додатнє ціле число b: "))
                if b <= 0:
                    print("Ви ввели недопустиме значення")
                    continue
            except ValueError:
                print('Ви ввели недопустиме значення')
                continue
            print(f"Логарифм числа {b} з основою {a} = {logarithm.log(a, b)}")
        elif x == "7":
            try:
                b = float(input("Введіть довільне додатнє число: "))
                if b <= 0:
                    print("Ви ввели недопустиме значення")
                    continue
            except ValueError:
                print('Ви ввели недопустиме значення')
                continue
            print(f"Натуральний логарифм числа {b} = {logarithm.ln(b)}")
        elif x == "8":
            try:
                b = float(input("Введіть довільне додатнє число: "))
                if b <= 0:
                    print("Ви ввели недопустиме значення")
                    continue
            except ValueError:
                print('Ви ввели недопустиме значення')
                continue
            print(f"Десятковий логарифм числа {b} = {logarithm.lg(b)}")