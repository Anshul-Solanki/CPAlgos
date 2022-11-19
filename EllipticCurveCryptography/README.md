
# Elliptic Curve Cryptography Algorithm

The major advantage of ECC is that it provides encryption keys of smaller length compared to RSA with same level of security (more technical explaination in later section). This would optimize E2E performance of any application using this encryption, wrt. encryption time and memory usage. However ECC has potential vulnerabilities which can be exloited by attackers, it requires selection of params carefully, to be standardised by experts who understand the real mathematical complexity of elliptic curve.  

Elliptic curves used for cryptography are special curves which support "Point Operations" based on which the cryptosystem is defined.  

Useful tool to visualize elliptic curves based on equation - https://www.desmos.com/calculator/ialhd71we3  

Resources:  
Best explanation for elliptic curve point operations: https://www.youtube.com/watch?v=XmygBPb7DPM  
Using point operations for cryptography - https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/  
Great technical details of ECC (+ about generator point) - https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc  
