import java.io.*;
import java.io.IOException;
import java.util.*;

class Main {
    static class Node implements Comparable<Node> {
        int idx;
        long v;

        Node(int idx, long v) {
            this.idx = idx;
            this.v = v;
        }

        @Override
        public int compareTo(Node node) {
            if (this.v > node.v) {
                return 1;
            } else if (this.v < node.v) {
                return -1;
            }
            return 0;
        }

    }

    static int n, m;
    static int a, b, c, d, answer;
    static int[] visited;
    static char[][] arr;
    static int[] dx = { 1, -1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };
    static BufferedWriter bw;

    public static void clear(PriorityQueue<Node> pq) {
        while (!pq.isEmpty() && visited[pq.peek().idx] == 1) {
            pq.poll();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            PriorityQueue<Node> npq = new PriorityQueue<>();
            PriorityQueue<Node> mpq = new PriorityQueue<>(Collections.reverseOrder());
            st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            visited = new int[m];
            for (int j = 0; j < m; j++) {
                st = new StringTokenizer(br.readLine());
                String a = st.nextToken();
                long v = Long.parseLong(st.nextToken());
                if (a.equals("I")) {
                    npq.add(new Node(j, v));
                    mpq.add(new Node(j, v));
                } else {
                    if (v == 1) {
                        clear(mpq);
                        if (mpq.size() != 0) {
                            Node node = mpq.poll();
                            visited[node.idx] = 1;
                        }
                    } else {
                        clear(npq);
                        if (npq.size() != 0) {
                            Node node = npq.poll();
                            visited[node.idx] = 1;
                        }
                    }
                }
            }
            clear(mpq);
            clear(npq);
            if (mpq.isEmpty()) {
                bw.write("EMPTY");
            } else {
                Node node = mpq.poll();
                bw.write(String.valueOf(node.v) + " ");
                node = npq.poll();
                bw.write(String.valueOf(node.v));
            }
            bw.newLine();
        }
        bw.flush();
        br.close();
        bw.close();
    }

}