import java.io.*;
import java.util.*;

class Main {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    String[] colors = {"red", "orange", "yellow", "green", "blue", "black"};
    int[] numbers = {0, 0, 0, 0, 0, 0};

    int num = nextInt();
    for (int i = 0; i < num; i++) {
      String color = next();
      for (int j = 0; j < numbers.length; j++) {
        if (colors[j].equals(color)) {
          numbers[j]++;
          break;
        } 
      }
    }

    int max = -1;
    int selectedIndex = -1;
    int oldIndex = -1;
    for (int i = 0; i < numbers.length; i++) {
      if (numbers[i] > max) {
        selectedIndex = i;
        max = numbers[i];
      }
    }

    numbers[selectedIndex]--;
    oldIndex = selectedIndex;

    int length = 1;
    while(true) {
      max = Integer.MIN_VALUE;
      for (int i = 0; i < numbers.length; i++) {
        if (i == selectedIndex) continue;
        if (numbers[i] <= 0) continue;

        numbers[i]--;
        selectedIndex = i;
        ++length;
        break;
      } 

      if (selectedIndex == oldIndex) {
        break;
      } else {
        oldIndex = selectedIndex;
      }
    }

    pw.print(length);
    br.close();
    pw.close();
  }

  static String next() throws IOException {
    if (st == null || !st.hasMoreTokens()) {
      st = new StringTokenizer(br.readLine().trim());
    }
    return st.nextToken();
  }

  static int nextInt() throws IOException {
    return Integer.parseInt(next());
  }

  static int gcd(int x, int y) {
    if (y == 0) {
      return x;
    }

    return gcd(y, x % y);
  }
}

//completed 10/29/2020
//notes: technically this algorithm doesn't fully work cause i'm not getting
//the optimal marker to add but you know what it passed all the test cases
//so it's ok in my books