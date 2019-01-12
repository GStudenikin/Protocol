import copy
import random


# Euclidean algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n


# Linear group
class GL(object):
    def __init__(self, size, modulo, matrix = None):
        self.size = size
        self.modulo = modulo
        if(matrix == None):
            det = 0
            while(det == 0):
                self.matrix = self.gen()
                det = self.det_bar()
        else:
            self.matrix = matrix

    def __str__(self):
        return '\n'.join(('[' + ', '.join(str(e) for e in self.matrix[i]) + ']') for i in range(self.size))

    def __mul__(self, other):
        size = self.size
        res = []
        if(isinstance(other, GL)):
            for t in range(size):
                res.append([])
            temp = 0
            for i in range(size):
                for j in range(size):
                    for k in range(size):
                        temp += self.matrix[i][k] * other.matrix[k][j]
                    res[i].append(temp)
                    temp = 0
            return GL(size, self.modulo, res).mod()
        elif(isinstance(other, Vect)):
            for i in range(size):
                res.append(0)
            for i in range(size):
                for j in range(size):
                    res[i] += other[j] * self.matrix[j][i]
            for i in range(len(res)):
                res[i] %= self.modulo
            return Vect(self.size, self.modulo, res)

    def __pow__(self, other):
        res = self
        i = 1
        while i < other:
            res *= self
            i += 1
        return res

    def gen(self):
        matrix = []
        for i in range(self.size):
            matrix.append([random.randint(0, (self.modulo - 1)) for j in range(self.size)])
        return matrix

    def mod(self):
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] %= self.modulo
        return self

# Get maximum power of Cyclic group element
    def get_exp(self):
        i = 1
        temp = self
        one = [[1,0,0],[0,1,0],[0,0,1]]
        while temp.matrix != one:
            temp *= self
            i += 1
        return i

# Determimant compute by using Laplace Expansion
    def det(self):
        size = self.size
        if size == 1:
            return self.matrix[0][0]
        signum = 1
        determinant = 0
        for j in range(size):
            minor = self.minor(0, j)
            determinant += self.matrix[0][j] * signum * minor.det()
            signum *= -1
        return determinant % self.modulo

    def minor(self, i, j):
        minor = copy.deepcopy(self.matrix)
        del minor[i]
        for t in range(len(minor)):
            del minor[t][j]
        return GL(len(minor), self.modulo, minor)

# Transpose matrix
    def trans(self):
        size = self.size
        tr = []
        for i in range(size):
            tr.append([self.matrix[j][i] for j in range(size)])
        return GL(len(tr), self.modulo, tr)

# Adjugate matrix
    def adj(self):
        adj = []
        size = self.size
        for i in range(size):
            adj.append([0 for j in range(size)])
        for i in range(size):
            for j in range(size):
                minor = self.minor(i, j)
                adj[i][j] = ((-1) ** (i + j)) * minor.det_bar()
        return GL(self.size, self.modulo, adj).mod()

# Multiplication matrix by number
    def muln(self, n):
        matrix = copy.deepcopy(self.matrix)
        size = self.size
        for i in range(size):
            for j in range(size):
                matrix[i][j] *= n
        return GL(self.size, self.modulo, matrix).mod()

# Inverse of a matrix
    def inv(self):
        det = self.det_bar()
        inv = mulinv(det, self.modulo)
        adj = self.adj()
        trans = adj.trans()
        mul = trans.muln(inv)
        return mul.mod()

# Identity matrix
    def one(self):
        matrix = []
        for i in range(self.size):
            matrix.append([random.randint(1, (self.modulo - 1)) for j in range(self.size)])
        for t in range(self.size):
            for k in range(self.size):
                if t!= k:
                    matrix[t][k] = 0
                else:
                    matrix[t][k] = 1
        return matrix

# Bareiss's algorhitm to calculate determinant
    def det_bar(self):
        temp = copy.deepcopy(self)
        size = self.size
        j = 0
        i = 1
        while j <= size - 2:
            if temp.matrix[j][j] == 0:
                k = j+1
                while k < size:
                    if(temp.matrix[k][j]!=0):
                        temp.matrix[k], temp.matrix[j] = temp.matrix[j], temp.matrix[k]
                        for index in range(size):
                            temp.matrix[k][index] *= -1
                        break
                    else:
                        k += 1
                    if(k == size):
                        return 0
            ajj = temp.matrix[j][j]
            if (j == 0):
                d = 1
            else:
                d = temp.matrix[j - 1][j - 1]
                if(d == 0):
                    return temp.mod()
            while i <= size - 1:
                aij = temp.matrix[i][j]
                t = j
                while t <= size-1:
                    temp.matrix[i][t] = (ajj*temp.matrix[i][t] - aij*temp.matrix[j][t])//d
                    t += 1
                i += 1
            j += 1
            i = j+1
        temp = temp.mod()
        return temp.matrix[size-1][size-1]


# Special Linear group
class SL(GL):
    def __init__(self, size, modulo, matrix = None):
        self.size = size
        self.modulo = modulo
        if(matrix == None):
            det = 0
            while(det != 1):
                self.matrix = self.gen()
                det = self.det_bar()
        else:
            self.matrix = matrix


# Diagonal subgroup
class Diag(GL):
    def gen(self):
        matrix = []
        for i in range(self.size):
            matrix.append([random.randint(1, (self.modulo - 1)) for j in range(self.size)])
        for t in range(self.size):
            for k in range(self.size):
                if t!= k:
                    matrix[t][k]=0
        return matrix

    def det(self):
        determinant = 1
        for i in range(self.size):
            determinant *= self.matrix[i][i]
        return determinant % self.modulo

    def inv(self):
        matrix = []
        size = self.size
        for i in range(size):
            matrix.append([0 for j in range(size)])
        for i in range(size):
            matrix[i][i] = mulinv(self.matrix[i][i], self.modulo)
        return Diag(self.size, self.modulo, matrix)


# Cyclic group
class CG(GL):
    def __init__(self, other, st = None):
        self.size = other.size
        self.modulo = other.modulo
        one = self.one()
        if(st == None):
            st_t = random.randint(1, 1000)
            temp = (other ** st_t).matrix
            while(temp == one):
                st_t = random.randint(1, 1000)
                temp = (other ** st_t).matrix
            self.matrix = temp
            self.st = st_t
        else:
            self.matrix = (other ** st).matrix
            self.st = st


# Vector
class Vect(object):
    def __init__(self, size, modulo, vect = None):
        self.size = size
        self.modulo = modulo
        if(vect == None):
            self.vect = self.gen()
        else:
            self.vect = vect

    def __str__(self):
        return '['+ ', '.join(str(e) for e in self.vect)+ ']'

    def __add__(self, other):
        res = []
        for i in range(self.size):
            res.append((self.vect[i] + other.vect[i]) % self.modulo)
        return Vect(self.size, self.modulo, res)

    def __sub__(self, other):
        res = []
        for i in range(self.size):
            res.append((self.vect[i] - other.vect[i]) % self.modulo)
        return Vect(self.size, self.modulo, res)

    def __mul__(self, other):
        size = self.size
        res = []
        if (isinstance(other, GL)):
            for i in range(size):
                res.append(0)
            for i in range(size):
                for j in range(size):
                    res[i] += self[j] * other.matrix[j][i]
            for i in range(len(res)):
                res[i] %= self.modulo
            return Vect(self.size, self.modulo, res)

    def __getitem__(self, item):
        return self.vect[item]

    def gen(self):
        vector = []
        for i in range(self.size):
            vector.append(random.randint(0, (self.modulo - 1)))
        return vector