import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {

        // 1. 입력값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int r = Integer.parseInt(input[0]); // 세로
        int c = Integer.parseInt(input[1]); // 가로

        // 단어 정보
        char[][] dict_arr = new char[r][c];
        for (int i = 0; i < r; i++) {
            String row = br.readLine();
            for (int j = 0; j < c; j++) {
                dict_arr[i][j] = row.charAt(j);
            }
        }

        ArrayList<String> extract_dict = new ArrayList<>();

        // 2. 가로 문자 확인
        for (int i = 0; i < r; i++) {
            StringBuilder word = new StringBuilder();

            for (int j = 0; j < c; j++) {
                if (dict_arr[i][j] != '#') {
                    word.append(dict_arr[i][j]);
                } else {
                    if (word.length() >= 2) extract_dict.add(word.toString());
                    word.setLength(0);
                }
            }
            if (word.length() >= 2) extract_dict.add(word.toString());
        }

        // 3. 세로 문자 확인
        for (int i = 0; i < c; i++) {
            StringBuilder word = new StringBuilder();

            for (int j = 0; j < r; j++) {
                if (dict_arr[j][i] != '#') {
                    word.append(dict_arr[j][i]);
                } else {
                    if (word.length() >= 2) extract_dict.add(word.toString());
                    word.setLength(0);
                }
            }
            if (word.length() >= 2) extract_dict.add(word.toString());
        }

        // 4. 저장된 모든 단어 정렬
        Collections.sort(extract_dict);

        // 5. 가장 앞에 있는 단어 출력
        System.out.println(extract_dict.get(0));
    }
}
