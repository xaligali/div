#считываем данные из файла
import sys

def div(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append([float(x) for x in line.split()])

    a = data[0][0]
    b = data[0][1]
    return a / b

if __name__ == '__main__':
    filename = sys.argv[1]
    div(filename)