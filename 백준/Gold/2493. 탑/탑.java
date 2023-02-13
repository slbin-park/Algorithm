import java.io.*;
import java.util.Stack;
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
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        int[] answer = new int[N];
        Stack<int[]> stack = new Stack<>();
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = N - 1; i >= 0; i--) {
            if (stack.isEmpty()) {
                stack.add(new int[]{arr[i], i});
            } else {
                while (!stack.isEmpty() && stack.peek()[0] < arr[i]) {
                    int[] a = stack.pop();
                    answer[a[1]] = i + 1;
                }
                stack.add(new int[]{arr[i], i});
            }
        }
        for (int i = 0; i < N; i++) {
            bw.write(String.valueOf(answer[i]) + " ");
        }
        bw.newLine();
        bw.flush();
    }
}