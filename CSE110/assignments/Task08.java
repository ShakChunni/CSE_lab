import java.util.Scanner;
public class Task08{
  public static void main(String[]args){
    Scanner g = new Scanner(System.in);
    System.out.println("Enter a number");
    int n = g.nextInt();
    for(int c=1,z=0; c<=n; c++, z++){
      for(int y=n; y>c; y--){
        System.out.print(" ");
      }
      for(int x=1; x<=c+z; x++){
        System.out.print(x);
      }
      
      System.out.println();
    }
    
    
  }
  
}