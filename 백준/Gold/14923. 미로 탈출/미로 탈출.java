
import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

class Main {
    static class Node {
        int x, y;
        int use;

        public Node(int x, int y, int use) {
            this.x = x;
            this.y = y;
            this.use = use;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "x=" + x +
                    ", y=" + y +
                    ", use=" + use +
                    '}';
        }
    }

    static int n, m, hx, hy, ex, ey;
    static int[][] arr;
    static int time;
    static int[][][] visited;
    static int[] dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static int bfs() {
        Deque<Node> dq = new ArrayDeque<>();
        dq.add(new Node(hx, hy, 0));
        visited[hx][hy][0] = 0;
        while (!dq.isEmpty()) {
            Node node = dq.poll();
            int x = node.x;
            int y = node.y;
//            System.out.println(node);
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                int use = node.use;

                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (node.use == 0 && arr[nx][ny] == 1) {
                        if (visited[nx][ny][1] > visited[x][y][0] + 1) {
                            visited[nx][ny][1] = visited[x][y][0] + 1;
                            if (nx == ex && ny == ey) {
                                return visited[x][y][0] + 1;
                            }
                            dq.add(new Node(nx, ny, 1));
                        }
                    } else if (arr[nx][ny] == 0) {
                        if (visited[nx][ny][use] > visited[x][y][use] + 1) {
                            visited[nx][ny][use] = visited[x][y][use] + 1;
                            dq.add(new Node(nx, ny, use));
                            if (nx == ex && ny == ey) {
                                return visited[x][y][use] + 1;
                            }
                        }
                    }
                }
            }
        }
        return -1;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        visited = new int[n][m][2];
        st = new StringTokenizer(br.readLine());
        hx = Integer.parseInt(st.nextToken()) - 1;
        hy = Integer.parseInt(st.nextToken()) - 1;
        st = new StringTokenizer(br.readLine());
        ex = Integer.parseInt(st.nextToken()) - 1;
        ey = Integer.parseInt(st.nextToken()) - 1;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                visited[i][j][0] = Integer.MAX_VALUE;
                visited[i][j][1] = Integer.MAX_VALUE;
            }
        }
        System.out.println(bfs());
    }

}