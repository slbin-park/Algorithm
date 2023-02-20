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

    public static void dv(int n, int r, int c) {
        if (n == 2) {
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < 2; j++) {
                    cnt += 1;
                    if (r + i == M && c + j == K) {
                        System.out.println(cnt - 1);
                        System.exit(0);
                        return;
                    }
                }
            }
            return;
        }
        if (r + n / 2 >= M && c + n / 2 >= K) {
            dv(n / 2, r, c);
        } else {
            cnt += (n / 2) * (n / 2);
        }

        if (r + n / 2 >= M && c + n >= K) {
            dv(n / 2, r, c + n / 2);
        } else {
            cnt += (n / 2) * (n / 2);
        }

        if (r + n >= M && c + n / 2 >= K) {
            dv(n / 2, r + n / 2, c);
        } else {
            cnt += (n / 2) * (n / 2);
        }

        if (r + n >= M && c + n >= K) {
            dv(n / 2, r + n / 2, c + n / 2);
        } else {
            cnt += (n / 2) * (n / 2);
        }


    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        N = (int) Math.pow(2, N);
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        cnt = 0;
        dv(N, 0, 0);
        bw.flush();
    }
}