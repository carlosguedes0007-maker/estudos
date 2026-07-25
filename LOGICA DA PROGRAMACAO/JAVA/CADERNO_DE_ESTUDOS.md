<div align="center">

# 📓 Java 21+, POO, Coleções, Streams & Arquitetura (Meu Caderno) - Meu Caderno de Anotações (70+ Tópicos) 🚀

**Minhas anotações sobre Orientação a Objetos avançada, Java Collections, Streams API, Records e Design Patterns.**

[![Status](https://img.shields.io/badge/Status-70%2B_Tópicos_Estudados-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Estudante](https://img.shields.io/badge/Estudante-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

## 🎯 Visão Geral dos Meus Estudos

Este documento organiza o meu caderno pessoal de anotações, resumos teóricos e experimentos de código nesta especialização dentro do meu repositório de **Estudos**. Estruturei meu aprendizado rigorosamente em **7 Módulos de Investigação**, totalizando **70 tópicos de estudo detalhados**, onde documentei a teoria, armadilhas comuns, macetes corporativos e desenvolvi códigos de laboratório para fixar cada conceito.

---

## 📚 Índice de Resumos & Experimentos

### 🔹 Módulo 1: O Ecossistema Java, JVM, Tipos e Operadores (Tópicos 01 a 10)
**Pasta de Resumos e Experimentos:** `/Modulo_01_Fundamentos_e_Sintaxe_Java/`

- 📌 Tópico 01: A arquitetura Java: JDK, JRE, JVM e o bytecode independente de plataforma
- 📌 Tópico 02: Estrutura básica de uma classe Java e o método public static void main
- 📌 Tópico 03: Tipos primitivos (byte, short, int, long, float, double, boolean, char) vs Classes Wrappers
- 📌 Tópico 04: Declaração de variáveis, constantes (final) e inferência de tipos com 'var' (Java 10+)
- 📌 Tópico 05: Operadores aritméticos, relacionais, lógicos e o operador condicional ternário
- 📌 Tópico 06: Conversão de tipos (Casting implícito e explícito) em precisões numéricas
- 📌 Tópico 07: Estruturas de controle de fluxo (if, else if, else)
- 📌 Tópico 08: A estrutura switch moderna com Switch Expressions e Yield (Java 14+)
- 📌 Tópico 09: Laços de repetição (for tradicional, enhanced for-each, while, do-while)
- 📌 Tópico 10: A classe String em Java: Imutabilidade, Pool de Strings e métodos principais

### 🔹 Módulo 2: Orientação a Objetos no Padrão de Ouro (Tópicos 11 a 20)
**Pasta de Resumos e Experimentos:** `/Modulo_02_Orientacao_a_Objetos_Profunda/`

- 📌 Tópico 01: Conceito de Classe vs Instância de Objeto na JVM
- 📌 Tópico 02: O construtor da classe, sobrecarga de construtores (Overloading) e a palavra-chave 'this'
- 📌 Tópico 03: Encapsulamento corporativo: Modificadores de acesso (private, default/package, protected, public)
- 📌 Tópico 04: Atributos e métodos estáticos (static): Compartilhamento no escopo da classe
- 📌 Tópico 05: Herança de classes com a palavra-chave 'extends' e chamada a construtores com 'super()'
- 📌 Tópico 06: Sobrescrita de métodos (Overriding) e a anotação @Override
- 📌 Tópico 07: Polimorfismo de inclusão: Referências genéricas acionando comportamentos específicos
- 📌 Tópico 08: Classes Abstratas e Métodos Abstratos (abstract): Definindo esqueletos de negócio
- 📌 Tópico 09: Interfaces Java (interface): Contratos de comportamento, métodos default e estáticos
- 📌 Tópico 10: Records em Java (Java 16+): Criando classes de transporte de dados imutáveis automáticas (DTOs)

### 🔹 Módulo 3: Java Collections Framework e Generics (Tópicos 21 a 30)
**Pasta de Resumos e Experimentos:** `/Modulo_03_Colecoes_e_Generics/`

- 📌 Tópico 01: Introdução aos Generics (<T>): Tipagem segura em tempo de compilação em Java
- 📌 Tópico 02: A hierarquia de Coleções: A interface Collection e suas sub-interfaces principais
- 📌 Tópico 03: Trabalhando com Listas dinâmicas: ArrayList vs LinkedList (Quando usar cada uma?)
- 📌 Tópico 04: Conjuntos sem duplicatas: A interface Set com HashSet, LinkedHashSet e TreeSet
- 📌 Tópico 05: Mapeamento Chave-Valor: A interface Map com HashMap, LinkedHashMap e TreeMap
- 📌 Tópico 06: Iteração segura com Iterator e ListIterator vs Laços for-each
- 📌 Tópico 07: Ordenação de coleções com as interfaces Comparable e Comparator
- 📌 Tópico 08: Estruturas de fila e pilha no Java: Queue, Deque e ArrayDeque
- 📌 Tópico 09: A classe utilitária Collections (sort, reverse, shuffle, unmodifiableList)
- 📌 Tópico 10: Boas práticas corporativas no uso de Coleções Java e prevenção de NullPointerException

### 🔹 Módulo 4: Programação Funcional, Lambdas e Streams API (Tópicos 31 a 40)
**Pasta de Resumos e Experimentos:** `/Modulo_04_Programacao_Funcional_e_Streams/`

- 📌 Tópico 01: Evolução do Java: Interfaces Funcionais e a anotação @FunctionalInterface
- 📌 Tópico 02: Expressões Lambda (->) em Java: Escrevendo código anônimo, conciso e elegante
- 📌 Tópico 03: Interfaces funcionais nativas (Predicate<T>, Function<T, R>, Consumer<T>, Supplier<T>)
- 📌 Tópico 04: Method References (::) - Referenciando métodos estáticos e de instância com elegância
- 📌 Tópico 05: O que é a Streams API (java.util.stream)? Processamento de dados de forma declarativa
- 📌 Tópico 06: Operações intermediárias de transformação: map(), filter(), flatMap(), sorted(), distinct()
- 📌 Tópico 07: Operações terminais de consolidação: forEach(), collect(), count(), reduce()
- 📌 Tópico 08: Agrupando e sumarizando dados com Collectors (toList, groupingBy, joining)
- 📌 Tópico 09: Optional<T> em Java: Eliminando para sempre o fantasma do NullPointerException
- 📌 Tópico 10: Streams paralelas (parallelStream): Processamento multicore em grandes coleções

### 🔹 Módulo 5: Tratamento de Exceções, I/O Moderno (NIO.2) e Recursos (Tópicos 41 a 50)
**Pasta de Resumos e Experimentos:** `/Modulo_05_Excecoes_e_Manipulacao_de_Arquivos/`

- 📌 Tópico 01: A hierarquia de exceções da JVM: Throwable, Exception, RuntimeException e Error
- 📌 Tópico 02: Exceções Verificadas (Checked Exceptions) vs Não-Verificadas (Unchecked / Runtime)
- 📌 Tópico 03: O bloco de tratamento try, catch, finally e o lançamento com throw / throws
- 📌 Tópico 04: O gerenciamento automático de recursos com Try-with-Resources (AutoCloseable)
- 📌 Tópico 05: Criando hierarquias de exceções de negócio personalizadas para o ERP / Sistemas
- 📌 Tópico 06: Introdução a entrada e saída de dados com Java I/O (InputStream, OutputStream, Reader, Writer)
- 📌 Tópico 07: Java NIO.2 (java.nio.file): As classes modernas Path, Paths e Files
- 📌 Tópico 08: Leitura e gravação de arquivos texto e linhas completas com uma única chamada NIO.2
- 📌 Tópico 09: Manipulação de diretórios, verificação de existência e cópia com Files
- 📌 Tópico 10: Serialização e desserialização de objetos Java (Serializable e serialVersionUID)

### 🔹 Módulo 6: Concorrência (Threads) e Padrões de Projeto Gang of Four (Tópicos 51 a 60)
**Pasta de Resumos e Experimentos:** `/Modulo_06_Concorrencia_e_Padroes_de_Projeto/`

- 📌 Tópico 01: Introdução à concorrência no Java: Ciclo de vida de uma Thread e a interface Runnable
- 📌 Tópico 02: Sincronização de métodos e blocos com a palavra-chave 'synchronized'
- 📌 Tópico 03: O pacote java.util.concurrent: ExecutorService e Thread Pools para alta performance
- 📌 Tópico 04: Tarefas assíncronas com retorno de dados usando Callable<V> e Future<V>
- 📌 Tópico 05: Padrões de Criação 1: Singleton (Instância única) e Builder (Construção fluida de objetos)
- 📌 Tópico 06: Padrões de Criação 2: Factory Method e Abstract Factory para criação desacoplada
- 📌 Tópico 07: Padrões de Estrutura: Adapter (Adaptando interfaces) e Decorator (Adicionando comportamentos dinâmicos)
- 📌 Tópico 08: Padrões de Comportamento 1: Strategy (Algoritmos intercambiáveis) e Observer (Notificação de eventos)
- 📌 Tópico 09: Padrões de Comportamento 2: Repository / DAO (Isolamento do acesso ao banco de dados)
- 📌 Tópico 10: Injeção de Dependências (DI) e Inversão de Controle (IoC): Os pilares do Spring Framework

### 🔹 Módulo 7: Maestria em Java - Arquitetura de Sistema Corporativo (Tópicos 61 a 70)
**Pasta de Resumos e Experimentos:** `/Modulo_07_Projetos_Reais_e_Maestria_Java/`

- 📌 Tópico 01: Modelagem orientada a domínios (DDD) para o ecossistema literário do Carlos Guedes
- 📌 Tópico 02: Implementação do modelo do Domínio Literário (Livros, Leitores, Empréstimos) usando Records e POO
- 📌 Tópico 03: Desenvolvimento do Padrão Repository / DAO em memória com Java Collections e Streams
- 📌 Tópico 04: Implementação de regras de validação de negócios e tratamento customizado de exceções
- 📌 Tópico 05: Construção de uma interface de linha de comando (CLI) interativa com menus e relatórios
- 📌 Tópico 06: Geração de relatórios analíticos complexos (Livros mais emprestados, Atrasos) via Streams API
- 📌 Tópico 07: Persistência automática dos dados do sistema em arquivos locais no formato JSON/Texto via NIO.2
- 📌 Tópico 08: Auditoria de desempenho e uso de memória da JVM durante o processamento do acervo
- 📌 Tópico 09: Escrita de testes unitários automatizados profissionais com JUnit 5 (Assertions e Testes de Exceção)
- 📌 Tópico 10: Projeto Final: O Sistema ERP Biblioteca Corporativo Core (Engine 100% em Java 21) Carlos Guedes

---

<div align="center">
  <p>💡 <i>"A constância nos estudos e o teste diário no código são os verdadeiros segredos para evoluir na engenharia de software."</i></p>
  <p><b>Caderno e laboratório mantido por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> ❤️🚀</b></p>
</div>
