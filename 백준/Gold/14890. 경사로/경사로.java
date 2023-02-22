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
    static int[] dx = {0, 0, 1, 1};
    static int[] dy = {0, 1, 0, 1};
    static int[] A, B, C, D, E, F;
    static int[][] arr;
    static StringTokenizer st;
    static int[] visited;
    static int N, M, flag;
    static BufferedReader br;

    static BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
    );

    public static boolean check(int x) {
        int[] visited = new int[N];
        for (int i = 1; i < N; i++) {
            // 두개가 같지 않을 경우
            if (arr[x][i] != arr[x][i - 1]) {
                // 1이상 차이 나면 false
                if (Math.abs(arr[x][i] - arr[x][i - 1]) != 1) {
                    return false;
                }
                // i-1이 더 작을경우
                if (arr[x][i] > arr[x][i - 1]) {
                    int prev = i - 1;
                    if (visited[prev] == 1) {
                        return false;
                    }
                    visited[prev] = 1;
                    int cnt = 1;
                    while (prev - 1 >= 0 && cnt != M) {
                        prev -= 1;
                        if (arr[x][prev] != arr[x][prev + 1]) return false;
                        // 이미 다리가 깔려있으면
                        if (visited[prev] == 1) {
                            return false;
                        }
                        visited[prev] = 1;
                        cnt += 1;
                    }
                    if (cnt != M) {
                        return false;
                    }
                } else {
                    // i-1이 더 클경우
                    int next = i;
                    if (visited[next] == 1) {
                        return false;
                    }
                    visited[next] = 1;
                    int cnt = 1;
                    while (next + 1 < N && cnt != M) {
                        next += 1;
                        if (arr[x][next] != arr[x][next - 1]) return false;
                        // 이미 다리가 깔려있으면
                        if (visited[next] == 1) {
                            return false;
                        }
                        visited[next] = 1;
                        cnt += 1;
                    }
                    if (cnt != M) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public static boolean check2(int x) {
        int[] visited = new int[N];
        for (int i = 1; i < N; i++) {
            // 두개가 같지 않을 경우
            if (arr[i][x] != arr[i - 1][x]) {
                // 1이상 차이 나면 false
                if (Math.abs(arr[i][x] - arr[i - 1][x]) != 1) {
                    return false;
                }
                // i-1이 더 작을경우
                if (arr[i][x] > arr[i - 1][x]) {
                    int prev = i - 1;
                    if (visited[prev] == 1) {
                        return false;
                    }
                    visited[prev] = 1;
                    int cnt = 1;
                    while (prev - 1 >= 0 && cnt != M) {
                        prev -= 1;
                        if (arr[prev][x] != arr[prev + 1][x]) return false;
                        // 이미 다리가 깔려있으면
                        if (visited[prev] == 1) {
                            return false;
                        }
                        visited[prev] = 1;
                        cnt += 1;
                    }
                    if (cnt != M) {
                        return false;
                    }
                } else {
                    // i-1이 더 클경우
                    int next = i;
                    if (visited[next] == 1) {
                        return false;
                    }
                    visited[next] = 1;
                    int cnt = 1;
                    while (next + 1 < N && cnt != M) {
                        next += 1;
                        if (arr[next][x] != arr[next - 1][x]) return false;
                        // 이미 다리가 깔려있으면
                        if (visited[next] == 1) {
                            return false;
                        }
                        visited[next] = 1;
                        cnt += 1;
                    }
                    if (cnt != M) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int answer = 0;
        for (int i = 0; i < N; i++) {
            if (check(i)) {
                answer += 1;
            }
            if (check2(i)) {
                answer += 1;
            }
        }
        System.out.println(answer);
        bw.flush();
    }

}