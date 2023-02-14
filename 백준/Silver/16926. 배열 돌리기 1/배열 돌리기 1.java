import java.io.*;
import java.util.StringTokenizer;

class Main {
    static class Node {
        int u, v, w;

        public Node(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }

    }

    static int INF = Integer.MIN_VALUE;
    static int[] dx = {-1, 0, 1};
    static int[] dy = {1, 1, 1};
    static StringTokenizer st;
    //    static List<Integer> arr;
    static int[] visited;
    static int N, M, res;
    static BufferedReader br;

    static BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
    );

    public static void rotate(int[][] arr, int depth) {
        // 왼쪽 밑
        int temp = arr[N - 1 - depth][depth];
        // 왼쪽 돌리기
        for (int i = N - depth - 2; i >= depth; i--) {
            arr[i + 1][depth] = arr[i][depth];
        }
        // 위쪾 돌리기
        for (int i = depth + 1; i < M - depth; i++) {
            arr[depth][i - 1] = arr[depth][i];
        }
        // 오른쪽
        for (int i = depth + 1; i < N - depth; i++) {
            arr[i - 1][M - depth - 1] = arr[i][M - depth - 1];
        }
        for (int i = M - depth - 2; i > depth; i--) {
            arr[N - depth - 1][i + 1] = arr[N - depth - 1][i];
        }
        arr[N - 1 - depth][depth + 1] = temp;
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int a = Integer.parseInt(st.nextToken());
                arr[i][j] = a;
            }
        }
        for (int i = 0; i < Math.min(N, M) / 2; i++) {
            for (int j = 0; j < R; j++) {
                rotate(arr, i);
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                bw.write(String.valueOf(arr[i][j]) + " ");
            }
            bw.newLine();
        }
        bw.newLine();
        bw.flush();
    }
}