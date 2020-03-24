import sys

def readFile(input):
    f = open(input, "r")
    matrix = []
    nLine = f.read().split('\n')

    for i in range (4):
        num = nLine[i].split(' ')
        if len(num) == 5:
            empty = num.index('')
            num.pop(empty)
        matrix.append(num)

    return matrix

def matrixPrint(matrix):
    print('-------------')
    for i in range (4):
        for j in range (4):
            if matrix[i][j] == '':
                sys.stdout.write('|  ')
            elif int(matrix[i][j]) < 10:
                sys.stdout.write('| ' + matrix[i][j])
            else:
                sys.stdout.write('|' + matrix[i][j])
        print('|' + '\n-------------');


matrix = readFile("input.txt")
matrixPrint(matrix)


