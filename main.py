# from mypackage import m1, m2

# print("Задача 1:")
# m1.task1()

# print("\nЗадача 2:")
# m2.task2()
#лёгкий уровень
class Range:
    def __init__(self, left: float, right: float):
        self.left = left
        self.right = right

    def get_info(self) -> str:
        length = self.right - self.left
        return f'Квадрат длины диапазона: {length ** 2:.2f}'

    def process_values(self) -> float:
        return self.left + self.right


def main():
    left_value = float(input("Введите левую границу диапазона: "))
    right_value = float(input("Введите правую границу диапазона: "))

    range_obj = Range(left_value, right_value)

    print(range_obj.get_info())
    print(f'Сумма границ: {range_obj.process_values()}')


if __name__ == "__main__":
    main()
