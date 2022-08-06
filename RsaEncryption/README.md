# RSA Encryption Algorithm

Public and private keys are computed with below steps:  
Use two prime numbers p and q (generally big values to ensure security) to find n = p*q  
Compute totient function value as phi(n) = (p-1) * (q-1)  
Choose a number 'e' coprime to phi(n).  
Compute inverse modulo of 'e' mod (phi(n)). This is always possible as gcd(e, phi(n)) = 1, and using extended euclidean algorithm.  

public key is 'e' and 'n'.  
private key is 'd'. (and phi(n) is also considered secret info, as it can be used along with n to derive values of p and q)  

Encryption: enData = (data ^ e ) mod n , data should be less than n to avoid loosing info  
enData is the encrypted data  

Decryption: data = (enData ^ d) mod n  

Proof:  
Given that d is modulo inverse of e  
e*d mod phi(n) = 1 mod phi(n)  
hence,  
e*d = k*phi(n) + 1  

And using euler's theorem, we know that:  
(a ^ (phi(n))) mod n = 1 mod n , if a is coprime to n (what if a is not coprime to n?)  
hence,  
(data ^ (k*phi(n)+1) ) mod n = data  

This site has great documentation: https://brilliant.org/wiki/rsa-encryption/
