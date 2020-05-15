import java.io.*;
import java.util.*;

public class dmojccc07s1 {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    int c = nextInt();
    int year, month, day;

    for (int i = 0; i < c; ++i) {
      year = nextInt();
      month = nextInt();
      day = nextInt();

      if (2007-year > 18) pw.println("Yes");
      else if (2007-year == 18) {
        if (month < 2) pw.println("Yes");
        else if (month == 2) {
          if (day <= 27) pw.println("Yes");
          else pw.println("No");
        } else pw.println("No");
      } else pw.println("No");
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
  //completed 01/05/2020 (dd/mm/yyyy)
  //note: ah yes i enjoy easy 5 pointers but seriously i think my java is fine enough for >5 point problems now
}