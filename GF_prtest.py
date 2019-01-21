import Hurley
import LinGr
import GLn

s = 7
p = 5
n = 2

irp = [1,1,2]
elems = GLn.gen_elems(p,n)
mat_mul = GLn.get_mul_table(p,n,irp)
mat_sum = GLn.get_sum_table(p,n)

# init
parS = Hurley.initSender(s, p, n, irp, elems, mat_mul, mat_sum)
parR = Hurley.initReciever(s, p, n, irp, elems, mat_mul, mat_sum)

xv = [18,17,16,15,1,8,9]
x = GLn.Vect(s, p, n, irp, elems, mat_mul, mat_sum, xv)
#

#
mesR1 = Hurley.rec1(parR)
mesS1 = Hurley.sen1(x, parS, mesR1)
mesR2 = Hurley.rec2(parR, mesS1)
mesS2 = Hurley.sen2(parS, mesR2)


res = Hurley.getMes(parR, mesS2)
print(res)