import java.util.*;
public class Arrayist{
  public static void main(String[]args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter a value: ");
    int x = sc.nextInt();
    System.out.println("Enter another value: ");
    int d = sc.nextInt();
    System.out.println("Enter another value: ");
    int c = sc.nextInt();
    System.out.println("Enter another value: ");
    int b = sc.nextInt();
    System.out.println("Enter another value: ");
    int a = sc.nextInt();
    System.out.println("Enter another value: ");
    int y = sc.nextInt();
    System.out.println("Enter another value: ");
    int z = sc.nextInt();
    System.out.println("Enter another value: ");
    ArrayList<Integer> arr = new ArrayList<Integer>();
    
    arr.add(x);
    arr.add(y);
    arr.add(z);
    arr.add(a);
    arr.add(b);
    arr.add(c);
    arr.add(d);
    
    for(c=1; c<arr.size(); c+=1){
      System.out.println(arr.get(c));
    }
    System.out.println(arr.contains(9));
    List<Integer> sublist = arr.subList(3,5);
    
    
    
  }
}