
# Elliptic Curve Cryptography Algorithm

The major advantage of ECC is that it provides encryption keys of smaller length compared to RSA with same level of security (more technical explaination in later section). This would optimize E2E performance of any application using this encryption, wrt. encryption time and memory usage. However ECC has potential vulnerabilities which can be exloited by attackers, it requires selection of params carefully, to be standardised by experts who understand the real mathematical complexity of elliptic curve.  

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

These point (addition/multiplication) operations on EC are made irreversible with some steps (trapdoor) to be used for encryption  

Useful tool to visualize elliptic curves based on equation - https://www.desmos.com/calculator/ialhd71we3  

**Public / Private keys - EC points**  

**Discrete logarithm problem**  
ECC is secured with DLP: https://www.doc.ic.ac.uk/~mrh/330tutor/ch06s02.html#:~:text=The%20discrete%20logarithm%20problem%20is,logarithms%20depends%20on%20the%20groups   

**Why ECC supports shorter key lengths compared to RSA**  
This difference is due to fact that -  
ECC is based on discrete logarithm problem  
RSA is based on integer factorization  
This is decided based on which algos are available to break encryption and the comparative difficulty comparision across RSA and ECC  
My theory is - because RSA can be solved with various algorithms to factor a large prime number (like sieve algo)  
The discrete logarithm in particular cannot be solved with such algo, hence it is more secure with lesser key length  

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

Resources:  
1. Best explanation for elliptic curve point operations: https://www.youtube.com/watch?v=XmygBPb7DPM  
2. Using point operations for cryptography - https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/  
3. Great technical details of ECC (+ about generator point) - https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc  
4. Point Multiplication - https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication  
5. Point Operations - https://www.idc-online.com/technical_references/pdfs/data_communications/Point%20Multiplication.pdf  
6. Subgroup of EC - https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc#order-and-cofactor-of-elliptic-curve  
7. Small subgroup attach EC - https://www.rfc-editor.org/rfc/rfc2785  
