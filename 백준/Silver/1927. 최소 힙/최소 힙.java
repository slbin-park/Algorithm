import java.io.*;
import java.io.IOException;
import java.util.*;

class Main {
    static int n, m;
    static int a, b, c, d, answer;
    static int[][] visited;
    static char[][] arr;
    static int[] dx = { 1, -1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };
    static BufferedWriter bw;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            if (a == 0) {
                if (pq.size() == 0) {
                    bw.write("0");
                } else {
                    bw.write(String.valueOf(pq.poll()));
                }
                bw.newLine();
            } else {
                pq.add(a);
            }
        }
        bw.flush();
        br.close();
        bw.close();
    }

}