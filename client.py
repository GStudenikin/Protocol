import socket
import pickle
import Hurley


# start
s = 3
m = 11
params = Hurley.initReciever(s, m)

# setup socket
sock = socket.socket()
sock.connect(('localhost', 9090))

# 1st step
mes1 = Hurley.rec1(params)
inf = pickle._dumps(mes1.vect)
sock.send(inf)

# 2nd step
data = sock.recv(1024)
mesS1 = pickle.loads(data)
mes2 = Hurley.rec2(params, mesS1)
inf2 = pickle._dumps(mes2)
sock.send(inf2)

# decryption
data2 = sock.recv(1024)
res = pickle.loads(data2)
message = Hurley.getMes(params,res)
print(message)

sock.close()