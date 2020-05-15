import java.io.*;
import java.util.*;

public class defaultJavaFile {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

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