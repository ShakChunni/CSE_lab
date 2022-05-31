import java.util.Scanner;
public class Task09{
  public static void main(String []args){
    Scanner goat = new Scanner(System.in);
    System.out.println("Give a number");
    int n1 = goat.nextInt();
    for(int c=1; c<=n1; c++){
      for(int j=n1; j>c; j=j-2){
        System.out.print(" ");
      }
      for(int x=1; x<=c; x=x+2){
        System.out.print(x);
        
        
      }
      System.out.println();
    }
  }
}