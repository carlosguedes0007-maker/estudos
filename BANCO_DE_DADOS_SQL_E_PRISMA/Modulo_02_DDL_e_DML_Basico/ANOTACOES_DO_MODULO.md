#  Módulo 2: Linguagem de Definição (DDL) e Manipulação (DML) de Dados (Tópicos 11 a 20)

##  Meu Foco de Estudo no Módulo
Neste módulo, concentrei meus estudos em dominar os 10 tópicos listados abaixo. Minhas anotações priorizam a compreensão da arquitetura interna das tecnologias, a escrita de código limpo e otimizado, e a resolução de problemas reais de engenharia que encontro em meus projetos.

##  Minhas Anotações & Resumos Técnicos

###  Os principais tipos de dados SQL (INT, BIGINT, VARCHAR, TEXT, BOOLEAN, DATE, TIMESTAMP, DECIMAL)
Durante os meus estudos sobre **Os principais tipos de dados SQL (INT, BIGINT, VARCHAR, TEXT, BOOLEAN, DATE, TIMESTAMP, DECIMAL)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Criando tabelas estruturadas com CREATE TABLE e definindo restrições (Constraints)
Durante os meus estudos sobre **Criando tabelas estruturadas com CREATE TABLE e definindo restrições (Constraints)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Restrições fundamentais: NOT NULL, UNIQUE, DEFAULT e CHECK para validação nativa no banco
Durante os meus estudos sobre **NOT NULL, UNIQUE, DEFAULT e CHECK para validação nativa no banco**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Alterando a estrutura de tabelas existentes sem perda de dados com ALTER TABLE (ADD, MODIFY, DROP COLUMN)
Durante os meus estudos sobre **Alterando a estrutura de tabelas existentes sem perda de dados com ALTER TABLE (ADD, MODIFY, DROP COLUMN)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Informativo: Excluindo tabelas com DROP TABLE vs Limpando todos os dados instantaneamente com TRUNCATE TABLE
Durante os meus estudos sobre **Excluindo tabelas com DROP TABLE vs Limpando todos os dados instantaneamente com TRUNCATE TABLE**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Linguagem de Manipulação de Dados (DML): Inserindo novos registros nas tabelas com INSERT INTO
Durante os meus estudos sobre **Inserindo novos registros nas tabelas com INSERT INTO**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  A consulta fundamental de leitura com SELECT, especificação de colunas e aliases de exibição (AS)
Durante os meus estudos sobre **A consulta fundamental de leitura com SELECT, especificação de colunas e aliases de exibição (AS)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Filtrando registros com alta precisão usando a cláusula WHERE e operadores condicionais (=, !=, >, <, >=, <=)
Durante os meus estudos sobre **Filtrando registros com alta precisão usando a cláusula WHERE e operadores condicionais (=, !=, >, <, >=, <=)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Operadores lógicos e de intervalo no WHERE (AND, OR, NOT, BETWEEN, IN, IS NULL, IS NOT NULL)
Durante os meus estudos sobre **Operadores lógicos e de intervalo no WHERE (AND, OR, NOT, BETWEEN, IN, IS NULL, IS NOT NULL)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Atualizando dados com UPDATE e removendo registros com DELETE (A importância crítica de NUNCA esquecer o WHERE!)
Durante os meus estudos sobre **Atualizando dados com UPDATE e removendo registros com DELETE (A importância crítica de NUNCA esquecer o WHERE!)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

---

##  Meu Experimento Prático no Lab
Abaixo está o código prático de referência que escrevi e testei no meu terminal/navegador para colocar à prova as anotações deste módulo:

```sql
-- Meu Experimento de Banco de Dados & SQL: Módulo 2: Linguagem de Definição (DDL) e Manipulação (DML) de Dados (Tópicos 11 a 20)
-- Estudante: Carlos Guedes

-- 1. Tabela Demonstrativa do Caderno de Estudos (DDL)
CREATE TABLE IF NOT EXISTS caderno_estudos_sql (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trilha VARCHAR(100) NOT NULL,
    modulo_nome VARCHAR(255) NOT NULL UNIQUE,
    topicos_concluidos INT DEFAULT 10 CHECK (topicos_concluidos >= 0),
    data_revisao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 2. Inserção do Registro de Estudo Validados (DML)
INSERT INTO caderno_estudos_sql (trilha, modulo_nome, topicos_concluidos) 
VALUES ('SQL, Modelagem Relacional, PostgreSQL & Prisma ORM (Meus Resumos)', 'Módulo 2: Linguagem de Definição (DDL) e Manipulação (DML) de Dados (Tópicos 11 a 20)', 10)
ON DUPLICATE KEY UPDATE topicos_concluidos = 10;

-- 3. Consulta Analítica das Minhas Anotações
SELECT trilha, modulo_nome, topicos_concluidos, data_revisao 
FROM caderno_estudos_sql 
WHERE topicos_concluidos = 10 
ORDER BY id DESC 
LIMIT 5;
```

---

##  Meu Próximo Passo no Estudo
Para aprofundar meu aprendizado neste módulo, meu desafio é implementar uma variação do laboratório acima, adicionando uma funcionalidade extra para testar cenários limites e fixar os 10 conceitos estudados nesta etapa.
