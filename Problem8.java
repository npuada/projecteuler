import java.io.FileReader;
import java.util.*;
class Problem8 {
	
	static ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
	static int product;
	static int max;

	public Problem8() {
		product = 1;
		max = 0;
	}

	static void process() {	
		for(List<Integer> l : list)
		{	for(int i = 0; i < l.size(); i++)
				if(i >= 5) {
					product /= l.get(i-5);
					product *= l.get(i);

					if(product > max)
						max = product;
				}
				else
					product *= l.get(i);
			
			if(product > max)
				max = product;
			
			product = 1;
		}
	}


	public static void main(String args[]) throws Exception {
		
		new Problem8();
		FileReader fr = new FileReader("Problem8.txt");

		int n = 0;
		do {
			ArrayList<Integer> l = new ArrayList<Integer>();
			do {			
				n = fr.read();
			} while (n == 48);
 
			do {
				if(n != 10)
					l.add(n-48);
				n = fr.read();
			} while (n != 48 && n != -1);

			list.add(l);
		} while (n != -1);
		fr.close();

		process();
		System.out.print(max);
	}
}
