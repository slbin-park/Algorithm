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
        TreeSet<String> set = new TreeSet<String>(Collections.reverseOrder());
        int a = Integer.parseInt(st.nextToken());
        int cnt = 0;
        for (int i = 0; i < a; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String el = st.nextToken();
            if (el.equals("enter")) {
                set.add(name);
            } else {
                set.remove(name);
            }
        }
        Iterator iter = set.iterator();
        while (iter.hasNext()) {
            System.out.println(iter.next());
        }
        bw.flush();
        br.close();
        bw.close();
    }

}