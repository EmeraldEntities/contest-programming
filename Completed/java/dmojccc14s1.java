import java.io.*;
import java.util.*;

public class Main {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    int nonexistantFriends = nextInt();
    int rounds = nextInt();
    int[] friends = new int[nonexistantFriends];
    for (int i = 0; i < nonexistantFriends; i++) {
      friends[i] = i+1;
    }

    for (int i = 0; i < rounds; i++) {
      int index = 0;
      int indexToYeet = nextInt();

      for (int j = 0; j < friends.length; j++) {
        if (friends[j] != -1) {
          ++index;
          if (index % indexToYeet == 0) {
            friends[j] = -1;
          }
        }
      }
    }

    for (int i = 0; i < friends.length; i++) {
      if (friends[i] != -1) {
        pw.print(friends[i] + "\n");
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
}

//completed 10/29/2020
//notes: is it time to finally get back into cp
//also idek why i didn't just use an array at the start I had to be "special"
//and use an arraylist for some reason