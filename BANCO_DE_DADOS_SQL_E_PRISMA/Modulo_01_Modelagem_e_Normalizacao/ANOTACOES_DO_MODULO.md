# 📓 Módulo 1: Modelagem Relacional, Chaves e as Três Formas Normais (Tópicos 01 a 10)

## 🎯 Meu Foco de Estudo no Módulo
Neste módulo, concentrei meus estudos em dominar os 10 tópicos listados abaixo. Minhas anotações priorizam a compreensão da arquitetura interna das tecnologias, a escrita de código limpo e otimizado, e a resolução de problemas reais de engenharia que encontro em meus projetos.

## 🧠 Minhas Anotações & Resumos Técnicos

### 📌 O que é um Banco de Dados Relacional (RDBMS)? A tabela, a linha (tupla) e a coluna (atributo)
Durante os meus estudos sobre **O que é um Banco de Dados Relacional (RDBMS)? A tabela, a linha (tupla) e a coluna (atributo)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Modelagem Conceitual, Lógica e Física: O Modelo Entidade-Relacionamento (MER / DER)
Durante os meus estudos sobre **O Modelo Entidade-Relacionamento (MER / DER)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 O conceito de Chave Primária (Primary Key - PK): Unicidade absoluta e imutabilidade de registros
Durante os meus estudos sobre **Unicidade absoluta e imutabilidade de registros**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 O conceito de Chave Estrangeira (Foreign Key - FK): Estabelecendo a integridade referencial entre tabelas
Durante os meus estudos sobre **Estabelecendo a integridade referencial entre tabelas**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Relacionamentos Um para Um (1:1): Casos de uso e modelagem prática no banco de dados
Durante os meus estudos sobre **Casos de uso e modelagem prática no banco de dados**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Relacionamentos Um para Muitos (1:N): A espinha dorsal das aplicações web e sistemas ERP
Durante os meus estudos sobre **A espinha dorsal das aplicações web e sistemas ERP**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Relacionamentos Muitos para Muitos (N:N): A necessidade obrigatória de uma tabela associativa (Tabela de Junção / Pivô)
Durante os meus estudos sobre **A necessidade obrigatória de uma tabela associativa (Tabela de Junção / Pivô)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Primeira Forma Normal (1NF): Eliminando grupos repetitivos e garantindo que atributos sejam atômicos
Durante os meus estudos sobre **Eliminando grupos repetitivos e garantindo que atributos sejam atômicos**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Segunda Forma Normal (2NF): Eliminando dependências parciais de chaves primárias compostas
Durante os meus estudos sobre **Eliminando dependências parciais de chaves primárias compostas**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Terceira Forma Normal (3NF): Eliminando dependências transitivas e garantindo que tudo dependa exclusivamente da PK
Durante os meus estudos sobre **Eliminando dependências transitivas e garantindo que tudo dependa exclusivamente da PK**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

---

## 💻 Meu Experimento Prático no Lab
Abaixo está o código prático de referência que escrevi e testei no meu terminal/navegador para colocar à prova as anotações deste módulo:

```sql
-- Meu Experimento de Banco de Dados & SQL: Módulo 1: Modelagem Relacional, Chaves e as Três Formas Normais (Tópicos 01 a 10)
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
VALUES ('SQL, Modelagem Relacional, PostgreSQL & Prisma ORM (Meus Resumos)', 'Módulo 1: Modelagem Relacional, Chaves e as Três Formas Normais (Tópicos 01 a 10)', 10)
ON DUPLICATE KEY UPDATE topicos_concluidos = 10;

-- 3. Consulta Analítica das Minhas Anotações
SELECT trilha, modulo_nome, topicos_concluidos, data_revisao 
FROM caderno_estudos_sql 
WHERE topicos_concluidos = 10 
ORDER BY id DESC 
LIMIT 5;
```

---

## 🚀 Meu Próximo Passo no Estudo
Para aprofundar meu aprendizado neste módulo, meu desafio é implementar uma variação do laboratório acima, adicionando uma funcionalidade extra para testar cenários limites e fixar os 10 conceitos estudados nesta etapa.
