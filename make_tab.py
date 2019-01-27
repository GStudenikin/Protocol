import GLn
import os
import timeit

primes = [2,3,5,7,11,13,17,19,23]

irps = [[[],[],[1,1,1],[1,1,0,1],[1,1,0,0,1],[1,0,1,0,0,1],[1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1],[1,1,1,0,0,0,0,1,1],[1,0,0,0,1,0,0,0,0,1],[1,0,0,1,0,0,0,0,0,0,1]],
       [[],[],[1,1,2],[1,2,0,1],[1,1,0,0,2],[1,1,0,1,0,1],[1,1,0,0,0,0,2]],
       [[],[],[1,1,2],[1,1,0,2],[1,1,0,1,3]],
       [[],[],[1,1,3],[1,1,1,2]],
       [[],[],[1,1,7],[1,1,0,5]],
       [[],[],[1,1,2]],
       [[],[],[1,1,3]],
       [[],[],[1,1,2]],
       [[],[],[1,1,7]]]

def n_mat(matrix, elems):
    nmt = []
    for i in range(len(matrix)):
        nmt.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            nmt[i].append(elems.index(matrix[i][j]))
    return nmt

def elems_f(p, n):
    f = open(r"D:\PyProjects\Protocol\GF\""[:-1]+str(p)+r"\""[:-1]+str(n)+"\elems.txt", 'r')
    el = []
    for line in f:
        el.append(line[1:-2])
    f.close()
    elems = []
    for i in el:
        elem = i.split(", ")
        e = []
        for j in elem:
            e.append(int(j))
        elems.append(e)
    return elems

def mul_tab_f(p,n, elems):
    f = open(r"D:\PyProjects\Protocol\GF\""[:-1]+str(p)+r"\""[:-1]+str(n)+"\mul_tab.txt", 'r')
    mt = []
    for line in f:
        mt.append(line[1:-2])
    f.close()
    mat_mul = []
    for i in mt:
        emul = i.split(", ")
        e = []
        for j in emul:
            e.append(elems[int(j)])
        mat_mul.append(e)
    return mat_mul

def sum_tab_f(p,n, elems):
    f = open(r"D:\PyProjects\Protocol\GF\""[:-1]+str(p)+r"\""[:-1]+str(n)+"\sum_tab.txt", 'r')
    st = []
    for line in f:
        st.append(line[1:-2])
    f.close()
    mat_sum = []
    for i in st:
        esum = i.split(", ")
        e = []
        for j in esum:
            e.append(elems[int(j)])
        mat_sum.append(e)
    return mat_sum