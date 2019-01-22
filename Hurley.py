import LinGr
import GLn

# initialization Reciever's parameters
# return params(y, B, B1, B2)
# c - generator of cyclic group
def initReciever(s, p, n, c = None, elems = None, mat_mul = None, mat_sum = None, cyclic = None):
    params = []
    if(n == 1):
        params.append(LinGr.Vect(s, p))
        if(c == None):
            params.append(LinGr.Diag(s, p))
            params.append(LinGr.Diag(s, p))
            params.append(LinGr.Diag(s, p))
        else:
            params.append(LinGr.CG(c))
            params.append(LinGr.CG(c))
            params.append(LinGr.CG(c))
    else:
        if(cyclic == None):
            params.append(GLn.Vect(s, p, n, c, elems, mat_mul, mat_sum))
            params.append(GLn.Diag(p, n, c, s, elems, mat_mul, mat_sum))
            params.append(GLn.Diag(p, n, c, s, elems, mat_mul, mat_sum))
            params.append(GLn.Diag(p, n, c, s, elems, mat_mul, mat_sum))
        else:
            params.append(GLn.Vect(s, p, n, c, elems, mat_mul, mat_sum))
            params.append(GLn.CG(cyclic))
            params.append(GLn.CG(cyclic))
            params.append(GLn.CG(cyclic))
    return params

# initialization Sender's parameters
# return params(A, A1)
# c - generator of cyclic group
def initSender(s, p, n, c = None, elems = None, mat_mul = None, mat_sum = None, cyclic = None):
    params = []
    if(n == 1):
        if(c == None):
            params.append(LinGr.Diag(s, p))
            params.append(LinGr.Diag(s, p))
        else:
            params.append(LinGr.CG(c))
            params.append(LinGr.CG(c))
    else:
        if (cyclic == None):
            params.append(GLn.Diag(p, n, c, s, elems, mat_mul, mat_sum))
            params.append(GLn.Diag(p, n, c, s, elems, mat_mul, mat_sum))
        else:
            params.append(GLn.CG(cyclic))
            params.append(GLn.CG(cyclic))
    return params

# 1st step of reciever
# get reciever's params = (y, B, B1, B2)
# return mes = yB
def rec1(params):
    return params[0]*params[1]

# 1st step of sender
# x - message for reciever
# sender's params = (A, A1)
# rMes = yb
# return mes = (xA, yBA1)
def sen1(x, params, rMes):
    mes = []
    mes.append(x * params[0])
    mes.append(rMes * params[1])
    return mes

# 2nd step of reciever
# reciever's params = (y, B, B1, B2)
# sMes = (xA, yBA1)
# return mes = (xAB1, yA1B2)
def rec2(params, sMes):
    mes = []
    mes.append(sMes[0]*params[2])
    bi = params[1].inv()
    mes.append(sMes[1]*bi)
    mes[1] *= params[3]
    return mes

# 2nd step of sender
# sender's params = (A, A1)
# rMes = (xAB1, yA1B2)
# return mes = xB1 - yB2
def sen2(params, rMes):
    ai = params[0].inv()
    a1i = params[1].inv()
    mes1 = rMes[0]*ai
    mes2 = rMes[1]*a1i
    mes = mes1 - mes2
    return mes

# decrypt message
# reciever's params = (y, B, B1, B2)
# sMes = xB1 - yB2
# return decrypted message
def getMes(params, sMes):
    b1i = params[2].inv()
    ost = params[0] * params[3]
    ost *= b1i
    res = sMes * b1i
    res += ost
    if(isinstance(res, GLn.Vect)):
        vec = []
        for i in range(res.size):
            vec.append(res.vect[i].elnum)
        return vec
    return res

def vstr(Vect):
    strm = "|".join([str(elem) for elem in Vect.vect])
    return strm

def strv(size, modulo, string):
    new = string.split("|")
    for i in range(len(new)):
        new[i] = int(new[i])
    return LinGr.Vect(size, modulo, new)