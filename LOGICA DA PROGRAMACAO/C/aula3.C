int main () {
    int hora_cinema = 20;
    int hora_atual = 20
    if (hora_atual > hora_cinema + 30) {
        printf("Passou to tempo limite, nao pode entrar\n");

    } else if(hora_atual < hora_cinema - 30) {
        printf("Ainda falta muito tempo, nao pode entrar\n");
    } else {
        printf("Pode entrar\n");
    }
    return 0;
}