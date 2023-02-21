import java.io.*;
import java.util.StringTokenizer;

class Main {
    static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int INF = Integer.MIN_VALUE;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};
    static int[] A, B, C, D, E, F;
    static int[][] arr;
    static StringTokenizer st;
    static int[] visited;
    static int N, M, flag;
    static BufferedReader br;

    static BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
    );

    public static boolean is_xy(int x, int y) {
        if (0 <= x && x < N && 0 <= y && y < M) {
            return true;
        }
        return false;
    }

    public static int solve(int x, int y, int dir) {

        int cnt = 0;
        while (true) {
//            System.out.println(x + " " + y);
            if (arr[x][y] == 0) {
                arr[x][y] = 2;
                cnt += 1;
            }
            int flag = 0;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (is_xy(nx, ny) && arr[nx][ny] == 0) {
                    flag = 1;
                    break;
                }
            }

            // 청소되지 않은 빈 칸이 없고 뒤가 벽일 경우
            if (flag == 0 && !is_xy(x - dx[dir], y - dy[dir])) {
                return cnt;
            }

            // 청소되지 않은 빈 칸이 없고 뒤가 1일경우
            if (flag == 0 && arr[x - dx[dir]][y - dy[dir]] == 1) {
                return cnt;
            }

            // 후진이 가능할 경우
            if (flag == 0 && arr[x - dx[dir]][y - dy[dir]] != 1) {
                x -= dx[dir];
                y -= dy[dir];
                continue;
            }
            dir = (dir + 1) % 4;
            if (is_xy(x + dx[dir], y + dy[dir]) && arr[x + dx[dir]][y + dy[dir]] == 0) {
                x += dx[dir];
                y += dy[dir];
            }
        }
    }


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];
        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int dir = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // 북 서 남 동
        if (dir == 1) dir = 3;
        else if (dir == 3) dir = 1;
        System.out.println(solve(r, c, dir));
        bw.flush();
    }

}