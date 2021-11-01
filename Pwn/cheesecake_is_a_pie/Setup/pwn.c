#include <stdio.h>
#include <stdlib.h>

char cheesecake[] = "I LOVE CHEESECAKE!!";

volatile void flag() {
    FILE * file;
    file = fopen("flag.txt", "r");
    char flag[100] = {0};

    if(file == NULL) {
        puts("Hurry up and try it on the remote machine!");
        exit(0x69);
    }

    fread(flag, 1, 100, file);
    puts("Your reward for believing that Cheesecake is a kind of PIE!!!");
    puts(flag);
    exit(69);
}


void vuln() {
    char buf[8] = {0};

    puts("First of all, Cheesecake is a kind of PIE!");
    puts("And here is the proof!!");
    printf("%p\n", cheesecake);
    puts("Whats your favorite type of PIE?");
    printf("> ");

    fgets(buf, 33, stdin);
}

int main() { 
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    fflush(stdout);


    vuln();
    exit(69);
}