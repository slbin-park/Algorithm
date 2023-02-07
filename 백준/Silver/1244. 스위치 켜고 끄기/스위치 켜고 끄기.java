import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static int[] arr;
	static boolean[] visited;
	static BufferedWriter bw;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		int[] arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		m = Integer.parseInt(st.nextToken());
		for (int i = 0; i < m; i++) {

			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			if (a == 1) {
				for (int j = b - 1; j < n; j += b) {
					if (arr[j] == 0) {
						arr[j] = 1;
					} else
						arr[j] = 0;
				}
			} else {
				b -= 1;
				if (arr[b] == 1) {
					arr[b] = 0;
				} else
					arr[b] = 1;
				int cnt = 1;

				while (true) {
					if (b + cnt >= n || b - cnt < 0)
						break;
					if (arr[b + cnt] == arr[b - cnt]) {
						if (arr[b + cnt] == 0) {
							arr[b + cnt] = 1;
							arr[b - cnt] = 1;
						} else {
							arr[b + cnt] = 0;
							arr[b - cnt] = 0;
						}
						cnt += 1;
					} else {
						break;
					}
				}
			}

		}
		for (int j = 0; j < n; j++) {
			bw.write(String.valueOf(arr[j]) + " ");
			if ((j + 1) % 20 == 0)
				bw.newLine();
		}
		bw.newLine();
		br.close();
		bw.flush();
	}
}