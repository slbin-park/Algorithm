import java.io.*;
import java.io.IOException;
import java.util.*;

class Main {
    static int n, m;
    static int a, b, c, d, answer;
    static int[] visited;
    static char[][] arr;
    static int[] dx = { 1, -1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };

    // static LinkedList<Integer> result_dfs = new LinkedList<Integer>();
    // static LinkedList<Integer> result_bfs = new LinkedList<Integer>();

    public static boolean is_move(int x, int y) {
        if (0 <= x && x < n && 0 <= y && y < m) {
            return true;
        }
        return false;
    }

    public static void dfs(int x, int y, int cnt) {
        answer = Math.max(answer, cnt);
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (is_move(nx, ny) && visited[(int) arr[nx][ny]] == 0) {
                visited[(int) arr[nx][ny]] = 1;
                dfs(nx, ny, cnt + 1);
                visited[(int) arr[nx][ny]] = 0;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        answer = 0;
        visited = new int[200];
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new char[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            for (int j = 0; j < m; j++) {
                arr[i][j] = a.charAt(j);
            }
        }
        visited[arr[0][0]] = 1;
        dfs(0, 0, 1);
        System.out.println(answer);
        br.close();
        bw.close();
    }

}