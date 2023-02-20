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
    static int[] dx = {-1, 0, 1};
    static int[] dy = {1, 1, 1};
    static int[][] arr;
    static StringTokenizer st;
    //    static List<Integer> arr;
    static int[] visited;
    static int[][] rotates;
    static int[] pers;
    static int N, M, res, K, cnt, call;
    static BufferedReader br;

    static BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
    );

    public static int get_cnt(int cnt) {
        int res = 1;
        cnt -= M;
        if (cnt > 0) {
            res += cnt / K;
            if (cnt % K > 0) {
                res += 1;
            }
        }

        return res;
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        long answer = 0;
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            answer += get_cnt(arr[i]);
        }
        System.out.println(answer);
        bw.flush();
    }
}