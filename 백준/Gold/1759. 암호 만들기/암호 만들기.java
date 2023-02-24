import java.io.*;
import java.io.IOException;
import java.util.*;

class Main {
    static int n, m;
    static int a, b, c, d, answer;
    static int[] visited;
    static char[] arr;
    static int[] dx = { 1, -1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };
    static char[] check = { 'a', 'e', 'i', 'o', 'u' };
    static BufferedWriter bw;

    public static void dfs(int depth, int index) throws IOException {
        if (depth == n) {
            int cnt = 0;
            for (int i = 0; i < m; i++) {
                if (visited[i] == 1) {
                    for (int j = 0; j < 5; j++) {
                        if (arr[i] == check[j]) {
                            cnt += 1;
                            break;
                        }
                    }
                }
            }
            if (cnt < 1 || cnt > n - 2) {
                return;
            }
            for (int i = 0; i < m; i++) {
                if (visited[i] == 1) {
                    bw.write(String.valueOf(arr[i]));
                }
            }
            bw.newLine();
            return;
        }
        for (int i = index; i < m; i++) {
            if (visited[i] == 0) {
                visited[i] = 1;
                dfs(depth + 1, i + 1);
                visited[i] = 0;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new char[m];
        visited = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            arr[i] = st.nextToken().charAt(0);
        }
        Arrays.sort(arr);
        dfs(0, 0);
        bw.flush();
        br.close();
        bw.close();
    }

}