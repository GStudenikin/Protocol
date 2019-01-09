import socket
import pickle
import Hurley
import LinGr


# start
s = 3
m = 11
params = Hurley.initSender(s, m)
xv = [3,2,5]
x = LinGr.Vect(s,m,xv)

# setup socket
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

# 1st step
data = conn.recv(1024)
mesv = pickle.loads(data)
mesR1 = LinGr.Vect(s,m,mesv)
mes1 = Hurley.sen1(x, params, mesR1)
inf1 = pickle._dumps(mes1)
conn.send(inf1)

# 2nd step
data2 = conn.recv(1024)
mesR2 = pickle.loads(data2)
mes2 = Hurley.sen2(params, mesR2)
inf2 = pickle._dumps(mes2)
conn.send(inf2)

conn.close()