import java.util.Scanner;
public class Task8
{
  public static void main (String [] args)
  {
    Scanner sc=new Scanner(System.in);
    String [] a=new String [10];
    a[0]="zero";
    a[1]="one";
    a[2]="two";
    a[3]="three";
    a[4]="four";
    a[5]="five";
    a[6]="six";
    a[7]="seven";
    a[8]="eight";
    a[9]="nine";
    System.out.println("Enter a number: ");
    int n=sc.nextInt();
    if (n>=0 && n<=9)
    {
      System.out.println(a[n]);
    }
    sc.close();
  }
}