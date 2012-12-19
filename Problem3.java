import java.util.ArrayList;

class Problem3 {
	private static final long i = 600851475143L;
	private ArrayList<Integer> primeList;

	public Problem3()
	{
		primeList = new ArrayList<Integer>();
		primeList.add(2);
	}

	public void generatePrimeList(int limit)
	{
		for(int i = 3; i < limit; i+=2)	
		{	int j = (int)Math.sqrt(i);
			while(j>1 && i%j != 0)
				j--;
			if(j == 1)
				primeList.add(i);
		}
	}

	public int getLargestPrimeFactor()
	{
		int max = 2;		
		
		for(int j : primeList)
		{	if (i%j == 0)
				max = j;
		}
		return max;
	}

	public static void main(String args[])
	{
		Problem3 e = new Problem3();
		int limit = (int)Math.sqrt(i);
		e.generatePrimeList(limit);
		System.out.println(e.getLargestPrimeFactor());
	}
}
