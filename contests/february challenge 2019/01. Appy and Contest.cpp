//did not work for larger test cases -> shifted to python.

#include <iostream>
#include <boost/math/common_factor.hpp> 
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	while(t-->0){
		int n, a, b, k;
		cin>>n; 
		cin>>a; 
		cin>>b;
		cin>>k;

		int x=n/a;
		int y=n/b;
		int z=n/boost::math::lcm(a,b);

		if(x+y-(2*z)>=k)
			cout<<"Win\n";
		else
			cout<<"Lose\n";

	}
	return 0;
}