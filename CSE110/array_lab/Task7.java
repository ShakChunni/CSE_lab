import java.util.Scanner;
public class Task7
{
  public static void main (String [] args)
  {
    Scanner sc=new Scanner(System.in);
    int [] a=new int [10];
    for (int c=0; c<a.length; c++)
    {
      System.out.println("Enter input"+(c+1));
      a[c]=sc.nextInt();
    }
    for (int c=0; c<a.length; c++)
    {
      if (c%2!=0)
      {
        System.out.print(c);
      }
      else
      {
        System.out.print(c);
      }
    }
    sc.close();
  }
}