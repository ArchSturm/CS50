#include <cs50.h>
#include <stdio.h>

int main() {
    int height = 0;

    do {
        height = get_int("Height: ");
    } while ((height <= 0) || (height > 8));

    for (int i = 1; i <= height; ++i) {
        for (int j = 0; j < (height - i); ++j) {
            printf(" ");
        }
        for (int j = (height - i); j < height; ++j) {
            printf("#");
        }
        printf("  ");
        for (int j = (height - i); j < height; ++j) {
            printf("#");
        }
        printf("\n");
    }
}
