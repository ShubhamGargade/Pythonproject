from Crypto.Cipher import AES
import socket
iv=12
def pad(st):
    return st + (((16-len(s))%16) * '{')
def encrypt(plaintext,key):
    aes=AES.new(key,AES.MODE_CBC,iv)
    ciphertext=aes.encrypt(plaintext)
    print ("\nCiphertext is: ",ciphertext)
    return ciphertext
def decrypt(cipher):
    global key
    aes=AES.new(key,AES.MODE_CBC,iv)
    normaltext=aes.decrypt(cipher).decode("utf-8")
    c=normaltext.count('{')
    return normaltext[:len(normaltext)-c]
s=socket.socket()
host=socket.gethostname()
port=1234
s.connect((host,port))
p=1234
g=8767
b=6731
B=(g**b)%p
s.send(bytes(B))
A=s.recv(1024)
print((int.from_bytes(A,byteorder='big')))
key=bytes((int.from_bytes(A,byteorder='big')**b)%p)
print(key)
cmd1=""
while cmd1!="bye":
   print ("\nSERVER: ",decrypt(s.recv(1024)))
   cmd1=input("\nCLIENT: ")
   ecmd1=encrypt(pad(cmd1),key)
   s.send(ecmd1)
s.close()
