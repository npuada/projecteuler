class Problem16 {
	private static int digits[] = new int[400];	
	
	public Problem16()
	{
		int i;		
		for(i = 0; i < 399; i++)
			digits[i] = 0;
		digits[i] = 2;
	}

	public void pow2(int power)
	{	for(int ctr = 1; ctr < power; ctr++)
		{	int carry = 0;
			for(int i = 399; i >= 0; i--)
			{	digits[i] *= 2;
				digits[i] += carry;
			
				carry = digits[i]/10;
				digits[i] %= 10;		
			}
		}
	}


	public int getSumOfDigits()
	{	int sum = 0;
		for(int i = 0; i < 400; i++)
			sum += digits[i];

		return sum;
	}

	public static void main(String args[])
	{
		Problem16 e = new Problem16();
		
		e.pow2(1000);
		System.out.print(e.getSumOfDigits());
	}
}
