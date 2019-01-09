import copy
import random

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

class GL(object):
    def __init__(self, size, modulo, matrix = None):
        self.size = size
        self.modulo = modulo
        if(matrix == None):
            det = 0
            while(det == 0):
                self.matrix = self.gen()
                det = self.det()
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

    def trans(self):
        size = self.size
        tr = []
        for i in range(size):
            tr.append([self.matrix[j][i] for j in range(size)])
        return GL(len(tr), self.modulo, tr)

    def adj(self):
        adj = []
        size = self.size
        for i in range(size):
            adj.append([0 for j in range(size)])
        for i in range(size):
            for j in range(size):
                minor = self.minor(i, j)
                adj[i][j] = ((-1) ** (i + j)) * minor.det()
        return GL(self.size, self.modulo, adj).mod()

    def muln(self, n):
        matrix = copy.deepcopy(self.matrix)
        size = self.size
        for i in range(size):
            for j in range(size):
                matrix[i][j] *= n
        return GL(self.size, self.modulo, matrix).mod()

    def inv(self):
        det = self.det()
        inv = mulinv(det, self.modulo)
        adj = self.adj()
        trans = adj.trans()
        mul = trans.muln(inv)
        return mul.mod()

class SL(GL):
    def __init__(self, size, modulo, matrix = None):
        self.size = size
        self.modulo = modulo
        if(matrix == None):
            det = 0
            while(det != 1):
                self.matrix = self.gen()
                det = self.det()
        else:
            self.matrix = matrix

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
        determinant = 0
        for i in range(self.size):
            determinant += self.matrix[i][i]
        return determinant % self.modulo

    def inv(self):
        matrix = []
        size = self.size
        for i in range(size):
            matrix.append([0 for j in range(size)])
        for i in range(size):
            matrix[i][i] = mulinv(self.matrix[i][i], self.modulo)
        return Diag(self.size, self.modulo, matrix)



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