//Assignment 1
import java.util.*;
public class A1 {
	public static void main(String[] args) {
		int[]source= {10,20,30,40,50,60};//{4,5,0,0,0}
		int k=3;
		shiftLeft(source,k);
		System.out.println(java.util.Arrays.toString(source));  //ei print method ta stack overflow theke nisi, otherwise address print hoy :(
	}
	public static void shiftLeft(int[]array,int n1) {
		for(int i=0;i<=array.length-n1-1;i++) {
			array[i]=array[i+n1];
		}
		for(int i=array.length-1;i>=n1;i--){
			array[i]=0;
		}
		return;
	}
}

//Assignment 2
import java.util.*;
public class A2 {
		public static void main(String[] args) {
			int[]source= {10,20,30,40,50,60};//{4,5,6,0,0,0}
			int k=3;
			rotateLeft(source,k);
			System.out.println(java.util.Arrays.toString(source));
		}
		public static void rotateLeft(int[]array,int n1) {
			for(int i=array.length-(1+n1),j=array.length-1;j>=n1;i--,j--) {
				int temp=array[i];//30
				array[i]=array[j];//30 er jaygay index 2 e 60 nisi
				array[j]=temp;//60 re 30 diye replace korsi 
			}
			return;
	}
}

//Assignment 3
import java.util.*;
public class A3 {
	public static void main(String[] args) {
		int source[]= {10,20,30,40,50,0,0};
		int size=5;
		int removalIndex=2;
		remove(source,size,removalIndex);
		System.out.println(java.util.Arrays.toString(source));
	}
	public static void remove(int[]array, int n1, int n2){
		for(int i=n2;i<=n1;i++) {
			array[i]=array[i+1];
		}
		return;						
	}
}

//Assignment 4
import java.util.*;
public class A4 {
	public static void main(String[] args) {
		int source[]= {10,2,30,2,50,2,2,0,0};                // output {10,30,50,0,0,0,0,0,0}
		int size=7;
		int removalelement=2;
		removeAll(source,size,removalelement);
		System.out.println(Arrays.toString(source));
	}
	public static void removeAll(int[]array, int n1, int n2){
		for(int i=0;i<=n1;i++) {
			if(array[i]==n2){
				array[i]=0;
			}
		}	
		for(int i=0;i<n1;i++) {
			if(array[i]==0) {
				for(int j=i;j<n1;j++) {                   //[10, 0, 30, 0, 50, 0, 0, 0, 0]
					array[j]=array[j+1];
				}
			}
		}
		return;					
	}
}

//Assignment 5
import java.util.Arrays;
import java.util.Scanner;
public class A6 {
	public static void main(String[] args) {
		int n;		
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the size of the array: ");
		n=sc.nextInt();
		boolean var = false;
		int[]A=new int[n];	
		for(int i=0;i<n;i++) {
			System.out.println("Enter values of the array: ");
			A[i]=sc.nextInt();
		}
		split(A,n,var);
		
	}
	public static void split(int []array,int n1,boolean var1) {
		int sum=0;	
		for(int i=0;i<n1;i++) {
	
			sum=sum+array[i]; //Sum
		}
		if(sum%2!=0) {
			var1=false;
		}
		else{
			int n2;
			int sum2=0;
			n2=sum/2;
			for(int i:array) {
				sum2=sum2+i;
				if(sum2==n2) {
					var1=true;
					break;
				}
				else {
					var1=false;
				}
			}
		}
		System.out.println(var1);	
	}
}


//Assignment 6
import java.util.*;
public class A5 {
    public static void main(String[] args) {
        int n;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a value: ");
        n=sc.nextInt();
        int[] A=new int[n*n];    
        input(A,n);
        System.out.println(Arrays.toString(A));        
    }
    public static void input(int[] array, int n1) {
        int size = array.length-1;
        for(int i=n1-1; i>=0; i--) {          
             int var1=1, var2=n1-i;   //n1-n1+1
            while(var1<=n1) {
                if (var2<=n1) {
                    array[size]=var1; // replace kortese last er ta 1 diye {0,0,0,1}
                    var2++;
                }
                else if(var2>n1) {  // first value 0 kortese
                    array[size]=0; 
                }
                var1++;
                size--;
        }
     }
  return;
} 
}



//Assignment 7
import java.util.*;
public class A7 {
	public static void main(String[] args) {
		int n,max=1;		
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the size of the array: ");
		n=sc.nextInt();
		int[]A=new int[n];	
		for(int i=0;i<n;i++) {
			System.out.println("Enter values of the array: ");
			A[i]=sc.nextInt();
		}
		maxCout(A,n,max);
		//System.out.println(max); //hoy nah eine kan jani :(
	}
	public static void maxCout(int []array, int n1, int maxima) {
		int var1=1;
		for(int i=1;i<n1;i++) {
			if(array[i]==array[i-1]) {
				var1+=1;
				if(var1>maxima) {
				maxima=var1;
			}
			continue;
			}
			if(var1>maxima) {
				maxima=var1;
			}
		var1=1;
	}
		System.out.println(maxima);	
	}
}



import java.util.*;
public class A8 {
	public static void main(String[] args) {
		int n;		
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the size of the array: ");
		n=sc.nextInt();
		boolean var = true;
		int[]A=new int[n];	
		for(int i=0;i<n;i++) {
			System.out.println("Enter values of the array: ");
			A[i]=sc.nextInt();
		}
		chagolAmi(A,n,var);
		//System.out.println(var);//Ekhane print hocche nah!!
	}
	public static void chagolAmi(int[]array,int n1, boolean var3) {
		int []array1=new int[n1];
		int var1=0, var2=0;
		for(int i:array) {	
			for(int j:array) {
				if(i==j) {
					var1+=1;
					}}
				if(var1!=1) {
					array1[var2]=var1;
				var2+=1;
				}
				var1=0;}
				if(array1[0]==0) {
					var3=false;}
			for(int i:array1) {
				if(i!=array1[0] && i!=0) {
						var3=false;
					}}					
			System.out.println(var3);
		}
	}
//Circular Question 1
import java.util.*;

public class CQ1 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter values seperated by comma:");
        String str= sc.nextLine();
        String [] array = str.split(",");
        int array2[]=new int[array.length];
        for(int i=0; i<array.length; i++) {
            array2 [i] = Integer.parseInt(array [i]);
        }
        System.out.println("Enter start value:");
        int start = sc.nextInt();
        System.out.println("Enter size value:");
        int size = sc.nextInt();
        palindrome(array2, start, size);
    }
    public static void palindrome(int[]array3, int index, int size1) {
        boolean check = true;
        for(int i=0; i<size1; i++) {
            int temp = (index+size1-1)%array3.length;
            if (array3[index]!=array3[temp]) {
                check = false;
            }
        }
        System.out.println(check);
    } 
}

//Circular Question 2
import java.util.*;

public class CQ2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter array 1 seperated by comma:");
        String str= sc.nextLine();
        String [] array = str.split(",");
        int array1[]=new int[array.length];
        for(int i=0; i<array.length; i++) {
            array1 [i] = Integer.parseInt(array [i]);
        }
        System.out.println("Enter start value:");
        int start1 = sc.nextInt();
        System.out.println("Enter size value:");
        int size1 = sc.nextInt();
        
        sc.nextLine();
        System.out.println("Enter array 2 seperated by comma:");
        String strx= sc.nextLine();
        String [] arrayx = strx.split(",");
        int array2[]=new int[arrayx.length];
        for(int i=0; i<arrayx.length; i++) {
            array2 [i] = Integer.parseInt(arrayx [i]);
        }
        System.out.println("Enter start value:");
        int start2 = sc.nextInt();
        System.out.println("Enter size value:");
        int size2 = sc.nextInt();
        palindrome(array1, start1, size1, array2, start2, size2);
    }
    
    public static void palindrome(int[]array3, int index1, int size1, int[]array4, int index2, int size2) {
        int result[]= new int[array3.length];
        int x = 0;
        int y = index2;
        for(int i=0; i<size1; i++) {
            for(int j=0; j<size2; j++) {
                if (array3[index1] == array4[index2]) {
                    result[x] = array3[index1];
                    x++;
                }
            index2 = (index2+1)%array4.length;
            }
            index2 = y;
        index1 = (index1+1)%array3.length;
        }
        System.out.println(Arrays.toString(result));
    }
}