import java.io.*;
import java.io.IOException;
import java.util.*;

class Main {
    static int n, m;
    static int a, b, c, d;
    static int[] result;

    // static LinkedList<Integer> result_dfs = new LinkedList<Integer>();
    // static LinkedList<Integer> result_bfs = new LinkedList<Integer>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int i = 1;
        int sum = 1;
        while (sum + i <= n) {
            sum += i;
            i += 1;
        }
        // 짝수일때 밑에서 시작
        if (i % 2 == 0) {
            n -= sum;
            bw.write(String.valueOf(1 + n) + "/" + String.valueOf(i - n));
        } else {
            n -= sum;
            bw.write(String.valueOf(i - n) + "/" + String.valueOf(1 + n));
        }
        // i 가
        // bw.newLine();
        // bw.write("i = " + String.valueOf(i));
        // bw.newLine();
        // bw.write("n = " + String.valueOf(n));
        // bw.newLine();
        // bw.write("sum = " + String.valueOf(sum));
        bw.newLine();

        br.close();
        bw.close();
    }

}