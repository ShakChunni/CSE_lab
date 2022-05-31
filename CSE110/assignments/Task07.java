import java.util.Scanner;
public class Task07{
  public static void main(String []args){
    Scanner goat = new Scanner(System.in);
    System.out.println("Give a number");
    int n1 = goat.nextInt();
    for(int c=n1; c>=n1; c--){
      for(int j=n1; j<c; j++){
        System.out.print(" ");
      }
      for(int x=1; x<=c; x++){
        System.out.print(x);
        
        
      }
      System.out.println();
    }
  }
}