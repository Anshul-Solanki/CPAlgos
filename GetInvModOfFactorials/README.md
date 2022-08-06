This algorithm uses Fermat's little theorem to efficiently compute inverse mod of factorials of consecutive numbers in O(N) time complexity.  
(N^P)%P = ((1 + N-1)^P)%P = 1 + ((N-1)^P)%P = N%P  
Above eq is true only if P is prime number, which ensures that pCr is multiple of P for r between 1 to P-1  
So Fermat's theorm works for P: prime and N: any number not divisible by P  

This is how GetInvModOfFactorials work:  
First find inv mod of N! in log(P) time  
Then inv mod of (N-1)! = (InvMod[N] * N) % P    
