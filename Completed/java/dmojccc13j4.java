import java.io.*;
import java.util.*;

public class dmojccc13j4 {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    int time = readInt();
    int chore = readInt();
    PriorityQueue<Integer> chores = new PriorityQueue<Integer>(chore);

    for (int i = 0; i < chore; ++i) {
      chores.offer(readInt());
    } 

    int usedTime = 0;
    int choreAmount = 0;

    while (true) {
      if (usedTime + chores.peek() > time) {
        pw.println(choreAmount);
        break;
      }

      usedTime += chores.poll();
      ++choreAmount;
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
}