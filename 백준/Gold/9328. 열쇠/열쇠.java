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

    static int n, m, hx, hy, ex, ey, answer;
    static char[][] arr;
    static int time;
    static int[][] visited;
    static int[] keys;
    static int[] dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static Deque<Node> dq;
    static ArrayList<ArrayDeque<Node>> key_node;

    public static int bfs() {


        while (!dq.isEmpty()) {
            Node node = dq.poll();
            int x = node.x;
            int y = node.y;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (visited[nx][ny] == 0) {
                        if (arr[nx][ny] == '.') {
                            dq.offer(new Node(nx, ny));
                            visited[nx][ny] = 1;
                        } else if (arr[nx][ny] != '*') {
                            if (arr[nx][ny] == '$') {
                                answer++;
                                dq.offer(new Node(nx, ny));
                                visited[nx][ny] = 1;
                            } else if (arr[nx][ny] < 'a') {
                                if (keys[arr[nx][ny] - 'A'] == 1) {
                                    visited[nx][ny] = 1;
                                    dq.offer(new Node(nx, ny));
                                } else {
                                    // 대기열에 추가
                                    key_node.get(arr[nx][ny] - 'A').add(new Node(nx, ny));
                                }
                            } else {
                                //소문자 일 때는
                                visited[nx][ny] = 1;
                                //키 등록
                                keys[arr[nx][ny] - 'a'] = 1;
                                if (key_node.get(arr[nx][ny] - 'a').size() != -0) {
                                    while (key_node.get(arr[nx][ny] - 'a').size() != 0) {
                                        dq.offer(key_node.get(arr[nx][ny] - 'a').poll());
                                    }
                                }
                                dq.offer(new Node(nx, ny));
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
        int T = Integer.parseInt(st.nextToken());
        for (int a = 0; a < T; a++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            arr = new char[n][m];
            visited = new int[n][m];
            keys = new int['Z' - 'A' + 1];
            answer = 0;
            dq = new ArrayDeque<>();
            key_node = new ArrayList<>();
            for (int i = 0; i < 'z' - 'a' + 1; i++) {
                key_node.add(new ArrayDeque<>());
            }
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                String str = st.nextToken();
                for (int j = 0; j < m; j++) {
                    arr[i][j] = str.charAt(j);
                    if (i == 0 || i == n - 1 || j == 0 || j == m - 1) {
                        if (str.charAt(j) == '.') {
                            dq.offer(new Node(i, j));
                            visited[i][j] = 1;
                        }
                        if (str.charAt(j) == '$') {
                            dq.offer(new Node(i, j));
                            visited[i][j] = 1;
                            answer++;
                        }
                        if (arr[i][j] >= 'a') {
                            keys[arr[i][j] - 'a'] = 1;
                        }
                    }
                }
            }

            st = new StringTokenizer(br.readLine());
            String key = st.nextToken();
            if (!key.equals("0")) {
                for (int i = 0; i < key.length(); i++) {
                    int idx = key.charAt(i) - 'a';
                    keys[idx] = 1;
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (arr[i][j] != '*' && arr[i][j] != '$' && arr[i][j] != '.') {
                        if (i == 0 || i == n - 1 || j == 0 || j == m - 1) {
                            if (arr[i][j] < 'a') {
                                if (keys[arr[i][j] - 'A'] == 1) {
                                    dq.offer(new Node(i, j));
                                    visited[i][j] = 1;
                                } else {
                                    key_node.get(arr[i][j] - 'A').add(new Node(i, j));
                                }
                            }
                            if (arr[i][j] >= 'a') {
                                dq.offer(new Node(i, j));
                                visited[i][j] = 1;
                                if (key_node.get(arr[i][j] - 'a').size() != 0) {
                                    while (!key_node.get(arr[i][j] - 'a').isEmpty()) {
                                        dq.offer(key_node.get(arr[i][j] - 'a').poll());
                                    }
                                }
                            }
                        }
                    }
                }
            }
            bfs();
            System.out.println(answer);
        }

    }
}