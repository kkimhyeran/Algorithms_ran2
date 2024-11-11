import java.util.*;
class Solution {
    public int solution(int[] nums) {
        
        // 1. hashmap 생성 (폰켓몬 종료 번호 = 순번)
        Map<Integer, Integer> ponkets = new HashMap<>();
        for (int num: nums) {
            ponkets.put(num, ponkets.getOrDefault(num, 0) + 1);
            // System.out.println("결과 : " + ponkets);
        }
        
        // System.out.println("결과 : " + ponkets);
        
        // 2. 폰켓몬 가져가기
        // return 되는 값은 폰켓몬 최대 종류 수
        int half_len = nums.length / 2;
        if (half_len <= ponkets.size()) {
            return half_len;
        } else {
            return ponkets.size();
        }
        
    }
}