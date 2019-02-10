#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	while(t-->0){
		int d, temp_p, temp_d, q;
		int res[31]={0};
		cin>>d;
		while(d-->0){
			cin>>temp_d;
			cin>>temp_p;
			res[temp_d-1]=temp_p;
		}
		for(int i=1; i<31; i++)
			res[i]+=res[i-1];
		cin>>q;
		while(q-->0){
			int dead, req;
			cin>>dead;
			cin>>req;
			if(req<=res[dead-1])
				cout<<"Go Camp"<<endl;
			else
				cout<<"Go Sleep"<<endl;
		}
	}
	return 0;
}