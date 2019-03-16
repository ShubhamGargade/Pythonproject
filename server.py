import socket
def Encrypt_XOR(cmd,key):
    st=""
    for i in cmd:
        st+=str(ord(i))+str(ord('{'))
    cipher=int(st)^key
    h=hex(cipher)
    print("\nciphertext:",h)
    return h
def Decrypt_XOR():
        t=int(decrypt,0)
        pt=(t^key)
        pt=str(pt)
        bt=''
        plaintext=''
        s=''
        count=0
        v=count
        l=(len(pt)-2)
        for i in range(0,len(pt)):
          if count>v:
              v=v+1
              continue
          if i<l:
            bt=pt[i]+pt[i+1]+pt[i+2]
            if bt == '123':
                count+=2
                bt=0
                plaintext+=chr(int(s))
                s=''
            else:
                s+=(pt[i])
                bt=0
        return plaintext
def create_key():
    p=2379
    q=3289
    a=6734
    A=(q**a)%p
    c.send(bytes(str(A),'utf8'))
    B=c.recv(1024).decode('utf8')
    key=(int(B)**a)%p
    return key
s=socket.socket()
host=socket.gethostname()
port=1234
print("ip: ",host)
s.bind((host,port))
s.listen()
c,add=s.accept()
print ("\nGot connection with: ",add)
key=create_key()
cmd=""
while cmd!="bye":
  cmd=input("\nSERVER: ")
  ecmd=Encrypt_XOR(cmd,key)
  c.send(bytes(ecmd,'utf8'))
  if cmd == 'bye' and r == 'bye':
     break
  r=c.recv(1024).decode('utf8')
  print ("\nCLIENT: ",r)
c.close()
