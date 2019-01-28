import LinGr
import timeit
import Hurley
import GLn
import make_tab

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

par = [[2,2],[2,3],[3,2],[2,4],[5,2],[3,3],[2,5],[7,2],[2,6],[3,4],[11,2],[5,3],[2,7],[13,2],[3,5],[2,8],[17,2],[7,3],[19,2],[2,9],[23,2],[5,4],[3,6],[2,10]]

def mean(time):
    s = 0
    for i in range(len(time)):
        s += time[i]
    return s / len(time)


def prot_test_diag_prime():
    print("protocol Diag test for primes STARTED")
    f = open('D:\PyProjects\Protocol\experiments\prot_primes_diag.txt', 'w')
    f.close()
    f = open('D:\PyProjects\Protocol\experiments\prot_primes_diag.txt', 'a')
    i = 1
    while i < len(primes):
        m = primes[i]
        f.write(str(m)+"\n\n")
        s = 3
        while(s <= 100):
            time = []
            x = LinGr.Vect(s, m)
            for j in range(10):
                a = timeit.default_timer()
                parS = Hurley.initSender(s, m, 1)
                parR = Hurley.initReciever(s, m, 1)

                mesR1 = Hurley.rec1(parR)
                mesS1 = Hurley.sen1(x, parS, mesR1)
                mesR2 = Hurley.rec2(parR, mesS1)
                mesS2 = Hurley.sen2(parS, mesR2)
                res = Hurley.getMes(parR, mesS2)
                t = timeit.default_timer() - a
                time.append(t)
                if (t > 2):
                    res_t = mean(time)
                    f.write(str(m) + " " + str(s) + " " + str(res_t) + "\n")
                    f.close()
                    f = open('D:\PyProjects\Protocol\experiments\prot_primes_diag.txt', 'a')
                    break
            res_t = mean(time)
            f.write(str(m) + " " + str(s) + " " + str(res_t) + "\n")
            if(res_t > 2):
                f.close()
                f = open('D:\PyProjects\Protocol\experiments\prot_primes_diag.txt', 'a')
                break
            if (s % 10 == 0):
                print(s)
                f.close()
                f = open('D:\PyProjects\Protocol\experiments\prot_primes_diag.txt', 'a')
            s+=1
        f.write("\n\n\n")
        i+=1
    f.close()
    print("protocol Diag test for primes FINISHED")


def prot_test_cyclic_prime():
    print("protocol Cyclic test for primes STARTED")
    f = open('D:\PyProjects\Protocol\experiments\prot_primes_cyc.txt', 'w')
    f.close()
    f = open('D:\PyProjects\Protocol\experiments\prot_primes_cyc.txt', 'a')
    i = 1
    while i < len(primes):
        m = primes[i]
        f.write(str(m)+"\n\n")
        s = 3
        while(s <= 100):
            c = LinGr.GL(s,m)
            time = []
            x = LinGr.Vect(s, m)
            for j in range(10):
                a = timeit.default_timer()
                parS = Hurley.initSender(s, m, 1, c)
                parR = Hurley.initReciever(s, m, 1, c)

                mesR1 = Hurley.rec1(parR)
                mesS1 = Hurley.sen1(x, parS, mesR1)
                mesR2 = Hurley.rec2(parR, mesS1)
                mesS2 = Hurley.sen2(parS, mesR2)
                res = Hurley.getMes(parR, mesS2)
                t = timeit.default_timer() - a
                time.append(t)
                if (t > 2):
                    res_t = mean(time)
                    f.write(str(m) + " " + str(s) + " " + str(res_t) + "\n")
                    f = open('D:\PyProjects\Protocol\experiments\prot_primes_cyc.txt', 'a')
                    break
            res_t = mean(time)
            if (res_t > 2):
                res_t = mean(time)
                f.write(str(m) + " " + str(s) + " " + str(res_t) + "\n")
                f = open('D:\PyProjects\Protocol\experiments\prot_primes_cyc.txt', 'a')
                break
            f.write(str(m) + " " + str(s) + " " + str(res_t) + "\n")
            if (s % 10 == 0):
                print(s)
                f.close()
                f = open('D:\PyProjects\Protocol\experiments\prot_primes_cyc.txt', 'a')
            s+=1
        f.write("\n\n\n")
        i+=1
    f.close()
    print("protocol Cyclic test for primes FINISHED")


def prot_test_diag_gf():
    print("protocol Diag test for GF STARTED")
#    f = open('D:\PyProjects\Protocol\experiments\prot_GF_diag_final.txt', 'w')
#    f.close()
    f = open('D:\PyProjects\Protocol\experiments\prot_GF_diag_final.txt', 'a')
    s = 1750
    while(s < 20000):
        p = 2
        n = 10
        irp = irps[primes.index(p)][n]
        elems = make_tab.elems_f(p,n)
        mat_mul = make_tab.mul_tab_f(p,n,elems)
        mat_sum = make_tab.sum_tab_f(p,n,elems)
        time = []
        x = GLn.Vect(s,p,n,irp,elems,mat_mul,mat_sum)
        for j in range(1):
            a = timeit.default_timer()
            parS = Hurley.initSender(s, p, n, irp, elems, mat_mul, mat_sum)
            parR = Hurley.initReciever(s, p, n, irp, elems, mat_mul, mat_sum)

            mesR1 = Hurley.rec1(parR)
            mesS1 = Hurley.sen1(x, parS, mesR1)
            mesR2 = Hurley.rec2(parR, mesS1)
            mesS2 = Hurley.sen2(parS, mesR2)
            res = Hurley.getMes(parR, mesS2)
            t = timeit.default_timer() - a
            time.append(t)
        res_t = mean(time)
        f.write('{:>4}'.format(str(p**n))+'{:>3}'.format(str(p)) + '{:>3}'.format(str(n)) + " " + str(s) + " " + str(res_t) + "\n")
        f.close()
        f = open('D:\PyProjects\Protocol\experiments\prot_GF_diag_final.txt', 'a')
        print(s)
        s+=250
    f.close()
    print("protocol Diag test for GF FINISHED")


def prot_test_cyclic_gf():
    print("protocol Cyclic test for GF STARTED")
#    f = open('D:\PyProjects\Protocol\experiments\prot_GF_cyc.txt', 'w')
#    f.close()
    f = open('D:\PyProjects\Protocol\experiments\prot_GF_cyc.txt', 'a')
    i = 5
    p = primes[i]
    while (p <= 23):
        p = primes[i]
        n = 2
        while(n < 3):
            f.write(str(p)+ " " + str(n) +"\n\n")
            s = 3
            irp = irps[i][n]
            elems = GLn.gen_elems(p, n)
            mat_mul = GLn.get_mul_table(p, n, irp)
            mat_sum = GLn.get_sum_table(p, n)
            while(s <= 3):
                time = []
                c = GLn.GL_f(p,n,irp,s,elems,mat_mul,mat_sum)
                x = GLn.Vect(s,p,n,irp,elems,mat_mul,mat_sum)
                for j in range(10):
                    a = timeit.default_timer()
                    parS = Hurley.initSender(s, p, n, irp, elems, mat_mul, mat_sum, c)
                    parR = Hurley.initReciever(s, p, n, irp, elems, mat_mul, mat_sum, c)

                    mesR1 = Hurley.rec1(parR)
                    mesS1 = Hurley.sen1(x, parS, mesR1)
                    mesR2 = Hurley.rec2(parR, mesS1)
                    mesS2 = Hurley.sen2(parS, mesR2)
                    res = Hurley.getMes(parR, mesS2)
                    t = timeit.default_timer() - a
                    time.append(t)
                    if (t > 2):
                        res_t = mean(time)
                        f.write(str(p) + " " + str(n) + " " + str(s) + " " + str(res_t) + "\n")
                        f.close()
                        f = open('D:\PyProjects\Protocol\experiments\prot_GF_cyc.txt', 'a')
                        break
                res_t = mean(time)
                f.write(str(p) + " " + str(n) + " " + str(s) + " " + str(res_t) + "\n")
                if(res_t > 2):
                    f.close()
                    f = open('D:\PyProjects\Protocol\experiments\prot_GF_cyc.txt', 'a')
                    break
                print(s)
                f.close()
                f = open('D:\PyProjects\Protocol\experiments\prot_GF_cyc.txt', 'a')
                s+=1
            f.write("\n\n\n")
            n += 1
        i+=1
    f.close()
    print("protocol Cyclic test for GF FINISHED")



prot_test_diag_gf()

