import java.io.*;
import java.util.*;

public class ecoo2020p1 {
  static BufferedReader br;
  static PrintWriter pw;
  static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    String[] mt = {"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"};
    //              0    1    2     3     4    5     6    7    8     9    10   11
    int t = nextInt();
    HashMap<String, Integer> note = new HashMap<>(t);
    for (int i = 0; i < 12; i++) {
      note.put(mt[i], i);
    }

    for (int i = 0; i < t; ++i) {
      String start = next();
      String next = next();

      int index = note.get(start);
      int count = 0;
      int[] places = new int[3];
      int pInd = 0;

      while (true) {
        index = (index + 1)%12;
        ++count;
        if (mt[index].equals(next)) {
          places[pInd] = count;
          ++pInd; 
          count = 0;
          if (pInd >= 3) break;
          next = next();
        }
      }

      if(places[0]==4&&places[1]==3&&places[2]==3) pw.println("root");
      else if(places[0]==3&&places[1]==3&&places[2]==2) pw.println("first");
      else if(places[0]==3&&places[1]==2&&places[2]==4) pw.println("second");
      else if(places[0]==2&&places[1]==4&&places[2]==3) pw.println("third");
      else pw.println("invalid");
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
  // so i tried ecoo out and it was fun but i did the worst in my school so poggers
  // future reference: don't skip the easy questions, dont overcomplicate it
}