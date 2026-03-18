public class exercicio1 {

    public int[] numeros = {10,20};

    public exercicio1() {
        int soma = 0;
        for(int i = 0; i < numeros.length; i++) {
            soma+=numeros[i];
        }
        System.out.println(soma);
    }

    public static void main(String[] args) {
        new exercicio1();
    }
}
