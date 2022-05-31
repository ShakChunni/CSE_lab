import java.util.Scanner;
public class Task03{
  public static void main(String []args){
    Scanner goat = new Scanner(System.in);
    System.out.println("Give a number");
    int n1 = goat.nextInt();
    System.out.println("Give another number");
    int n2 = goat.nextInt();
    int c = 1;
    int x = 1;
    while(c<=n1){
      x = 1;
      while(x<=n2){
        System.out.print("*");
        x++;
      }
      c++; 
      System.out.println();
    }
    
  }
}