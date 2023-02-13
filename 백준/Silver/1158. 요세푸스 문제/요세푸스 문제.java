import java.io.*;
import java.util.*;

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
        M = Integer.parseInt(st.nextToken());
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 1; i <= N; i++) {
            dq.add(i);
        }
        List<Integer> answer = new ArrayList<>();
        while (dq.size() > 1) {
            for (int i = 0; i < M - 1; i++) {
                dq.add(dq.poll());
            }
            answer.add(dq.poll());
        }
        answer.add(dq.poll());
        bw.write("<");
        for (int i = 0; i < answer.size() - 1; i++) {
            bw.write(String.valueOf(answer.get(i)) + ", ");
        }
        bw.write(String.valueOf(answer.get(answer.size() - 1)) + ">");
        bw.flush();
    }
}