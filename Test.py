import Hurley
import LinGr
import timeit

def mean(time):
    s = 0
    for i in range(len(time)):
        s += time[i]
    return s / len(time)


s = 10
m = 151
n = 1

f = open('D:\pyproject\GitHub\Protocol\experiments\prot_final_diag.txt', 'w')
f.close()


while s < 100000:
    time = []
    f = open('D:\pyproject\GitHub\Protocol\experiments\prot_final_diag.txt', 'a')
    for i in range(10):
        a = timeit.default_timer()
        parS = Hurley.initSender(s, m, n)
        parR = Hurley.initReciever(s, m, n)
        x = LinGr.Vect(s, m)

        mesR1 = Hurley.rec1(parR)
        mesS1 = Hurley.sen1(x, parS, mesR1)
        mesR2 = Hurley.rec2(parR, mesS1)
        mesS2 = Hurley.sen2(parS, mesR2)
        res = Hurley.getMes(parR, mesS2)
        time.append(timeit.default_timer() - a)
    f.write(str(s) + " " + str(mean(time)) + "\n")
    f.close()
    print(s)
    s += 10

