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

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
//        M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N + 1];
        int[] parent = new int[N + 1];
        for (int i = 1; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a] += 1;
            arr[b] += 1;
        }
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (a == 2) {
                bw.write("yes\n");
            } else {
                if (arr[b] == 0) {
                    bw.write("no\n");
                } else if (arr[b] == 1 && parent[b] == 0) {
                    bw.write("no\n");
                } else {
                    bw.write("yes\n");
                }
            }
        }

        bw.flush();
    }
}