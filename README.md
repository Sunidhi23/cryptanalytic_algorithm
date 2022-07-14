# cryptanalytic_algorithm
Fully homomorphic encryption supports meaningful computations on encrypted 
data and hence, is widely used in cloud computing and big data environments.
The special encryption scheme can convert operations on plaintexts into those on 
ciphertexts. So we can perform arbitrarily many addition and multiplication 
operations on ciphertexts in order to obtain the computational results on the 
corresponding plaintexts without decrypting the ciphertexts. The proposed 
homomorphic encryption scheme supports many homomorphic additions and a 
limited number of homomorphic multiplications. The use of encryption scheme is 
to design a privacy-preserving-outsourced association rule mining scheme on 
vertically partitioned databases. The basic idea of the mining algorithm is just to 
utilize the symmetric homomorphic encryption scheme to encrypt the binary 
realness value of each transaction. The realness value represents whether the 
transaction is real or fictitious. In this way, a cloud can explore the homomorphic 
computation properties on ciphertexts to mine association rules without 
decryptions. Hence, the data privacy is protected during the information 
processing on transaction data. In this project we implemented an efficient 
cryptanalytic attack on homomorphic encryption scheme. The attack can 
reconstruct the whole secret key and can be divided into two stages. In the first 
stage, we use two ciphertexts to construct a rational number. Then the first part of 
the secret key is retrieved by exhausting all the polynomially many convergent 
fractions of the derived rational number. The second stage of the attack recovers 
the second part of the secret key just by performing one time the Euclidean 
algorithm to get the greatest common divisor of two integers derived from the 
first stage. In case of more than two homomorphic multiplications, all the secret 
keys of the randomly instantiated encryption schemes can be very efficiently 
recovered, and the success probability is at least 98% for one homomorphic
multiplication.
