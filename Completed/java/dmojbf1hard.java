import java.io.*;
import java.util.*;

public class dmojbf1hard {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    int t = nextInt();
    PriorityQueue<Integer> a = new PriorityQueue<>(t);
    for (int i = 0; i < t; ++i) a.offer(nextInt());
    while(!a.isEmpty()) pw.println(a.poll());

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
  // completed 01/05/2020
  // notes: i guess priority queues are slower than just sorting? unless the judge was bad lol idk
}