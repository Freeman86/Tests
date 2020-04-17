
from sys import argv

path = argv[1]  # указываю путь к файлу

with open(path, 'r') as f:       # читаю файл
    file = f.read().splitlines()

data = list(map(int, file))  # преобразую строки в числа


def median(data):          # медиана
    size = len(data)
    sort = sorted(data)
    k = size // 2
    if size % 2 == 0:
        return '{:.2f}'.format(0.5 * (sort[k] + sort[k-1]))
    else:
        return '{:.2f}'.format(sort[k])


def percentile(data):                     #  процентиль
    pecentile_90 = (len(data) - 1) * 0.9
    return '{:.2f}'.format(pecentile_90)


# специально разными сортироваками показал как можно находить max и min

def max_num(data):                   # максимальное число
    for i in range(len(data)):
        idx_min = i
        for j in range(i + 1, len(data)):
            if data[j] < data[idx_min]:
                idx_min = j
            data[idx_min], data[i] = data[i], data[idx_min]
    return '{:.2f}'.format(data[len(data)-1])

def min_num(data):                        # минимальное число
    for i in range(1, len(data)):
        spam = data[i]
        j = i
        while data[j - 1] > spam and j > 0:
            data[j] = data[j - 1]
            j -= 1

        data[j] = spam
    return '{:.2f}'.format(data[0])

def average(data):                              # среднее
    return '{:.2f}'.format(sum(data) / len(data))


print(percentile(data) + '\n')
print(median(data) + '\n')
print(max_num(data) + '\n')
print(min_num(data) + '\n')
print(average(data) + '\n')

