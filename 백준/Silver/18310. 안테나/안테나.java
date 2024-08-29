import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{
        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] adrs_array = new int[n];
        for (int i =0 ; i < n; i++) {
            adrs_array[i] = Integer.parseInt(st.nextToken());
        }

        // 2, 오름차순 정렬
        Arrays.sort(adrs_array);

        // 3. 가운데 집 찾기
        int result = 0;
        if (n % 2 == 0) {
            result = adrs_array[n/2 - 1];
        }
        else {
            result = adrs_array[n/2];
        }
        System.out.println(result);
    }
}