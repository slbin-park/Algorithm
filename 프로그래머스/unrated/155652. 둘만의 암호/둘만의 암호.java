import java.util.*;
class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        Map<String,Integer> map = new HashMap<>();
        for(int i=0;i<skip.length();i++){
            map.put(String.valueOf(skip.charAt(i)),1);
        }
        for(int i=0;i<s.length();i++){
            char curC = s.charAt(i);
            for(int j=0;j<index;j++){
                curC+=1;
                if(curC>'z'){
                    curC = 'a';
                }
                while(map.getOrDefault(String.valueOf(curC),-1) != -1){
                    curC+=1;
                    if(curC>'z'){
                    curC = 'a';
                    }
                }
            }
            answer+=String.valueOf(curC);
        }
        return answer;
    }
}