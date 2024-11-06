import java.util.*;

class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        
        // 1. 시간 초단위로 변환
        int videoLength = timeToSeconds(video_len);
        int position = timeToSeconds(pos);
        int opStart = timeToSeconds(op_start);
        int opEnd = timeToSeconds(op_end);

        // 2. 사용자 command 수행
        for (String command : commands) {
            // 오프닝 구간 확인
            if (position >= opStart && position <= opEnd) {
                position = opEnd;
            }
            
            // prev
            if (command.equals("prev")) {
                position = Math.max(0, position - 10);

            }
            // next
            else if (command.equals("next")) {
                position = Math.min(videoLength, position + 10);
            }
            
            // 오프닝 구간 확인
            if (position >= opStart && position <= opEnd) {
                position = opEnd;
            }
        }
        
        return secondsToTime(position);
    }

    // 시간 > 초 변환
    private int timeToSeconds(String time) {
        String[] parts = time.split(":");
        int minutes = Integer.parseInt(parts[0]);
        int seconds = Integer.parseInt(parts[1]);
        return minutes * 60 + seconds;
    }

    // 초 > 시간
    private String secondsToTime(int totalSeconds) {
        int minutes = totalSeconds / 60;
        int seconds = totalSeconds % 60;
        return String.format("%02d:%02d", minutes, seconds);
    }
}
