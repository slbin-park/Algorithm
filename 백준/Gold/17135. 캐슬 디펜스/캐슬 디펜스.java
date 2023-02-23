import java.io.*;
import java.util.StringTokenizer;

class Main {
    static class Node {
        int l;
        int cst;

        public Node(int x, int y) {
            this.l = x;
            this.cst = y;
        }
    }

    static int INF = Integer.MIN_VALUE;
    static int[] dx = {0, 0, 1, 1};
    static int[] dy = {0, 1, 0, 1};
    static int[][] arr;
    static StringTokenizer st;
    static int[] visited, arrow;
    static int N, M, D, flag, res;
    static BufferedReader br;

    static BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
    );

    // 순열 뽑기
    public static void dfs(int depth, int index) {
        if (depth == 3) {
            solve();
        } else {
            for (int i = index; i < M; i++) {
                if (visited[i] == 0) {
                    visited[i] = 1;
                    arrow[depth] = i;
                    dfs(depth + 1, i);
                    visited[i] = 0;
                    arrow[depth] = 0;
                }
            }
        }
    }

    // 적들 한칸 이동
    public static void move_enemy(int[][] arr2) {
        // 마지막줄은 그냥 초기화
        for (int i = 0; i < M; i++) arr2[N - 1][i] = 0;
        // 한칸씩 내리기
        for (int i = N - 2; i >= 0; i--) {
            for (int j = 0; j < M; j++) {
                if (arr2[i][j] == 1) {
                    arr2[i + 1][j] = 1;
                    arr2[i][j] = 0;
                }
            }
        }
    }

    // 거리 얻기
    public static int get_dis(int x, int y, int arrow_number) {
        return Math.abs(x - N) + Math.abs(arrow[arrow_number] - y);
    }


    public static int delete_target(int[][] arr2) {
        int[][] target = new int[3][3];
        int cnt = 0;
        target[0][0] = 99999;
        target[1][0] = 99999;
        target[2][0] = 99999;
        for (int i = N - 1; i >= 0; i--) {
            for (int j = 0; j < M; j++) {
                if (arr2[i][j] == 1) {
                    // 궁수번호
                    for (int k = 0; k < 3; k++) {
                        int a = get_dis(i, j, k);
                        // 전에 잡은 타겟 보다 가까운 경우
                        if (a < target[k][0] && a <= D) {
                            target[k][0] = a;
                            target[k][1] = i;
                            target[k][2] = j;
                        }
                        if (a == target[k][0] && j < target[k][2]) {
                            target[k][0] = a;
                            target[k][1] = i;
                            target[k][2] = j;
                        }
                    }
                }
            }
        }
        for (int i = 0; i < 3; i++) {
            if (target[i][0] != 99999 && arr2[target[i][1]][target[i][2]] == 1) {
                arr2[target[i][1]][target[i][2]] = 0;
                cnt += 1;
            }
        }
        return cnt;
    }

    public static void solve() {
        int cnt = 0;
        int[][] arr2 = new int[N][M];
        for (int i = 0; i < N; i++) {
            arr2[i] = arr[i].clone();
        }
        for (int i = 0; i < N; i++) {
            cnt += delete_target(arr2);
            move_enemy(arr2);
        }
        res = Math.max(res, cnt);
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        res = 0;
        arr = new int[N][M];
        arrow = new int[3];
        visited = new int[M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0, 0);
        bw.write(String.valueOf(res));
        bw.newLine();
        bw.flush();
    }

}