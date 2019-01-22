import Hurley
import LinGr
import GLn

s = 3
p = 2
n = 2

irp = [1,1,1]
elems = GLn.gen_elems(p,n)
mat_mul = GLn.get_mul_table(p,n,irp)
mat_sum = GLn.get_sum_table(p,n)

c = GLn.GL_f(p,n,irp,s,elems,mat_mul,mat_sum)
# init
parS = Hurley.initSender(s, p, n, irp, elems, mat_mul, mat_sum, c)
parR = Hurley.initReciever(s, p, n, irp, elems, mat_mul, mat_sum, c)

xv = [1,2,3]
x = GLn.Vect(s, p, n, irp, elems, mat_mul, mat_sum, xv)
#

#
mesR1 = Hurley.rec1(parR)
mesS1 = Hurley.sen1(x, parS, mesR1)
mesR2 = Hurley.rec2(parR, mesS1)
mesS2 = Hurley.sen2(parS, mesR2)


res = Hurley.getMes(parR, mesS2)
print(res)