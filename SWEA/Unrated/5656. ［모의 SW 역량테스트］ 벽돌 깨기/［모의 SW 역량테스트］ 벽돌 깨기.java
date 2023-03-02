
import java.util.*;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Solution {
    static class Node {
        int x;
        int y;
        int v;

        public Node(int x, int y, int v) {
            this.x = x;
            this.y = y;
            this.v = v;
        }
    }

    static int N, W, H;
    static int answer;
    static int[][] arr;
    static int[] combi;
    static int depth;
    static int[] dx = { 0, 0, 1, -1 };
    static int[] dy = { 1, -1, 0, 0 };

    public static void brk(int[][] c_arr, int x, int y) {
        if (c_arr[x][y] == 1) {
            c_arr[x][y] = 0;
            return;
        }
        Deque<Node> dq = new ArrayDeque<>();
        dq.offer(new Node(x, y, c_arr[x][y]));
        c_arr[x][y] = 0;
        while (!dq.isEmpty()) {
            Node node = dq.poll();
            for (int i = 0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                for (int j = 1; j < node.v; j++) {
                    if (!is_move(nx, ny)) {
                        break;
                    }
                    if (c_arr[nx][ny] > 1) {
                        dq.add(new Node(nx, ny, c_arr[nx][ny]));
                    }
                    c_arr[nx][ny] = 0;
                    nx += dx[i];
                    ny += +dy[i];
                }
            }
        }
    }

    public static void clean(int[][] c_arr) {
        for (int i = H - 2; i >= 0; i--) {
            for (int j = 0; j < W; j++) {
                if (c_arr[i][j] == 0) {
                    continue;
                }
                int nx = i;
                int tmp = c_arr[i][j];
                for (int k = i + 1; k < H; k++) {
                    // System.out.println("k = " + k + " arr = " + arr[k][j]);
                    if (c_arr[k][j] == 0) {
                        nx = k;
                    } else {
                        break;
                    }
                }
                // while (nx + 1 < H && c_arr[nx + 1][j] == 0) {
                // nx += 1;
                // }
                // System.out.println(nx + " = nx " + " j = " + j);
                // System.out.println(arr[nx][j]);
                if (c_arr[nx][j] == 0) {
                    c_arr[i][j] = 0;
                    c_arr[nx][j] = tmp;
                    // System.out.println("청소함");
                }
            }
        }
    }

    public static boolean is_move(int x, int y) {
        if (0 <= x && x < H && 0 <= y && y < W) {
            return true;
        }
        return false;
    }

    public static void solve() {
        int cnt = 0;
        int[][] c_arr = new int[H][W];
        for (int i = 0; i < H; i++) {
            c_arr[i] = arr[i].clone();
        }
        for (int i = 0; i < N; i++) {
            int y = combi[i];
            int x = 0;
            while (x < H && c_arr[x][y] == 0) {
                x += 1;
            }
            if (x == H) {
                continue;
            }
            if (c_arr[x][y] == 0) {
                continue;
            } else {
                brk(c_arr, x, y);
                clean(c_arr);
            }
            // for (int k = 0; k < H; k++) {
            // System.out.println(Arrays.toString(c_arr[k]));
            // }
            // System.out.println();
        }
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (c_arr[i][j] > 0) {
                    cnt += 1;
                }
            }
        }
        // System.out.println();
        answer = Math.min(answer, cnt);
    }

    public static void dfs(int depth) {
        if (depth == N) {
            solve();
            // System.out.println(Arrays.toString(combi));
            return;
        }
        for (int i = 0; i < W; i++) {
            combi[depth] = i;
            dfs(depth + 1);
        }
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        for (int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());
            combi = new int[N];
            answer = Integer.MAX_VALUE;
            arr = new int[H][W];
            for (int i = 0; i < H; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < W; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            dfs(0);
            // combi[0] = 2;
            // combi[1] = 2;
            // combi[2] = 6;
            // solve();
            bw.write("#" + test_case + " " + answer);
            bw.newLine();
            // System.out.println("#" + test_case + " " + 0);
        }
        bw.flush();
        bw.close();
    }
}