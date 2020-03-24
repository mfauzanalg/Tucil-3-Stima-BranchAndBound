import sys
from copy import deepcopy

class Matrix:
    matrix = []
    weight = 0

    def __init__(self):    
        self.matrix = []
        self.weight = 0
    
    def __init__(self, mat):
        self.matrix = mat
        self.weight = 0

    def print(self):
        print('-------------')
        for i in range (4):
            for j in range (4):
                if self.matrix[i][j] == '':
                    sys.stdout.write('|  ')
                elif int(self.matrix[i][j]) < 10:
                    sys.stdout.write('| ' + self.matrix[i][j])
                else:
                    sys.stdout.write('|' + self.matrix[i][j])
            print('|' + '\n-------------');

    def searchEmpty(self):
        p = Point()
        found = False
                
        i = 0
        while i < 4 and not(found):
            j = 0
            while j < 4 and not(found):
                if self.matrix[i][j] == '':
                    p.x = i
                    p.y = j
                    found = True
                j+=1
            i+=1
        return p
    

    def moveUp(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.searchEmpty()
        m.matrix[p.x][p.y] = self.matrix[p.x-1][p.y]
        m.matrix[p.x-1][p.y] = ''
        return m
    
    def moveRight(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.searchEmpty()
        m.matrix[p.x][p.y] = self.matrix[p.x][p.y+1]
        m.matrix[p.x][p.y+1] = ''
        return m
    
    def moveDown(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.searchEmpty()
        m.matrix[p.x][p.y] = self.matrix[p.x+1][p.y]
        m.matrix[p.x+1][p.y] = ''
        return m
    
    def moveLeft(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.searchEmpty()
        m.matrix[p.x][p.y] = self.matrix[p.x][p.y-1]
        m.matrix[p.x][p.y-1] = ''
        return m


class Point:
    def __init__(self):    
        self.x = 0
        self.y = 0
    

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

mat = Matrix(readFile("input.txt"))




