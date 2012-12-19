import java.util.ArrayList;

class Problem21 {	
	public static void main(String args[])
	{
		int i = 2, total = 0;
		ArrayList<Integer> sumList = new ArrayList<Integer>();

		sumList.add(0); sumList.add(0);
		while(i < 10000)
		{
			int j, temp = 1, sum = 0;
			for(j = i; j > temp; j--)
			{	if(i%j == 0)
				{	temp = i/j;
					if(j != i && j != temp) {
						sum += j;
					}

					sum += (i/j);
				}
			}
			
			sumList.add(sum);
			if(sumList.size() > sum && sumList.get(sum) == i && sum != i)
				total = total + sum + i;
			i++;
		}

		System.out.print(total);
	}
}
