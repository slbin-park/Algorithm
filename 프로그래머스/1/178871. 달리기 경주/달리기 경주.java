import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = new String[players.length];
        Map<String,Integer> map = new HashMap<>();
        for(int i=0;i<players.length;i++){
            answer[i] = players[i];
            map.put(players[i],i);
        }
        for(int i=0;i<callings.length;i++){
            String curPlayer = callings[i];
            int curRank = map.get(curPlayer);
            String nextPlayer = answer[curRank-1];
            answer[curRank] = nextPlayer;
            answer[curRank-1] = curPlayer;
            map.put(nextPlayer,curRank);
            map.put(curPlayer,curRank-1);
        }
        return answer;
    }
}