// 5073번 브론즈3 삼각형과 세 변

/*
문제
https://www.acmicpc.net/problem/5073

입력
각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.

출력
각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.

예제 입력 1
7 7 7
6 5 4
3 2 5
6 2 6
0 0 0
예제 출력 1
Equilateral
Scalene
Invalid
Isosceles
*/

package baekjoon.Math;

import java.io.*;
import java.util.*;

public class b5073 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[3];

//      Equilateral :  세 변의 길이가 모두 같은 경우
//      Isosceles : 두 변의 길이만 같은 경우
//      Scalene : 세 변의 길이가 모두 다른 경우

        while (true) {
            StringTokenizer st = new StringTokenizer(bf.readLine());

            arr[0] = Integer.parseInt(st.nextToken());
            arr[1] = Integer.parseInt(st.nextToken());
            arr[2] = Integer.parseInt(st.nextToken());
            if (arr[0] == 0 && arr[1] == 0 && arr[2] == 0) break;

            Arrays.sort(arr);
            if (arr[2] >= arr[0] + arr[1]) {
                System.out.println("Invalid");
            } else if (arr[0] == arr[1] && arr[1] == arr[2]) {
                System.out.println("Equilateral");
            } else if (arr[0] == arr[1] || arr[1] == arr[2] || arr[2] == arr[0]) {
                System.out.println("Isosceles");
            } else {
                System.out.println("Scalene");
            }
        }
    }
}
