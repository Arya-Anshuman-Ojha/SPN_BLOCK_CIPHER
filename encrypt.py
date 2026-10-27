import sys
import pickle
from utils import *

fkey=open("KEY.dat",'rb')
fperm=open("PERMUTATION.dat",'rb')
fsubs=open("SUBSTITUTION.dat",'rb')

key=pickle.load(fkey)
P=pickle.load(fperm)
table=pickle.load(fsubs)

fkey.close()
fperm.close()
fsubs.close()

def encipher(x,key,P,table):
    x=xor(x,key)
    x=substitute_enc(x,table)
    x=permute(x,P)
    return x

def process(x):
    plain=encoder(x)
    l=block_crypt(plain,block_size_crypt)
    for s in key:
        for i in range(0,len(l)):
            l[i]=encipher(l[i],s,P,table)
    ciphertext=decoder(deblock(l))
    return ciphertext


if sys.argv[1]=='text':
    plaintext=sys.argv[2]
    ciphertext=process(plaintext)
    print("\n\n\n",ciphertext,"\n\n\n")

elif sys.argv[1]=='file':
    f=open(f"{sys.argv[2]}",'r')
    fc=open(f"{sys.argv[2][0:-4]}_cipher.txt",'w')
    plaintext=f.read()
    ciphertext=process(plaintext)
    fc.write(ciphertext)
    fc.flush()
    fc.close()