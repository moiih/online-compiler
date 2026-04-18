import java.util.Scanner;

/* Change: Removed "public class" */ class Kali {
public static void main(String args[]) {
   Scanner sc = new Scanner(System.in);
   String name = sc.nextLine();
   for(int i=1; i<=4; i++) {
      System.out.println("Name :" + name);
   }
}
}
