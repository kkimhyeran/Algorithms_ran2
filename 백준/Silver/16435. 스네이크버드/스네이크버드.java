import java.io.*;
import java.util.*;

import static java.util.Arrays.sort;

public class Main {
    public static void main(String[] args) throws IOException{
        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(br.readLine());
        int[] h_array = new int[n];
        for (int i = 0; i < n; i++){
            h_array[i] = Integer.parseInt(st.nextToken());
        }

        // 2. 높이 오름차순 정렬
        Arrays.sort(h_array);

        // 3. 높이가 낮은 과일부터 차례로 먹는다.
        for (int i = 0; i < n; i++){
            if (l >= h_array[i]){
                l++;
            }
        }
        System.out.println(l);
    }
}
