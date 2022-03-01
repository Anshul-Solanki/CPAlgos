> This algorithm uses Fermet's little theorem to efficiently compute inverse mod of factorials of consecutive numbers in O(N) time complexity.
> First find inv mod of N! in log(P) time
> Then inv mod of (N-1)! = (InvMod[N] * N) % P  
