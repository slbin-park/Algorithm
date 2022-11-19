class Solution {
    public String solution(int[] food) {
        String answer = "";
         for(int n=1; n<food.length; n++){
        if(food[n]%2!=0){
            food[n]--;
        }
        if(food[n]==0){
            continue;
        }
         int a=food[n]/2;
            for(a=0; a<food[n];a+=2){
                    answer+=Integer.toString(n);
             }
         }
        int b=0;
        answer+="0";
        for(int i=answer.length()-2;i>=0;i--){
            answer+= String.valueOf(answer.charAt(i));
        }
        return answer;
    }
}