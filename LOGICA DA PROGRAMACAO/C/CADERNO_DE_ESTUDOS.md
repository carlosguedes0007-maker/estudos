<div align="center">

#  Linguagem C, Alocação de Memória, Ponteiros & Sistemas (Meus Resumos) - Meu Caderno de Anotações (70+ Tópicos) 

**Minhas investigações sobre controle manual de memória, ponteiros, structs, alocação dinâmica e chamadas POSIX.**

[![Status](https://img.shields.io/badge/Status-70%2B_Tópicos_Estudados-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Estudante](https://img.shields.io/badge/Estudante-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

##  Visão Geral dos Meus Estudos

Este documento organiza o meu caderno pessoal de anotações, resumos teóricos e experimentos de código nesta especialização dentro do meu repositório de **Estudos**. Estruturei meu aprendizado rigorosamente em **7 Módulos de Investigação**, totalizando **70 tópicos de estudo detalhados**, onde documentei a teoria, armadilhas comuns, macetes corporativos e desenvolvi códigos de laboratório para fixar cada conceito.

---

##  Índice de Resumos & Experimentos

###  Módulo 1: Compilação, Sintaxe, Tipos Nativos e E/S Formatada (Tópicos 01 a 10)
**Pasta de Resumos e Experimentos:** `/Modulo_01_Fundamentos_e_Compilacao/`

-  Tópico 01: O processo de compilação C (Pré-processador, Compilador, Assembler, Linker)
-  Tópico 02: Anatomia da função main() e valores de retorno (0 vs códigos de erro)
-  Tópico 03: Tipos primitivos em C (int, char, float, double, short, long, unsigned)
-  Tópico 04: Operadores aritméticos, relacionais, lógicos e bit a bit (&, |, ^, ~, <<, >>)
-  Tópico 05: Saída formatada com printf() e especificadores de conversão (%d, %s, %f, %x)
-  Tópico 06: Entrada de dados segura com fgets() vs os perigos do scanf()
-  Tópico 07: Estruturas condicionais (if, else, switch/case)
-  Tópico 08: Laços de repetição em C (for, while, do-while)
-  Tópico 09: Constantes, macros (#define) e a diretiva #include
-  Tópico 10: Depuração básica e detecção de erros de sintaxe e aviso do compilador (-Wall)

###  Módulo 2: O Domínio dos Ponteiros e Endereços de Memória (Tópicos 11 a 20)
**Pasta de Resumos e Experimentos:** `/Modulo_02_Ponteiros_e_Memoria/`

-  Tópico 01: O que é memória RAM? Endereços hexadecimais e o operador &
-  Tópico 02: Conceito de Ponteiro (*): Variáveis que armazenam endereços de outras variáveis
-  Tópico 03: Desreferenciamento de ponteiros: Lendo e alterando valores indiretamente
-  Tópico 04: Aritmética de ponteiros (incremento, decremento e deslocamento em bytes)
-  Tópico 05: Ponteiros para ponteiros (**ptr) e matrizes multidimensionais
-  Tópico 06: Passagem de parâmetros por valor vs Passagem por referência em funções
-  Tópico 07: O ponteiro NULL e a prevenção de falhas de segmentação (Segmentation Fault)
-  Tópico 08: A relação íntima e indissolúvel entre Vetores (Arrays) e Ponteiros em C
-  Tópico 09: Ponteiros constantes vs Constantes apontadas por ponteiros (const int * vs int * const)
-  Tópico 10: Ponteiros de funções: Passando blocos de código como argumentos em C

###  Módulo 3: Vetores, Matrizes e Manipulação de Strings Nativas (Tópicos 21 a 30)
**Pasta de Resumos e Experimentos:** `/Modulo_03_Arrays_e_Strings/`

-  Tópico 01: Declaração, inicialização e limites de Vetores unidimensionais (Arrays)
-  Tópico 02: Matrizes bidimensionais e multidimensionais (Representação tabular em memória)
-  Tópico 03: O que é uma String em C? Vetores de caracteres terminados pelo caractere nulo (\0)
-  Tópico 04: Manipulação de strings da biblioteca <string.h>: strlen(), strcpy(), strncpy()
-  Tópico 05: Concatenação e comparação de strings: strcat(), strcmp(), strncmp()
-  Tópico 06: Busca em strings com strchr() e strstr()
-  Tópico 07: Formatando strings em buffers de memória com sprintf() e snprintf()
-  Tópico 08: Conversão de strings em números: atoi(), atof(), strtol(), strtod()
-  Tópico 09: Os perigos de Buffer Overflow na manipulação insegura de arrays de caracteres
-  Tópico 10: Construindo uma biblioteca própria de manipulação de strings 100% segura

###  Módulo 4: Alocação Dinâmica de Memória e Gestão do Heap (Tópicos 31 a 40)
**Pasta de Resumos e Experimentos:** `/Modulo_04_Alocacao_Dinamica/`

-  Tópico 01: Arquitetura de memória de um programa: Stack (Pilha) vs Heap (Monte)
-  Tópico 02: A função malloc(): Solicitando blocos brutos de memória em tempo de execução
-  Tópico 03: A função calloc(): Alocação contígua e zerada de vetores dinâmicos
-  Tópico 04: Redimensionamento dinâmico de blocos com realloc()
-  Tópico 05: A regra de ouro da gestão de memória: Para todo malloc, um free() obrigatório
-  Tópico 06: Vazamentos de memória (Memory Leaks) e auditoria técnica com Valgrind
-  Tópico 07: Ponteiros soltos (Dangling Pointers) e boas práticas de limpeza de referências
-  Tópico 08: Alocação dinâmica de matrizes bidimensionais no Heap
-  Tópico 09: Implementação manual de um vetor autodescritivo dinâmico (Estilo std::vector / ArrayList)
-  Tópico 10: Tratamento de falhas de esgotamento de memória (Quando o malloc retorna NULL)

###  Módulo 5: Estruturas (structs), Uniões, Enumerações e Arquivos (Tópicos 41 a 50)
**Pasta de Resumos e Experimentos:** `/Modulo_05_Estruturas_e_Tipos/`

-  Tópico 01: Criando tipos de dados compostos com struct
-  Tópico 02: Acesso a campos de estruturas (. vs operador seta -> em ponteiros de structs)
-  Tópico 03: Aninhamento de estruturas e vetores dentro de structs
-  Tópico 04: Simplificando declarações com typedef
-  Tópico 05: O que é uma union? Compartilhando o mesmo endereço de memória entre múltiplos tipos
-  Tópico 06: Enumerações com enum para definição de estados legíveis
-  Tópico 07: Manipulação de arquivos em C via FILE*: fopen(), fclose() e modos de abertura
-  Tópico 08: Leitura e gravação sequencial de texto com fprintf(), fscanf(), fputs(), fgets()
-  Tópico 09: Leitura e gravação de blocos binários puros com fread() e fwrite()
-  Tópico 10: Posicionamento aleatório em arquivos com fseek(), ftell() e rewind()

###  Módulo 6: Estruturas de Dados Avançadas em C Puro (Tópicos 51 a 60)
**Pasta de Resumos e Experimentos:** `/Modulo_06_Estruturas_de_Dados_em_C/`

-  Tópico 01: A necessidade de estruturas encadeadas vs Arrays estáticos
-  Tópico 02: Implementação do nó fundamental (Node) com autorreferência
-  Tópico 03: Lista Encadeada Simples (Singly Linked List): Inserção no início e no fim
-  Tópico 04: Busca, remoção e percurso em Listas Encadeadas
-  Tópico 05: Listas Duplamente Encadeadas (Doubly Linked List): Navegação bidirecional
-  Tópico 06: Implementação de uma Pilha LIFO (Stack) dinâmica em C
-  Tópico 07: Implementação de uma Fila FIFO (Queue) dinâmica em C
-  Tópico 08: Introdução a Árvores Binárias de Busca (BST - Binary Search Tree)
-  Tópico 09: Tabelas Hash (Hash Tables) básicas em C com resolução de colisões por encadeamento
-  Tópico 10: Por que o conhecimento de estruturas em C é o alicerce para todos os softwares modernos?

###  Módulo 7: Maestria em C - Programação de Sistemas e Automação (Tópicos 61 a 70)
**Pasta de Resumos e Experimentos:** `/Modulo_07_Projetos_Sistemas_e_Maestria/`

-  Tópico 01: Interação com o Sistema Operacional via chamadas POSIX e variáveis de ambiente
-  Tópico 02: Processamento de argumentos de terminal avançados (argc, argv e getopt)
-  Tópico 03: Criação e execução de subprocessos básicos com fork() e exec() (Visão Linux)
-  Tópico 04: Comunicação entre processos com Pipes (pipe)
-  Tópico 05: Otimização extrema de código em C e sinalizações de compilação -O2 / -O3
-  Tópico 06: Arquitetura de um sistema de banco de dados em memória gerido por ponteiros em C
-  Tópico 07: Desenvolvendo um analisador e interpretador de comandos em linha (Mini Shell)
-  Tópico 08: Construindo uma ferramenta de diagnóstico de portas e rede ultrarrápida em C puro
-  Tópico 09: Escrita de testes de verificação e asserções nativas com o cabeçalho <assert.h>
-  Tópico 10: Projeto Final: O Gerenciador de Acervo e Diagnóstico de Memória em C Puro Carlos Guedes

---

<div align="center">
  <p> <i>"A constância nos estudos e o teste diário no código são os verdadeiros segredos para evoluir na engenharia de software."</i></p>
  <p><b>Caderno e laboratório mantido por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> </b></p>
</div>
