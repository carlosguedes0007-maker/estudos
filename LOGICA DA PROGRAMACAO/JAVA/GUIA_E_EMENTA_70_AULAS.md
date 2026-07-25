<div align="center">

# 📖 Java 21+, POO, Coleções, Streams & Arquitetura Corporativa - Ementa Completa (70+ Aulas) 🚀

**Trilha robusta sobre a linguagem líder empresarial: Orientação a Objetos profunda, Java Collections, Streams API e Padrões de Projeto.**

[![Status](https://img.shields.io/badge/Status-70%2B_Aulas_Concluídas-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Autor](https://img.shields.io/badge/Autor-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

## 🎯 Visão Geral da Trilha de Especialização

Este documento representa o plano pedagógico e técnico integral desta especialização dentro do hub **Estudos**. O conteúdo foi divido rigorosamente em **7 Módulos de Maestria Progressive**, totalizando **70 aulas detalhadas**, com códigos, fundamentos científicos, melhores práticas da indústria e desafios de engenharia.

---

## 📚 Índice de Módulos & Aulas

### 🔹 Módulo 1: O Ecossistema Java, JVM, Tipos e Operadores (Aulas 01 a 10)
**Diretório de Aulas e Práticas:** `/Modulo_01_Fundamentos_e_Sintaxe_Java/`

- A arquitetura Java: JDK, JRE, JVM e o bytecode independente de plataforma
- Estrutura básica de uma classe Java e o método public static void main
- Tipos primitivos (byte, short, int, long, float, double, boolean, char) vs Classes Wrappers
- Declaração de variáveis, constantes (final) e inferência de tipos com 'var' (Java 10+)
- Operadores aritméticos, relacionais, lógicos e o operador condicional ternário
- Conversão de tipos (Casting implícito e explícito) em precisões numéricas
- Estruturas de controle de fluxo (if, else if, else)
- A estrutura switch moderna com Switch Expressions e Yield (Java 14+)
- Laços de repetição (for tradicional, enhanced for-each, while, do-while)
- A classe String em Java: Imutabilidade, Pool de Strings e métodos principais

### 🔹 Módulo 2: Orientação a Objetos no Padrão de Ouro (Aulas 11 a 20)
**Diretório de Aulas e Práticas:** `/Modulo_02_Orientacao_a_Objetos_Profunda/`

- Conceito de Classe vs Instância de Objeto na JVM
- O construtor da classe, sobrecarga de construtores (Overloading) e a palavra-chave 'this'
- Encapsulamento corporativo: Modificadores de acesso (private, default/package, protected, public)
- Atributos e métodos estáticos (static): Compartilhamento no escopo da classe
- Herança de classes com a palavra-chave 'extends' e chamada a construtores com 'super()'
- Sobrescrita de métodos (Overriding) e a anotação @Override
- Polimorfismo de inclusão: Referências genéricas acionando comportamentos específicos
- Classes Abstratas e Métodos Abstratos (abstract): Definindo esqueletos de negócio
- Interfaces Java (interface): Contratos de comportamento, métodos default e estáticos
- Records em Java (Java 16+): Criando classes de transporte de dados imutáveis automáticas (DTOs)

### 🔹 Módulo 3: Java Collections Framework e Generics (Aulas 21 a 30)
**Diretório de Aulas e Práticas:** `/Modulo_03_Colecoes_e_Generics/`

- Introdução aos Generics (<T>): Tipagem segura em tempo de compilação em Java
- A hierarquia de Coleções: A interface Collection e suas sub-interfaces principais
- Trabalhando com Listas dinâmicas: ArrayList vs LinkedList (Quando usar cada uma?)
- Conjuntos sem duplicatas: A interface Set com HashSet, LinkedHashSet e TreeSet
- Mapeamento Chave-Valor: A interface Map com HashMap, LinkedHashMap e TreeMap
- Iteração segura com Iterator e ListIterator vs Laços for-each
- Ordenação de coleções com as interfaces Comparable e Comparator
- Estruturas de fila e pilha no Java: Queue, Deque e ArrayDeque
- A classe utilitária Collections (sort, reverse, shuffle, unmodifiableList)
- Boas práticas corporativas no uso de Coleções Java e prevenção de NullPointerException

### 🔹 Módulo 4: Programação Funcional, Lambdas e Streams API (Aulas 31 a 40)
**Diretório de Aulas e Práticas:** `/Modulo_04_Programacao_Funcional_e_Streams/`

- Evolução do Java: Interfaces Funcionais e a anotação @FunctionalInterface
- Expressões Lambda (->) em Java: Escrevendo código anônimo, conciso e elegante
- Interfaces funcionais nativas (Predicate<T>, Function<T, R>, Consumer<T>, Supplier<T>)
- Method References (::) - Referenciando métodos estáticos e de instância com elegância
- O que é a Streams API (java.util.stream)? Processamento de dados de forma declarativa
- Operações intermediárias de transformação: map(), filter(), flatMap(), sorted(), distinct()
- Operações terminais de consolidação: forEach(), collect(), count(), reduce()
- Agrupando e sumarizando dados com Collectors (toList, groupingBy, joining)
- Optional<T> em Java: Eliminando para sempre o fantasma do NullPointerException
- Streams paralelas (parallelStream): Processamento multicore em grandes coleções

### 🔹 Módulo 5: Tratamento de Exceções, I/O Moderno (NIO.2) e Recursos (Aulas 41 a 50)
**Diretório de Aulas e Práticas:** `/Modulo_05_Excecoes_e_Manipulacao_de_Arquivos/`

- A hierarquia de exceções da JVM: Throwable, Exception, RuntimeException e Error
- Exceções Verificadas (Checked Exceptions) vs Não-Verificadas (Unchecked / Runtime)
- O bloco de tratamento try, catch, finally e o lançamento com throw / throws
- O gerenciamento automático de recursos com Try-with-Resources (AutoCloseable)
- Criando hierarquias de exceções de negócio personalizadas para o ERP / Sistemas
- Introdução a entrada e saída de dados com Java I/O (InputStream, OutputStream, Reader, Writer)
- Java NIO.2 (java.nio.file): As classes modernas Path, Paths e Files
- Leitura e gravação de arquivos texto e linhas completas com uma única chamada NIO.2
- Manipulação de diretórios, verificação de existência e cópia com Files
- Serialização e desserialização de objetos Java (Serializable e serialVersionUID)

### 🔹 Módulo 6: Concorrência (Threads) e Padrões de Projeto Gang of Four (Aulas 51 a 60)
**Diretório de Aulas e Práticas:** `/Modulo_06_Concorrencia_e_Padroes_de_Projeto/`

- Introdução à concorrência no Java: Ciclo de vida de uma Thread e a interface Runnable
- Sincronização de métodos e blocos com a palavra-chave 'synchronized'
- O pacote java.util.concurrent: ExecutorService e Thread Pools para alta performance
- Tarefas assíncronas com retorno de dados usando Callable<V> e Future<V>
- Padrões de Criação 1: Singleton (Instância única) e Builder (Construção fluida de objetos)
- Padrões de Criação 2: Factory Method e Abstract Factory para criação desacoplada
- Padrões de Estrutura: Adapter (Adaptando interfaces) e Decorator (Adicionando comportamentos dinâmicos)
- Padrões de Comportamento 1: Strategy (Algoritmos intercambiáveis) e Observer (Notificação de eventos)
- Padrões de Comportamento 2: Repository / DAO (Isolamento do acesso ao banco de dados)
- Injeção de Dependências (DI) e Inversão de Controle (IoC): Os pilares do Spring Framework

### 🔹 Módulo 7: Maestria em Java - Arquitetura de Sistema Corporativo (Aulas 61 a 70)
**Diretório de Aulas e Práticas:** `/Modulo_07_Projetos_Reais_e_Maestria_Java/`

- Modelagem orientada a domínios (DDD) para o ecossistema literário do Carlos Guedes
- Implementação do modelo do Domínio Literário (Livros, Leitores, Empréstimos) usando Records e POO
- Desenvolvimento do Padrão Repository / DAO em memória com Java Collections e Streams
- Implementação de regras de validação de negócios e tratamento customizado de exceções
- Construção de uma interface de linha de comando (CLI) interativa com menus e relatórios
- Geração de relatórios analíticos complexos (Livros mais emprestados, Atrasos) via Streams API
- Persistência automática dos dados do sistema em arquivos locais no formato JSON/Texto via NIO.2
- Auditoria de desempenho e uso de memória da JVM durante o processamento do acervo
- Escrita de testes unitários automatizados profissionais com JUnit 5 (Assertions e Testes de Exceção)
- Projeto Final: O Sistema ERP Biblioteca Corporativo Core (Engine 100% em Java 21) Carlos Guedes

---

<div align="center">
  <p>💡 <i>"O estudo metódico, aliado à prática contínua, é o caminho indiscutível para a maestria em engenharia de software."</i></p>
  <p><b>Desenvolvido com precisão tecnológica por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> ❤️🚀</b></p>
</div>
