import socket
def Encrypt_XOR():
    st=""
    for i in cmd:
        st+=str(ord(i))+str(ord('{'))
    cipher=int(st)^key
    h=hex(cipher)
    print("\nciphertext:",h)
    return h
def Decrypt_XOR(decrypt,key):
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
    b=3432
    B=(q**b)%p
    s.send(bytes(str(B),'utf8'))
    A=s.recv(1024).decode('utf8')
    key=(int(A)**b)%p
    return key
s=socket.socket()
host=socket.gethostname()
port=1234
s.connect((host,port))
key=create_key()
cmd1=""
while cmd1!="bye":
   print ("\nSERVER: ",Decrypt_XOR(s.recv(1024).decode('utf8'),key))
   cmd1=input("\nCLIENT: ")
   ecmd1=cmd1
   s.send(bytes(ecmd1,'utf8'))
r=s.recv(1024).decode('utf8')
if r == 'bye':
       print("\nSERVER: ",r)
s.close()
