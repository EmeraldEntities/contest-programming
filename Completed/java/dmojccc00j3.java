import java.io.*;
import java.util.*;

public class dmojccc00j3 {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    int m = nextInt();
    int t = 0;
    int mindex = 0;
    int[] mach = {nextInt(), nextInt(), nextInt()}; 
    int[][] mlimit = {{35, 30}, {100, 60}, {10, 9}};

    while (m > 0) {
      --m;
      ++t;
      ++mach[mindex];
      if (mach[mindex] == mlimit[mindex][0]) {
        mach[mindex] = 0;
        m += mlimit[mindex][1];
      }
      mindex = (mindex + 1) % 3;
    }

    pw.println("Martha plays " + t + " times before going broke.");

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
  //completed 30/04/2020 (dd/mm/yyyy)
  //note: i didn't actually need an array for this problem, guess im too eager for those
  //array ACCESSES
}