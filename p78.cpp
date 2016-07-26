#include <stdio.h>

#define M (80000)
int jw[M][M];

int c(int n, int m) {
	if (n==0 || n==1 || m==1) return 1;
	if (m>n) return c(n,n);
	if (jw[n][m]) return jw[n][m];
	int res=c(n-m,m)+c(n,m-1);
	res%=1000000;
	jw[n][m]=res;
	return res;
}

int main() {
	for (int n=1; n<M; n++) {
		printf("c(%d)\n", n);
		if (c(n,n)==0) {
			printf("%d\n", n);
			break;
		}
	}
}
