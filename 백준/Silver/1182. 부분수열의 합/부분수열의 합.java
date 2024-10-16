import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, s;
    static int[] number_arr;
    static int rslt;

    public static void main(String[] args) throws IOException {

        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        n = Integer.parseInt(input[0]); // 정수의 개수
        s = Integer.parseInt(input[1]); // 목표 합

        number_arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            number_arr[i] = Integer.parseInt(st.nextToken());
        }


        // 2. 백트래킹 시작
        backtracking(0, 0);

        // 3. 결과 출력
        System.out.println(rslt);
    }

    // 백트래킹 함수
    public static void backtracking(int sum, int idx) {

        if (idx >= n) {
            return;
        }

        if (sum + number_arr[idx] == s) {
            rslt++;
        }


        // 현재 idx 요소 포함하는 경우
        backtracking(sum + number_arr[idx], idx + 1);
        // 현재 idx 요소 포함하지 않는 경우
        backtracking(sum, idx + 1);
    }
}
