public class Aula4 extends aula4utils {
    
    


    public Aula4(double peso, String nome) {
        super(peso, nome);

        //TODO Auto-generated constructor stub
    }

    public static void main(String[] args) {
        Aula4 aula4 = new Aula4(75.5, "Carlos");
        aula4.pegaIdade();

    }

    class Teste {
        public void print() {
            System.out.println("OKAY!!!");
        }
    }
}

