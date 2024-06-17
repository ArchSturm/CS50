#include "cs50.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, string argv[]) {
    // Make sure every character in argv[1] is a digit
    if (argc != 2) {
        printf("Usage: ./ceasar key\n");
        return 1;
    }
    for (int i = 0; argv[1][i] != '\0'; ++i) {
        if (isdigit(argv[1][i]) == 0) {
            printf("Usage: ./ceasar key\n");
            return 1;
        }
    }

    // Convert argv[1] from a `string` to an `int`
    int key = atoi(argv[1]);

    // Prompt user for plaintext
    string plaintext = get_string("plaintext: ");

    printf("ciphertext:  ");

    // For each character in the plaintext:
    for (int i = 0; plaintext[i] != '\0'; i++) {
        // Rotate the character if it's a letter
        if (isalpha(plaintext[i]) != 0) {
            if (isupper(plaintext[i])) {
                printf("%c", ((plaintext[i] - 'A' + key) % 26) + 'A');
            } else {
                printf("%c", ((plaintext[i] - 'a' + key) % 26) + 'a');
            }
        } else {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
    return 0;
}