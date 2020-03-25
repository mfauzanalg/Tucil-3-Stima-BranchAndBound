# Library
import sys
import heapq
import time
from copy import deepcopy

# Kelas Matrix
class Matrix:
    matrix = []
    bobot = -1
    stepBefore = ""
    index = 1

    # Konstruktor
    def __init__(self, mat):
        self.matrix = mat
        self.bobot = -1
        self.stepBefore = ""
        index = 1

    # Matrix less than
    def __lt__(self, other):
        if self.myBobot() == other.myBobot():
            if self.index < other.index:
                return True
            else:
                return False
        elif self.myBobot() < other.myBobot():
            return True
        else:
            return False

        

    def same (self, other):
        return self.matrix == other.matrix

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
index = 1
aras = 1
track = []
matHidup = []
matGen = []
empty = Point()
stop = False
stepBefore = ""

# Load file
matExpand = Matrix(readFile("input.txt"))

# Print kondisi awal
print("Kondisi Awal Puzzle")
matExpand.print()

track.append(matExpand)
matGen.append(matExpand)

heapq.heapify(matHidup)

print("Nilai fungsi kurang dari puzzle : " + str(matExpand.fungsiKurangAll()))

# Priority : Up, Right, Down, Left
# Start execution
start_time = time.time()
while not(matExpand.myBobot() == 0):
    empty = matExpand.search('')

    # Ekspan Up
    if (empty.x != 0 and stepBefore != "down"):
        matUp = matExpand.moveUp()

        isSame = False
        i = 0
        while (i < len(matGen) and not(isSame)) :
            isSame = matUp.same(matGen[i])
            i+=1

        # print(isSame)
        if not(isSame):
            matUp.bobot = matUp.myBobot() + aras
            matUp.stepBefore = "up"
            index += 1
            matUp.index = index
            heapq.heappush(matHidup,matUp)
            matGen.append(matUp)
            # matUp.print()
            # print(matUp.bobot)
    
    # Ekspan Right
    if (empty.y != 3 and stepBefore != "left"):
        matRight = matExpand.moveRight()

        isSame = False
        i = 0
        while (i < len(matGen) and not(isSame)) :
            isSame = matRight.same(matGen[i])
            i+=1

        # print(isSame)
        if not(isSame):
            matRight.bobot = matRight.myBobot() + aras    
            matRight.stepBefore = "right"    
            index += 1
            matRight.index = index
            heapq.heappush(matHidup,matRight)
            matGen.append(matRight)
            # matRight.print()
            # print(matRight.bobot)

    # Ekspan Down
    if (empty.x != 3 and stepBefore != "up"):
        matDown = matExpand.moveDown()

        isSame = False
        i = 0
        while (i < len(matGen) and not(isSame)) :
            isSame = matDown.same(matGen[i])
            i+=1

        # print(isSame)
        if not(isSame):
            matDown.bobot = matDown.myBobot() + aras
            matDown.stepBefore = "down"
            index += 1
            matDown.index = index
            heapq.heappush(matHidup,matDown)
            matGen.append(matDown)
            # matDown.print()
            # print(matDown.bobot)

    # Ekspan Left
    if (empty.y != 0 and stepBefore != "right"):
        matLeft = matExpand.moveLeft()

        isSame = False
        i = 0
        while (i < len(matGen) and not(isSame)) :
            isSame = matLeft.same(matGen[i])
            i+=1

        # print(isSame)
        if not(isSame):
            matLeft.bobot = matLeft.myBobot() + aras
            matLeft.stepBefore = "left"
            index += 1
            matLeft.index = index
            heapq.heappush(matHidup,matLeft)
            matGen.append(matLeft)
            # matLeft.print()
            # print(matLeft.bobot)

    print(len(matGen))
    
    # for x in matHidup:
    #     print(str(x.index) + " ", end ='')
    
    # print()

    # for x in matHidup:
    #     print(str(x.bobot) + "(" + str(x.index) + ")" + " ", end ='')

    # print()

    # get matExpand from matHidup
    # heapq.heapify(matHidup)
    matExpand = heapq.heappop(matHidup)
    # print("ini yg diekspan " + str(matExpand.bobot))

    # time.sleep(3)
    matExpand.print()
    print("my bobot : " + str(matExpand.myBobot()))
    print("aras : " + str(aras))
    print("step before : " + matExpand.stepBefore)
    print("index : " + str(matExpand.index))
    print()

    


    track.append(matExpand)
    # aras = f(i)
    aras += 1
    stepBefore = matExpand.stepBefore



end_time = time.time()
# End Execution



# Print langkah
# for i in range (len(track)):
#     track[i].print()

# Execution time
waktu = end_time - start_time
print(waktu)

