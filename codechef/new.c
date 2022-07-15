int solve(int t, int n, int sumN){
    if(n==sumN){
        return pow(n,2);
    }else if(sumN > n*t){
        return t*(pow(n,2));
    }
    int aproaching_sum = 0;
    int ans = 0;
    for(int i =0; i<t; i++){
        if(aproaching_sum +n > sumN){
            ans += pow((sumN - aproaching_sum), 2);
            break;
        }else{
            ans += pow(n, 2);
        }
        aproaching_sum += n;
    }
    return ans
}