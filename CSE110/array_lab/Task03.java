import java.util.*;

public class Task03 {

  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int[] a = new int[5];
    for (int c = 0; c < a.length; c++) {
      System.out.println("Enter a number: ");
      a[c] = s.nextInt();
    }
    int z = a[0], blc = a[0];
    for (int c = 1; c < a.length; c++) {
      if (a[c] > z) {
        z = a[c];
        blc = c;
      }
    }
    int x = a[0], slc = a[0];
    for (int j = 1; j < a.length; j++) {
      if (a[j] < x) {
        x = a[j];
        slc = j;
      }
    }

    System.out.println(
      "Smallest number is " + x + " is found at location " + slc
    );
    System.out.println(
      "Largest number is " + z + " is found at location " + blc
    );
  }
}
