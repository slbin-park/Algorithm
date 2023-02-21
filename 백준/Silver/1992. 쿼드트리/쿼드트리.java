import java.io.*;
import java.util.StringTokenizer;

class Main {
    static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int INF = Integer.MIN_VALUE;
    static int[] dx = {0, 0, 1, 1};
    static int[] dy = {0, 1, 0, 1};
    static int[] A, B, C, D, E, F;
    static int[][] arr;
    static StringTokenizer st;
    static int[] visited;
    static int N, M, flag;
    static BufferedReader br;

    static BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
    );

    public static void solve(char[][] arr1, int n, int x, int y) throws IOException {
        char start = arr1[x][y];
        int flag = 0;
        for (int i = x; i < x + n; i++) {
            for (int j = y; j < y + n; j++) {
                if (start != arr1[i][j]) {
                    flag = 1;
                    break;
                }
            }
        }

        if (flag == 0) {
            bw.write(String.valueOf(start));
        } else {
            bw.write("(");

            for (int i = 0; i < 4; i++) {
                solve(arr1, n / 2, x + n / 2 * dx[i], y + n / 2 * dy[i]);
            }
            bw.write(")");

        }
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        char[][] arr1 = new char[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            arr1[i] = a.toCharArray();
        }
        solve(arr1, N, 0, 0);
        bw.flush();
    }

}