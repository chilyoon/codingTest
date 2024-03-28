// 2292번 브론즈2 벌집

/*
문제
https://www.acmicpc.net/problem/2292

입력
첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

출력
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

예제 입력 1 
13
예제 출력 1 
3
-> 범위 계산 잘하기
*/

package baekjoon.Math;

import java.io.*;
import java.util.*;

public class b2292 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int num = Integer.parseInt(bf.readLine());
        int room = 6;
        if (num == 1) {
            System.out.println(1);
        }
        else {
            int cnt = 1;
            long s = 0;
            long e = 6;
            num--;
            while (true) {
//                System.out.println(1+(room*(cnt-1)));
//                System.out.println(1+(room*cnt));
                if (s < num && e >= num) {
                    System.out.println(cnt+1);
                    break;
                } else {
                    s = e;
                    e += (room * ++cnt);
                }
            }
        }
    }
}
