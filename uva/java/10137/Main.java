public class Main {

	public static int compute(int[] array) {
		int avg = 0;
		int rem = 0;
		int total = 0;

		for (int c : array) {
			total += c;
		}
		avg = total / array.length;
		rem = total % array.length;		 

		int totalPos = 0;
		int nBiggerAvg = 0;

		for (int c : array) {
			if (c > avg) {
				totalPos += c - avg;
				nBiggerAvg++;
			}
		}
		//don't need to give remaining pennies to the people that will give money
		return totalPos - (Math.min(nBiggerAvg,rem));
	}

	public static void main(String[] args) {
		java.util.Scanner sc = new java.util.Scanner(System.in);
		int nStudents = -1;
		
		nStudents = Integer.parseInt(sc.nextLine());
		do {
			int[] costs = new int[nStudents];
			for (int i = 0; i < nStudents; i++) {
				String line = sc.nextLine();
				int cents = (Integer.parseInt(line.replace(".","")));
				costs[i] = cents;
			}

			int toExchange = compute(costs);
			System.out.printf("$%d.%02d\n",toExchange / 100, toExchange % 100);
			nStudents = Integer.parseInt(sc.nextLine());
		} while (nStudents != 0); 
	}
}
