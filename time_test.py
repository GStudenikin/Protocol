import LinGr
import timeit

def mean(time):
    s = 0
    for i in range(len(time)):
        s += time[i]
    return s / len(time)

s = 1
m = 11
while s < 1000:
    time = []
    for i in range(1000):
        b = LinGr.GL(s,m)
        a = timeit.default_timer()
        det = b.det_bar()
        time.append(timeit.default_timer()-a)
    print(s, mean(time))
    s += 1