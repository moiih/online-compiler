class Parent {
     int get_val(int a) {
          return a+10;
     }
}

public class Child extends Parent {
     void display(int b) {
          Parent obj = new Parent();
           System.out.println("\nYour Value Is: " + obj.get_val(b));
     }

     public static void main(String args []) {
          Child c = new Child();
          c.display(90);

          StackTraceElement[] stack = Thread.currentThread ().getStackTrace ();
          StackTraceElement main = stack[stack.length - 1];          
          String mainClass = main.getClassName ();
          System.out.println("Main Class: " +mainClass);
     }
}