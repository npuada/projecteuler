import java.util.ArrayList;

class Problem7 {
	private ArrayList<Integer> primeList;

	public Problem7()
	{
		primeList = new ArrayList<Integer>();
		primeList.add(2);
	}

	public void generatePrimeList()
	{
		int count = 1;		
		for(int i = 3; count < 10002; i+=2)	
		{	int j = (int)Math.sqrt(i);
			while(j>1 && i%j != 0)
				j--;
			if(j == 1)
			{	primeList.add(i);
				count++;
			}
		}

		System.out.print(primeList.get(10000));
	}

	public static void main(String args[])
	{
		Problem7 e = new Problem7();
		e.generatePrimeList();
	}
}
