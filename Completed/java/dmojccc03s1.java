import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException{
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    int[][] ladders = {{9, 34}, {40, 64}, {67, 86}};
    int[][] snake = {{54, 19}, {90, 48}, {99, 77}};

    int square = 1;
    int add;
    while(true) {
      add = Integer.parseInt(input.readLine());

      if (add == 0) {
        System.out.println("You Quit!");
        break;
      }

      if (!(square + add > 100)) {
        square += add;
        for (int i = 0; i < 3; ++i) {
          if (ladders[i][0] == square) {
            square = ladders[i][1];
            break;
          } else if (snake[i][0] == square) {
            square = snake[i][1];
            break;
          }
        }
      }

      System.out.println("You are now on square " + square);

      if (square == 100) {
        System.out.println("You Win!");
        break;
      }
    }
  }
  //completed 28/04/2020 (dd/mm/yyyy)
  //notes: did this for ecoo prep to practice my very non-existant java skills 
}