#include <stdio.h>

int main(int argc, char const *argv[])
{
	int t, n, qo, rem, out[3];
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		scanf("%d", &n);
		n--;
		qo = n/26;
		rem = n%26;
		for(int j=0; j<3; j++)
			out[j]=0;
		if(rem<2)
			out[0] = 1;
		else if(rem<10)
			out[1] = 1;
		else
			out[2] = 1;
		for(int j=0; j<3; j++)
			printf("%d", out[j]*qo);
	}
	return 0;
}