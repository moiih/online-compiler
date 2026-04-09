import java.util.Scanner;

class Quadratic {
	int[] eq1 = new int[3];
	int[] eq2 = new int[3];
	
	Quadratic(int eq1[], int eq2[]) {
		this.eq1 = eq1;
		this.eq2 = eq2;				
	}
	
	int[] simple_form(int a,int b) {
		int min;
		int[] frac = new int[2];
		min = (Math.abs(a)<Math.abs(b))?Math.abs(a):Math.abs(b);				
		
		for(int i=min; i>=1; i--) {			
			if( a%i == 0 && b%i == 0 ) {		
				a = a/i;
				b = b/i;
				break;
			}				
		}
				
		frac[0] = a;
		frac[1] = b;
		//System.out.println(frac[0]+" --- "+frac[1]);
		return frac;
	}
	
	String solve_quad() {
		/*System.out.println("Equation 1:-");
		for(int i=0; i<3; i++) {
			System.out.println(eq1[i]);
		}
		
		System.out.println("Equation 2:-");
		for(int i=0; i<3; i++) {
			System.out.println(eq2[i]);
		}*/
		
		int x1,x2;
		x1 = Math.abs(eq1[0]);
		x2 = Math.abs(eq2[0]);
		
		for(int i=0; i<2; i++) {
			
			if( i == 1 ) {
				if( (eq1[0]>0 && eq2[0]>0) || (eq1[0]<0 && eq2[0]<0) )  // if both are either positive or negative
					x1 = -x1;
			}
				
			for(int j=0; j<3; j++) {
				if( i == 0 )
					eq1[j] = eq1[j]*x2;				
				else{					
					eq2[j] = eq2[j]*x1;
				}						
			}
		}
		
		System.out.println("Equation 1:-");
		for(int i=0; i<3; i++) {
			System.out.println(eq1[i]);
		}
		
		System.out.println("Equation 2:-");
		for(int i=0; i<3; i++) {
			System.out.println(eq2[i]);
		}
		
		// Now, After eliminating 'x2(square)' we are solving the value of 'y'
		int c = (eq1[2]+eq2[2])*-1;
		int y = eq1[1]+eq2[1];
		
		int[] res = simple_form(c,y);
		
		System.out.println("\n"+res[0]+" --- "+res[1]);
		
		String temp1 = Integer.toString(res[0]);
		String temp2 = Integer.toString(res[1]);
		
		System.out.println("To Return : "+(temp1+"+"+temp2)+"\n");
		
		return (temp1+"+"+temp2);		
	}
	
	public static void main(String args[]) {		
		Scanner in = new Scanner(System.in);
		int[] e1 = new int[3];
		int[] e2 = new int[3];
		
		for(int i=1; i<=2; i++) {		
			System.out.println("Enter Co-efficient of x2 of eq"+i+" :-");
			int x = in.nextInt();
			System.out.println("Enter Co-efficient of y of eq"+i+" :-");
			int y = in.nextInt();
			System.out.println("Enter Constant value of eq"+i+" :-");
			int c = in.nextInt();
			System.out.println();
			
			if( i == 1 ) {
				e1[0] = x;
				e1[1] = y;
				e1[2] = c;
			}
			else {
				e2[0] = x;
				e2[1] = y;
				e2[2] = c;				
			}
		}				
	
		Quadratic obj = new Quadratic(e1, e2);
		String res = obj.solve_quad();
		String temp = "";
		
		for(int i=0; i<res.length(); i++) {			
			System.out.println(res.charAt(i));
			
		}
						
	}
}