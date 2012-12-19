import java.util.*;
import java.io.*;

class Problem13 {
	public static void main(String args[]) throws IOException {
		FileReader fr = new FileReader("Problem13.txt");

		int n=0;
		long sum = 0;
		do {

			String s = "";				
			for(int i = 0; i < 13 && n != -1; i++) {
				n=fr.read();
				s = s+(n-48);
			}

			long l = Long.parseLong(s);
			if (l > 0)			
				sum += l;
			System.out.println(l);

			do {
				n = fr.read();
			} while(n != 10 && n != -1);

		} while(n != -1);

		System.out.print(sum+49);
	}
}
