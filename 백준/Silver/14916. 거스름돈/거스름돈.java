import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 거스름돈 액수

        // 2. 동전 개수 구하기
        int cnt = 0; // 동전 개수
        while (true) {
            if (n % 5 == 0) {
                cnt += n/5;
                System.out.println(cnt);
                break;
            }
            else {
                n -= 2;
                cnt += 1;
            }
            if (n < 0){
                System.out.println(-1);
                break;
            }
        }

    }
}