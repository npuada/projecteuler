import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class LargeArithmetic {

	public ArrayList<Integer> toArrayList(int u) {
		int i = 0;
		int powTen = 1;
		ArrayList<Integer> intList = new ArrayList<Integer>();

		if (u >= 10) {
			while(powTen < u) {
				powTen *= 10;
				i++;
			}

			for(int x = 0; x < i; x++) {
				powTen /= 10;
				int temp = u / powTen;
				temp %= 10;
				intList.add(temp);
			}
		}
		else
			intList.add(u);

		return intList;
	}

	public ArrayList<Integer> multiply(ArrayList<Integer> u, ArrayList<Integer> v) {
		ArrayList<Integer> w = new ArrayList<Integer>();
		int i;
		for(i = 0; i < v.size() + u.size(); i++)
			w.add(0);
		
		int t = 0; int j;
		for(i = v.size()-1; i >= 0; i--) {
			int carry = 0;
			for(j = u.size(); j >= 0; j--) {
				if(j>0) {
					t = u.get(j-1) * v.get(i) + w.get(i+j) + carry;
					w.set(i+j, t%10);
					carry = t/10;
				}
			}
			
			w.set(i, carry);
		}
		
		return w;
	}

	public ArrayList<Integer> add(ArrayList<Integer> u, ArrayList<Integer> v) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		result.add(0);
		
		if(u.size() >= v.size()) {
			result.addAll(u);
		}
		else {
			result.addAll(v);
		}

		int i = u.size()-1;
		int j = v.size()-1;
		int index = result.size()-1;
		int carry = 0;
		while(i >= 0 && j >= 0) {
			int temp = u.get(i) + v.get(j) + carry;
			if(temp >= 10) {
				carry = 1;
				temp %= 10;
			}
			else
				carry = 0;
			
			result.set(index, temp);
			i--;
			j--;
			index--;
		}

		if(carry == 1) {
			if(i == j) {
				result.set(0, 1);
				return result;
			}
			else {
				while(carry == 1 && index >= 0) {
					int temp = result.get(index) + carry;
					if (temp >= 10) {
						carry = 1;
						temp %= 10;
					}
					else
						carry = 0;
					result.set(index, temp);
					index--;
				}
			}
		}

		return result;
	}

	public ArrayList<Integer> add(ArrayList<Integer> u, int v) {
		ArrayList<Integer> s = toArrayList(v);
		return add(u, s);
	}
}

class Main {
	public static void main(String args[]) {
		LargeArithmetic l = new LargeArithmetic();
		ArrayList<Integer> u = new ArrayList<Integer>();
		ArrayList<Integer> v = new ArrayList<Integer>();
		
		u.add(1); v.add(1);
		System.out.print("Input: ");
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();

		for(int i = 1; i < x; i++) {
			v = l.add(v, 1);

			while(u.get(0) == 0)
				u.remove(0);

			while(v.get(0) == 0)
				v.remove(0);

			u = l.multiply(u,v);
		}

		int sum = 0;

		if(u.get(0) == 0)
			u.remove(0);

		for(int i : u)
			System.out.print(i);
		System.out.println();

		for(int i = 0; i < u.size(); i++)
			sum += u.get(i);
			
		System.out.print(sum);
	}
}