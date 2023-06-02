import java.util.*;

public class Task02 {

  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int[] a = new int[5];
    for (int c = 0; c < a.length; c++) {
      System.out.println("Enter a number: ");
      a[c] = s.nextInt();
    }
    int l = a[0], lc = 0;
    for (int c = 1; c < a.length; c++) {
      if (a[c] > l) {
        l = a[c];
        lc = c;
      }
    }
    System.out.println(
      "The largest number is: " + l + " and it's located at " + lc
    );
  }
}
