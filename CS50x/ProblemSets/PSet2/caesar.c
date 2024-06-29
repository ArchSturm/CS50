#include "cs50.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

bool only_digits(string s);
char rotate(char c, int n);

int main(int argc, string argv[]) {
    // Make sure every character in argv[1] is a digit
    if (argc != 2) {
        printf("Usage: ./ceasar key\n");
        return 1;
    }
    if (only_digits(argv[1]) == false) {
        printf("Usage: ./ceasar key\n");
        return 1;
    }

    // Convert argv[1] from a `string` to an `int`
    int key = atoi(argv[1]);

    // Prompt user for plaintext
    string plaintext = get_string("plaintext:  ");

    printf("ciphertext: ");

    // For each character in the plaintext:
    for (int i = 0; plaintext[i] != '\0'; i++) {
        // Rotate the character if it's a letter
        printf("%c", rotate(plaintext[i], key));
    }
    printf("\n");

    return 0;
}

bool only_digits(string s) {
    for (int i = 0; s[i] != '\0'; ++i) {
        if (isdigit(s[i]) == 0) {
            return false;
        }
    }
    return true;
}

char rotate(char c, int k) {
    if (isalpha(c) != 0) {
        if (isupper(c)) {
            return (((c - 'A' + k) % 26) + 'A');
        } else {
            return (((c - 'a' + k) % 26) + 'a');
        }
    } else {
        return c;
    }
}
