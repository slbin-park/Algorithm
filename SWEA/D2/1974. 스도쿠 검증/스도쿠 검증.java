
import java.util.*;
import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
    static final int N = 9;

    public static boolean check_three(int[][] arr) {
        boolean[] visited;
        for (int i = 0; i < N; i += 3) {
            visited = new boolean[N + 1];
            for (int j = i; j < i + 3; j++) {
                for (int k = i; k < i + 3; k++) {
                    int cur = arr[j][k];
                    if (visited[cur] == false) {
                        visited[cur] = true;
                    } else {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public static boolean check_wh(int[][] arr) {
        boolean[] visited;
        for (int i = 0; i < N; i++) {
            visited = new boolean[N + 1];
            for (int j = 0; j < N; j++) {
                int cur = arr[i][j];
                if (visited[cur] == false) {
                    visited[cur] = true;
                } else {
                    return false;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            visited = new boolean[N + 1];
            for (int j = 0; j < N; j++) {
                int cur = arr[j][i];
                if (visited[cur] == false) {
                    visited[cur] = true;
                } else {
                    return false;
                }
            }
        }

        return true;
    }

    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);

        int T;
        T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int[][] arr = new int[N][N];
            // 입력 받기
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }
            if (check_three(arr) && check_wh(arr)) {
                System.out.println("#" + test_case + " " + 1);
                continue;
            }
            System.out.println("#" + test_case + " " + 0);

        }
    }
}