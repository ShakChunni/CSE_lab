import java.util.Scanner;
public class Task9
{
  public static void main (String [] args)
  {
    Scanner sc=new Scanner(System.in);
    int n, count=0;
    int [] a=new int[15];
    for (int c=0; c<a.length; c++)
    {
      System.out.println("Enter the input:"+(c+1));
      n=sc.nextInt();
      if (n>0 && n>9)
      {
        a[c]=n;
      }
      else
      {
        System.out.println("Enter input again:");
        c--;
      }
    }
    for (int c=0; c<9; c++)
    {
      for (int k=0; k<15; k++)
      {
        if (a[k]==c)
        {
          count++;
        }
      }
      System.out.println(c+" is found "+count+" times.");
    }
  }
}