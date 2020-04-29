/* [dmojccc09j1.java]
 * Joseph Wang
 * Fun fun dmoj
 */
import java.util.Scanner;

public class dmojccc09j1 {
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int totalNum = 91;
    int num;
    for (int x = 0; x < 3; x++){
      num = input.nextInt();
      if (x % 2 == 0 ){
        totalNum += num * 1;
      } else {
         totalNum += num * 3;
        }
    }  
    System.out.println("The 1-3-sum is " + totalNum);
  }
}

//completed 09/18/2019
//notes: this was just to try out java so it's not optimized at all