<div align="center">

#  SQL, Modelagem Relacional, PostgreSQL & Prisma ORM (Meus Resumos) - Meu Caderno de Anotações (70+ Tópicos) 

**Meu caderno de banco de dados: normalização 3NF, consultas complexas, índices, transações ACID e Prisma ORM.**

[![Status](https://img.shields.io/badge/Status-70%2B_Tópicos_Estudados-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Estudante](https://img.shields.io/badge/Estudante-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

##  Visão Geral dos Meus Estudos

Este documento organiza o meu caderno pessoal de anotações, resumos teóricos e experimentos de código nesta especialização dentro do meu repositório de **Estudos**. Estruturei meu aprendizado rigorosamente em **7 Módulos de Investigação**, totalizando **70 tópicos de estudo detalhados**, onde documentei a teoria, armadilhas comuns, macetes corporativos e desenvolvi códigos de laboratório para fixar cada conceito.

---

##  Índice de Resumos & Experimentos

###  Módulo 1: Modelagem Relacional, Chaves e as Três Formas Normais (Tópicos 01 a 10)
**Pasta de Resumos e Experimentos:** `/Modulo_01_Modelagem_e_Normalizacao/`

-  Tópico 01: O que é um Banco de Dados Relacional (RDBMS)? A tabela, a linha (tupla) e a coluna (atributo)
-  Tópico 02: Modelagem Conceitual, Lógica e Física: O Modelo Entidade-Relacionamento (MER / DER)
-  Tópico 03: O conceito de Chave Primária (Primary Key - PK): Unicidade absoluta e imutabilidade de registros
-  Tópico 04: O conceito de Chave Estrangeira (Foreign Key - FK): Estabelecendo a integridade referencial entre tabelas
-  Tópico 05: Relacionamentos Um para Um (1:1): Casos de uso e modelagem prática no banco de dados
-  Tópico 06: Relacionamentos Um para Muitos (1:N): A espinha dorsal das aplicações web e sistemas ERP
-  Tópico 07: Relacionamentos Muitos para Muitos (N:N): A necessidade obrigatória de uma tabela associativa (Tabela de Junção / Pivô)
-  Tópico 08: Primeira Forma Normal (1NF): Eliminando grupos repetitivos e garantindo que atributos sejam atômicos
-  Tópico 09: Segunda Forma Normal (2NF): Eliminando dependências parciais de chaves primárias compostas
-  Tópico 10: Terceira Forma Normal (3NF): Eliminando dependências transitivas e garantindo que tudo dependa exclusivamente da PK

###  Módulo 2: Linguagem de Definição (DDL) e Manipulação (DML) de Dados (Tópicos 11 a 20)
**Pasta de Resumos e Experimentos:** `/Modulo_02_DDL_e_DML_Basico/`

-  Tópico 01: Os principais tipos de dados SQL (INT, BIGINT, VARCHAR, TEXT, BOOLEAN, DATE, TIMESTAMP, DECIMAL)
-  Tópico 02: Criando tabelas estruturadas com CREATE TABLE e definindo restrições (Constraints)
-  Tópico 03: Restrições fundamentais: NOT NULL, UNIQUE, DEFAULT e CHECK para validação nativa no banco
-  Tópico 04: Alterando a estrutura de tabelas existentes sem perda de dados com ALTER TABLE (ADD, MODIFY, DROP COLUMN)
-  Tópico 05: Informativo: Excluindo tabelas com DROP TABLE vs Limpando todos os dados instantaneamente com TRUNCATE TABLE
-  Tópico 06: Linguagem de Manipulação de Dados (DML): Inserindo novos registros nas tabelas com INSERT INTO
-  Tópico 07: A consulta fundamental de leitura com SELECT, especificação de colunas e aliases de exibição (AS)
-  Tópico 08: Filtrando registros com alta precisão usando a cláusula WHERE e operadores condicionais (=, !=, >, <, >=, <=)
-  Tópico 09: Operadores lógicos e de intervalo no WHERE (AND, OR, NOT, BETWEEN, IN, IS NULL, IS NOT NULL)
-  Tópico 10: Atualizando dados com UPDATE e removendo registros com DELETE (A importância crítica de NUNCA esquecer o WHERE!)

###  Módulo 3: O Domínio dos JOINs, Agregações, Agrupamentos e Funções (Tópicos 21 a 30)
**Pasta de Resumos e Experimentos:** `/Modulo_03_Consultas_Avancadas_e_Joins/`

-  Tópico 01: Por que relacionamentos exigem junção de tabelas na leitura? O conceito e o perigo do Produto Cartesiano
-  Tópico 02: INNER JOIN: Retornando apenas os registros que possuem correspondência em ambas as tabelas relacionadas
-  Tópico 03: LEFT JOIN (ou Left Outer Join): Preservando todos os registros da tabela à esquerda mesmo sem correspondência na direita
-  Tópico 04: RIGHT JOIN (ou Right Outer Join) e FULL OUTER JOIN: Compreendendo os demais tipos de junção externa
-  Tópico 05: Junções em tabelas associativas: Consultando relacionamentos Muitos-para-Muitos em três ou mais tabelas com múltiplos JOINs
-  Tópico 06: Funções de Agregação Matemática em SQL: COUNT(x), SUM(x), AVG(x), MIN(x) e MAX(x)
-  Tópico 07: Agrupando resultados consolidados pela cláusula GROUP BY para relatórios e estatísticas gerenciais
-  Tópico 08: Filtrando grupos agregados de dados com a cláusula HAVING (Por que não podemos usar agregação diretamente no WHERE?)
-  Tópico 09: Ordenação crescente e decrescente dos resultados da consulta com ORDER BY (ASC / DESC)
-  Tópico 10: Limitando a quantidade de linhas retornadas e implementando paginação com LIMIT e OFFSET (MySQL/PostgreSQL)

###  Módulo 4: Subconsultas, CTEs, Índices de Performance e Views (Tópicos 31 a 40)
**Pasta de Resumos e Experimentos:** `/Modulo_04_Subconsultas_Indice_e_Performance/`

-  Tópico 01: O que são Subconsultas (Subqueries)? Aninhando consultas SQL dentro de cláusulas WHERE, FROM ou SELECT
-  Tópico 02: Subconsultas correlacionadas vs não correlacionadas e os operadores condicionais EXISTS e NOT EXISTS
-  Tópico 03: Common Table Expressions (CTEs) com a cláusula WITH: Escrevendo consultas complexas de forma modular, limpa e legível
-  Tópico 04: O segredo da velocidade no banco de dados: Como funcionam os Índices B-Tree na busca por registros
-  Tópico 05: Criando e removendo índices com CREATE INDEX e DROP INDEX para aceleração extrema de consultas em colunas muito buscadas
-  Tópico 06: O custo oculto dos Índices: Por que não podemos indexar todas as colunas? O impacto de performance em operações INSERT e UPDATE
-  Tópico 07: Analisando e otimizando o plano de execução de uma consulta SQL através do comando EXPLAIN e EXPLAIN ANALYZE
-  Tópico 08: Índices únicos (Unique Indexes) e Índices compostos (Composite Indexes: A importância da ordem das colunas no índice)
-  Tópico 09: O que são Views (Visões)? Encapsulando consultas complexas e longas como tabelas virtuais reutilizáveis e seguras
-  Tópico 10: Boas práticas corporativas na escrita de consultas SQL de alta performance e prevenção de Full Table Scans lentos

###  Módulo 5: Transações (ACID), Travamento, Funções e Especificidades do PostgreSQL (Tópicos 41 a 50)
**Pasta de Resumos e Experimentos:** `/Modulo_05_Transacoes_ACID_e_PostgreSQL/`

-  Tópico 01: As 4 propriedades invioláveis das Transações no Banco de Dados: Atomicidade, Consistência, Isolamento e Durabilidade (ACID)
-  Tópico 02: Controlando transações na prática com os comandos BEGIN TRANSACTION, COMMIT e ROLLBACK em casos de falha do sistema
-  Tópico 03: Níveis de isolamento de transação (Read Uncommitted, Read Committed, Repeatable Read, Serializable) e problemas de concorrência
-  Tópico 04: O fenômeno do Travamento (Locks), Deadlocks no banco de dados e estratégias para prevenção em aplicações de alto tráfego
-  Tópico 05: Por que o PostgreSQL é considerado o banco de dados open-source mais avançado do mundo para engenharia de software moderna?
-  Tópico 06: Recursos poderosos do PostgreSQL 1: O tipo de dado nativo JSON e JSONB e consultas de campos em documentos estruturados
-  Tópico 07: Recursos poderosos do PostgreSQL 2: O tipo de dado nativo UUID (Universally Unique Identifier) como chave primária distribuída
-  Tópico 08: Recursos poderosos do PostgreSQL 3: Arrays nativos e pesquisa textual completa (Full Text Search) para motores de busca internos
-  Tópico 09: Funções armazenadas (Stored Procedures / Functions) em SQL e PL/pgSQL no PostgreSQL: Encapsulando lógica dentro do próprio banco
-  Tópico 10: Gatilhos automáticos de eventos (Triggers): Executando ações programadas no banco de dados ANTES ou DEPOIS de inserções e atualizações

###  Módulo 6: O Poder do Prisma ORM em Aplicações TypeScript e Next.js (Tópicos 51 a 60)
**Pasta de Resumos e Experimentos:** `/Modulo_06_Prisma_ORM_no_Ecossistema_TS/`

-  Tópico 01: O que é um ORM (Object-Relational Mapping)? Vantagens, desvantagens e a revolução da tipagem estática ponta a ponta
-  Tópico 02: A arquitetura do Prisma ORM: O arquivo de modelagem schema.prisma, o Prisma Client gerado e a engine em Rust
-  Tópico 03: Modelando o banco de dados via schema.prisma: Definindo Modelos, tipos de dados, chaves primárias @id e padrões @default
-  Tópico 04: Modelando relacionamentos no Prisma: Um-para-Muitos (@relation) e Muitos-para-Muitos explícito vs implícito sem escrever SQL
-  Tópico 05: O fluxo de migração de banco de dados com Prisma Migrate (npx prisma migrate dev): Evolução contínua e versionada do schema
-  Tópico 06: Inspecionando e editando os dados do banco visualmente no navegador com o estúdio interativo Prisma Studio (npx prisma studio)
-  Tópico 07: Executando consultas CRUD tipadas e autocompletadas no código TypeScript usando o cliente prisma.modelo.findMany / create / update
-  Tópico 08: Consultas relacionais de alto desempenho no Prisma com os modificadores include (eager loading) e select (projeção específica de campos)
-  Tópico 09: Executando transações seguras de múltiplas operações no Prisma ORM através do método prisma.$transaction([...])
-  Tópico 10: Quando o ORM não é suficiente: Executando consultas SQL brutas puras de forma segura com prisma.$queryRaw e tipagem genérica

###  Módulo 7: Maestria Completa - Arquitetura e Modelagem do Banco ERP Literário (Tópicos 61 a 70)
**Pasta de Resumos e Experimentos:** `/Modulo_07_Projetos_Reais_e_Maestria_SQL/`

-  Tópico 01: Análise de requisitos e modelagem conceitual (MER) para o Banco de Dados do ERP Biblioteca Corporativo Carlos Guedes
-  Tópico 02: Construção do script DDL de criação de todas as tabelas normalizadas em 3NF com chaves primárias, estrangeiras e restrições CHECK
-  Tópico 03: Escrita de script DML para população inicial (Seed) de dados de teste realistas com categorias, autores, livros e usuários
-  Tópico 04: Desenvolvimento de um conjunto de 5 consultas SQL analíticas de nível executivo utilizando múltiplos JOINs, agregações GROUP BY e CTEs
-  Tópico 05: Criação e aplicação de índices de otimização estratégica nas colunas de busca frequente de livros por título e ISBN
-  Tópico 06: Desenvolvimento de uma View analítica consolidada para exibição do status completo dos empréstimos ativos e atrasados na biblioteca
-  Tópico 07: Modelagem e tradução 100% fiel de toda a estrutura arquitetural relacional para um arquivo oficial schema.prisma do Next.js
-  Tópico 08: Desenvolvimento de um script TypeScript que utiliza o Prisma Client para realizar uma transação bancária / de empréstimo complexa e segura
-  Tópico 09: Auditoria de segurança, criação de usuários de banco com privilégios mínimos (Least Privilege) e política de backups de rotina
-  Tópico 10: Projeto Final: O Banco de Dados Relacional e ORM de Grau Corporativo (100% Otimizado e Tipado) Carlos Guedes

---

<div align="center">
  <p> <i>"A constância nos estudos e o teste diário no código são os verdadeiros segredos para evoluir na engenharia de software."</i></p>
  <p><b>Caderno e laboratório mantido por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> </b></p>
</div>
