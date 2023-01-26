import java.io.*;
import java.io.IOException;
import java.util.*;

class Main {
    static int n, m;
    static int a, b, c, d;
    static int[] parent;

    // static LinkedList<Integer> result_dfs = new LinkedList<Integer>();
    // static LinkedList<Integer> result_bfs = new LinkedList<Integer>();

    public static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int answer = 0;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        parent = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            parent[i] = i;
        }
        st = new StringTokenizer(br.readLine());
        int g = Integer.parseInt(st.nextToken());
        for (int i = 0; i < g; i++) {
            st = new StringTokenizer(br.readLine());
            int gi = Integer.parseInt(st.nextToken());
            int p = find(gi);
            if (p == 0) {
                break;
            }
            parent[p] = find(p - 1);
            answer += 1;
        }
        bw.write(String.valueOf(answer));
        bw.newLine();
        br.close();
        bw.close();
    }

}