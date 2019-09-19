/* [dmojbf3.java]
 * Joseph Wang
 * Fun fun dmoj
 */

import java.util.Scanner;
import java.lang.Math;

public class dmojbf3 {
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int num = input.nextInt();
    boolean works = true;
    
    double sqrtNum = Math.sqrt(num);
      
    for (int x = 1; x <= sqrtNum; x++) {
      if ((num % x == 0) && (x != 1) || (sqrtNum == 1)) {
        works = false;
        break;
      }
    }
    
    if (!works) {
      while (!works) {
        if ((num % 2 == 0) || (num == 1)) {
          num += 1;
        } else {
          num += 2;
        }
        works = true;
        for (int x = 1; x <= Math.sqrt(num); x++) {
          if ((num % x == 0) && (x != 1)) {
            works = false;
            break;
          }
        }
      } 
    }
    
    System.out.println(num);
    
  }
}