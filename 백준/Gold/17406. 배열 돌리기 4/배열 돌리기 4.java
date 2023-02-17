import java.io.*;
import java.util.StringTokenizer;

class Main {
    static class Node {
        int value;
        int c_value;

        public Node(int value, int c_value) {
            this.value = value;
            this.c_value = c_value;

        }


    }

    static int INF = Integer.MIN_VALUE;
    static int[] dx = {-1, 0, 1};
    static int[] dy = {1, 1, 1};
    static int[][] arr;
    static StringTokenizer st;
    //    static List<Integer> arr;
    static int[] visited;
    static int[][] rotates;
    static int[] pers;
    static int N, M, res, K;
    static BufferedReader br;

    static BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
    );

    public static int[][] copy_arr(int[][] arr) {
        int[][] res = new int[N][M];
        for (int i = 0; i < arr.length; i++) {
            System.arraycopy(arr[i], 0, res[i], 0, arr[i].length);
        }
        return res;
    }

    public static void per(int depth) {
        if (depth == K) {
            int[][] cur_arr = copy_arr(arr);
            for (int i = 0; i < K; i++) {
                cur_arr = rotate(cur_arr, rotates[pers[i]][0], rotates[pers[i]][1], rotates[pers[i]][2]);
            }
            res = Math.min(get_res(cur_arr), res);
        }
        for (int i = 0; i < K; i++) {
            if (visited[i] == 0) {
                visited[i] = 1;
                pers[depth] = i;
                per(depth + 1);
                visited[i] = 0;

            }
        }
    }

    public static int get_res(int[][] arr) {
        int res = 100000000;
        for (int i = 0; i < N; i++) {
            int cur_v = 0;
            for (int j = 0; j < M; j++) {
                cur_v += arr[i][j];
            }
            res = Math.min(cur_v, res);
        }
        return res;
    }

    public static int[][] rotate(int[][] arr, int r, int c, int s) {
        int[][] res = copy_arr(arr);
        int start_r = r - s;
        int start_c = c - s;
        int end_r = r + s;
        int end_c = c + s;
        for (int i = 0; i < s; i++) {
            // 왼쪽거 위로 올리기
            for (int j = start_r + i + 1; j <= end_r - i; j++) {
                res[j - 1][start_c + i] = arr[j][start_c + i];
            }

            //밑에꺼 왼쪾으로
            for (int j = start_c + i + 1; j <= end_c - i; j++) {
                res[end_r - i][j - 1] = arr[end_r - i][j];
            }

            for (int j = end_r - i - 1; j >= start_r + i; j--) {
                res[j + 1][end_c - i] = arr[j][end_c - i];
            }
//            // 위에꺼 오른쪽으로
            for (int j = start_c + i; j < end_c - i; j++) {
                res[start_r + i][j + 1] = arr[start_r + i][j];
            }
        }
        return res;
    }


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }

        }

//        for (int i = 0; i < N; i++) {
//            System.out.println(Arrays.toString(arr[i]));
//        }
        res = Integer.MAX_VALUE;
        rotates = new int[K][3];
        visited = new int[K];
        pers = new int[K];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            rotates[i][0] = a - 1;
            rotates[i][1] = b - 1;
            rotates[i][2] = c;
        }
        per(0);
        System.out.println(res);
//        bw.newLine();
        bw.flush();
    }
}