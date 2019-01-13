import LinGr
import timeit
import Hurley

def mean(time):
    s = 0
    for i in range(len(time)):
        s += time[i]
    return s / len(time)

def det_time_test():
    s = 1
    m = 11
    while s < 1000:
        time = []
        for t in range(1000):
            b = LinGr.GL(s,m)
            a = timeit.default_timer()
            b.det_bar()
            time.append(timeit.default_timer()-a)
        print(s, mean(time))
        s += 1

def test_vec(s,m):
    res = []
    for i in range(s):
        res.append(i % m)
    return res

def prot_test():
    s = 3
    m = 11
    while(s <= 100):
        time = []
#        xv = vectors[s-3]
#        x = LinGr.Vect(s, m, xv)
        xv = test_vec(s,m)
        x = LinGr.Vect(s, m, xv)
        for i in range(10):
            a = timeit.default_timer()
#            c = LinGr.CG(LinGr.GL(s, m))
            parS = Hurley.initSender(s, m)
            parR = Hurley.initReciever(s, m)

            mesR1 = Hurley.rec1(parR)
            mesS1 = Hurley.sen1(x, parS, mesR1)
            mesR2 = Hurley.rec2(parR, mesS1)
            mesS2 = Hurley.sen2(parS, mesR2)
            res = Hurley.getMes(parR, mesS2)
            time.append(timeit.default_timer() - a)
        print(s, mean(time))
        s+=1

prot_test()