#include <stdio.h>
#include <string.h>

// Aula 7 - Pedra, Papel e Tesoura

int main() {
    char player1[256];
    char player2[256];

    printf("Player 1... Sua vez: \n");
    scanf("%s", player1);
    printf("Player 2... Sua vez: \n");
    scanf("%s", player2);


//PLAYER 1
    if(strcmp(player1,"papel") == 0) {
        printf("Player 1 jogou papel");
    }
    else if(strcmp(player1,"pedra") == 0) {
        printf("Player 1 jogou pedra");
    }
    else if(strcmp(player1,"tesoura") == 0) {
        printf("Player 1 jogou tesoura");
    }
    else {
        printf("Jogada inválida");

//PLAYER 2
    }
    if(strcmp(player2,"papel") == 0) {
        printf("\nPlayer 2 jogou papel");
    }
    else if(strcmp(player2,"pedra") == 0) {
        printf("\nPlayer 2 jogou pedra");
    }
    else if(strcmp(player2,"tesoura") == 0) {
        printf("\nPlayer 2 jogou tesoura");
    }
    else {
        printf("\nJogada inválida");
    }

//RESULTADO
    if(strcmp(player1, player2) == 0) {
        printf("\nEmpate!");
    }
    else if((strcmp(player1,"papel") == 0 && strcmp(player2,"pedra") == 0) || (strcmp(player1,"pedra") == 0 && strcmp(player2,"tesoura") == 0) || (strcmp(player1,"tesoura") == 0 && strcmp(player2,"papel") == 0)) {
        printf("\nPlayer 1 venceu!");
    }
    else {
        printf("\nPlayer 2 venceu!");
    }
    return 0;
}