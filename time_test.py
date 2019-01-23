import LinGr
import timeit
import Hurley
import GLn

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499]

irps = [[[],[],[1,1,1],[1,1,0,1],[1,1,0,0,1],[1,0,1,0,0,1],[1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1],[1,1,1,0,0,0,0,1,1],[1,0,0,0,1,0,0,0,0,1],[1,0,0,1,0,0,0,0,0,0,1]],
       [[],[],[1,1,2],[1,2,0,1],[1,1,0,0,2],[1,1,0,1,0,1],[1,1,0,0,0,0,2],[1,1,0,1,0,0,0,1],[1,0,0,1,0,0,0,0,2],[1,0,1,0,1,0,0,0,0,1],[1,1,0,1,0,0,0,0,0,0,2]],
       [[],[],[1,1,2],[1,1,0,2],[1,1,0,1,3],[1,0,0,1,0,2],[1,1,0,0,0,0,2],[1,1,0,0,0,0,0,2],[1,0,0,1,0,1,0,0,3],[1,0,1,1,0,0,0,0,0,3],[1,1,0,1,0,0,0,0,0,0,3]],
       [[],[],[1,1,3],[1,1,1,2],[1,1,1,0,3],[1,1,0,0,0,4],[1,1,1,0,0,0,3],[1,0,1,0,0,0,0,4],[1,1,0,0,0,0,0,0,3],[1,1,0,0,0,0,1,0,0,2],[1,1,1,0,0,0,0,0,0,0,3]],
       [[],[],[1,1,7],[1,1,0,5],[1,0,0,1,2],[1,0,1,1,0,9],[1,1,0,0,0,1,7],[1,1,0,0,0,0,0,5],[1,0,0,0,1,0,0,1,2]],
       [[],[],[1,1,2],[1,1,0,7],[1,1,0,1,2],[1,0,1,0,1,11],[1,1,0,1,0,0,6],[1,0,0,1,0,0,0,6],[1,0,1,1,0,0,0,0,2]],
       [[],[],[1,1,3],[1,0,1,14],[1,1,0,0,5],[1,1,0,0,0,14],[1,1,0,0,0,0,3],[1,0,0,0,1,0,0,14]],
       [[],[],[1,1,2],[1,1,0,16],[1,1,0,0,2],[1,0,0,0,1,16],[1,0,0,0,0,1,3],[1,0,1,0,0,0,0,9]],
       [[],[],[1,1,7],[1,1,0,16],[1,0,0,1,11],[1,0,0,0,18],[1,0,0,0,0,7]]]



def mean(time):
    s = 0
    for i in range(len(time)):
        s += time[i]
    return s / len(time)

def pow_test():
    print("pow_test STARTED")
    f = open('D:\pyproject\GitHub\Protocol\experiments\pow_time.txt', 'w')
    f.close()
    s = 3
    p = 23
    n = 1
    f = open('D:\pyproject\GitHub\Protocol\experiments\pow_time.txt', 'a')
    while(n < 1000):
        time = []
        for i in range(100):
            el = LinGr.GL(s, p)
            a = timeit.default_timer()
            el**n
            time.append(timeit.default_timer() - a)
        f.write(str(n) + " " + str(mean(time)) + "\n")
        if (n % 10 == 0):
            print(n)
            f.close()
            f = open('D:\pyproject\GitHub\Protocol\experiments\pow_time.txt', 'a')
        n += 1
    print("pow_test FINISHED")
    f.close()

def dh_pow_test():
    print("dh_pow_test STARTED")
    f = open('D:\pyproject\GitHub\Protocol\experiments\dh_pow_time.txt', 'w')
    f.close()
    s = 3
    p = 23
    n = 1
    f = open('D:\pyproject\GitHub\Protocol\experiments\dh_pow_time.txt', 'a')
    while(n < 1000):
        time = []
        for i in range(100):
            el = LinGr.GL(s, p)
            a = timeit.default_timer()
            el.pow(n)
            time.append(timeit.default_timer() - a)
        f.write(str(n) + " " + str(mean(time)) + "\n")
        if (n % 10 == 0):
            print(n)
            f.close()
            f = open('D:\pyproject\GitHub\Protocol\experiments\dh_pow_time.txt', 'a')
        n += 1
    print("dh_pow_test FINISHED")
    f.close()

def det_bar_test():
    print("bar_test STARTED")
    f = open('D:\pyproject\GitHub\Protocol\experiments\det_bar_time.txt', 'w')
    f.close()
    s = 1
    m = 23
    f = open('D:\pyproject\GitHub\Protocol\experiments\det_bar_time.txt', 'a')
    while s < 200:
        time = []
        if(s > 100):
            exps = 10
        else:
            exps = 100
        for t in range(exps):
            b = LinGr.GL(s,m)
            a = timeit.default_timer()
            b.det_bar()
            time.append(timeit.default_timer()-a)
        f.write(str(s) + " " + str(mean(time)) + "\n")
        s += 1
        if(s%10 == 0):
            print(s)
            f.close()
            f = open('D:\pyproject\GitHub\Protocol\experiments\det_bar_time.txt', 'a')
    print("bar_test FINISHED")
    f.close()

def det_test():
    print("laplace test STARTED")
    f = open('D:\pyproject\GitHub\Protocol\experiments\det_lap_time.txt', 'w')
    f.close()
    s = 1
    m = 23
    f = open('D:\pyproject\GitHub\Protocol\experiments\det_lap_time.txt', 'a')
    while s <= 10:
        time = []
        if(s > 8):
            exps = 10
        else:
            exps = 100
        for t in range(exps):
            b = LinGr.GL(s,m)
            a = timeit.default_timer()
            b.det()
            time.append(timeit.default_timer()-a)
        f.write(str(s) + " " + str(mean(time)) + "\n")
        s += 1
        print(s)
        f.close()
        f = open('D:\pyproject\GitHub\Protocol\experiments\det_bar_time.txt', 'a')
    print("laplace test FINISHED")
    f.close()

def prot_test_diag_prime():
    print("protocol Diag test for primes STARTED")
    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_primes_diag.txt', 'w')
    f.close()
    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_primes_diag.txt', 'a')
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
                    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_primes_diag.txt', 'a')
                    break
            res_t = mean(time)
            f.write(str(m) + " " + str(s) + " " + str(res_t) + "\n")
            if(res_t > 2):
                f.close()
                f = open('D:\pyproject\GitHub\Protocol\experiments\prot_primes_diag.txt', 'a')
                break
            if (s % 10 == 0):
                print(s)
                f.close()
                f = open('D:\pyproject\GitHub\Protocol\experiments\prot_primes_diag.txt', 'a')
            s+=1
        f.write("\n\n\n")
        i+=1
    f.close()
    print("protocol Diag test for primes FINISHED")

def prot_test_cyclic_prime():
    print("protocol Cyclic test for primes STARTED")
    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_primes_cyc.txt', 'w')
    f.close()
    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_primes_cyc.txt', 'a')
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
                time.append(timeit.default_timer() - a)
            res_t = mean(time)
            f.write(str(m) + " " + str(s) + " " + str(res_t) + "\n")
            if(res_t > 2):
                f.close()
                f = open('D:\pyproject\GitHub\Protocol\experiments\prot_primes_cyc.txt', 'a')
                break
            if (s % 10 == 0):
                print(s)
                f.close()
                f = open('D:\pyproject\GitHub\Protocol\experiments\prot_primes_cyc.txt', 'a')
            s+=1
        f.write("\n\n\n")
        i+=1
    f.close()
    print("protocol Cyclic test for primes FINISHED")

def prot_test_diag_GF():
    print("protocol Diag test for GF STARTED")
    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_GF_diag.txt', 'w')
    f.close()
    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_GF_diag.txt', 'a')
    i = 0
    p = primes[i]
    while (p <= 23):
        p = primes[i]
        n = 2
        while(n < len(irps[i])):
            f.write(str(p)+ " " + str(n) +"\n\n")
            s = 3
            irp = irps[i][n]
            elems = GLn.gen_elems(p, n)
            mat_mul = GLn.get_mul_table(p, n, irp)
            mat_sum = GLn.get_sum_table(p, n)
            while(s <= 100):
                time = []
                x = GLn.Vect(s,p,n,irp,elems,mat_mul,mat_sum)
                for j in range(10):
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
                    if (t > 2):
                        res_t = mean(time)
                        f.write(str(p) + " " + str(n) + " " + str(s) + " " + str(res_t) + "\n")
                        f.close()
                        f = open('D:\pyproject\GitHub\Protocol\experiments\prot_primes_diag.txt', 'a')
                        break
                res_t = mean(time)
                f.write(str(p) + " " + str(n) + " " + str(s) + " " + str(res_t) + "\n")
                if(res_t > 2):
                    f.close()
                    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_GF_diag.txt', 'a')
                    break
                if (s % 10 == 0):
                    print(s)
                    f.close()
                    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_GF_diag.txt', 'a')
                s+=1
            f.write("\n\n\n")
            n += 1
        i+=1
    f.close()
    print("protocol Diag test for GF FINISHED")

def prot_test_cyclic_GF():
    print("protocol Cyclic test for GF STARTED")
    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_GF_cyc.txt', 'w')
    f.close()
    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_GF_cyc.txt', 'a')
    i = 0
    p = primes[i]
    while (p <= 23):
        p = primes[i]
        n = 2
        while(n < len(irps[i])):
            f.write(str(p)+ " " + str(n) +"\n\n")
            s = 3
            irp = irps[i][n]
            elems = GLn.gen_elems(p, n)
            mat_mul = GLn.get_mul_table(p, n, irp)
            mat_sum = GLn.get_sum_table(p, n)
            while(s <= 100):
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
                        f = open('D:\pyproject\GitHub\Protocol\experiments\prot_primes_diag.txt', 'a')
                        break
                res_t = mean(time)
                f.write(str(p) + " " + str(n) + " " + str(s) + " " + str(res_t) + "\n")
                if(res_t > 2):
                    f.close()
                    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_GF_cyc.txt', 'a')
                    break
                print(s)
                f.close()
                f = open('D:\pyproject\GitHub\Protocol\experiments\prot_GF_cyc.txt', 'a')
                s+=1
            f.write("\n\n\n")
            n += 1
        i+=1
    f.close()
    print("protocol Cyclic test for GF FINISHED")

dh_pow_test()
pow_test()
prot_test_diag_GF()
prot_test_cyclic_GF()
prot_test_cyclic_prime()
prot_test_diag_prime()
det_bar_test()
det_test()

