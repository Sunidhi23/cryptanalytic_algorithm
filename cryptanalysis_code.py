#############The Encryption Scheme (KeyGen (p,q,s,d,m1,m2,m3,r1,r2,r3,n are taken as per research paper Initial Values)and Encryption(c1,c2,c3)#######################

from sympy import primefactors
p = 469912017615039696657898333324665521332926989239767910768317623337711665463118526537545576515165287
q = 1039125240703888392755807
s = 412508113739099722581862617392145275494249761372960796922560608994137286538503346495320623264234557
d = 1
r1 = 170453863991
m1 = 1
d = 1
r2 = 782935439797
m2 = 0
r3 = 884145581244
m3 = 1
n = 153
SK = []   #Secret key to be retrieved
c1=((s**d)*(r1*q+m1))%p
print('*****************************************The Encryption Scheme Results*********************************************')
print("m1 : ",m1)
print("c1 : ",c1)
c2=((s**d)*(r2*q+m2))%p
print("m2 : ",m2)
print("c2: ",c2)
c3=((s**d)*(r3*q+m3))%p
print("m3 : ",m3)
print("c3: ",c3)

##################The Cryptanalytic Algorithm############################################
####The First Stage(c,fk and s calculation)and Second Stage(r1q,r2q,gcd and q calculation)###########


############ c calculation ################################
def modulo_multiplicative_inverse(A, M):
    gcd, x, y = extended_euclid_gcd(A, M)
    if x < 0:
        x += M
    
    return x

def extended_euclid_gcd(a, b):
  
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r//r
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]



invc1 = modulo_multiplicative_inverse(c1, p)
c = (invc1*c2)%p
print('\n')
print('**************************The Cryptoanalytic Algorithm (1st and 2nd Stage Results)*******************************')
print('\n')
print('The First stage c =',c)
print('\n')
print('*****************************************************************************************************************')
print('\n')
############ fk,s(The First Stage) r1q,r2q,gcd , q (The second stage) calculation calculation ################################

f=[]
e=[]
g=[]
convlist = []


def r2cf(n1,n2):
  while n2:
    n1, (t1, n2) = n2, divmod(n1, n2)
    yield t1
    


def gcd (a,b):
    r=a%b
    while r:
        a=b
        b=r
        r=a%b
    return b


def convergent ():
    
    for k in range (2,n+1):
        e.append((convlist[k]*e[k-1]) + e[k-2])
        f.append((convlist[k]*f[k-1])+ f[k-2])
    for m in range (2,n+1):
        if gcd(e[m],f[m]) == 1:
            ck = e[m]/f[m]
            
    
    
    



def modulo_multiplicative_inverse(A, M):
    gcd, x, y = extended_euclid_gcd(A, M)
    if x < 0:
        x += M
    
    return x

def extended_euclid_gcd(a, b):
   
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r//r 
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]

def euclideangcd(a, b):
	if a == 0:
		return (b)
	else:
		return euclideangcd(b%a,a)





def Cryptanalyticalgo ():
    for k in range (1,n+1):
        a = f [k]
        invofa = modulo_multiplicative_inverse(a, p)
        s = (invofa*c1)%p
        invofs = modulo_multiplicative_inverse(s, p)
        r1q = ((c1*invofs)-(m1%p))
        r2q = ((c2*invofs)-(m2%p))
        if (k ==74):
            print('*****************************************************************************************************************')
            print('\n')
            print('The First Stage s value is -->',s)
            print('\n')
            print('*****************************************************************************************************************')
            invofs = modulo_multiplicative_inverse(s, p)
            r1q = ((c1*invofs)-(m1%p))%p
            r2q = ((c2*invofs)-(m2%p))%p
            print('\n')
            print('**********************************2nd Stage Results**************************************************************')
            print('r1q-->',r1q)
            print('r2q-->',r2q)
            q = euclideangcd(r1q,r2q)
            if q%2 != 0 :
                q = primefactors(q)[-1] # largest prime factor of gcd(r1q, r2q) is q
                print('gcd is ',q)
            message = ((invofs*c3)%p)%q
            if message == m3 :
                SK.append(s)
                SK.append(q)
    print ('Secret Key SK(s,q) is ', SK)   #############Final Secret key SK retrieved######################
    print('\n')
    print ('ATTACK SUCCESSFUL!')
            
        
        
        
convlist = list(r2cf(c,p))
e.append(convlist[0])
f.append(1)
e.append((convlist[0]*convlist[1])+ 1)
f.append(convlist[1])
convergent()
print('\n')
print('First stage fk values are \n -->',f)
Cryptanalyticalgo()
