# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.


def max_num() -> int:
    max_number: int = 0
    while True:
        n: int = int(input("Введите число: "))
        if n == 0:
            break
        if n > max_number:
            max_number = n
    return max_number
print(f"Максимальное значение  {max_num()} ")