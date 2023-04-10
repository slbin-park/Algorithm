import java.io.*;
import java.util.*;

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
			return "Node{" + "x=" + x + ", y=" + y + '}';
		}
	}

	static int N, M, K, cnt, X, Y, res;
	static int[][] arr;
	static int[] color = { 1, 2, 3, 4, 5 };
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		arr = new int[10][10];
		cnt = 0;
		res = Integer.MAX_VALUE;
		for (int i = 0; i < 10; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 10; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int[] a = { 5, 5, 5, 5, 5 };
		solve(0, a);
		if (res == Integer.MAX_VALUE) {
			System.out.println(-1);
		} else {
			System.out.println(res);
		}

		bw.newLine();
		bw.flush();
		bw.close();
	}

	public static void solve(int x, int[] colorArr) {
		if (res <= cnt) {
			return;
		}

		for (int i = x; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				if (arr[i][j] == 1) {
					for (int k = 4; k >= 0; k--) {
						if (colorArr[k] != 0) {
							if (isPut(i, j, k)) {
								// 0 으로 바꿈
								changeValue(i, j, k, 0);
								cnt++;
								// 남은 색종이 제거
								colorArr[k] -= 1;
								solve(i, colorArr);
								colorArr[k] += 1;
								changeValue(i, j, k, 1);
								cnt--;
							}
						}
					}
					return;
				}
			}
		}
//		System.out.println("??");
		res = Math.min(res, cnt);
	}

	static boolean isPut(int x, int y, int size) {
		for (int i = x; i <= x + size; i++) {
			if (i >= 10) {
				return false;
			}
			for (int j = y; j <= y + size; j++) {
				if (j >= 10) {
					return false;
				}
				if (arr[i][j] == 0) {
					return false;
				}
			}
		}
		return true;
	}

	static void changeValue(int x, int y, int size, int v) {
		for (int i = x; i <= x + size; i++) {
			for (int j = y; j <= y + size; j++) {
//				System.out.println("i = " + i + " j = " + j);
				arr[i][j] = v;
			}
		}
	}
}
