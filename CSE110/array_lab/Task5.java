import java.util.Scanner;
public class Task5
{
  public static void main (String[]agrs)
  {
    Scanner sc= new Scanner(System.in);
    int [] a=new int[5];
    for (int c=0; c<a.length; c++)
    {
      System.out.println("Enter input "+(c+1));
      a[c]=sc.nextInt();
    }
    int i=0;
    for (int c=0; c<a.length; c++)
    {
      for (int k=c; k<a.length; k++)
      {
        if (a[k]>a[c])
        {
          i=a[c];
          a[c]=a[k];
          a[k]=i;
        }
      }
    }
    for (int c=0; c<a.length; c++)
    {
      System.out.println(a[c]);
    }
    sc.close();
  }
}