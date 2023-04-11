import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
    static class Node implements Comparable<Node> {
        int idx;
        double value;
        int cnt;

        public Node(int idx, double value, int cnt) {
            this.idx = idx;
            this.value = value;
            this.cnt = cnt;
        }

        @Override
        public int compareTo(Node o) {
            if (value > o.value) {
                return -1;
            } else if (value < o.value) {
                return 1;
            }
            return 0;
        }
    }


    static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = {0, -1, -1, -1, 0, 1, 1, 1};
    static int[] sdx = {-1, 0, 1, 0};
    static int[] sdy = {0, -1, 0, 1};
    static int sx, sy, sd, answer, res, cnt, N, M;
    static int[][] fishArr;
    static double[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Queue<Node> pq = new PriorityQueue<>();
        double minV = Double.MAX_VALUE;
        double maxV = Double.MIN_VALUE;
        double answer = Double.MAX_VALUE;
        N = Integer.parseInt(st.nextToken());
        arr = new double[N];
        if (N != 0)
            st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Double.parseDouble(st.nextToken());
            pq.add(new Node(i, arr[i], 1));
            minV = Double.min(minV, arr[i]);
            maxV = Double.max(maxV, arr[i]);
        }
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

        answer = maxV - minV;
//        System.out.println(minV + " " + maxV);
        while (M-- > 0 && !pq.isEmpty()) {
            Node node = pq.poll();
            double cur_v = arr[node.idx] / (double) (node.cnt + 1);
//            System.out.println("cur_v = " + cur_v);
            minV = Double.min(minV, cur_v);
            if (!pq.isEmpty())
                maxV = Double.max(pq.peek().value, cur_v);
            answer = Double.min(answer, maxV - minV);
            pq.add(new Node(node.idx, cur_v, node.cnt + 1));
        }
//        System.out.println(minV + " " + maxV);
        if (N == 0) {
            System.out.println(0);
        } else {
            System.out.println(answer);
        }
    }


}