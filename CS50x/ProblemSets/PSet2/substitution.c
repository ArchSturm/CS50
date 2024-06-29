#include "cs50.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_alpha(string s);
bool only_uniques(string s);
char substitute(char c, string s);

int main(int argc, string argv[]) {
    // Make sure every character in argv[1] is a digit
    if (argc != 2) {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    if (strlen(argv[1]) != 26) {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    if (only_alpha(argv[1]) == false) {
        printf("Key must only contain alphabetic characters.\n");
        return 1;
    }
    if (only_uniques(argv[1]) == false) {
        printf("Key must not contain repeated characters.\n");
        return 1;
    }

    // Prompt user for plaintext
    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");

    // For each character in the plaintext:
    for (int i = 0; plaintext[i] != '\0'; i++) {
        // Substitute the character if it's a letter
        printf("%c", substitute(plaintext[i], argv[1]));
    }
    printf("\n");

    return 0;
}

bool only_alpha(string s) {
    for (int i = 0; s[i] != '\0'; ++i) {
        if (isalpha(s[i]) == 0) {
            return false;
        }
    }
    return true;
}

bool only_uniques(string s) {
    for (int i = 0; s[i] != '\0'; ++i) {
        for (int j = i + 1; s[j] != '\0'; ++j) {
            if (s[i] == s[j]) {
                return false;
            }
        }
    }
    return true;
}

char substitute(char c, string s) {
    if (isalpha(c) != 0) {
        if (isupper(c)) {
            return toupper(s[(c - 'A')]);
        } else {
            return tolower(s[(c - 'a')]);
        }
    } else {
        return c;
    }
}