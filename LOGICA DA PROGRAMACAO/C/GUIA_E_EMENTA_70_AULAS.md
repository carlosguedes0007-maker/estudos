<div align="center">

# 📖 Linguagem C, Alocação de Memória, Ponteiros & Sistemas - Ementa Completa (70+ Aulas) 🚀

**Trilha fundamental sobre a mãe das linguagens modernas: controle manual de memória, ponteiros, estruturas e chamadas POSIX.**

[![Status](https://img.shields.io/badge/Status-70%2B_Aulas_Concluídas-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Autor](https://img.shields.io/badge/Autor-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

## 🎯 Visão Geral da Trilha de Especialização

Este documento representa o plano pedagógico e técnico integral desta especialização dentro do hub **Estudos**. O conteúdo foi divido rigorosamente em **7 Módulos de Maestria Progressive**, totalizando **70 aulas detalhadas**, com códigos, fundamentos científicos, melhores práticas da indústria e desafios de engenharia.

---

## 📚 Índice de Módulos & Aulas

### 🔹 Módulo 1: Compilação, Sintaxe, Tipos Nativos e E/S Formatada (Aulas 01 a 10)
**Diretório de Aulas e Práticas:** `/Modulo_01_Fundamentos_e_Compilacao/`

- O processo de compilação C (Pré-processador, Compilador, Assembler, Linker)
- Anatomia da função main() e valores de retorno (0 vs códigos de erro)
- Tipos primitivos em C (int, char, float, double, short, long, unsigned)
- Operadores aritméticos, relacionais, lógicos e bit a bit (&, |, ^, ~, <<, >>)
- Saída formatada com printf() e especificadores de conversão (%d, %s, %f, %x)
- Entrada de dados segura com fgets() vs os perigos do scanf()
- Estruturas condicionais (if, else, switch/case)
- Laços de repetição em C (for, while, do-while)
- Constantes, macros (#define) e a diretiva #include
- Depuração básica e detecção de erros de sintaxe e aviso do compilador (-Wall)

### 🔹 Módulo 2: O Domínio dos Ponteiros e Endereços de Memória (Aulas 11 a 20)
**Diretório de Aulas e Práticas:** `/Modulo_02_Ponteiros_e_Memoria/`

- O que é memória RAM? Endereços hexadecimais e o operador &
- Conceito de Ponteiro (*): Variáveis que armazenam endereços de outras variáveis
- Desreferenciamento de ponteiros: Lendo e alterando valores indiretamente
- Aritmética de ponteiros (incremento, decremento e deslocamento em bytes)
- Ponteiros para ponteiros (**ptr) e matrizes multidimensionais
- Passagem de parâmetros por valor vs Passagem por referência em funções
- O ponteiro NULL e a prevenção de falhas de segmentação (Segmentation Fault)
- A relação íntima e indissolúvel entre Vetores (Arrays) e Ponteiros em C
- Ponteiros constantes vs Constantes apontadas por ponteiros (const int * vs int * const)
- Ponteiros de funções: Passando blocos de código como argumentos em C

### 🔹 Módulo 3: Vetores, Matrizes e Manipulação de Strings Nativas (Aulas 21 a 30)
**Diretório de Aulas e Práticas:** `/Modulo_03_Arrays_e_Strings/`

- Declaração, inicialização e limites de Vetores unidimensionais (Arrays)
- Matrizes bidimensionais e multidimensionais (Representação tabular em memória)
- O que é uma String em C? Vetores de caracteres terminados pelo caractere nulo (\0)
- Manipulação de strings da biblioteca <string.h>: strlen(), strcpy(), strncpy()
- Concatenação e comparação de strings: strcat(), strcmp(), strncmp()
- Busca em strings com strchr() e strstr()
- Formatando strings em buffers de memória com sprintf() e snprintf()
- Conversão de strings em números: atoi(), atof(), strtol(), strtod()
- Os perigos de Buffer Overflow na manipulação insegura de arrays de caracteres
- Construindo uma biblioteca própria de manipulação de strings 100% segura

### 🔹 Módulo 4: Alocação Dinâmica de Memória e Gestão do Heap (Aulas 31 a 40)
**Diretório de Aulas e Práticas:** `/Modulo_04_Alocacao_Dinamica/`

- Arquitetura de memória de um programa: Stack (Pilha) vs Heap (Monte)
- A função malloc(): Solicitando blocos brutos de memória em tempo de execução
- A função calloc(): Alocação contígua e zerada de vetores dinâmicos
- Redimensionamento dinâmico de blocos com realloc()
- A regra de ouro da gestão de memória: Para todo malloc, um free() obrigatório
- Vazamentos de memória (Memory Leaks) e auditoria técnica com Valgrind
- Ponteiros soltos (Dangling Pointers) e boas práticas de limpeza de referências
- Alocação dinâmica de matrizes bidimensionais no Heap
- Implementação manual de um vetor autodescritivo dinâmico (Estilo std::vector / ArrayList)
- Tratamento de falhas de esgotamento de memória (Quando o malloc retorna NULL)

### 🔹 Módulo 5: Estruturas (structs), Uniões, Enumerações e Arquivos (Aulas 41 a 50)
**Diretório de Aulas e Práticas:** `/Modulo_05_Estruturas_e_Tipos/`

- Criando tipos de dados compostos com struct
- Acesso a campos de estruturas (. vs operador seta -> em ponteiros de structs)
- Aninhamento de estruturas e vetores dentro de structs
- Simplificando declarações com typedef
- O que é uma union? Compartilhando o mesmo endereço de memória entre múltiplos tipos
- Enumerações com enum para definição de estados legíveis
- Manipulação de arquivos em C via FILE*: fopen(), fclose() e modos de abertura
- Leitura e gravação sequencial de texto com fprintf(), fscanf(), fputs(), fgets()
- Leitura e gravação de blocos binários puros com fread() e fwrite()
- Posicionamento aleatório em arquivos com fseek(), ftell() e rewind()

### 🔹 Módulo 6: Estruturas de Dados Avançadas em C Puro (Aulas 51 a 60)
**Diretório de Aulas e Práticas:** `/Modulo_06_Estruturas_de_Dados_em_C/`

- A necessidade de estruturas encadeadas vs Arrays estáticos
- Implementação do nó fundamental (Node) com autorreferência
- Lista Encadeada Simples (Singly Linked List): Inserção no início e no fim
- Busca, remoção e percurso em Listas Encadeadas
- Listas Duplamente Encadeadas (Doubly Linked List): Navegação bidirecional
- Implementação de uma Pilha LIFO (Stack) dinâmica em C
- Implementação de uma Fila FIFO (Queue) dinâmica em C
- Introdução a Árvores Binárias de Busca (BST - Binary Search Tree)
- Tabelas Hash (Hash Tables) básicas em C com resolução de colisões por encadeamento
- Por que o conhecimento de estruturas em C é o alicerce para todos os softwares modernos?

### 🔹 Módulo 7: Maestria em C - Programação de Sistemas e Automação (Aulas 61 a 70)
**Diretório de Aulas e Práticas:** `/Modulo_07_Projetos_Sistemas_e_Maestria/`

- Interação com o Sistema Operacional via chamadas POSIX e variáveis de ambiente
- Processamento de argumentos de terminal avançados (argc, argv e getopt)
- Criação e execução de subprocessos básicos com fork() e exec() (Visão Linux)
- Comunicação entre processos com Pipes (pipe)
- Otimização extrema de código em C e sinalizações de compilação -O2 / -O3
- Arquitetura de um sistema de banco de dados em memória gerido por ponteiros em C
- Desenvolvendo um analisador e interpretador de comandos em linha (Mini Shell)
- Construindo uma ferramenta de diagnóstico de portas e rede ultrarrápida em C puro
- Escrita de testes de verificação e asserções nativas com o cabeçalho <assert.h>
- Projeto Final: O Gerenciador de Acervo e Diagnóstico de Memória em C Puro Carlos Guedes

---

<div align="center">
  <p>💡 <i>"O estudo metódico, aliado à prática contínua, é o caminho indiscutível para a maestria em engenharia de software."</i></p>
  <p><b>Desenvolvido com precisão tecnológica por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> ❤️🚀</b></p>
</div>
