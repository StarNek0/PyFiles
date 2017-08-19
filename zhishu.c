#include <cstdio>
int main() {
    int count = 1;
    int list[50] = {2};
    int num = 3;
    while (1) {
        if (count > 49)
            break;
        for (int i = 2; i < num; i++) {
            if (num % i == 0)
                break;
            if ((num % i != 0) && (i == num - 1))
                list[count++] = num;
        }
        num+=2;
    }
    for(int i=0;i<50;i++){
        printf("%d ", list[i]);
		if((i+1)%5==0)
			printf("\n");}
    printf("\n");
}
