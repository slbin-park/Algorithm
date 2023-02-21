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
    static int[] A, B, C, D, E, F;
    static int[] dy = {0, -1, 0, 1};
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

    //    public static int solve(int x, int y, int dir) {
//        int cnt = 0;
//        while (true) {
//            if (arr[x][y] == 0) {
//                arr[x][y] = 2;
//                cnt += 1;
//            }
//            int flag = 0;
//            System.out.println(x + " " + y);
//            for (int i = 0; i < 4; i++) {
//                int nx = x + dx[i];
//                int ny = y + dy[i];
//                if (is_xy(nx, ny) && arr[nx][ny] == 0) {
//                    flag = 1;
//                    break;
//                }
//            }
//
//            // 청소되지 않은 빈 칸이 없고 뒤가 0이 아닐경우
//            if (flag == 0 && arr[x - dx[dir]][y - dy[dir]] == 1) {
//                return cnt;
//            }
//            if (flag == 0 && arr[x - dx[dir]][y - dy[dir]] == 0) {
//                x -= dx[dir];
//                y -= dy[dir];
//                System.out.println("후진");
//                continue;
//            }
//            dir = (dir + 1) % 4;
//            if (is_xy(x + dx[dir], y + dy[dir]) && arr[x + dx[dir]][y + dy[dir]] == 0) {
//                x += dx[dir];
//                y += dy[dir];
//            }
//        }
//    }
//
//
//    public static void main(String[] args) throws IOException {
//        br = new BufferedReader(new InputStreamReader(System.in));
//        st = new StringTokenizer(br.readLine());
//        N = Integer.parseInt(st.nextToken());
//        M = Integer.parseInt(st.nextToken());
//        arr = new int[N][M];
//        st = new StringTokenizer(br.readLine());
//        int r = Integer.parseInt(st.nextToken());
//        int c = Integer.parseInt(st.nextToken());
//        int dir = Integer.parseInt(st.nextToken());
//        for (int i = 0; i < N; i++) {
//            st = new StringTokenizer(br.readLine());
//            for (int j = 0; j < M; j++) {
//                arr[i][j] = Integer.parseInt(st.nextToken());
//            }
//        }
//        System.out.println(solve(r, c, dir));
//        bw.flush();
//    }

    public static int back(int depth, int index) {
//        System.out.println(depth + " " + index);
        if (depth == 6) {
//            for (int i = 0; i < 6; i++) {
//                for (int j = 0; j < 3; j++) {
//                    System.out.print(arr[i][j]);
//                }
//                System.out.println();
//            }
//            System.out.println("+=======+");

            for (int i = 0; i < 3; i++) {
                if (arr[index][i] > 0) {
                    return -1;
                }
            }
            if (index == 5) flag = 1;
            return index;
        }
        // 현재에서  밑에꺼 중에 승 무 패를 정함
        // 시작 인덱스의 승을깔수 있을떄
        if (arr[depth][2] > 0 && arr[index][0] > 0) {
            arr[depth][2] -= 1;
            arr[index][0] -= 1;
            int a = back(depth + 1, index);
            if (a != -1) {
                back(index + 2, index + 1);
            }
            arr[depth][2] += 1;
            arr[index][0] += 1;
        }

        // 무를 깔수있을때
        if (arr[depth][1] > 0 && arr[index][1] > 0) {
            arr[depth][1] -= 1;
            arr[index][1] -= 1;
            int a = back(depth + 1, index);
            if (a != -1) {
                back(index + 2, index + 1);
            }
            arr[depth][1] += 1;
            arr[index][1] += 1;
        }
        // 패를 깔수있을때
        if (arr[depth][0] > 0 && arr[index][2] > 0) {
            arr[depth][0] -= 1;
            arr[index][2] -= 1;
            int a = back(depth + 1, index);
            if (a != -1) {
                back(index + 2, index + 1);
            }
            arr[depth][0] += 1;
            arr[index][2] += 1;
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            arr = new int[6][3];
            flag = 0;
            for (int j = 0; j < 6; j++) {
                for (int k = 0; k < 3; k++) {
                    arr[j][k] = Integer.parseInt(st.nextToken());
                }
            }
            back(1, 0);
            if (flag == 1) {
                bw.write("1 ");
            } else {
                bw.write("0 ");
            }
        }
        bw.newLine();
        bw.flush();
    }
}