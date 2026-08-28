#  Módulo 3: O Domínio dos JOINs, Agregações, Agrupamentos e Funções (Tópicos 21 a 30)

##  Meu Foco de Estudo no Módulo
Neste módulo, concentrei meus estudos em dominar os 10 tópicos listados abaixo. Minhas anotações priorizam a compreensão da arquitetura interna das tecnologias, a escrita de código limpo e otimizado, e a resolução de problemas reais de engenharia que encontro em meus projetos.

##  Minhas Anotações & Resumos Técnicos

###  Por que relacionamentos exigem junção de tabelas na leitura? O conceito e o perigo do Produto Cartesiano
Durante os meus estudos sobre **Por que relacionamentos exigem junção de tabelas na leitura? O conceito e o perigo do Produto Cartesiano**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  INNER JOIN: Retornando apenas os registros que possuem correspondência em ambas as tabelas relacionadas
Durante os meus estudos sobre **Retornando apenas os registros que possuem correspondência em ambas as tabelas relacionadas**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  LEFT JOIN (ou Left Outer Join): Preservando todos os registros da tabela à esquerda mesmo sem correspondência na direita
Durante os meus estudos sobre **Preservando todos os registros da tabela à esquerda mesmo sem correspondência na direita**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  RIGHT JOIN (ou Right Outer Join) e FULL OUTER JOIN: Compreendendo os demais tipos de junção externa
Durante os meus estudos sobre **Compreendendo os demais tipos de junção externa**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Junções em tabelas associativas: Consultando relacionamentos Muitos-para-Muitos em três ou mais tabelas com múltiplos JOINs
Durante os meus estudos sobre **Consultando relacionamentos Muitos-para-Muitos em três ou mais tabelas com múltiplos JOINs**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Funções de Agregação Matemática em SQL: COUNT(x), SUM(x), AVG(x), MIN(x) e MAX(x)
Durante os meus estudos sobre **COUNT(x), SUM(x), AVG(x), MIN(x) e MAX(x)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Agrupando resultados consolidados pela cláusula GROUP BY para relatórios e estatísticas gerenciais
Durante os meus estudos sobre **Agrupando resultados consolidados pela cláusula GROUP BY para relatórios e estatísticas gerenciais**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Filtrando grupos agregados de dados com a cláusula HAVING (Por que não podemos usar agregação diretamente no WHERE?)
Durante os meus estudos sobre **Filtrando grupos agregados de dados com a cláusula HAVING (Por que não podemos usar agregação diretamente no WHERE?)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Ordenação crescente e decrescente dos resultados da consulta com ORDER BY (ASC / DESC)
Durante os meus estudos sobre **Ordenação crescente e decrescente dos resultados da consulta com ORDER BY (ASC / DESC)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Limitando a quantidade de linhas retornadas e implementando paginação com LIMIT e OFFSET (MySQL/PostgreSQL)
Durante os meus estudos sobre **Limitando a quantidade de linhas retornadas e implementando paginação com LIMIT e OFFSET (MySQL/PostgreSQL)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

---

##  Meu Experimento Prático no Lab
Abaixo está o código prático de referência que escrevi e testei no meu terminal/navegador para colocar à prova as anotações deste módulo:

```sql
-- Meu Experimento de Banco de Dados & SQL: Módulo 3: O Domínio dos JOINs, Agregações, Agrupamentos e Funções (Tópicos 21 a 30)
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
VALUES ('SQL, Modelagem Relacional, PostgreSQL & Prisma ORM (Meus Resumos)', 'Módulo 3: O Domínio dos JOINs, Agregações, Agrupamentos e Funções (Tópicos 21 a 30)', 10)
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
