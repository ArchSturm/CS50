#include "cs50.h"
#include <stdio.h>

int get_card_length(long card);
int get_checksum(long card, int length);
string which_card(long card, int length);

int main() {
    long card = get_long("Number: ");
    int length = get_card_length(card);

    if ((get_checksum(card, length)) == 0) {
        printf("%s", which_card(card, length));
    } else {
        printf("INVALID\n");
    }
}

int get_card_length(long card) {
    int count = 0;
    while (card > 0) {
        ++count;
        card = card / 10;
    }
    return count;
}

int get_checksum(long card, int length) {
    int sum = 0;
    for (int i = 0; i < length; ++i) {
        int last = card % 10;
        card = (card - last) / 10;
        if ((i % 2) == 0) {
            sum += last;
        } else {
            last = last * 2;
            if (last > 9) {
                sum += ((last % 10) + 1);
            } else {
                sum += last;
            }
        }
    }
    return (sum % 10);
}

string which_card(long card, int length) {
    if (length == 13) {
        card = card / 1000000000000;
        if (card == 4) {
            return "VISA\n";
        } else {
            return "INVALID\n";
        }
    } else if (length == 15) {
        card = card / 10000000000000;
        if ((card == 34) || (card == 37)) {
            return "AMEX\n";
        } else {
            return "INVALID\n";
        }
    } else if (length == 16) {
        card = card / 100000000000000;
        if ((card > 50) && (card < 56)) {
            return "MASTERCARD\n";
        } else if ((card / 10) == 4) {
            return "VISA\n";
        } else {
            return "INVALID\n";
        }
    } else {
        return "INVALID\n";
    }
}
