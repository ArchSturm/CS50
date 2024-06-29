#include "cs50.h"
#include <stdio.h>

int calculate_coins(int cents);

int main(void) {
    int cents;

    do {
        cents = get_int("Change owed: ");
    } while (cents < 0);

    printf("%i", calculate_coins(cents));
}

int calculate_coins(int cents) {
    int coins = 0;
    int aux = 0;

    if (cents >= 25) {
        aux = cents / 25;
        cents = cents - (aux * 25);
        coins += aux;
    }
    if (cents >= 10) {
        aux = cents / 10;
        cents = cents - (aux * 10);
        coins += aux;
    }
    if (cents >= 5) {
        ++coins;
        cents -= 5;
    }
    return (coins + cents);
}