import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        
        
        // 1. 부서별 신청 예산 정렬 (내림차순)
        Arrays.sort(d);
            
        // 2. 예산 내에서 배분하기
        int answer = 0;

        for(int i=0; i < d.length; i++) {
            
            // 현재 남아있는 예산이 신청금액보다 작으면 break
            if(budget < d[i]) {
                break;
            }
            
            // 예산 배분
            budget -= d[i];
            answer += 1 ; // 부서 수 업데이트
        }
        
        return answer;
    }
}