
import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Solution {
    static ArrayList<Point> people, stair;
    static ArrayList<Integer> down;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int test = Integer.parseInt(st.nextToken());
        for (int t = 1; t <= test; t++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            people = new ArrayList<>();
            stair = new ArrayList<>();
            down = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    int val = Integer.parseInt(st.nextToken());
                    if (val == 1) {
                        people.add(new Point(i, j));
                    } else if (val > 1) {
                        stair.add(new Point(i, j));
                        down.add(val);
                    }
                }
            }
            int[][] dp = new int[1 << people.size()][people.size()];
            for (int i = 0; i < people.size(); i++) {
                for (int j = 0; j < 1 << people.size(); j++) {
                    if ((j & 1 << i) == 0) {
                        dp[j][i] = dis(people.get(i), stair.get(0));
                    } else {
                        dp[j][i] = dis(people.get(i), stair.get(1));
                    }
                }
            }
            int result = Integer.MAX_VALUE;
            for (int i = 0; i < 1 << people.size(); i++) {
                ArrayList<Integer> stair0 = new ArrayList<>();
                ArrayList<Integer> stair1 = new ArrayList<>();
                int maxv = Integer.MIN_VALUE;
                for (int j = 0; j < people.size(); j++) {
                    if ((i & 1 << j) == 0) {
                        stair0.add(dp[i][j]);
                    } else {
                        stair1.add(dp[i][j]);
                    }
                }
                Collections.sort(stair0);
                Collections.sort(stair1);
                if (!stair0.isEmpty()) {
                    if (stair0.size() <= 3) {
                        maxv = Math.max(maxv, stair0.get(stair0.size() - 1) + down.get(0));
                    } else {
                        int idx = (stair0.size() - 1) % 3;
                        int val = 0;
                        for (int j = idx; j < stair0.size(); j += 3) {
                            if (val >= stair0.get(j)) {
                                val += down.get(0);
                            } else {
                                val = stair0.get(j) + down.get(0);
                            }
                        }
                        maxv = Math.max(maxv, val);
                    }
                }
                if (!stair1.isEmpty()) {
                    if (stair1.size() <= 3) {
                        maxv = Math.max(maxv, stair1.get(stair1.size() - 1) + down.get(1));
                    } else {
                        int idx = (stair1.size() - 1) % 3;
                        int val = 0;
                        for (int j = idx; j < stair1.size(); j += 3) {
                            if (val >= stair1.get(j)) {
                                val += down.get(1);
                            } else {
                                val = stair1.get(j) + down.get(1);
                            }
                        }
                        maxv = Math.max(maxv, val);
                    }
                }
                result = Math.min(result, maxv);
            }
            System.out.println("#" + t + " " + result);
        }
    }

    static int dis(Point f, Point t) {
        return Math.abs(f.x - t.x) + Math.abs(f.y - t.y) + 1;
    }
}