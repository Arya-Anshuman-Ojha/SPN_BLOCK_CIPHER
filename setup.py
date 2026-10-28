import numpy as np
import random
import pickle
from utils import *

#CREATING THE PERMUTATION MATRIX====================================
rng=np.random.default_rng()
P=rng.permutation(np.eye(block_size_crypt))

#CREATING THE ROUND KEY=============================================
key=[]
for i in range(0,NumberOfRounds):
    k=random.randint(0,2**(block_size_crypt))
    k=bin(k)[2:].zfill(block_size_crypt)
    key.append(k)

#CREATING THE SUBSTITUTION LOOK-UP TABLE============================
table=dict()
k=[]
for i in range(0,2**(block_size_crypt)):
    k.append(bin(i)[2:].zfill(block_size_crypt))
v=random.sample(k,len(k))
for i in range(0,2**(block_size_crypt)):\
    table[k[i]]=v[i]

#SAVING ALL THE COMPONENTS==========================================
fkey=open("KEY.dat",'wb')
fperm=open("PERMUTATION.dat",'wb')
fsubs=open("SUBSTITUTION.dat",'wb')
fenc=open("ENCODING_SCHEME.dat",'wb')
pickle.dump(key,fkey)
pickle.dump(P,fperm)
pickle.dump(table,fsubs)
pickle.dump(encode,fenc)
fkey.flush()
fkey.close()
fperm.flush()
fperm.close()
fsubs.flush()
fsubs.close()
fenc.flush()
fenc.close()

#===================================================================
