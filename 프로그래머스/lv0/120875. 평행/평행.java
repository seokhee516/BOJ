class Solution {
    public double findSlope(int[] dot1, int[] dot2){
        return (double) (dot2[1] - dot1[1]) / (dot2[0] -dot1[0]);
    }
    public int solution(int[][] dots) {
        int answer = 0;
        if (findSlope(dots[0],dots[1]) == findSlope(dots[2],dots[3])){
            return 1;
        }
        if (findSlope(dots[0],dots[2]) == findSlope(dots[1],dots[3])){
            return 1;
        }
        if (findSlope(dots[0],dots[3]) == findSlope(dots[1],dots[2])){
            return 1;
        }
        return answer;
    }
}