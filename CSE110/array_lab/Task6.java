import java.util.Scanner;
public class Task6
{
  public static void main (String[]agrs)
  {
    Scanner sc= new Scanner(System.in);
    System.out.println("How many numbers to print: ");
    int n=sc.nextInt();
    int [] a=new int[n];
    int j=n/2;
    int median=0;
    for (int c=0; c<a.length; c++)
    {
      System.out.println("Enter input "+(c+1));
      a[c]=sc.nextInt();
    }
    for (int c=0; c<a.length; c++)
    {
      int i=0;
      for (int k=c; k<a.length; k++)
      {
        if (a[k]<a[c])
        {
          i=a[c];
          a[c]=a[k];
          a[k]=i;
        }
      }
      if (n%2==0)
      {
        median+=(a[j]+a[j+1])/2;
      }
      else
      {
        median=a[j];
      }
    }
    System.out.println(median);
    sc.close();
  }
}