#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	while(t-->0){
		
		int n;
		cin>>n;
		
		long int a[n];
		for(int i=0; i<n; i++)
			cin>>a[i];
		
		long long int sum=0;
		for(int i=0; i<n; i++)
			sum+=a[i];

		cout<<sum-n+1<<endl;

	}
	return 0;
}