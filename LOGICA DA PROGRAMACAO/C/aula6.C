#include <stdio.h>
#include <stdlib.h>

int main() {
    
    char nome[256];
    int idade;

    printf("Qual o seu nome? \n");
    scanf("%s", &nome);

    printf("Qual a sua idade? \n");
    scanf("%d", &idade);

    printf("O seu nome é %s e a sua idade é %d", nome, idade);

    printf("\nAguarde enquanto lemos seus dados...\n");

    printf("A primeira letra do seu nome é %c", nome[0]);

    if(idade >= 18) {
        printf("\nVocê é maior de idade.");
    } else {
        printf("\nVocê é menor de idade.");
    }
    return 0;
}
