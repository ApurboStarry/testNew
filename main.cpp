#include <cstdio>

int main() {
    int N;
    scanf("%d\n", &N);
    char x[110];
    while(N--) {
        scanf("0.%[0-9]...\n", &x);
        printf("0.%s\n", x);
    }

    return 0;
}