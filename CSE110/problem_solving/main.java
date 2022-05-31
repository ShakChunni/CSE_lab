import java.util.*;
public class main{
  public static void main(String[]args){
    Scanner goat = new Scanner(System.in);
    long a,b,c;
    a = goat.nextLong();
    b = goat.nextLong();
    c = goat.nextLong();
    
    if(a>b && a>c){
      if(b>c){
        System.out.println(b);
      }
      else{
        System.out.println(c);
      }
    }
    if(b>a && b>c){
      if(a>c){
        System.out.println(a);
      }
      else{
        System.out.println(c);
      }
    }
    if(c>a && c>b){
      if(b>a){
        System.out.println(b);
      }
      else{
        System.out.println(a);
      }
    }
  }
  
}


