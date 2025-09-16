#include <stdio.h>

int main() {
    int a, b;
    printf("Введите число a: ");
    scanf("%d", &a);
    printf("Введите число b: ");
    scanf("%d", &b);
    if (a != 0 && b % a == 0) {
        printf("%d — делитель %d\n", a, b);
    } else {
        printf("%d не делится на %d\n", b, a);
    }
}