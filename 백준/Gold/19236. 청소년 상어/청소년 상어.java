import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
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


    static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = {0, -1, -1, -1, 0, 1, 1, 1};
    static int[] sdx = {-1, 0, 1, 0};
    static int[] sdy = {0, -1, 0, 1};
    static int sx, sy, sd, answer, res, cnt;
    static int[][] fishArr;
    static ArrayList<Node> arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
//        M = Integer.parseInt(st.nextToken());
        arr = new ArrayList<>();
        fishArr = new int[4][4];
        for (int i = 0; i <= 16; i++) {
            arr.add(new Node(-1, -1, -1));
        }
        res = 0;
        sx = 0;
        sy = 0;
        answer = 0;
        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                int ai = Integer.parseInt(st.nextToken());
                int bi = Integer.parseInt(st.nextToken()) - 1;
                fishArr[i][j] = ai;
                arr.get(ai).x = i;
                arr.get(ai).y = j;
                arr.get(ai).dir = bi;
                if (i == 0 && j == 0) {
                    sd = bi;
                    arr.get(ai).x = -1;
                    arr.get(ai).y = -1;
                    arr.get(ai).dir = -1;
                    fishArr[0][0] = 0;
                    answer += ai;
                }
            }
        }
        solution();
        System.out.println(res);
//        bw.flush();
//        bw.close();
    }

    static void solution() {

        moveFish();
        ArrayList<Node> arr2 = new ArrayList<>();
        arr2.add(new Node(-1, -1, -1));
        for (int i = 1; i <= 16; i++) {
            Node node = arr.get(i);
            arr2.add(new Node(node.x, node.y, node.dir));
        }
        int[][] fishArr1 = new int[4][4];
        for (int i = 0; i < 4; i++) {
            fishArr1[i] = Arrays.copyOf(fishArr[i], 4);
        }
        int prev_cnt = cnt;
        int X = sx;
        int Y = sy;
        int dir = sd;
        int tmpAnswer = answer;
        for (int i = 1; i < 4; i++) {
            sx = X + i * dx[dir];
            sy = Y + i * dy[dir];
            sd = dir;
            answer = tmpAnswer;
            if (getNextShark()) {
//                System.out.println("i = " + i + " prev_cnt = " + prev_cnt + " cnt = " + cnt + " answer = " + answer);
//                System.out.println("sx = " + sx + " sy = " + sy + " sd = " + sd);
//                System.out.println("answer = " + answer);
//                System.out.println("넘어가자");
                cnt++;
//                printFish();
//                System.out.println("sx = " + sx + " sy" + sy + " sd = " + sd);
                solution();
            }
            arr = new ArrayList<>();
            arr.add(new Node(-1, -1, -1));
            for (int j = 1; j <= 16; j++) {
                Node node = arr2.get(j);
                arr.add(new Node(node.x, node.y, node.dir));
            }
            for (int j = 0; j < 4; j++) {
                fishArr[j] = Arrays.copyOf(fishArr1[j], 4);
            }
        }
    }

    static void printFish() {
        for (int i = 0; i < 4; i++) {
            System.out.println(Arrays.toString(fishArr[i]));
        }
    }

    static void arrser() {
        for (int i = 0; i < 16; i++) {
            System.out.println(arr.get(i));
        }
    }

    static boolean getNextShark() {
        if (0 <= sx && sx < 4 && 0 <= sy && sy < 4) {
            if (fishArr[sx][sy] != 0) {
//                System.out.println("sx = " + sx + " sy = " + sy);
//                System.out.println(arr.get(fishArr[sx][sy]));
//                System.out.println(fishArr[sx][sy]);
                arr.get(fishArr[sx][sy]).x = -1;
                sd = arr.get(fishArr[sx][sy]).dir;
                answer += fishArr[sx][sy];
                fishArr[sx][sy] = 0;
                res = Math.max(res, answer);
                return true;
            }
        }
        return false;
    }

    static void moveFish() {
        for (int i = 1; i <= 16; i++) {
//            printFish();
//            System.out.println("===");
            Node node = arr.get(i);
            int x = node.x;
            if (x == -1) {
                continue;
            }
//            System.out.println(" i  = " + i);
//            System.out.println(node);
//            printFish();
            int y = node.y;
            int dir = node.dir;
//            System.out.println(node);
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if (canMoveFish(nx, ny)) {
                int tmp = fishArr[nx][ny];
                arr.get(i).x = nx;
                arr.get(i).y = ny;
                fishArr[nx][ny] = fishArr[x][y];
                if (arr.get(tmp).x != -1) {
                    arr.get(tmp).x = x;
                    arr.get(tmp).y = y;
                    fishArr[x][y] = tmp;
                } else {
                    fishArr[x][y] = 0;
                }
            } else {
                while (true) {
                    dir++;
                    if (dir == 8) {
                        dir = 0;
                    }
                    if (dir == node.dir) {
                        break;
                    }
                    nx = x + dx[dir];
                    ny = y + dy[dir];
                    if (canMoveFish(nx, ny)) {
                        int tmp = fishArr[nx][ny];
                        arr.get(i).x = nx;
                        arr.get(i).y = ny;
                        arr.get(i).dir = dir;
                        fishArr[nx][ny] = fishArr[x][y];
                        if (arr.get(tmp).x != -1) {
                            arr.get(tmp).x = x;
                            arr.get(tmp).y = y;
                            fishArr[x][y] = tmp;
                        } else {
                            fishArr[x][y] = 0;
                        }
                        break;
                    }
                }
            }
        }
    }

    static boolean canMoveFish(int nx, int ny) {
//        System.out.println("nx = " + nx + " ny = " + ny);
        if (sx == nx && sy == ny)
            return false;
        if (0 <= nx && nx < 4 && 0 <= ny && ny < 4) {
            return true;
        }
        return false;
    }

}