/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		while(T>0)
		{
		    int n = sc.nextInt();
		    String s = sc.next();
		    
		    int result =  sort(n, s);
		    System.out.println(result);
		    
		    T--;
		}
	}
	
   static int sort(int N, String s)
	{
	    int last = -1;
        if(N == 1){
            return 0;
        }
        int count = 0;
        boolean one_found = false;
        for(int i=N-1; i<-1; i--){
            if (s.charAt(i) == '0' && last != -1 and one_found == true){
                StringBuilder input1 = new StringBuilder();
                input1.append(s.substrign(i+1, last));
                input1.reverse();
                s = s.substring(0, i+1) + input1 + s.substring(last, N+1);
                count += 1;
                last = i+1;
                one_found = false;
            }else if(s[i] == '0' && last == -1){
                last = i;
            }else if(s[i] == '1' and last != -1){
                one_found = true;
            }
        }
        if(one_found == true){
            count++;
        }
        return count;
	}
}