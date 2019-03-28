import socket
def Encrypt_XOR(cmd,key):                         #Encrypts the plaintext
    st=""
    for i in cmd:
        st+=str(ord(i))+str(ord('~'))      #converts characters into it's ASCII values and '~' acts as intermediate between them
    cipher=int(st)^key
    h=hex(cipher)
    #print("\nciphertext:",h[2:len(h)])
    return h[2:len(h)]
def Decrypt_XOR(decrypt,key):                               #Decrypts  the ciphertext
        t=int('0x'+str(decrypt),0)
        pt=(t^key)
        pt=str(pt)
        bt=''
        plaintext=''
        s=''
        count=0
        v=count
        l=(len(pt)-2)
        for i in range(0,len(pt)):         #used to convert ASCII values to it's characters
          if count>v:
              v=v+1
              continue
          if i<l:
            bt=pt[i]+pt[i+1]+pt[i+2]
            if bt == '126':                #acts as intermediate between two characters
                count+=2
                bt=0
                plaintext+=chr(int(s))
                s=''
            else:
                s+=(pt[i])
                bt=0
        return plaintext
def create_key():                               #Generates keys for encryption and decryption purpose using Diffe Hellman algorithm
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
print("\nCONNECTING............")
s.bind((host,port))
s.listen()
c,add=s.accept()
print ("\nCONNECTED WITH CLIENT: ",add)   #shows connection with client by displaying it's host and port
key=create_key()
cmd=""
r=''
while cmd!="bye":
  cmd=input("\nSERVER: ")
  if cmd == "":
      cmd=" "
  ecmd=Encrypt_XOR(cmd,key)
  c.send(bytes(ecmd,'utf8'))                                            #sends ciphertext to client
  if cmd == 'bye' and r == 'bye':
     break
  r=Decrypt_XOR(c.recv(1024).decode('utf8'),key)                #receives ciphertext from client
  print ("\nCLIENT: ",r)
c.close()
