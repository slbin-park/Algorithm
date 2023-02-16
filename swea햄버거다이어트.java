package datastructure.swea;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


class Solution {

    static class Node {
        int x, y, cnt, v;

        Node(int x, int y, int cnt, int v) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.v = v;
        }
    }

    static int T;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int N, M;
    static BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out)
    );

    public static int dfs(int[][] arr, int v, int k, int index) {
        if (index == N) {
            return v;
        }
        int a = dfs(arr, v, k, index + 1);
        if (k + arr[index][1] > M) {
            return Math.max(a, v);
        }
        int b = dfs(arr, v + arr[index][0], k + arr[index][1], index + 1);
        return Math.max(a, b);
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());

        for (int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            int[][] arr = new int[N][2];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                arr[i][0] = a;
                arr[i][1] = b;
            }
            int answer = dfs(arr, 0, 0, 0);
            bw.write("#" + String.valueOf(test_case) + " ");
            bw.write(String.valueOf(answer));
            bw.newLine();
        }
        bw.flush();
    }
}
