from numpy.linalg import inv as inverse
import sys
import pickle
from utils import *

fkey=open("KEY.dat",'rb')
fperm=open("PERMUTATION.dat",'rb')
fsubs=open("SUBSTITUTION.dat",'rb')

key=(pickle.load(fkey))[-1::-1]
P=inverse(pickle.load(fperm))
table=pickle.load(fsubs)

fkey.close()
fperm.close()
fsubs.close()

def decipher(x,key,P,table):
    x=permute(x,P)
    x=substitute_dec(x,table)
    x=xor(x,key)
    return x

def process(x):
    cipher=encoder(ciphertext)
    l=block_crypt(cipher,block_size_crypt)
    for s in key:
        for i in range(0,len(l)):
            l[i]=decipher(l[i],s,P,table)
    plaintext=decoder(deblock(l))
    return plaintext

if sys.argv[1]=='text':
    ciphertext=sys.argv[2]
    plaintext=process(ciphertext)
    print("\n\n\n",plaintext,"\n\n\n")


elif sys.argv[1]=='file':
    f=open(f"{sys.argv[2]}",'r')
    fp=open(f"{sys.argv[2][0:-4]}_plain.txt",'w')
    ciphertext=f.read()
    plaintext=process(ciphertext)
    fp.write(plaintext)
    fp.flush()
    fp.close()