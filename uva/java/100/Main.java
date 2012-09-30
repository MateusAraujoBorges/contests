public class Main {
	
	static int count(int n) {
		int current = n;
		int total = 1;

		while (current != 1) {
			if (current % 2 == 1) {
				current = current * 3 + 1;
			} else {
				current = current / 2;
			}
			total++; 
		}

		return total;
	}

	public static void main(String[] args) {
		java.util.Scanner sc = new java.util.Scanner(System.in);
		while (sc.hasNext()) {
			int i = sc.nextInt();
			int j = sc.nextInt();
			int low = Math.min(i,j);
			int hi = Math.max(i,j);
			int max = 0;
			for (int k = low; k <= hi; k++) {
				int r = count(k);
				max = Math.max(max,r);
			}
			System.out.printf("%d %d %d\n",i,j,max);
		}
	}
}
