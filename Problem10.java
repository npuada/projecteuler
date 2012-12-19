import java.util.ArrayList;

class Problem10 {
	private ArrayList<Integer> primeList;

	public Problem10()
	{
		primeList = new ArrayList<Integer>();
		primeList.add(2);
	}

	public void generatePrimeList()
	{
		int count = 1;		
		for(int i = 3; i < 2e6; i+=2)	
		{	int j = (int)Math.sqrt(i);
			while(j>1 && i%j != 0)
				j--;
			if(j == 1)
			{	primeList.add(i);
				count++;
			}
		}
	}
	
	public long getSum()
	{
		long sum = 0L;		
		for(int i : primeList)
			sum += i;

		return sum;
	}

	public static void main(String args[])
	{
		Problem10 e = new Problem10();
		e.generatePrimeList();
		System.out.println(e.getSum());
	}
}
