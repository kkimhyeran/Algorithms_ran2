import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 숫자 개수
        int m = Integer.parseInt(st.nextToken()); // 총합

        st = new StringTokenizer(br.readLine());
        int[] number_array = new int[n];
        for (int i = 0; i < n; i++) {
            number_array[i] = Integer.parseInt(st.nextToken());
        }


        // 숫자 더하기
        int cnt = 0;
        for (int i = 0; i < n; i++){
            int tmp_sum = 0;

            for (int j = i; j < n; j++) {
                tmp_sum += number_array[j];

                if (tmp_sum == m){
                    cnt += 1;
                }
                else if (tmp_sum > m) {
                    break;
                }
            }
        }
        System.out.println(cnt);

    }
}
