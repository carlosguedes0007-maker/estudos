/*manipulando tempo e segundos com if,else - parte 2*/

import java.util.Scanner;

public class exercicio3{

    public int[] numeros = {10,20,30};
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        double tempoAntigo = System.currentTimeMillis();
        String s = scanner.nextLine();
        

        if (exercicio3.convertTime(System.currentTimeMillis() - tempoAntigo) >= 2) {
            if(s.length() > 10) {
                System.out.println(s);
            }
            else {
                System.out.println("A string deve conter mais de 10 caracteres.");
            }
        }
        else{
            System.out.println("O tempo deve ser maior que 2 segundos.");
            tempoAntigo = System.currentTimeMillis();
            s = scanner.nextLine();
            if (exercicio3.convertTime(System.currentTimeMillis() - tempoAntigo) >= 2) {
                System.out.println("O tempo agora é maior que 2 segundos.");
            }
            else {
                System.out.println("O tempo ainda é menor que 2 segundos.");
            }
        }
    }

    public static double convertTime(double tempo) {
        return tempo / 1000;
    }
}