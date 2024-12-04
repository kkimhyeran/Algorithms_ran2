import java.util.*;

class Solution {
    public String[] solution(String[] files) {
        // 1. 파일명 head, number, tail로 자르기
        List<FileData> fileList = new ArrayList<>();
        for (int i = 0; i < files.length; i++) {
            fileList.add(parseFile(files[i], i));
        }
        
        // 2. 정렬
        Collections.sort(fileList, (a, b) -> {
            // 1순위 정렬은 head
            int headCompare = a.head.compareToIgnoreCase(b.head);
            if (headCompare != 0) return headCompare;
            
            // 2순위 정렬 number
            int numberCompare = Integer.compare(a.number, b.number);
            if (numberCompare != 0) return numberCompare;
            
            // 3순위 정렬은 원래 파일 순서 
            return Integer.compare(a.index, b.index);
        });
        
        // 3. 결과 
        String[] answer = new String[files.length];
        for (int i = 0; i < fileList.size(); i++) {
            answer[i] = fileList.get(i).original;
        }
        return answer;
    }
    
    // 파일 정보 저장 클래스
    static class FileData {
        String original; // 원본 파일명
        String head;     // HEAD 부분
        int number;      // NUMBER 부분
        int index;       // 입력 순서
        
        public FileData(String original, String head, int number, int index) {
            this.original = original;
            this.head = head;
            this.number = number;
            this.index = index;
        }
    }

    // 파일명 분리 메서드
    private static FileData parseFile(String file, int index) {
        String head = "";
        String number = "";
        
        // head
        int i = 0;
        while (i < file.length() && !Character.isDigit(file.charAt(i))) {
            head += file.charAt(i);
            i++;
        }
        
        // number
        while (i < file.length() && Character.isDigit(file.charAt(i)) && number.length() < 5) {
            number += file.charAt(i);
            i++;
        }
        
        // tail 
        int numValue = number.isEmpty() ? 0 : Integer.parseInt(number);
        
        return new FileData(file, head, numValue, index);
    }
}
