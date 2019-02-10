#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, n, k, i, j;
	long int arr[1000000];
	cin>>t;
	for(i=0; i<t; i++){
		cin>>n>>k;
		for (j=0; j<n; j++)
			cin>>arr[j];
		sort(arr, arr+n, greater<int>());
		j=k-1;
		while(arr[j]==arr[j+1])
			j++;
		cout<<j+1<<endl;
	}
	return 0;
}