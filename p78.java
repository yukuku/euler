public class p78 {

	static int[][] jw = new int[80000][80000];

	static int c(int n, int m) {
		if (n==0 || n==1 || m==1) return 1;
		if (m>n) return c(n,n);
		if (jw[n][m]!=0) return jw[n][m];
		int res=c(n-m,m)+c(n,m-1);
		res%=1000000;
		jw[n][m]=res;
		return res;
	}

	public static void main(String[] args) {
		for (int n=1; n<80000; n++) {
			System.out.printf("c(%d)\n", n);
			if (c(n,n)==0) {
				System.out.printf("%d\n", n);
				break;
			}
		}
	}

}