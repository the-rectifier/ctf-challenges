#include <stdio.h>

int main(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    
    char gift[32];

    printf("Hello, your gift code is:\n"
    "%lld\n"
    "Use it wisely!\n", gift);

    puts("What would you like to buy using the gift code?");
    gets(gift);

    return 0;
}