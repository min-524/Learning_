#include <stdio.h>

power(x, n){
    if(n=0) return 1;
    else return power(x, n-1);
}

p(x, n){
    // 탈출 조건
    if(n==0) return 1;
    // 1. 지속 조건
    if(n%2==0) return p(x, n/2);
    // 2. 지속 조건
    if(n%2==1) return p(x*x, (n-1)/2);
}

int main(){
    // non-recursive 
    int x = 2, result = 1;
    for(int i=1; i<=3; i++){
        result = result * x ;
    }
    
}
