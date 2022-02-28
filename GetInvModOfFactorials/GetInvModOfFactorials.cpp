#include <bits/stdc++.h>
using namespace std;

#define ll long long

ll P, N;

ll GetInvMod(ll x)
{
	ll xt = x;
	ll r = 1;
	ll i = P-2;
	
	while(i > 0)
	{
		if (i%2 == 1)
		{
			r = (r * xt)%P;
			i--;
		}
		else
		{
			xt = (xt*xt)%P;
			i /= 2;
		}
	}
	
	return r;
}

vector<ll> GetInvModOfFactorials()
{
	// result
	vector<ll> res(N+1);
	
	// Find inv mod of N! first in log(P)
	// Compute N!%P
	ll NFac = 1;
	for(ll i=1; i<=N; i++)
	{
		NFac = (NFac * i)%P;
	}
	
	res[N] = GetInvMod(NFac);
	
	// Find inv mod of rest of numbers in O(N)
	ll iFac = res[N];
	for(ll i=N; i>1; i--)
	{
		iFac = (iFac * i)%P;
		res[i-1] = iFac;
	}
	
	// overall time complexity = O(N) + log(P) =~ O(N)
	return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // P: any prime number
    // N: any number
    cin >> P >> N;
    
    vector<ll> out = GetInvModOfFactorials();
    
    // verify result
    ll prd = 1;
    ll r = 1;
    bool success = true;
    for(int i=1; i<=N; i++)
    {
    	prd = (prd * i)%P;
    	r = (out[i] * prd)%P;
    	
    	if (r != 1)
    	{
    		success = false;
    		break;
		}
	}
	
	if (success == true)
	{
		cout << "success!";
	}
	else
	{
		cout << "Failed!";
	}
    
    return 0;
}

