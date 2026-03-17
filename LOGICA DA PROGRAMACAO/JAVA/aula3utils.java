public class aula3utils {
    public int idade = 26;
    public double peso = 80.5;
    public float peso2 = 80.5f;
    public String nome = "João";

    public aula3utils(double peso, String nome) {
        this.peso = peso;
        this.nome = nome;
        System.out.println(this.nome);
        System.out.println(nome);
    }
    

    public int pegaIdade() {
        return idade;
    }
}
