import java.util.*;
import java.text.DecimalFormat;

public class k {
	
	final public static int MAGIC = 8*9*5*7;

	public static int n;
	public static int[] dist;
	public static int[] red;
	public static int[] green;
	public static int[] period;
	
	public static void main(String[] args) {
	
		Scanner stdin = new Scanner(System.in);
		n = stdin.nextInt();
		dist = new int[n];
		red = new int[n];
		green = new int[n];
		period = new int[n];
		
		for (int i=0; i<n; i++) {
			dist[i] = stdin.nextInt();
			red[i] = stdin.nextInt();
			green[i] = stdin.nextInt();
			period[i] = red[i]+green[i];
		}

		double[] res = new double[n+1];
		
		for (int mod=0; mod<MAGIC; mod++) {
			
			boolean[][] good = new boolean[100][100];
			for (int i=0; i<100; i++) Arrays.fill(good[i], true);
			int[] numCandidates = new int[100];
			for (int i=0; i<100; i++) numCandidates[i] = i;
			
			double curprob = 1;
			
			for (int i=0; i<n; i++) {
				
				int div = gcd(MAGIC, period[i]);
				int cycle = period[i]/div;
				
				if (cycle == 2 || cycle == 4) cycle = 8;
				if (cycle == 3) cycle = 9;

				if (numCandidates[cycle] == 0) break;
				
				int stopHere = 0;
				
				for (int j=0; j<cycle; j++) {
					
					if (!good[cycle][j]) continue;
					
					int time = MAGIC*j + mod + dist[i];
					int tAtLight = time%period[i];
					
					if (tAtLight < red[i]) {
						stopHere++;
						good[cycle][j] = false;
					}
				}
				

				
				res[i] += curprob*stopHere/numCandidates[cycle];

				curprob *= (1-1.0*stopHere/numCandidates[cycle]);
				
				numCandidates[cycle] -= stopHere;
			}
			
			res[n] += curprob;
		}
		
        for (int i=0; i<n+1; i++)
			System.out.format("%.12f\n", res[i]/MAGIC);
	}
	
	public static int gcd(int a, int b) {
		return b == 0 ? a : gcd(b, a%b);
	}
}