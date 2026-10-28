#ENCODING SCHEME================================================================

encode={
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'a':10,
    'b':11,
    'c':12,
    'd':13,
    'e':14,
    'f':15,
    'g':16,
    'h':17,
    'i':18,
    'j':19,
    'k':20,
    'l':21,
    'm':22,
    'n':23,
    'o':24,
    'p':25,
    'q':26,
    'r':27,
    's':28,
    't':29,
    'u':30,
    'v':31,
    'w':32,
    'x':33,
    'y':34,
    'z':35,
    'A':36,
    'B':37,
    'C':38,
    'D':39,
    'E':40,
    'F':41,
    'G':42,
    'H':43,
    'I':44,
    'J':45,
    'K':46,
    'L':47,
    'M':48,
    'N':49,
    'O':50,
    'P':51,
    'Q':52,
    'R':53,
    'S':54,
    'T':55,
    'U':56,
    'V':57,
    'W':58,
    'X':59,
    'Y':60,
    'Z':61,
    '?':62,
    ' ':63
        }

#==============================================================================

NumberOfRounds=5
block_size_ende=6
block_size_crypt=9

#==============================================================================

def encoder(data):
    s=''
    for i in data:
        s+=bin(encode[i])[2:].zfill(block_size_ende)
    return s

def decoder(data):
    s=''
    blocks = [data[i:i + block_size_ende] for i in range(0, len(data), block_size_ende)]
    for i in blocks:
        i=int(i,2)
        for k,v in dict.items(encode):
            if v==i:
                s+=k
    return s

def block_crypt(data,block_size_crypt):
    data+='0'*(block_size_crypt-len(data)%block_size_crypt)
    blocks = [data[i:i + block_size_crypt] for i in range(0, len(data), block_size_crypt)]
    return blocks

def deblock(blocks):
    s=''
    for i in blocks:
        s+=i
    return s

def xor(a,b):
    a=int(a,2)
    b=int(b,2)
    return bin(a^b)[2:].zfill(block_size_crypt)

def substitute_enc(x,table):
    return table[x]

def substitute_dec(x,table):
    for k,v in dict.items(table):
        if v==x:
            return k

def permute(x,P):
    r=''
    for i in P:
        n=list(i).index(1)
        r+=x[n]
    return r

#==============================================================================
