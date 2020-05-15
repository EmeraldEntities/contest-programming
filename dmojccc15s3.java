import java.io.*;
import java.util.*;

public class Main {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    int g = nextInt();
    TreeSet<Integer> gates = new TreeSet<>();
    int p = nextInt();
    int plane;
    int totalPlane = 0;

    for (int i = 0; i < p; ++i) {
      plane = nextInt();

      while(gates.contains(plane) && plane > 0) {
        --plane;
      }

      if (!(plane <= 0)) {
        gates.add(plane);
        totalPlane++;
      } else {
        break;
      }
    }
    pw.println(totalPlane);

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