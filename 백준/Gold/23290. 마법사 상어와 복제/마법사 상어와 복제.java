import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
    static class Node {
        int x, y, dir;

        public Node(int x, int y, int dir) {
            this.x = x;
            this.y = y;
            this.dir = dir;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "x=" + x +
                    ", y=" + y +
                    ", dir=" + dir +
                    '}';
        }
    }

    static int S, M;
    static long answer;
    static long[][][] arr, move_arr;
    static int[][] smell;
    static long[][] cnt_arr;
    static long maxFishCnt;
    static int X, Y;
    static int[] shark, prevMoveShark;
    static int[] dx = {0, -1, -1, -1, 0, 1, 1, 1}; // ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    static int[] dy = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] sdx = {-1, 0, 1, 0};
    static int[] sdy = {0, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        arr = new long[4][4][8];
        move_arr = new long[4][4][8];
        cnt_arr = new long[4][4];
        smell = new int[4][4];

        while (M-- > 0) {
            st = new StringTokenizer(br.readLine());
            int fx = Integer.parseInt(st.nextToken()) - 1;
            int fy = Integer.parseInt(st.nextToken()) - 1;
            int d = Integer.parseInt(st.nextToken()) - 1;
            arr[fx][fy][d] += 1;
        }
        st = new StringTokenizer(br.readLine());
        X = Integer.parseInt(st.nextToken()) - 1;
        Y = Integer.parseInt(st.nextToken()) - 1;
        while (S-- > 0) {
            shark = new int[3];
            prevMoveShark = new int[3];
            moveFishs();
            maxFishCnt = Integer.MIN_VALUE;

            getSharkDir(0);
            moveShark();
            clearSmell();
            clearFish();
            makeFishs();
        }

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 8; k++) {
                    answer += arr[i][j][k];
                }
            }
        }
        System.out.println(answer);
//        bw.flush();
//        bw.close();
    }

    static void moveFishs() {
        move_arr = new long[4][4][8];
        cnt_arr = new long[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 8; k++) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    boolean flag = true;
                    // 물고기가 있다면
                    if (arr[i][j][k] != 0) {
                        // 이동할 수 있다면
                        if (checkMove(nx, ny)) {
                            move_arr[nx][ny][k] += arr[i][j][k];
                            cnt_arr[nx][ny] += arr[i][j][k];
                        } else {
                            // 이동할 수 없을 때
                            int d = k;
                            while (true) {
                                d--;
                                if (d < 0) d = 7;
                                if (d == k) {
                                    move_arr[i][j][k] += arr[i][j][k];
                                    cnt_arr[i][j] += arr[i][j][k];
                                    break;
                                }
                                nx = i + dx[d];
                                ny = j + dy[d];
                                if (checkMove(nx, ny)) {
                                    move_arr[nx][ny][d] += arr[i][j][k];
                                    cnt_arr[nx][ny] += arr[i][j][k];
                                    break;
                                }
                            }
                        }
                        // 이동을 못한경우에 가만히 냅둠
                    }
                }
            }
        }
    }

    static void getSharkDir(int depth) {
        if (depth == 3) {
            moveShark();
            return;
        }
        for (int i = 0; i < 4; i++) {
            shark[depth] = i;
            getSharkDir(depth + 1);
        }
    }

    static void moveShark() {
        long cnt = 0;
        int nx = X;
        int ny = Y;
        boolean[][] prev = new boolean[4][4];
        for (int i = 0; i < 3; i++) {
            nx += sdx[shark[i]];
            ny += sdy[shark[i]];
            if (checkMoveShark(nx, ny)) {
                if (!prev[nx][ny]) {
                    cnt += cnt_arr[nx][ny];
                    prev[nx][ny] = true;
                }
            } else {
                return;
            }
        }
        if (maxFishCnt < cnt) {
            maxFishCnt = cnt;
            prevMoveShark = Arrays.copyOf(shark, shark.length);
        }
    }

    static boolean checkMoveShark(int x, int y) {
        if (0 <= x && x < 4 && 0 <= y && y < 4) {
            return true;
        }
        return false;
    }


    static boolean checkMove(int x, int y) {
        if (0 <= x && x < 4 && 0 <= y && y < 4) {
            if (X == x && Y == y) return false;
            if (smell[x][y] == 0) {
                return true;
            }
        }
        return false;
    }


    static void clearSmell() {
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (smell[i][j] > 0) {
                    smell[i][j] -= 1;
                }
            }
        }
    }

    static void clearFish() {
        for (int i = 0; i < 3; i++) {
            int dir = prevMoveShark[i];
            X += sdx[dir];
            Y += sdy[dir];
            if (cnt_arr[X][Y] > 0) {
                smell[X][Y] = 2;
            }
            cnt_arr[X][Y] = 0;
        }
    }

    static void makeFishs() {
        // 전에 있던건 무조건 복사가된다.
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 8; k++) {
                    if (cnt_arr[i][j] != 0) {
                        arr[i][j][k] += move_arr[i][j][k];
                    }
                }
            }
        }
    }
}