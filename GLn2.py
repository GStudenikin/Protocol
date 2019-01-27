import copy
import random

# Разность многочленов av и bv, представленных векторами координат
def subv(av,bv):
    a = copy.deepcopy(av)
    b = copy.deepcopy(bv)
    diff = len(a) - len(b)
    res = []
    if(diff < 0):
        for i in range(diff):
            a.insert(0,0)
    elif (diff > 0):
        for i in range(diff):
            b.insert(0, 0)
    for i in range(len(a)):
        res.append(a[i] - b[i])
    return res

# Сумма многочленов av и bv, представленных векторами координат
def sumv(av,bv):
    a = copy.deepcopy(av)
    b = copy.deepcopy(bv)
    diff = len(a) - len(b)
    res = []
    if(diff < 0):
        for i in range(diff):
            a.insert(0,0)
    elif (diff > 0):
        for i in range(diff):
            b.insert(0, 0)
    for i in range(len(a)):
        res.append(a[i] + b[i])
    return res

# Умножение многочлена a, представленного вектором координат на число n
def mulvn(a,n):
    res = []
    for i in range(len(a)):
        res.append(a[i] * n)
    return res

# Находление остатка от деления многочлена av, на многочлен ab в поле порядка n
def modv(av,bv,n):
    a = copy.deepcopy(av)
    b = copy.deepcopy(bv)
    if(a == zerv(a)):
        return a
    while(a[0] == 0):
        del(a[0])
    if(len(a) < len(b)):
        return a
    if(len(a) == len(b)):
        return vmodn(subv(a, vmodn(mulvn(b,a[0]), n)), n)
    if (len(a) > len(b)):
        while (len(a) > len(b)):
            subs = copy.deepcopy(b)
            while(len(subs) < len(a)):
                subs.append(0)
            a = vmodn(subv(a, vmodn(mulvn(subs,a[0]), n)), n)
            return modv(a,b,n)

def zerv(a):
    res = []
    for i in range(len(a)):
        res.append(0)
    return res

def onev(a):
    res = zerv(a)
    res[-1] += 1
    return res

# Произведение векторов a, b
def mulv(a,b):
    if (zerv(a) == a):
        return zerv(a)
    if (zerv(b) == b):
        return zerv(b)
    if (onev(a) == a):
        return b
    if (onev(b) == b):
        return a
    temp = []
    sres = len(a) + len(b) - 1
    for i in range(len(a)):
        temp.append(mulvn(b, a[i]))
        for j in range(len(a) -1 - i):
            temp[i].append(0)
        for j in range(sres - len(temp[i])):
            temp[i].insert(0,0)
    res = []
    for i in range(sres):
        res.append(0)
    for j in range(len(temp)):
        res = sumv(res, temp[j])
    while (res[0] == 0):
        del (res[0])
    return res

# Нахождение остатка от деления многочлена a на число n
def vmodn(a,n):
    res = []
    for i in range(len(a)):
        res.append(a[i] % n)
    return res

# Генерация массива элементов конечного поля порядка p^n
def gen_elems(p, n):
    res = []
    size = p**n
    for i in range(size):
        elem = []
        while(i > 0):
            elem.append(i%p)
            i = i//p
        elem = elem[::-1]
        if(len(elem) < n):
            for i in range((n + 1) - len(elem)):
                elem.insert(0,0)
        else:
            elem.insert(0, 0)
        res.append(elem)
    return res

# Генерация таблицы сложения элементов конечного поля порядка p^n
def get_sum_table(p,n):
    size = p**n
    elems = gen_elems(p,n)
    res = []
    for i in range(size):
        res.append([])
    for i in range(size):
        for j in range(size):
            res[i].append(vmodn(sumv(elems[i],elems[j]),p))
    return res

# Генерация таблицы умножения элементов конечного поля порядка p^n
def get_mul_table(p,n,irp):
    size = p**n
    elems = gen_elems(p,n)
    res = []
    for i in range(size):
        res.append([])
    for i in range(size):
        for j in range(size):
            pr = vmodn(mulv(elems[i],elems[j]),p)
            res[i].append(modv(pr, irp, p))
            for k in range(len(irp) - len(res[i][j])):
                res[i][j].insert(0,0)
    return res

def num_matrix(matrix, elems):
    res = []
    for i in range(len(matrix)):
        res.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            a = matrix[i][j]
            b = elems.index(a)
            res[i].append(b)
    return res


class GF(object):
    def __init__(self, prime, n, irp, elnum = None, elems = None, mat_mul = None, mat_sum = None):
        self.prime = prime
        self.n = n
        self.irp = irp
        if(elnum == None):
            self.elnum = random.randint(0, (self.prime ** self.n - 1))
        else:
            self.elnum = elnum
        if(elems == None):
            self.elems = gen_elems(prime,n)
        else:
            self.elems = elems
        if (mat_mul == None):
            self.mat_mul = num_matrix(get_mul_table(self.prime, self.n, self.irp), self.elems)
        else:
            self.mat_mul = mat_mul
        if(mat_sum == None):
            self.mat_sum = num_matrix(get_sum_table(self.prime, self.n), self.elems)
        else:
            self.mat_sum = mat_sum

    def __add__(self, other):
        return GF(self.prime, self.n, self.irp, self.elems.index(self.mat_sum[self.elnum][other.elnum]), self.elems, self.mat_mul, self.mat_sum)

    def __mul__(self, other):
        res = self.mat_mul[self.elnum][other.elnum]
        ind = self.elems.index(res)
        return GF(self.prime, self.n, self.irp, ind, self.elems, self.mat_mul, self.mat_sum)

    def __str__(self):
        return '[' + ', '.join(str(e) for e in self.elems[self.elnum]) + ']'

# Нахождение обратного элемента поля
    def inv(self):
        ind = self.mat_mul[self.elnum].index(self.elems[1])
        return GF(self.prime, self.n, self.irp, ind, self.elems, self.mat_mul, self.mat_sum)

    def muln(self, n):
        res = vmodn(mulvn(self.elems[self.elnum], n), self.prime)
        ind = self.elems.index(res)
        return GF(self.prime, self.n, self.irp, ind, self.elems,self.mat_mul, self.mat_sum)

    def elem(self):
        return self.elems[self.elnum]


class GL_f(object):
    def __init__(self, prime, n, irp, size, elems, mat_mul, mat_sum, matrix=None):
        self.prime = prime
        self.n = n
        self.irp = irp
        self.size = size
        self.elems = elems
        self.mat_mul = mat_mul
        self.mat_sum = mat_sum
        if(matrix == None):
            det = 0
            while(det == 0):
                self.matrix = self.gen()
                det = self.det().elnum
        else:
            res_m = []
            for i in range(self.size):
                res_m.append([])
            for i in range(self.size):
                for j in range(self.size):
                    res_m[i].append(GF(self.prime, self.n, self.irp, matrix[i][j], elems, mat_mul, mat_sum))
            self.matrix = res_m

    def __str__(self):
        return '\n'.join(('[' + ', '.join(str(e) for e in self.matrix[i]) + ']') for i in range(self.size))

    def __mul__(self, other):
        size = self.size
        res = []
        for t in range(size):
            res.append([])
        temp = GF(self.prime, self.n, self.irp, 0, self.elems, self.mat_mul, self.mat_sum)
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    ad = self.matrix[i][k] * other.matrix[k][j]
                    temp += ad
                res[i].append(temp.elnum)
                temp = GF(self.prime, self.n, self.irp, 0, self.elems, self.mat_mul, self.mat_sum)
        return GL_f(self.prime, self.n, self.irp, self.size, self.elems, self.mat_mul, self.mat_sum, res)

    def __pow__(self, other):
        res = self
        i = 1
        while i < other:
            res *= self
            i += 1
        return res

# Дихотомический алгоритм возведение в степень
    def pow(self, st):
        st = str(bin(st))[2::]
        if (st[-1] == str(0)):
            z = self.one()
        if (st[-1] == str(1)):
            z = copy.deepcopy(self)
        st = st[:-1:]
        q = copy.deepcopy(self)
        for i in range(len(st)):
            q *= q
            if (st[len(st) - 1 - i] == str(1)):
                z *= q
        return z

# Генерация элемента группы
    def gen(self):
        res = []
        p = self.prime
        n = self.n
        el_len = p ** n
        size = self.size
        for i in range(size):
            res.append([])
        for i in range(size):
            for j in range(size):
                res[i].append(GF(p, n, self.irp, random.randint(0, el_len - 1), self.elems, self.mat_mul, self.mat_sum))
        return res

    def num_mat(self):
        res = []
        for i in range(self.size):
            res.append([])
        for i in range(self.size):
            for j in range(self.size):
                res[i].append(self.matrix[i][j].elnum)
        return res

# Определитель матрицы
    def det(self):
        size = self.size
        mat = copy.deepcopy(self)
        if size == 1:
            return mat.matrix[0][0]
        signum = 1
        determinant = GF(self.prime, self.n, self.irp, 0, self.elems, self.mat_mul, self.mat_sum)
        for j in range(size):
            minor_mat = mat.minor(0, j)
            temp = mat.matrix[0][j] * minor_mat.det()
            su = temp.muln(signum)
            determinant += su
            signum *= -1
        return determinant

# Обратный элемент группы
    def inv(self):
        det = self.det()
        det_i = det.inv()
        adj = self.adj()
        trans = adj.trans()
        mul = trans.mulv(det_i)
        return mul

# Транспонирование матрицы
    def trans(self):
        size = self.size
        tr = []
        for i in range(size):
            tr.append([self.matrix[j][i] for j in range(size)])
        res = []
        for i in range(size):
            res.append([])
        for i in range(size):
            for j in range(size):
                res[i].append(tr[i][j].elnum)
        return GL_f(self.prime, self.n, self.irp, self.size, self.elems, self.mat_mul, self.mat_sum, res)

# Построение союзной матрицы
    def adj(self):
        adj = []
        size = self.size
        for i in range(size):
            adj.append([0 for j in range(size)])
        for i in range(size):
            for j in range(size):
                minor = self.minor(i, j)
                adj[i][j] = minor.det().muln((-1) ** (i + j)).elnum
        return GL_f(self.prime, self.n, self.irp, self.size, self.elems, self.mat_mul, self.mat_sum, adj)

# Сопряжение элемента группы элементом other
    def conj(self, other):
        other_i = other.inv()
        res = other * self
        res *= other_i
        return res

    def minor(self, i, j):
        minor = copy.deepcopy(self.matrix)
        del minor[i]
        for t in range(len(minor)):
            del minor[t][j]
        res = []
        for i in range(len(minor)):
            res.append([])
        for i in range(len(minor)):
            for j in range(len(minor)):
                res[i].append(minor[i][j].elnum)
        return GL_f(self.prime, self.n, self.irp, len(minor), self.elems, self.mat_mul, self.mat_sum, res)

# Умножение элемента группы на элемент поля
    def mulv(self, other):
        matrix = copy.deepcopy(self.matrix)
        size = self.size
        for i in range(size):
            for j in range(size):
                matrix[i][j] *= other
        res = []
        for i in range(size):
            res.append([])
        for i in range(size):
            for j in range(size):
                res[i].append(matrix[i][j].elnum)
        return GL_f(self.prime, self.n, self.irp, self.size, self.elems, self.mat_mul, self.mat_sum, res)

# Построение единичной матрицы
    def one(self):
        matrix = []
        for i in range(self.size):
            matrix.append([])
        for t in range(self.size):
            for k in range(self.size):
                if t!= k:
                    matrix[t].append(0)
                else:
                    matrix[t].append(1)
        return GL_f(self.prime, self.n, self.irp, self.size, self.elems, self.mat_mul, self.mat_sum, matrix)


class Diag(GL_f):
    def __mul__(self, other):
        size = self.size
        res = copy.deepcopy(self)
        for i in range(size):
            res.matrix[i][i] *= other.matrix[i][i]
        return res

# Генерация диагональной матрицы
    def gen(self):
        res = []
        p = self.prime
        n = self.n
        el_len = p ** n
        size = self.size
        for i in range(size):
            res.append([])
        for i in range(size):
            for j in range(size):
                if(i == j):
                    res[i].append(GF(p, n, self.irp, random.randint(1, el_len - 1), self.elems, self.mat_mul, self.mat_sum))
                else:
                    res[i].append(GF(p, n, self.irp, 0, self.elems, self.mat_mul, self.mat_sum))
        return res

# Определитель диагональной матрицы
    def det(self):
        size = self.size
        mat = copy.deepcopy(self)
        if size == 1:
            return mat.matrix[0][0]
        determinant = GF(self.prime, self.n, self.irp, 1, self.elems, self.mat_mul, self.mat_sum)
        for j in range(size):
            determinant *= mat.matrix[j][j]
        return determinant

# Построение обратного элемента группы
    def inv(self):
        res = copy.deepcopy(self)
        for i in range(self.size):
            res.matrix[i][i] = res.matrix[i][i].inv()
        return res


class CG(GL_f):
    def __init__(self, other, st = None):
        self.prime = other.prime
        self.n = other.n
        self.irp = other.irp
        self.size = other.size
        self.elems = other.elems
        self.mat_mul = other.mat_mul
        self.mat_sum = other.mat_sum
        if(st == None):
            st_t = random.randint(1, 100)
            temp = (other.pow(st_t)).matrix
            self.matrix = temp
            self.st = st_t
        else:
            self.matrix = (other.pow(st)).matrix
            self.st = st


class Vect(object):
    def __init__(self, size, prime, n, irp, elems, mat_mul, mat_sum, vect = None):
        self.size = size
        self.prime = prime
        self.n = n
        self.irp = irp
        self.elems = elems
        self.mat_mul = mat_mul
        self.mat_sum = mat_sum
        if(vect == None):
            self.vect = self.gen()
        else:
            if(isinstance(vect[0], GF)):
                self.vect = vect
            if (isinstance(vect[0], int)):
                res = []
                for i in range(self.size):
                    res.append(GF(self.prime, self.n, self.irp, vect[i], self.elems, self.mat_mul, self.mat_sum))
                self.vect = res

    def __str__(self):
        return '['+ ', '.join(str(e) for e in self.vect)+ ']'

    def __add__(self, other):
        res = []
        for i in range(self.size):
            res.append(self.vect[i] + other.vect[i])
        return Vect(self.size, self.prime, self.n, self.irp, self.elems, self.mat_mul, self.mat_sum, res)

    def __sub__(self, other):
        res = []
        for i in range(self.size):
            res.append(self.vect[i] + (other.vect[i].muln(-1)))
        return Vect(self.size, self.prime, self.n, self.irp, self.elems, self.mat_mul, self.mat_sum, res)

    def __mul__(self, other):
        size = self.size
        res = []
        temp = GF(self.prime, self.n, self.irp, 0, self.elems, self.mat_mul, self.mat_sum)
        if (isinstance(other, GL_f)):
            for i in range(size):
                for j in range(size):
                    temp += self.vect[j] * other.matrix[j][i]
                res.append(temp)
                temp = GF(self.prime, self.n, self.irp, 0, self.elems, self.mat_mul, self.mat_sum)
            return Vect(self.size, self.prime, self.n, self.irp, self.elems, self.mat_mul, self.mat_sum, res)

# Генерация вектора
    def gen(self):
        vector = []
        max = self.prime ** self.n
        for i in range(self.size):
            vector.append(GF(self.prime, self.n, self.irp, random.randint(0, max - 1), self.elems, self.mat_mul, self.mat_sum))
        return vector

p = 2
n = 10
s = 5
irp = [1,0,1,0,0,1]
elems = gen_elems(p,n)
mat_mul = get_mul_table(p,n,irp)
mat_sum = get_sum_table(p,n)
a = GL_f(p,n,irp,s,elems,mat_mul,mat_sum)
print(a)