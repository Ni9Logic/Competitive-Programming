def main():
	MAGIC = 8*9*5*7;

	// Storing data in parallel arrays.
	n = int(input())
	dist = [];
	red = [];
	green = [];
	period = [];

    for i in range(n):
        dist[i] = stdin.nextInt();
        red[i] = stdin.nextInt();
        green[i] = stdin.nextInt();
        period[i] = red[i]+green[i];
		
  		// Results will be stored here.
		double[] res = new double[n+1];
		
		// Here we consider all numbers of the form MAGIC(c) + mod, where c is an integer.
		for (int mod=0; mod<MAGIC; mod++) {
			
			// Everyone's good at first.
			boolean[][] good = new boolean[100][100];
			for (int i=0; i<100; i++) Arrays.fill(good[i], true);
			int[] numCandidates = new int[100];
			for (int i=0; i<100; i++) numCandidates[i] = i;
			
			double curprob = 1;
			
			// Now we go through each stoplight for "all numbers" in this mod class.
			for (int i=0; i<n; i++) {
				
				// Get the correct prime power.
				int div = gcd(MAGIC, period[i]);
				int cycle = period[i]/div;
				
				// So this is hacky but it works - due to our MAGIC number, when we have a mod of 27 or 81,
				// we need to treat both of these the same, not differently and just assume a mod of 81.
				// Same issue with powers of 2 past 8.
				if (cycle == 2 || cycle == 4) cycle = 8;
				if (cycle == 3) cycle = 9;

				// To avoid divide by 0...
				if (numCandidates[cycle] == 0) break;
				
				int stopHere = 0;
				
				// when I get here time is mod%MAGIC+dist[i]. Cycling through just these j's will give us each
				// unique mod we can achieve of our period length.
				for (int j=0; j<cycle; j++) {
					
					// This isn't good to begin with, so skip it.
					if (!good[cycle][j]) continue;
					
					// This is the time we are considering.
					int time = MAGIC*j + mod + dist[i];
					int tAtLight = time%period[i];
					
					// Oops, we stop.
					if (tAtLight < red[i]) {
						stopHere++;
						good[cycle][j] = false;
					}
				}
				

				
				// Add whatever stopped here.
				res[i] += curprob*stopHere/numCandidates[cycle];

				// This is who moves on.
				curprob *= (1-1.0*stopHere/numCandidates[cycle]);
				
				// Update # of candidates left.
				numCandidates[cycle] -= stopHere;
			}
			
			// This is who made it through.
			res[n] += curprob;
		}
		
		// Ta da!!!
		for (int i=0; i<n+1; i++)
			System.out.println(res[i]/MAGIC);
	}
	
	public static int gcd(int a, int b) {
		return b == 0 ? a : gcd(b, a%b);
	}
}