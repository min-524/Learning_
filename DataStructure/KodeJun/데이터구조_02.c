// 수행시간 측정
#include <stdio.h>
#include <time.h>   // clock() <-- 호출할 때의 clock cnt
                    // S <-- clock (100),, E <-- clock (2000)
                    // 2000 - 100 = 1900
int main()
{
    clock_t start_time, end_time; // int, char 과 같은 자료형

    start_time = clock();

    // duration -- clock cnt
    // duration / CLOCKS_PER_SEC --> 초 
    // Work
    
    int i;
    double k = 0.0;

    for(i = 1; i < 1000000; i++)
    {
        k = (k*k*k*k) / (double)i;
    }
    

    end_time = clock();

    printf("%d \n", end_time - start_time);

    return 0;
}
