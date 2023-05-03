import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = new String[players.length];
        Map<String,Integer> map = new HashMap<>();
        for(int i=0;i<players.length;i++){
            map.put(players[i],i);
        }
        for(int i=0;i<callings.length;i++){
            String curName = callings[i];
            int rank = map.get(curName);
            String prevName = players[rank-1];
            players[rank] = prevName;
            players[rank-1] = curName;
            map.put(prevName,rank);
            map.put(curName,rank-1);
        }
        for(int i=0;i<players.length;i++){
            answer[i] = players[i];
        }
        return answer;
    }
}