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
	static char[][] arr;
	static int[][] history;
	static int[] dx = { 0, 0, -1, 1 };
	static int[] dy = { 1, -1, 0, 0 };
	static int[] color = { 1, 2, 3, 4, 5 };
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		arr = new char[N][M];
		history = new int[N][M];
		cnt = 1;
		res = Integer.MAX_VALUE;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			String a = st.nextToken();
			for (int j = 0; j < M; j++) {
				arr[i][j] = a.charAt(j);
				if (a.charAt(j) == 'O') {
					history[i][j] = -1;
				}
			}
		}
		if (K >= 2) {
			createBfs();
		}

		cnt = 0;
//		K = K % 6;
		if (K > 2) {
			K -= 2;
			K = K % 4;
			if (K != 0) {
				while (true) {

					cnt++;
//				System.out.println("cnt" + cnt + " " + K);
					boom();

					if (cnt == K) {
						break;
					}

					cnt++;
					createBfs();

					if (cnt == K) {
						break;
					}

				}
			}
		}
		for (int i = 0; i < N; i++) {
//			System.out.println(Arrays.toString(history[i]));
			for (int j = 0; j < M; j++) {
				System.out.print(arr[i][j]);
			}
			System.out.println();
		}
		bw.newLine();
		bw.flush();
		bw.close();
	}

	public static void createBfs() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == '.') {
					history[i][j] = cnt;
					arr[i][j] = 'O';
				}
			}
		}
	}

	public static void boom() {
		char[][] arr2 = new char[N][M];
		for (int i = 0; i < N; i++) {
			arr2[i] = Arrays.copyOf(arr[i], M);
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr2[i][j] == 'O' && history[i][j] == cnt - 2) {
					arr[i][j] = '.';
					for (int k = 0; k < 4; k++) {
						int nx = i + dx[k];
						int ny = j + dy[k];
						if (0 <= nx && nx < N && 0 <= ny && ny < M) {
							arr[nx][ny] = '.';
						}
					}
				}
			}
		}
	}
}
