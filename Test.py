import Hurley
import LinGr
import timeit
import make_tab
import GLn

def mean(time):
    s = 0
    for i in range(len(time)):
        s += time[i]
    return s / len(time)

p = 251
n = 1
f = open('D:\PyProjects\Protocol\experiments\prot_final_CG_pr.txt', 'w')
f.write(str(p)+"\n")
f.close()
s = 30
while(s < 10000):
    time = []
    f = open('D:\PyProjects\Protocol\experiments\prot_final_CG_pr.txt', 'a')
    for i in range(1):
        a = timeit.default_timer()
        c = LinGr.GL(s,p)
        parS = Hurley.initSender(s, p, n, 0, c)
        parR = Hurley.initReciever(s, p, n, 0, c)
        x = LinGr.Vect(s,p)

        mesR1 = Hurley.rec1(parR)
        mesS1 = Hurley.sen1(x, parS, mesR1)
        mesR2 = Hurley.rec2(parR, mesS1)
        mesS2 = Hurley.sen2(parS, mesR2)
        res = Hurley.getMes(parR, mesS2)
        time = timeit.default_timer() - a
    f.write('{:>5}'.format(str(s)) +  " " + str(time) + "\n")
    f.close()
    s+=10
    print(s)