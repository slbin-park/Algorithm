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
    static int N, M, res;
    static BufferedReader br;

    static BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
    );


    public static int op_rank(String oper) {
        if (oper.equals("(")) {
            return 0;
        }
        if (oper.equals("+") || oper.equals("-")) {
            return 1;
        }
        if (oper.equals("*") || oper.equals("/")) {
            return 2;
        }
        return 3;
    }

    public static boolean is_oper(String oper) {
        if (oper.equals("(") || oper.equals(")") || oper.equals("+") ||
                oper.equals("-") || oper.equals("*") || oper.equals("/"))
            return true;
        return false;
    }

    public static boolean dfs(String[][] arr, int x, int y) {
        if (y == M - 1) {
            return true;
        }
        for (int i = 0; i < 3; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                if (arr[nx][ny].equals(".")) {
                    arr[nx][ny] = "X";
                    if (dfs(arr, nx, ny)) return true;
                }
            }
        }
        return false;
    }


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        res = 0;
        String[][] arr = new String[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            for (int j = 0; j < M; j++) {
                arr[i][j] = String.valueOf(a.charAt(j));
            }
        }
        for (int i = 0; i < N; i++) {
            if (dfs(arr, i, 0)) {
                res += 1;
            }
        }
//        for (int i = 0; i < N; i++) {
//            for (int j = 0; j < M; j++) {
//                System.out.print(arr[i][j] + " ");
//            }
//            System.out.println();
//        }
        System.out.println(res);
        bw.flush();
    }
}