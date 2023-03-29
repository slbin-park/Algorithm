import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

class Main {
    static class Node {
        int idx, cost;

        public Node(int idx, int cost) {
            this.idx = idx;
            this.cost = cost;
        }

    }

    static int n, m;
    static int a, b, c, d, answer;
    static int[] visited;
    static int[] dx = { 1, -1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };
    static BufferedWriter bw;
    static ArrayList<ArrayList<Node>> arr;

    public static void dfs(int idx, int cost) {
        for (Node node : arr.get(idx)) {
            if (visited[node.idx] == 0) {
                visited[node.idx] = cost + node.cost;
                dfs(node.idx, cost + node.cost);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashSet<Integer> set = new HashSet<Integer>();
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int cnt = 0;
        for (int i = 0; i < a; i++) {
            set.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < b; i++) {
            int c = Integer.parseInt(st.nextToken());
            if (set.contains(c)) {
                cnt += 1;
            }
        }
        System.out.println(a + b - cnt * 2);
        bw.flush();
        br.close();
        bw.close();
    }

}