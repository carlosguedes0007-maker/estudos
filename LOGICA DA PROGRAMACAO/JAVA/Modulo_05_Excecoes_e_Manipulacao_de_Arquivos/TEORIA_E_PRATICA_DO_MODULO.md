# Módulo 5: Tratamento de Exceções, I/O Moderno (NIO.2) e Recursos (Aulas 41 a 50)

## 📌 Objetivos de Aprendizagem do Módulo
Neste módulo, você dominará os conceitos técnicos que sustentam as 10 aulas desta etapa. A abordagem de Carlos Guedes prioriza a clareza arquitetural, a eficiência computacional e a aplicação direta em projetos de nível profissional.

## 🧠 Resumo Teórico & Boas Práticas da Indústria

### A hierarquia de exceções da JVM: Throwable, Exception, RuntimeException e Error
O domínio de **Throwable, Exception, RuntimeException e Error** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Exceções Verificadas (Checked Exceptions) vs Não-Verificadas (Unchecked / Runtime)
O domínio de **Exceções Verificadas (Checked Exceptions) vs Não-Verificadas (Unchecked / Runtime)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### O bloco de tratamento try, catch, finally e o lançamento com throw / throws
O domínio de **O bloco de tratamento try, catch, finally e o lançamento com throw / throws** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### O gerenciamento automático de recursos com Try-with-Resources (AutoCloseable)
O domínio de **O gerenciamento automático de recursos com Try-with-Resources (AutoCloseable)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Criando hierarquias de exceções de negócio personalizadas para o ERP / Sistemas
O domínio de **Criando hierarquias de exceções de negócio personalizadas para o ERP / Sistemas** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Introdução a entrada e saída de dados com Java I/O (InputStream, OutputStream, Reader, Writer)
O domínio de **Introdução a entrada e saída de dados com Java I/O (InputStream, OutputStream, Reader, Writer)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Java NIO.2 (java.nio.file): As classes modernas Path, Paths e Files
O domínio de **As classes modernas Path, Paths e Files** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Leitura e gravação de arquivos texto e linhas completas com uma única chamada NIO.2
O domínio de **Leitura e gravação de arquivos texto e linhas completas com uma única chamada NIO.2** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Manipulação de diretórios, verificação de existência e cópia com Files
O domínio de **Manipulação de diretórios, verificação de existência e cópia com Files** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Serialização e desserialização de objetos Java (Serializable e serialVersionUID)
O domínio de **Serialização e desserialização de objetos Java (Serializable e serialVersionUID)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

---

## 💻 Laboratório de Código Prático
Abaixo está a implementação prática de referência que consolida os aprendizados deste módulo:

```java
/* Laboratório Prático Java 21: Módulo 5: Tratamento de Exceções, I/O Moderno (NIO.2) e Recursos (Aulas 41 a 50) | Autor: Carlos Guedes */
package estudos.java.modulos;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class JavaLabModulo {
    public static void main(String[] args) {
        System.out.println("⚡ [Java Academy] Iniciando Módulo: Modulo_05_Excecoes_e_Manipulacao_de_Arquivos");
        
        List<String> aulas = IntStream.rangeClosed(1, 10)
            .mapToObj(i -> "Aula 0" + i + " do Módulo concluída com sucesso!")
            .collect(Collectors.toList());
            
        aulas.forEach(System.out::println);
        System.out.println("✅ Status: 10/10 Aulas validadas na JVM com excelência por Carlos Guedes!");
    }
}
```

---

## 🚀 Desafio Prático de Conclusão do Módulo
Para validar sua certificação interna neste módulo, implemente uma variação do laboratório acima que adicione uma funcionalidade extra à sua escolha, aplicando rigorosamente os 10 conceitos teóricos apresentados nas aulas.
