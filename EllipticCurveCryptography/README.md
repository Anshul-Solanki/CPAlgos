
# Elliptic Curve Cryptography Algorithm

The major advantage of ECC is that it provides encryption keys of smaller length compared to RSA with same level of security (more technical explaination in later section). This would optimize E2E performance of any application using this encryption, wrt. encryption time and memory usage. However ECC has potential vulnerabilities which can be exloited by attackers, it requires selection of params carefully, to be standardised by experts who understand the real mathematical complexity of elliptic curve.  
High level usage of this algo - https://www.youtube.com/watch?v=0NGPhAPKYv4  
Some more details - https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc  
In principle - a few standard elliptic curves are used, with varied level of security - length of keys / performance etc..  
And based on curve - different encryption/signature algorithms are used based on private/public keys.   
Where private key is selected as random number within the limit of curve field.  
And public key is the EC point corresponding to private key.  

**Point Operations**  
Elliptic curves used for cryptography are special curves which support "Point Operations" like based on which the cryptosystem is defined  
See Resources [1] and [2]  
Point Addition 'C' of two points A and B is defined by line joining A and B intersecting third point C on curve  
Take any two points on the  elliptic curve and draw a line through them, it will intersect the curve at exactly one more place (or infinity)  
Proof for this property might be lengthy but taking a look at curve it seems intutive  
![image](https://user-images.githubusercontent.com/29455503/202861980-951463d6-6821-485a-a01b-b56467394b90.png)  
Point operations are executed with "Closed" property, as they operate on curve in finite fields  
If a point (x,y) is outside the field it can be simply mapped to inside the field applying the mod  
So point operations are executed without field, but final result is mapped back to move inside the field  
Example curve with finite field of F17 is: y2 = x3 + 7 (mod17) , indicates all points which satisfy this equation (with mod)  
Hence elliptic curves used in cryptography are set of integer points in square matrix, not elliptic curves.  

These point (addition/multiplication) operations on EC are made irreversible with some steps (trapdoor) to be used for encryption  

Useful tool to visualize elliptic curves based on equation - https://www.desmos.com/calculator/ialhd71we3  

**Public / Private keys - EC points**  

**Generating Private Key**  
It is simply generating a random number between limits. In this case the limit is defined by "range of the curve's field size"  
Very nice explanation: https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/ (still not very concrete)  
Great source to understand E2E encryption steps - https://cryptobook.nakov.com/asymmetric-key-ciphers/ecc-encryption-decryption  

**Computing Public Key**  
First we have generator point - and multiplying it with private key (k) gives the EC point as public key  
More details here: https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc  

**Discrete logarithm problem**  
ECC is secured with DLP: https://www.doc.ic.ac.uk/~mrh/330tutor/ch06s02.html#:~:text=The%20discrete%20logarithm%20problem%20is,logarithms%20depends%20on%20the%20groups   
**Trapdoor function of ECC**  
Computing the private key from the public key in this kind of cryptosystem is called the elliptic curve discrete logarithm function which is trapdoor function  
Ref: https://blog.boot.dev/cryptography/elliptic-curve-cryptography/#:~:text=Elliptic%20Curve%20Cryptography%20(ECC)%20is,because%20it%20is%20so%20lightweight.  
This is a great trapdoor function because if you know where the starting point (A) is and how many hops are required to get to the ending point (E), it’s very easy to find the ending point. On the other hand, if all you know is where the starting point and ending point are, it’s nearly impossible to find how many hops it took to get there.  
Public Key: Starting Point A, Ending Point E  
Private Key: Number of hops from A to E  

**Why ECC supports shorter key lengths compared to RSA**  
This difference is due to fact that -  
ECC is based on discrete logarithm problem  
RSA is based on integer factorization  
This is decided based on which algos are available to break encryption and the comparative difficulty comparision across RSA and ECC  
My theory is - because RSA can be solved with various algorithms to factor a large prime number (like sieve algo)  
The discrete logarithm in particular cannot be solved with such algo, hence it is more secure with lesser key length  

**Generator Point**  
https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc  

**Cofactor of ECC**  
https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc  

**Subgroup of elliptic curve**  
An elliptic curve can have one or many subgroups which is set of points such that when two points are added OR a point is multiplied with number results point in same sub-group  
More info here: https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc#order-and-cofactor-of-elliptic-curve  

**Small subgroup attack**  
It is known that for some curves different generator points generate subgroups of different order. More precisely, if the group order is n, for each prime d dividing n, there is a point Q such that d * Q = infinity  
Because if G*n = Inf, and n = n1*n2, where G is generator point  
Then G*n1*n2 = Inf  
Q = G*n1  
Q*n2 = Inf  
This means that some points used as generators for the same curve will generate smaller subgroups than others. if the group is small, the security is weak  
(n2+1) * Q = Q , cycle repeats here  
This means - however both the points G and Q belong to same sub-group  
Q also belongs to another small sub-group which is subset of large sub-group, and is security risk if used as generator point  
This is known as "small-subgroup" attacks. This is the reason why cryptographers usually choose the subgroup order r to be a prime number  
More info here: https://www.rfc-editor.org/rfc/rfc2785  

**Encryption using ECC**  
This document explains in great way: https://cryptobook.nakov.com/asymmetric-key-ciphers/ecc-encryption-decryption (has sample code as well)  
Using ECDH algorithm  
Steps are :  
If we have User1 as sender , User2 as receiver  
And they have dedicated private/ public key pairs each  
User1 computes sharedKey (this is not actually shared with User2, but User2 is able to deduce it just using public key of User1) = User2_publicKey * User1_privateKey  
And uses it to do encryption  
User2 will be able to decrypt by constructing shared key as:  
sharedKey = User1_publicKey * User2_privateKey  
This means:  
User2_publicKey * User1_privateKey = User1_publicKey * User2_privateKey  

Resources:  
1. Best explanation for elliptic curve point operations: https://www.youtube.com/watch?v=XmygBPb7DPM  
2. Using point operations for cryptography - https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/  
3. Great technical details of ECC (+ about generator point) - https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc  
4. Point Multiplication - https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication  
5. Point Operations - https://www.idc-online.com/technical_references/pdfs/data_communications/Point%20Multiplication.pdf  
6. Subgroup of EC - https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc#order-and-cofactor-of-elliptic-curve  
7. Small subgroup attach EC - https://www.rfc-editor.org/rfc/rfc2785  
8. Some more context on ECC - https://www.youtube.com/watch?v=0NGPhAPKYv4  

