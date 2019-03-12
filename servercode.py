from Crypto.Cipher import AES
import socket
iv=12
def pad(st):
    return st + (((16-len(st))%16) * '{')
def encrypt(plaintext,key):
    aes=AES.new(key,AES.MODE_CBC,iv)
    ciphertext=aes.encrypt(plaintext)
    print ("\nCiphertext is: ",ciphertext)
    return ciphertext
def decrypt(cipher):
    global key
    aes=AES.new(key,AES.MODE_CBC,iv)
    normaltext=aes.decrypt(cipher).decode("utf-8")
    ct=normaltext.count('{')
    return normaltext[:len(normaltext)-ct]
s=socket.socket()
host='192.168.43.69'
port=1234
print ("ip is:",host)
s.bind((host,port))
s.listen(5)
c,add=s.accept()
print ("\nGot connection with: ",add)
p=1234
g=8767
a=7534
A=(g**a)%p
c.send(bytes(A))
B=c.recv(1024)
print((int.from_bytes(B,byteorder='big')))
key=bytes((int.from_bytes(B,byteorder="big")**a)%p)
cmd=""
while cmd!="bye":
  cmd=input("\nSERVER: ")
  ecmd=encrypt(pad(cmd),key)
  c.send(ecmd)
  print ("\nCLIENT: ",decrypt(c.recv(1024)))
c.close()
