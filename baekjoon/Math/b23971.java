// 23971번 브론즈3 ZOAC4

/*
문제
https://www.acmicpc.net/problem/23971

입력
H, W, N, M이 공백으로 구분되어 주어진다. (0 < H, W, N, M ≤ 50,000)

출력
강의실이 수용할 수 있는 최대 인원 수를 출력한다.

예제 입력 1
5 4 1 1
예제 출력 1
6
*  */

package baekjoon.Math;

import java.io.*;
import java.util.*;

public class b23971 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int height = (h-1)/(n+1)+1;
        int width = (w-1)/(m+1)+1;

        System.out.println(height * width);
    }
}
