import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine()); // 테스트 케이스 횟수

        // t 횟수 만큼 반복
        for (int i = 1; i < (t+1); i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int test_num = Integer.parseInt(st.nextToken()); // 현재 테스트 번호

            int cnt = 0;
            int[] num = new int[20]; // 학생수는 총 20명
            for (int s = 0; s<20; s++) {
                num[s] = Integer.parseInt(st.nextToken());
            }

            for (int j = 0; j < 20; j++) {
                for (int k = 0; k < j; k++) {
                    if (num[k] > num[j]) {
                        //System.out.println("num[k] > num[j] :" + num[k] + ">" + num[j]);
                        cnt ++; // 이동 순서 횟수 +1
                    }
                }
            }
            System.out.println(test_num + " " + cnt);
        }
    }
}
