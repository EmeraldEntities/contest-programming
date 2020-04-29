import java.io.*;
import java.util.*;

public class dmojccc16s2 {
  public static void main(String[] args) throws IOException {
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    int number = Integer.parseInt(input.readLine());
    int people = Integer.parseInt(input.readLine());
    int[] dSpeed = new int[people];
    int[] pSpeed = new int[people];

    String[] dpeople = input.readLine().split("\\s+");
    String[] ppeople = input.readLine().split("\\s+");
    for (int i = 0; i < people; ++i) {
      dSpeed[i] = Integer.parseInt(dpeople[i]);
      pSpeed[i] = Integer.parseInt(ppeople[i]);
    }

    Arrays.sort(dSpeed);
    Arrays.sort(pSpeed);

    int totalSpeed = 0;

    if (number == 1) {
      for (int i = 0; i < people; ++i) {
        totalSpeed += Math.max(pSpeed[i], dSpeed[i]);
      }
    } else if (number == 2) {
      for (int i = 0; i < people; ++i) {
        totalSpeed += Math.max(dSpeed[i], pSpeed[(people-1)-i]);
      }
    }

    System.out.println(totalSpeed);
  }
  // completed 28/04/2020 (dd/mm/yyyy)
  // note: look into new PrintWriter(new OutputStreamWriter(System.out)); and stringtokenizer (new StringTokenizer(br.readLine())
  // also make some premade functions to read i guess lol
}