<div align="center">

# 📖 SQL, Modelagem Relacional, PostgreSQL, MySQL & Prisma ORM - Ementa Completa (70+ Aulas) 🚀

**Trilha completa de inteligência de dados: normalização, consultas complexas, índices, ACID, Prisma ORM no Next.js e NoSQL.**

[![Status](https://img.shields.io/badge/Status-70%2B_Aulas_Concluídas-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Autor](https://img.shields.io/badge/Autor-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

## 🎯 Visão Geral da Trilha de Especialização

Este documento representa o plano pedagógico e técnico integral desta especialização dentro do hub **Estudos**. O conteúdo foi divido rigorosamente em **7 Módulos de Maestria Progressive**, totalizando **70 aulas detalhadas**, com códigos, fundamentos científicos, melhores práticas da indústria e desafios de engenharia.

---

## 📚 Índice de Módulos & Aulas

### 🔹 Módulo 1: Modelagem Relacional, Chaves e as Três Formas Normais (Aulas 01 a 10)
**Diretório de Aulas e Práticas:** `/Modulo_01_Modelagem_e_Normalizacao/`

- O que é um Banco de Dados Relacional (RDBMS)? A tabela, a linha (tupla) e a coluna (atributo)
- Modelagem Conceitual, Lógica e Física: O Modelo Entidade-Relacionamento (MER / DER)
- O conceito de Chave Primária (Primary Key - PK): Unicidade absoluta e imutabilidade de registros
- O conceito de Chave Estrangeira (Foreign Key - FK): Estabelecendo a integridade referencial entre tabelas
- Relacionamentos Um para Um (1:1): Casos de uso e modelagem prática no banco de dados
- Relacionamentos Um para Muitos (1:N): A espinha dorsal das aplicações web e sistemas ERP
- Relacionamentos Muitos para Muitos (N:N): A necessidade obrigatória de uma tabela associativa (Tabela de Junção / Pivô)
- Primeira Forma Normal (1NF): Eliminando grupos repetitivos e garantindo que atributos sejam atômicos
- Segunda Forma Normal (2NF): Eliminando dependências parciais de chaves primárias compostas
- Terceira Forma Normal (3NF): Eliminando dependências transitivas e garantindo que tudo dependa exclusivamente da PK

### 🔹 Módulo 2: Linguagem de Definição (DDL) e Manipulação (DML) de Dados (Aulas 11 a 20)
**Diretório de Aulas e Práticas:** `/Modulo_02_DDL_e_DML_Basico/`

- Os principais tipos de dados SQL (INT, BIGINT, VARCHAR, TEXT, BOOLEAN, DATE, TIMESTAMP, DECIMAL)
- Criando tabelas estruturadas com CREATE TABLE e definindo restrições (Constraints)
- Restrições fundamentais: NOT NULL, UNIQUE, DEFAULT e CHECK para validação nativa no banco
- Alterando a estrutura de tabelas existentes sem perda de dados com ALTER TABLE (ADD, MODIFY, DROP COLUMN)
- Informativo: Excluindo tabelas com DROP TABLE vs Limpando todos os dados instantaneamente com TRUNCATE TABLE
- Linguagem de Manipulação de Dados (DML): Inserindo novos registros nas tabelas com INSERT INTO
- A consulta fundamental de leitura com SELECT, especificação de colunas e aliases de exibição (AS)
- Filtrando registros com alta precisão usando a cláusula WHERE e operadores condicionais (=, !=, >, <, >=, <=)
- Operadores lógicos e de intervalo no WHERE (AND, OR, NOT, BETWEEN, IN, IS NULL, IS NOT NULL)
- Atualizando dados com UPDATE e removendo registros com DELETE (A importância crítica de NUNCA esquecer o WHERE!)

### 🔹 Módulo 3: O Domínio dos JOINs, Agregações, Agrupamentos e Funções (Aulas 21 a 30)
**Diretório de Aulas e Práticas:** `/Modulo_03_Consultas_Avancadas_e_Joins/`

- Por que relacionamentos exigem junção de tabelas na leitura? O conceito e o perigo do Produto Cartesiano
- INNER JOIN: Retornando apenas os registros que possuem correspondência em ambas as tabelas relacionadas
- LEFT JOIN (ou Left Outer Join): Preservando todos os registros da tabela à esquerda mesmo sem correspondência na direita
- RIGHT JOIN (ou Right Outer Join) e FULL OUTER JOIN: Compreendendo os demais tipos de junção externa
- Junções em tabelas associativas: Consultando relacionamentos Muitos-para-Muitos em três ou mais tabelas com múltiplos JOINs
- Funções de Agregação Matemática em SQL: COUNT(x), SUM(x), AVG(x), MIN(x) e MAX(x)
- Agrupando resultados consolidados pela cláusula GROUP BY para relatórios e estatísticas gerenciais
- Filtrando grupos agregados de dados com a cláusula HAVING (Por que não podemos usar agregação diretamente no WHERE?)
- Ordenação crescente e decrescente dos resultados da consulta com ORDER BY (ASC / DESC)
- Limitando a quantidade de linhas retornadas e implementando paginação com LIMIT e OFFSET (MySQL/PostgreSQL)

### 🔹 Módulo 4: Subconsultas, CTEs, Índices de Performance e Views (Aulas 31 a 40)
**Diretório de Aulas e Práticas:** `/Modulo_04_Subconsultas_Indice_e_Performance/`

- O que são Subconsultas (Subqueries)? Aninhando consultas SQL dentro de cláusulas WHERE, FROM ou SELECT
- Subconsultas correlacionadas vs não correlacionadas e os operadores condicionais EXISTS e NOT EXISTS
- Common Table Expressions (CTEs) com a cláusula WITH: Escrevendo consultas complexas de forma modular, limpa e legível
- O segredo da velocidade no banco de dados: Como funcionam os Índices B-Tree na busca por registros
- Criando e removendo índices com CREATE INDEX e DROP INDEX para aceleração extrema de consultas em colunas muito buscadas
- O custo oculto dos Índices: Por que não podemos indexar todas as colunas? O impacto de performance em operações INSERT e UPDATE
- Analisando e otimizando o plano de execução de uma consulta SQL através do comando EXPLAIN e EXPLAIN ANALYZE
- Índices únicos (Unique Indexes) e Índices compostos (Composite Indexes: A importância da ordem das colunas no índice)
- O que são Views (Visões)? Encapsulando consultas complexas e longas como tabelas virtuais reutilizáveis e seguras
- Boas práticas corporativas na escrita de consultas SQL de alta performance e prevenção de Full Table Scans lentos

### 🔹 Módulo 5: Transações (ACID), Travamento, Funções e Especificidades do PostgreSQL (Aulas 41 a 50)
**Diretório de Aulas e Práticas:** `/Modulo_05_Transacoes_ACID_e_PostgreSQL/`

- As 4 propriedades invioláveis das Transações no Banco de Dados: Atomicidade, Consistência, Isolamento e Durabilidade (ACID)
- Controlando transações na prática com os comandos BEGIN TRANSACTION, COMMIT e ROLLBACK em casos de falha do sistema
- Níveis de isolamento de transação (Read Uncommitted, Read Committed, Repeatable Read, Serializable) e problemas de concorrência
- O fenômeno do Travamento (Locks), Deadlocks no banco de dados e estratégias para prevenção em aplicações de alto tráfego
- Por que o PostgreSQL é considerado o banco de dados open-source mais avançado do mundo para engenharia de software moderna?
- Recursos poderosos do PostgreSQL 1: O tipo de dado nativo JSON e JSONB e consultas de campos em documentos estruturados
- Recursos poderosos do PostgreSQL 2: O tipo de dado nativo UUID (Universally Unique Identifier) como chave primária distribuída
- Recursos poderosos do PostgreSQL 3: Arrays nativos e pesquisa textual completa (Full Text Search) para motores de busca internos
- Funções armazenadas (Stored Procedures / Functions) em SQL e PL/pgSQL no PostgreSQL: Encapsulando lógica dentro do próprio banco
- Gatilhos automáticos de eventos (Triggers): Executando ações programadas no banco de dados ANTES ou DEPOIS de inserções e atualizações

### 🔹 Módulo 6: O Poder do Prisma ORM em Aplicações TypeScript e Next.js (Aulas 51 a 60)
**Diretório de Aulas e Práticas:** `/Modulo_06_Prisma_ORM_no_Ecossistema_TS/`

- O que é um ORM (Object-Relational Mapping)? Vantagens, desvantagens e a revolução da tipagem estática ponta a ponta
- A arquitetura do Prisma ORM: O arquivo de modelagem schema.prisma, o Prisma Client gerado e a engine em Rust
- Modelando o banco de dados via schema.prisma: Definindo Modelos, tipos de dados, chaves primárias @id e padrões @default
- Modelando relacionamentos no Prisma: Um-para-Muitos (@relation) e Muitos-para-Muitos explícito vs implícito sem escrever SQL
- O fluxo de migração de banco de dados com Prisma Migrate (npx prisma migrate dev): Evolução contínua e versionada do schema
- Inspecionando e editando os dados do banco visualmente no navegador com o estúdio interativo Prisma Studio (npx prisma studio)
- Executando consultas CRUD tipadas e autocompletadas no código TypeScript usando o cliente prisma.modelo.findMany / create / update
- Consultas relacionais de alto desempenho no Prisma com os modificadores include (eager loading) e select (projeção específica de campos)
- Executando transações seguras de múltiplas operações no Prisma ORM através do método prisma.$transaction([...])
- Quando o ORM não é suficiente: Executando consultas SQL brutas puras de forma segura com prisma.$queryRaw e tipagem genérica

### 🔹 Módulo 7: Maestria Completa - Arquitetura e Modelagem do Banco ERP Literário (Aulas 61 a 70)
**Diretório de Aulas e Práticas:** `/Modulo_07_Projetos_Reais_e_Maestria_SQL/`

- Análise de requisitos e modelagem conceitual (MER) para o Banco de Dados do ERP Biblioteca Corporativo Carlos Guedes
- Construção do script DDL de criação de todas as tabelas normalizadas em 3NF com chaves primárias, estrangeiras e restrições CHECK
- Escrita de script DML para população inicial (Seed) de dados de teste realistas com categorias, autores, livros e usuários
- Desenvolvimento de um conjunto de 5 consultas SQL analíticas de nível executivo utilizando múltiplos JOINs, agregações GROUP BY e CTEs
- Criação e aplicação de índices de otimização estratégica nas colunas de busca frequente de livros por título e ISBN
- Desenvolvimento de uma View analítica consolidada para exibição do status completo dos empréstimos ativos e atrasados na biblioteca
- Modelagem e tradução 100% fiel de toda a estrutura arquitetural relacional para um arquivo oficial schema.prisma do Next.js
- Desenvolvimento de um script TypeScript que utiliza o Prisma Client para realizar uma transação bancária / de empréstimo complexa e segura
- Auditoria de segurança, criação de usuários de banco com privilégios mínimos (Least Privilege) e política de backups de rotina
- Projeto Final: O Banco de Dados Relacional e ORM de Grau Corporativo (100% Otimizado e Tipado) Carlos Guedes

---

<div align="center">
  <p>💡 <i>"O estudo metódico, aliado à prática contínua, é o caminho indiscutível para a maestria em engenharia de software."</i></p>
  <p><b>Desenvolvido com precisão tecnológica por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> ❤️🚀</b></p>
</div>
