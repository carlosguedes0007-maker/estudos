int main ()
{
    char nome[256];
    char sobrenome[256];
    int ano_nascimento;
    int idade;

    printf("Digite seu nome: \n");
    scanf("%s", nome);

    printf("Que legal, %s! Agora digite sua idade: \n", nome);
    scanf("%d", &idade);

    printf("Muito bom! O %d tem %d anos de idade. \n", nome, idade);
}