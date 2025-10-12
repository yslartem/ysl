#include <stdio.h>

int main() {
    int m, n;
    printf("Введите m & n: ");
    scanf("%d%d", &m, &n);
    if ( m > n ) {
        printf("Number %d > %d", m, n);
    } else if (m < n) {
        printf("Number %d < %d", m, n);
    } else {
        printf("The numbers are equal", m, n);
    }
}