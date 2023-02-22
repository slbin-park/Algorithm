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

    public static boolean is_move(int x, int y) {
        if (x < N && y < N) {
            if (arr[x][y] == 0) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        arr = new int[N][N];
        int[][][] dp = new int[N][N][3];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dp[0][1][0] = 1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int nx = i + 1;
                int ny = j + 1;
                if (is_move(i, ny)) {
                    dp[i][ny][0] += dp[i][j][0] + dp[i][j][2];
                }
                if (is_move(nx, j)) {
                    dp[nx][j][1] += dp[i][j][1] + dp[i][j][2];
                }
                if (is_move(nx, ny)) {
                    if (is_move(nx, j) && is_move(i, ny)) {
                        dp[nx][ny][2] += dp[i][j][0];
                        dp[nx][ny][2] += dp[i][j][1];
                        dp[nx][ny][2] += dp[i][j][2];
                    }
                }
            }
        }
//        for (int i = 0; i < N; i++) {
//            for (int j = 0; j < N; j++) {
//                for (int k = 0; k < 3; k++)
//                    System.out.printf(dp[i][j][k] + " ");
//                System.out.print("  ");
//            }
//            System.out.println();
//        }
        System.out.println(dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2]);
        bw.flush();
    }

}