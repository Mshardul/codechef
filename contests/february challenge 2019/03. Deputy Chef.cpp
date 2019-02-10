#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	while(t-->0){
		int n, ans=0, found=0;
		cin>>n;
		int a[n], d[n];
		for(int i=0; i<n; i++)
			cin>>a[i];
		for(int i=0; i<n; i++)
			cin>>d[i];

		if(d[0]>(a[1]+a[n-1])){
			found=1;
			ans=d[0];
		}
		if(d[n-1]>(a[n-2]+a[0])){
			found=1;
			ans=max(ans, d[n-1]);
		}
		for(int i=1; i<n-1; i++){
			if(d[i]>(a[i-1]+a[i+1])){
				found=1;
				ans=max(ans, d[i]);
			}
		}
		if(!found)
			cout<<"-1";
		else
			cout<<ans;
		cout<<endl;
	}
	return 0;
}