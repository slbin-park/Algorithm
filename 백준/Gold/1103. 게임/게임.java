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
    static char[] check = { 'a', 'e', 'i', 'o', 'u' };
    static BufferedWriter bw;

    public static boolean isMove(int x, int y) {
        if (0 <= x && x < n && 0 <= y && y < m) {
            return true;
        }
        return false;
    }

    public static void dfs(int x, int y) {
        answer = Math.max(answer, visited[x][y]);
        for (int i = 0; i < 4; i++) {
            int v = Integer.parseInt(String.valueOf(arr[x][y]));
            int nx = x + dx[i] * v;
            int ny = y + dy[i] * v;
            if (isMove(nx, ny) && arr[nx][ny] != 'H') {
                if (visited[nx][ny] < visited[x][y] + 1) {
                    if (visited[x][y] > n * m) {
                        System.out.println("-1");
                        System.exit(0);
                    }
                    visited[nx][ny] = visited[x][y] + 1;
                    dfs(nx, ny);
                }
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
        arr = new char[n][m];
        visited = new int[n][m];
        visited[0][0] = 1;
        answer = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            for (int j = 0; j < m; j++) {
                arr[i][j] = a.charAt(j);
            }
        }
        dfs(0, 0);
        System.out.println(answer);
        bw.flush();
        br.close();
        bw.close();
    }

}