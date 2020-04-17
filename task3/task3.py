
from sys import argv

path = argv[1]

def read_Cash(path):  # функция читает все пять файлов и собирает их них один список списков
    cash = []
    temp = []
    for i in range(1, 6):
        with open(path + '\Cash' + str(i) + '.txt', 'r') as f:       # читаю файл
            file = f.read().splitlines()
            for j in range(len(file)):
                temp = list(map(float, file)) # преобразую строки в числа
        cash.append(temp)
    return cash

def summ_all_interval(cash):        # функция суммирует все значения в каждом интервале времени
    summ = [sum(i) for i in zip(*cash)]

    def max_interval(summ):         # функция вычисляет интервал с максимальным значением
        max_count = 0
        max_int = 0
        for i in range(len(summ)):
            if summ[i] >= max_count:
                max_count = summ[i]
                max_int = (i+1)
        return max_int
    return max_interval(summ)


print(summ_all_interval(read_Cash(path)))
