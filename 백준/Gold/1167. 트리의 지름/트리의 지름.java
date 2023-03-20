import java.io.*;
import java.io.IOException;
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
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        visited = new int[n + 1];
        arr = new ArrayList<ArrayList<Node>>();
        for (int i = 0; i <= n; i++)
            arr.add(new ArrayList<>());
        answer = 0;
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int j = Integer.parseInt(st.nextToken());
            while (true) {
                int idx = Integer.parseInt(st.nextToken());
                if (idx == -1)
                    break;
                int cost = Integer.parseInt(st.nextToken());
                arr.get(j).add(new Node(idx, cost));
            }
        }
        dfs(1, 0);
        int max_v = 0;
        int idx = 0;
        visited[1] = 0;
        for (int i = 1; i <= n; i++) {
            if (visited[i] > max_v) {
                max_v = visited[i];
                idx = i;
            }
        }
        visited = new int[n + 1];
        dfs(idx, 0);
        max_v = 0;
        visited[idx] = 0;
        for (int i = 1; i <= n; i++) {
            if (visited[i] > max_v) {
                max_v = visited[i];
            }
        }
        System.out.println(max_v);
        bw.flush();
        br.close();
        bw.close();
    }

}