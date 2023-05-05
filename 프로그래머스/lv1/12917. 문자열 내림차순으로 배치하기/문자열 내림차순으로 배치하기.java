import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        for(int i=s.length()-1;i>=0;i--){
            answer+=String.valueOf(arr[i]);
        }
        return answer;
    }
}