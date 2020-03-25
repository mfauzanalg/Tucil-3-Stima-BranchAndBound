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
    aras = 1
    path = []

    # Konstruktor
    def __init__(self, mat):
        self.matrix = mat
        self.bobot = -1
        self.stepBefore = ""
        index = 1
        aras = 1
        path = []

    # Matrix less than
    def __lt__(self, other):
        if self.bobot == other.bobot:
            if self.index > other.index:
                return True
            else:
                return False
        elif self.bobot < other.bobot:
            return True
        else:
            return False

    # Print matrix
    def printMat(self):
        print('-------------')
        for i in range (4):
            for j in range (4):
                if self.matrix[i][j] == '':
                    sys.stdout.write('|  ')
                elif int(self.matrix[i][j]) < 10:
                    sys.stdout.write('| ' + self.matrix[i][j])
                else:
                    sys.stdout.write('|' + self.matrix[i][j])
            print('|');
        print('-------------')

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
        m.path = deepcopy(self.path)
        m.matrix = deepcopy(self.matrix)
        p = self.search('')
        m.matrix[p.x][p.y] = self.matrix[p.x-1][p.y]
        m.matrix[p.x-1][p.y] = ''
        return m
    
    # Move empty space right
    def moveRight(self):
        m = Matrix([])
        m.path = deepcopy(self.path)
        m.matrix = deepcopy(self.matrix)
        p = self.search('')
        m.matrix[p.x][p.y] = self.matrix[p.x][p.y+1]
        m.matrix[p.x][p.y+1] = ''
        return m
    
    # Move empty space down
    def moveDown(self):
        m = Matrix([])
        m.path = deepcopy(self.path)
        m.matrix = deepcopy(self.matrix)
        p = self.search('')
        m.matrix[p.x][p.y] = self.matrix[p.x+1][p.y]
        m.matrix[p.x+1][p.y] = ''
        return m
    
    # Move empty space left
    def moveLeft(self):
        m = Matrix([])
        m.path = deepcopy(self.path)
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
            print ("X = 1")
        else:
            print ("X = 0")
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

   # Print path
    def printPath(self):
        m = Matrix([])
        m.matrix = deepcopy(self.matrix)
        for i in range (len(self.path)):
            print("Step ke " + str(i+1) + " : " + self.path[i])
            if (self.path[i] == "U"):
                m = m.moveUp()
                m.printMat()
            elif (self.path[i] == "R"):
                m = m.moveRight()
                m.printMat()
            elif (self.path[i] == "D"):
                m = m.moveDown()
                m.printMat()
            else:
                m = m.moveLeft()
                m.printMat()

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
matHidup = []
matGen = []
empty = Point()
stop = False
stepBefore = ""
matGen = set()

#getInput
print ("pilih file test")
print("1. test1.txt")
print("2. test2.txt")
print("3. test3.txt")
print("4. test4.txt")
print("5. test5.txt")
sys.stdout.write("input angka 1-5 : ")

select = input()
while (int(select) > 5 or int(select) < 1):
    print("input tidak valid")
    sys.stdout.write("input angka 1-5 : ")
    select = input()

if (int(select) == 1):
    file = "../test/test1.txt"
elif (int(select) == 2):
    file = "../test/test2.txt"
elif (int(select) == 3):
    file = "../test/test3.txt"
elif (int(select) == 4):
    file = "../test/test4.txt"
elif (int(select) == 5):
    file = "../test/test5.txt"


# Load file
matExpand = Matrix(readFile(file))
matAwal = Matrix(readFile(file))

# Print kondisi awal
print("Kondisi Awal Puzzle")
matExpand.printMat()
print("")

# Nilai fungsi kurang untuk setiap petak
print("Fungsi Kurang untuk setiap ubin")
print("-------------------------")
print ("Ubin-i" + "   FungsiKurang(i)")
for i in range (1, 16):
    if (i < 10):
        print("   " + str(i) + "           " + str(matExpand.fungsiKurangI(i)))
    else:
        print("   " + str(i) + "          " + str(matExpand.fungsiKurangI(i)))
print("   16" + "          " + str(matExpand.fungsiKurangI('')))
print("-------------------------\n")

# Nilai dari Kurang(i)+X
Y = matExpand.fungsiKurangAll()
print("Sigma (KURANG(i)) + X = " + str(Y))
if (int(select) == 3):
    print("Mohon tunggu banyak simpul yang di generate...")

# Start execution
start_time = time.time()
# Apakah Permasalahan dapat diselesaikan
if (Y % 2 == 1):
    print("Permasalahan Puzzle tidak dapat diselesaikan")
else:
    matGen.add(str(matExpand.matrix))
    heapq.heapify(matHidup)

    # Priority : Up, Right, Down, Left
    while not(matExpand.myBobot() == 0):
        empty = matExpand.search('')

        # Ekspan Up
        if (empty.x != 0 and stepBefore != "down"):
            matUp = matExpand.moveUp()
            if not(str(matUp.matrix) in matGen):
                matUp.aras = matExpand.aras + 1
                matUp.bobot = matUp.myBobot() + matUp.aras
                matUp.stepBefore = "up"
                index += 1
                matUp.index = index
                heapq.heappush(matHidup,matUp)
                matGen.add(str(matUp.matrix))
                matUp.path.append("U")
          
        # Ekspan Right
        if (empty.y != 3 and stepBefore != "left"):
            matRight = matExpand.moveRight()
            if not(str(matRight.matrix) in matGen):
                matRight.aras = matExpand.aras + 1
                matRight.bobot = matRight.myBobot() + matRight.aras    
                matRight.stepBefore = "right"    
                index += 1
                matRight.index = index
                heapq.heappush(matHidup,matRight)
                matGen.add(str(matRight.matrix))
                matRight.path.append("R")

        # Ekspan Down
        if (empty.x != 3 and stepBefore != "up"):
            matDown = matExpand.moveDown()
            if not(str(matDown.matrix) in matGen):
                matDown.aras = matExpand.aras + 1
                matDown.bobot = matDown.myBobot() + matDown.aras
                matDown.stepBefore = "down"
                index += 1
                matDown.index = index
                heapq.heappush(matHidup,matDown)
                matGen.add(str(matDown.matrix))
                matDown.path.append("D")

        # Ekspan Left
        if (empty.y != 0 and stepBefore != "right"):
            matLeft = matExpand.moveLeft()
            if not(str(matLeft.matrix) in matGen):
                matLeft.aras = matExpand.aras + 1
                matLeft.bobot = matLeft.myBobot() + matLeft.aras
                matLeft.stepBefore = "left"
                index += 1
                matLeft.index = index
                heapq.heappush(matHidup,matLeft)
                matGen.add(str(matLeft.matrix))
                matLeft.path.append("L")

        # get matExpand from matHidup
        matExpand = heapq.heappop(matHidup)
        stepBefore = matExpand.stepBefore
        
    # Jumlah Simpul
    print("Jumlah simpul yang dibangkitkan = " + str(matExpand.index))
    print("Urutan penyelesaian = " + str(matExpand.path) + "\n")
    matAwal.path = deepcopy(matExpand.path)
    matAwal.printPath()

# End Execution
end_time = time.time()

# Execution time
waktu = end_time - start_time
print("Waktu eksekusi = " + str(waktu) + " seconds")
