import java.io.*;
import java.util.*;

public class Main {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    int trees = nextInt();
    int[] treearr = new int[trees];
    for (int i = 0; i < trees; i++) {
      treearr[i] = nextInt();
    }

    long[] prefixSumArr = new long[trees];
    prefixSumArr[0] = treearr[0];
    for (int i = 1; i < prefixSumArr.length; i++) {
      prefixSumArr[i] = prefixSumArr[i-1] + treearr[i];
    }

    int queries = nextInt();
    for (int i = 0; i < queries; i++) {
      int from = nextInt();
      int to = nextInt();

      if (from == 0) {
        pw.print(prefixSumArr[to] + "\n");
      } else {
        pw.print((prefixSumArr[to] - prefixSumArr[from - 1]) + "\n");
      }
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
//notes: just used a prefix sum array, thanks compsci club