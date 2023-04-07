import java.io.*;
import java.util.*;

class Main {
	static class Node {
		int x, y;

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public String toString() {
			return "Node{" + "x=" + x + ", y=" + y + '}';
		}
	}

	static int n, m, hx, hy, ex, ey, answer, S, M, R, C;
	static int[][] arr;
	static int time;
	static int[][] visited;
	static int X, Y;
	static int[] dx = { 1, -1, 0, 0 }, dy = { 0, 0, 1, -1 };
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static Deque<Node> fishs;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		arr = new int[R][C];
		X = -1;
		Y = -1;
		M = R;
		int minv = Integer.MAX_VALUE;
		for (int i = 0; i < R; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < C; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (minv > arr[i][j] && (i + j) % 2 == 1) {
					minv = arr[i][j];
					X = i;
					Y = j;
				}
			}
		}
//		System.out.println("x ==" + X + " y = " + Y);
		if (R % 2 == 0) {
			if (C % 2 == 0) {
				make02();
			} else {
				make01();
			}
		} else {
			make00();
		}
		bw.newLine();
		bw.flush();
		bw.close();
	}

	// 홀수 , 홀 +짝
	static void make00() throws IOException {
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C - 1; j++) {
				if (i % 2 == 0) {
					bw.write("R");
				} else {
					bw.write("L");
				}
			}
			if (i != R - 1)
				bw.write("D");
		}
	}

	// 짝+홀
	static void make01() throws IOException {
		for (int i = 0; i < C; i++) {
			for (int j = 0; j < R - 1; j++) {
				if (i % 2 == 0) {
					bw.write("D");
				} else {
					bw.write("U");
				}
			}
			if (i != C - 1)
				bw.write("R");
		}
	}

	// 짝+짝
	static void make02() throws IOException {
//		boolean LRFLAG = true;
		boolean LRFLAG = true;
		for (int i = 0; i < R; i++) {
			boolean dirFlag = true;
			boolean DFLAG = false;
			for (int j = 0; j < C - 1; j++) {
				// 진행 방향 오른쪽
				if (i == X || i + 1 == X) {
					if (LRFLAG) {
						// 내려감
						if (dirFlag) {
							if (check(i + 1, j)) {
								bw.write("R");
								// 방향 안바꿈
								if (j == C - 2) {
									bw.write("D");
								}
							} else {
								bw.write("D");
								bw.write("R");
								// 방향 바꿈
								dirFlag = false;
							}
						} else {
							if (check(i, j)) {
								bw.write("R");
							} else {
								// 올라감
								bw.write("U");
								bw.write("R");
								dirFlag = true;
								if (j == C - 2) {
									bw.write("D");
								}
							}
						}
					}
					// 진행방향 왼쪽
					else {
						// 내려감
						if (dirFlag) {
							if (check(i + 1, C - j - 1)) {
								bw.write("L");
								// 방향 안바꿈
								if (j == C - 2) {
									bw.write("D");
								}
							} else {
								bw.write("D");
								bw.write("L");
								// 방향 바꿈
								dirFlag = false;
							}
						} else {
							if (check(i + 1, C - j - 1)) {
								bw.write("L");
							} else {
								// 올라감
								bw.write("U");
								bw.write("L");
								dirFlag = true;
								if (j == C - 2) {
									bw.write("D");
								}
							}
						}
					}
				} else {
					if (LRFLAG) {
						bw.write("R");
					} else {
						bw.write("L");
					}
				}
			}
			LRFLAG = !LRFLAG;
			if ((i == X || i + 1 == X)) {
				i++;
			}
//			System.out.println("i = " + i);
			if (i < R - 1) {
				bw.write("D");
//				bw.write("추가됨");
			}
//			bw.newLine();
		}
	}

	static boolean check(int x, int y) {
		if (x == X && y == Y) {
			return true;
		}
		return false;
	}
}