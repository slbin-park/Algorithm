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
        String str = st.nextToken();
        int[] visited = new int['Z' - 'A' + 1];
        for (int i = 0; i < str.length(); i++) {
            visited[(int) str.charAt(i) - 'A'] += 1;
        }
        String res = "";
        String last = "";
        for (int i = 0; i < str.length() / 2; i++) {
            for (int j = 0; j < 'Z' - 'A' + 1; j++) {
                if (visited[j] >= 2) {
                    visited[j] -= 2;
                    res += String.valueOf((char) (j + 'A'));
                    last = String.valueOf((char) (j + 'A')) + last;
                    break;
                }
            }
        }
        for (int j = 0; j < 'Z' - 'A' + 1; j++) {
            if (visited[j] == 1) {
                res += String.valueOf((char) (j + 'A'));
                break;
            }
        }
        res += last;
        if (str.length() == res.length()) {
            System.out.println(res);
        } else {
            System.out.println("I'm Sorry Hansoo");
        }

        bw.flush();
        br.close();
        bw.close();
    }

}