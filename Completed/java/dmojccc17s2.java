import java.io.*;
import java.util.*;

public class dmojccc17s2 {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    int s = readInt();
    int[] samples = new int[s];
    
    for (int i = 0; i < s; ++i) {
      samples[i] = readInt();
    }

    Arrays.sort(samples);
    int midIndex = (int)(Math.ceil(s/2.0));

    int offset = 0;
    while (offset < midIndex) {
      pw.print(samples[(midIndex-1) - offset] + " ");

      if ((offset + midIndex) >= s) {
        break;
      } else {
        pw.print(samples[midIndex + offset] + " ");
      }
      ++offset;
    }

    br.close();
    pw.close();
  }

  static String next() throws IOException {
    if (st == null || !st.hasMoreTokens()) {
      st = new StringTokenizer(br.readLine().trim());
    }
    return st.nextToken();
  }

  static int readInt() throws IOException {
    return Integer.parseInt(next());
  }

  static int gcd(int x, int y) {
    if (y == 0) {
      return x;
    }

    return gcd(y, x % y);
  }
  //completed 29/04/2020 (dd/mm/yyyy)
  //notes: fun practice, added gcd method, next time use Arrays.sort with Integer or
  //Collections.sort for faster sorting speed
}