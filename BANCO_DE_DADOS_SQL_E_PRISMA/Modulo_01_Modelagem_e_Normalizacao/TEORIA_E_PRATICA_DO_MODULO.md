# Módulo 1: Modelagem Relacional, Chaves e as Três Formas Normais (Aulas 01 a 10)

## 📌 Objetivos de Aprendizagem do Módulo
Neste módulo, você dominará os conceitos técnicos que sustentam as 10 aulas desta etapa. A abordagem de Carlos Guedes prioriza a clareza arquitetural, a eficiência computacional e a aplicação direta em projetos de nível profissional.

## 🧠 Resumo Teórico & Boas Práticas da Indústria

### O que é um Banco de Dados Relacional (RDBMS)? A tabela, a linha (tupla) e a coluna (atributo)
O domínio de **O que é um Banco de Dados Relacional (RDBMS)? A tabela, a linha (tupla) e a coluna (atributo)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Modelagem Conceitual, Lógica e Física: O Modelo Entidade-Relacionamento (MER / DER)
O domínio de **O Modelo Entidade-Relacionamento (MER / DER)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### O conceito de Chave Primária (Primary Key - PK): Unicidade absoluta e imutabilidade de registros
O domínio de **Unicidade absoluta e imutabilidade de registros** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### O conceito de Chave Estrangeira (Foreign Key - FK): Estabelecendo a integridade referencial entre tabelas
O domínio de **Estabelecendo a integridade referencial entre tabelas** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Relacionamentos Um para Um (1:1): Casos de uso e modelagem prática no banco de dados
O domínio de **Casos de uso e modelagem prática no banco de dados** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Relacionamentos Um para Muitos (1:N): A espinha dorsal das aplicações web e sistemas ERP
O domínio de **A espinha dorsal das aplicações web e sistemas ERP** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Relacionamentos Muitos para Muitos (N:N): A necessidade obrigatória de uma tabela associativa (Tabela de Junção / Pivô)
O domínio de **A necessidade obrigatória de uma tabela associativa (Tabela de Junção / Pivô)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Primeira Forma Normal (1NF): Eliminando grupos repetitivos e garantindo que atributos sejam atômicos
O domínio de **Eliminando grupos repetitivos e garantindo que atributos sejam atômicos** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Segunda Forma Normal (2NF): Eliminando dependências parciais de chaves primárias compostas
O domínio de **Eliminando dependências parciais de chaves primárias compostas** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Terceira Forma Normal (3NF): Eliminando dependências transitivas e garantindo que tudo dependa exclusivamente da PK
O domínio de **Eliminando dependências transitivas e garantindo que tudo dependa exclusivamente da PK** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

---

## 💻 Laboratório de Código Prático
Abaixo está a implementação prática de referência que consolida os aprendizados deste módulo:

```sql
-- Laboratório Prático de Banco de Dados & SQL: Módulo 1: Modelagem Relacional, Chaves e as Três Formas Normais (Aulas 01 a 10)
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
VALUES ('SQL, Modelagem Relacional, PostgreSQL, MySQL & Prisma ORM', 'Módulo 1: Modelagem Relacional, Chaves e as Três Formas Normais (Aulas 01 a 10)', 10)
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
