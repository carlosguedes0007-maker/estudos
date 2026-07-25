# Módulo 4: Subconsultas, CTEs, Índices de Performance e Views (Aulas 31 a 40)

## 📌 Objetivos de Aprendizagem do Módulo
Neste módulo, você dominará os conceitos técnicos que sustentam as 10 aulas desta etapa. A abordagem de Carlos Guedes prioriza a clareza arquitetural, a eficiência computacional e a aplicação direta em projetos de nível profissional.

## 🧠 Resumo Teórico & Boas Práticas da Indústria

### O que são Subconsultas (Subqueries)? Aninhando consultas SQL dentro de cláusulas WHERE, FROM ou SELECT
O domínio de **O que são Subconsultas (Subqueries)? Aninhando consultas SQL dentro de cláusulas WHERE, FROM ou SELECT** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Subconsultas correlacionadas vs não correlacionadas e os operadores condicionais EXISTS e NOT EXISTS
O domínio de **Subconsultas correlacionadas vs não correlacionadas e os operadores condicionais EXISTS e NOT EXISTS** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Common Table Expressions (CTEs) com a cláusula WITH: Escrevendo consultas complexas de forma modular, limpa e legível
O domínio de **Escrevendo consultas complexas de forma modular, limpa e legível** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### O segredo da velocidade no banco de dados: Como funcionam os Índices B-Tree na busca por registros
O domínio de **Como funcionam os Índices B-Tree na busca por registros** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Criando e removendo índices com CREATE INDEX e DROP INDEX para aceleração extrema de consultas em colunas muito buscadas
O domínio de **Criando e removendo índices com CREATE INDEX e DROP INDEX para aceleração extrema de consultas em colunas muito buscadas** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### O custo oculto dos Índices: Por que não podemos indexar todas as colunas? O impacto de performance em operações INSERT e UPDATE
O domínio de **Por que não podemos indexar todas as colunas? O impacto de performance em operações INSERT e UPDATE** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Analisando e otimizando o plano de execução de uma consulta SQL através do comando EXPLAIN e EXPLAIN ANALYZE
O domínio de **Analisando e otimizando o plano de execução de uma consulta SQL através do comando EXPLAIN e EXPLAIN ANALYZE** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Índices únicos (Unique Indexes) e Índices compostos (Composite Indexes: A importância da ordem das colunas no índice)
O domínio de **A importância da ordem das colunas no índice)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### O que são Views (Visões)? Encapsulando consultas complexas e longas como tabelas virtuais reutilizáveis e seguras
O domínio de **O que são Views (Visões)? Encapsulando consultas complexas e longas como tabelas virtuais reutilizáveis e seguras** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Boas práticas corporativas na escrita de consultas SQL de alta performance e prevenção de Full Table Scans lentos
O domínio de **Boas práticas corporativas na escrita de consultas SQL de alta performance e prevenção de Full Table Scans lentos** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

---

## 💻 Laboratório de Código Prático
Abaixo está a implementação prática de referência que consolida os aprendizados deste módulo:

```sql
-- Laboratório Prático de Banco de Dados & SQL: Módulo 4: Subconsultas, CTEs, Índices de Performance e Views (Aulas 31 a 40)
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
VALUES ('SQL, Modelagem Relacional, PostgreSQL, MySQL & Prisma ORM', 'Módulo 4: Subconsultas, CTEs, Índices de Performance e Views (Aulas 31 a 40)', 10)
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
