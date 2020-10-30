import java.io.*;
import java.util.*;

public class dmojccc19j3 {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    int num = nextInt();
    for (int j = 0; j < num; ++j) {
      String yes = next();

      int current = 1;
      char currentChar = yes.charAt(0);
      String output = "";

      for (int i = 1; i < yes.length(); ++i) {
        if (yes.charAt(i) != currentChar) {
          output += String.valueOf(current) + " " + currentChar + " ";
          currentChar = yes.charAt(i);
          current = 0;
        }

        ++current;
      }

      output += String.valueOf(current) + " " + currentChar + " ";
      currentChar = yes.charAt(yes.length() - 1);

      System.out.println(output.strip());
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
}

// completed 07/09/2020 ddmmyyyy
// notes: so I didnt use java the entirety of the summer and now I have to
// practice it again and get used to it