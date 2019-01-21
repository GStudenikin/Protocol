import Hurley
import LinGr

s = 5
m = 11
n = 1
c = LinGr.CG(LinGr.GL(s,m))
parS = Hurley.initSender(s, m, n, c)
parR = Hurley.initReciever(s, m, n, c)

xv = [3,4,1,2,8]
x = LinGr.Vect(s, m, xv)

mesR1 = Hurley.rec1(parR)
mesS1 = Hurley.sen1(x, parS, mesR1)
mesR2 = Hurley.rec2(parR, mesS1)
mesS2 = Hurley.sen2(parS, mesR2)
res = Hurley.getMes(parR, mesS2)
print(res)