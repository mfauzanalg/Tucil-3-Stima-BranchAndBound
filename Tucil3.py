# Library
import sys
import heapq
import time
from copy import deepcopy

# Kelas Matrix
class Matrix:
    matrix = []
    bobot = 0
    stepBefore = ""

    # Konstruktor
    def __init__(self, mat):
        self.matrix = mat
        self.bobot = 0
        self.stepBefore = ""

    # Matrix less than
    def __lt__(self, other):
        return self.bobot < other.bobot

    # Matrix equal
    def __eq__(self, other):
        return self.bobot == other.bobot

    # Print matrix
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

    # Search point of x
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
    
    # Move empty space up
    def moveUp(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.search('')
        m.matrix[p.x][p.y] = self.matrix[p.x-1][p.y]
        m.matrix[p.x-1][p.y] = ''
        return m
    
    # Move empty space right
    def moveRight(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.search('')
        m.matrix[p.x][p.y] = self.matrix[p.x][p.y+1]
        m.matrix[p.x][p.y+1] = ''
        return m
    
    # Move empty space down
    def moveDown(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.search('')
        m.matrix[p.x][p.y] = self.matrix[p.x+1][p.y]
        m.matrix[p.x+1][p.y] = ''
        return m
    
    # Move empty space left
    def moveLeft(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        p = self.search('')
        m.matrix[p.x][p.y] = self.matrix[p.x][p.y-1]
        m.matrix[p.x][p.y-1] = ''
        return m

    # Menghitung fungsi kurang untuk i
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

    # Menghitung fungsi kurang untuk sebuah matriks
    def fungsiKurangAll(self):
        ret = 0
        for i in range (1, 16):
            ret += self.fungsiKurangI(i)
        ret += self.fungsiKurangI('')
        p = self.search('')
        if (((p.x+p.y)%2) == 1):
            ret += 1
        return ret

    # Menghitung g(i) matriks
    def myBobot(self):
        ret = 0
        value = 1
        for i in range (3):
            for j in range (4):
                if (self.matrix[i][j] != str(value)):
                    ret+=1
                value+=1
        
        for j in range (3):
            if (self.matrix[3][j] != str(value)):
                ret+=1
            value+=1 
        return ret

# Kelas Point
class Point:
    def __init__(self):    
        self.x = 0
        self.y = 0

# Membaca file eksternal
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


# Main program
aras = 1
track = []
matHidup = []
empty = Point()
stop = False
stepBefore = ""

# Load file
matExpand = Matrix(readFile("input.txt"))
track.append(matExpand)
heapq.heapify(matHidup)

# Priority : Up, Right, Down, Left
# Start execution
start_time = time.time()
while not(stop):
    if(matExpand.myBobot() == 0):
        stop = True
        
    empty = matExpand.search('')
    if (empty.x != 0 and stepBefore != "down"):
        matUp = matExpand.moveUp()
        matUp.bobot = matUp.myBobot() + aras
        matUp.stepBefore = "up"
        heapq.heappush(matHidup,matUp)
        
    if (empty.y != 3 and stepBefore != "left"):
        matRight = matExpand.moveRight()
        matRight.bobot = matRight.myBobot() + aras    
        matRight.stepBefore = "right"    
        heapq.heappush(matHidup,matRight)

    if (empty.x != 3 and stepBefore != "up"):
        matDown = matExpand.moveDown()
        matDown.bobot = matDown.myBobot() + aras
        matDown.stepBefore = "down"
        heapq.heappush(matHidup,matDown)

    if (empty.y != 0 and stepBefore != "right"):
        matLeft = matExpand.moveLeft()
        matLeft.bobot = matLeft.myBobot() + aras
        matLeft.stepBefore = "left"
        heapq.heappush(matHidup,matLeft)

    heapq.heapify(matHidup)
    matExpand = heapq.heappop(matHidup)
    track.append(matExpand)
    aras += 1
    stepBefore = matExpand.stepBefore
end_time = time.time()

# track = track[:-1]
for i in range (len(track)):
    track[i].print()

waktu = start_time - end_time   
