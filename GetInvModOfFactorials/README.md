This algorithm uses Fermat's little theorem to efficiently compute inverse mod of factorials of consecutive numbers in O(N) time complexity.  
(N^P)%P = ((1 + N-1)^P)%P = 1 + ((N-1)^P)%P = N%P  
First find inv mod of N! in log(P) time  
Then inv mod of (N-1)! = (InvMod[N] * N) % P    
