#include "cs50.h"
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void) {
    // Prompt the user for some text
    string text = get_string("Text: ");
    int letters;
    int words;
    int sentences;

    // Count the number of letters, words, and sentences in the text
    letters = count_letters(text);
    if (letters == 0) {
        words = 0;
        sentences = 0;
    } else {
        words = count_words(text);
        sentences = count_sentences(text);
    }

    // Compute the Coleman-Liau index
    float l = (letters / (float)words) * 100;
    float s = (sentences / (float)words) * 100;
    float index = 0.0588 * l - 0.296 * s - 15.8;
    int grade = (int)round(index);

    // Print the grade level
    if (grade < 1) {
        printf("Before Grade 1\n");
    } else if (grade >= 16) {
        printf("Grade 16+\n");
    } else {
        printf("Grade %i\n", grade);
    }
    return 0;
}

int count_letters(string text) {
    // Return the number of letters in text
    int num_letters = 0;
    for (int i = 0; text[i] != '\0'; ++i) {
        if (isalpha(text[i]) != 0) {
            ++num_letters;
        }
    }
    printf("\nl = %i\n", num_letters);
    return num_letters;
}

int count_words(string text) {
    // Return the number of words in text
    int num_words = 1;
    for (int i = 0, last = '\0'; text[i] != '\0'; ++i) {
        if ((text[i] == ' ') && (last != text[i])) {
            ++num_words;
        }
        last = text[i];
    }
    printf("w = %i\n", num_words);
    return num_words;
}

int count_sentences(string text) {
    // Return the number of sentences in text
    int num_sentences = 0;
    for (int i = 0; text[i] != '\0'; ++i) {
        if ((text[i] == '.') || (text[i] == '!') || (text[i] == '?')) {
            ++num_sentences;
        }
    }
    printf("s = %i\n", num_sentences);
    return num_sentences;
}