import java.io.*;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.StringTokenizer;

class Main {
    static class Node {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "x=" + x +
                    ", y=" + y +
                    '}';
        }
    }

    static int n, m;
    static int[] dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};
    static int[] edgeCount;
    static int[][] visited;


    static Deque<Integer> dq;
    static Deque<Integer> answer;
    static ArrayList<ArrayList<Integer>> arr;

    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static void TC() {
        while (!dq.isEmpty()) {
            int curIdx = dq.poll();
            answer.add(curIdx);
            ArrayList<Integer> curArr = arr.get(curIdx);
            for (int i = 0; i < curArr.size(); i++) {
                edgeCount[curArr.get(i)]--;
                if (edgeCount[curArr.get(i)] == 0) {
                    dq.add(curArr.get(i));
                }
            }
        }
    }

    static void printAll() throws IOException {
        while (!answer.isEmpty()) {
            int a = answer.pollLast();
            bw.write(String.valueOf(a) + " ");
        }
        bw.newLine();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new ArrayList<>();
        edgeCount = new int[n + 1];
        dq = new ArrayDeque<>();
        answer = new ArrayDeque<>();
        for (int i = 0; i <= n; i++) {
            arr.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            arr.get(B).add(A);
            edgeCount[A]++;
        }
        for (int i = 1; i <= n; i++) {
            if (edgeCount[i] == 0) {
                dq.offer(i);
            }
        }
        TC();
        printAll();
        bw.flush();
        bw.close();
        br.close();
    }
}