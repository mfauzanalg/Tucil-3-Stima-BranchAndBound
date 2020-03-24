import sys
import heapq
from queue import PriorityQueue
from copy import deepcopy

class Matrix:
    matrix = []
    bobot = 0

    def __init__(self):    
        self.matrix = []
        self.bobot = 0
    
    def __init__(self, mat):
        self.matrix = mat
        self.bobot = 0

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

    def search(self, x):
        p = Point()
        found = False
        i = 0
        while i < 4 and not(found):
            j = 0
            while j < 4 and not(found):
                if self.matrix[i][j] == x:
                    p.x = i
                    p.y = j
                    found = True
                j+=1
            i+=1
        return p
    

    def moveUp(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.searc('')
        m.matrix[p.x][p.y] = self.matrix[p.x-1][p.y]
        m.matrix[p.x-1][p.y] = ''
        return m
    
    def moveRight(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.search('')
        m.matrix[p.x][p.y] = self.matrix[p.x][p.y+1]
        m.matrix[p.x][p.y+1] = ''
        return m
    
    def moveDown(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.search('')
        m.matrix[p.x][p.y] = self.matrix[p.x+1][p.y]
        m.matrix[p.x+1][p.y] = ''
        return m
    
    def moveLeft(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.search('')
        m.matrix[p.x][p.y] = self.matrix[p.x][p.y-1]
        m.matrix[p.x][p.y-1] = ''
        return m

    def fungsiKurangI(self, z):
        ret = 0
        z = str(z)
        p = self.search(z)
        if z == '':
            z = 16

        for j in range (p.y, 4):
            this = self.matrix[p.x][j]
            if (this != '' and int(this) < int(z)):
                ret += 1

        for i in range (p.x+1, 4):
            for j in range (0, 4):
                this = self.matrix[i][j]
                if (this != '' and int(this) < int(z)):
                    ret += 1
        return ret

    def fungsiKurangAll(self):
        ret = 0
        for i in range (1, 16):
            ret += self.fungsiKurangI(i)
        ret += self.fungsiKurangI('')
        p = self.search('')
        if (((p.x+p.y)%2) == 1):
            ret += 1
        return ret

    def myBobot(self):
        ret = 0
        value = 1
        for i in range (3):
            for j in range (4):
                if (self.matrix[i][j] != str(value)):
                    ret+=1
                    print(str(i) + " " + str(j))
                value+=1
        
        for j in range (3):
            if (self.matrix[3][j] != str(value)):
                ret+=1
                print(str(i) + " " + str(j))
            value+=1 

        print(ret)

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
mat.myBobot()
