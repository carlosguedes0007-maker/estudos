# Módulo 2: Linguagem de Definição (DDL) e Manipulação (DML) de Dados (Aulas 11 a 20)

## 📌 Objetivos de Aprendizagem do Módulo
Neste módulo, você dominará os conceitos técnicos que sustentam as 10 aulas desta etapa. A abordagem de Carlos Guedes prioriza a clareza arquitetural, a eficiência computacional e a aplicação direta em projetos de nível profissional.

## 🧠 Resumo Teórico & Boas Práticas da Indústria

### Os principais tipos de dados SQL (INT, BIGINT, VARCHAR, TEXT, BOOLEAN, DATE, TIMESTAMP, DECIMAL)
O domínio de **Os principais tipos de dados SQL (INT, BIGINT, VARCHAR, TEXT, BOOLEAN, DATE, TIMESTAMP, DECIMAL)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Criando tabelas estruturadas com CREATE TABLE e definindo restrições (Constraints)
O domínio de **Criando tabelas estruturadas com CREATE TABLE e definindo restrições (Constraints)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Restrições fundamentais: NOT NULL, UNIQUE, DEFAULT e CHECK para validação nativa no banco
O domínio de **NOT NULL, UNIQUE, DEFAULT e CHECK para validação nativa no banco** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Alterando a estrutura de tabelas existentes sem perda de dados com ALTER TABLE (ADD, MODIFY, DROP COLUMN)
O domínio de **Alterando a estrutura de tabelas existentes sem perda de dados com ALTER TABLE (ADD, MODIFY, DROP COLUMN)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Informativo: Excluindo tabelas com DROP TABLE vs Limpando todos os dados instantaneamente com TRUNCATE TABLE
O domínio de **Excluindo tabelas com DROP TABLE vs Limpando todos os dados instantaneamente com TRUNCATE TABLE** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Linguagem de Manipulação de Dados (DML): Inserindo novos registros nas tabelas com INSERT INTO
O domínio de **Inserindo novos registros nas tabelas com INSERT INTO** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### A consulta fundamental de leitura com SELECT, especificação de colunas e aliases de exibição (AS)
O domínio de **A consulta fundamental de leitura com SELECT, especificação de colunas e aliases de exibição (AS)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Filtrando registros com alta precisão usando a cláusula WHERE e operadores condicionais (=, !=, >, <, >=, <=)
O domínio de **Filtrando registros com alta precisão usando a cláusula WHERE e operadores condicionais (=, !=, >, <, >=, <=)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Operadores lógicos e de intervalo no WHERE (AND, OR, NOT, BETWEEN, IN, IS NULL, IS NOT NULL)
O domínio de **Operadores lógicos e de intervalo no WHERE (AND, OR, NOT, BETWEEN, IN, IS NULL, IS NOT NULL)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Atualizando dados com UPDATE e removendo registros com DELETE (A importância crítica de NUNCA esquecer o WHERE!)
O domínio de **Atualizando dados com UPDATE e removendo registros com DELETE (A importância crítica de NUNCA esquecer o WHERE!)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

---

## 💻 Laboratório de Código Prático
Abaixo está a implementação prática de referência que consolida os aprendizados deste módulo:

```sql
-- Laboratório Prático de Banco de Dados & SQL: Módulo 2: Linguagem de Definição (DDL) e Manipulação (DML) de Dados (Aulas 11 a 20)
-- Autor: Carlos Guedes

-- 1. Criação de Tabela Demonstrativa com Restrições (DDL)
CREATE TABLE IF NOT EXISTS modulos_estudo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trilha VARCHAR(100) NOT NULL,
    modulo_nome VARCHAR(255) NOT NULL UNIQUE,
    aulas_concluidas INT DEFAULT 10 CHECK (aulas_concluidas >= 0),
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 2. Inserção de Dados Validados (DML)
INSERT INTO modulos_estudo (trilha, modulo_nome, aulas_concluidas) 
VALUES ('SQL, Modelagem Relacional, PostgreSQL, MySQL & Prisma ORM', 'Módulo 2: Linguagem de Definição (DDL) e Manipulação (DML) de Dados (Aulas 11 a 20)', 10)
ON DUPLICATE KEY UPDATE aulas_concluidas = 10;

-- 3. Consulta Analítica de Verificação
SELECT trilha, modulo_nome, aulas_concluidas, data_atualizacao 
FROM modulos_estudo 
WHERE aulas_concluidas = 10 
ORDER BY id DESC 
LIMIT 5;
```

---

## 🚀 Desafio Prático de Conclusão do Módulo
Para validar sua certificação interna neste módulo, implemente uma variação do laboratório acima que adicione uma funcionalidade extra à sua escolha, aplicando rigorosamente os 10 conceitos teóricos apresentados nas aulas.
