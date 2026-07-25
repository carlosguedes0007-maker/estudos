<div align="center">

# 📓 PHP 8.3+, POO, PDO, MVC & Segurança Web (Meus Estudos) - Meu Caderno de Anotações (70+ Tópicos) 🚀

**Meus resumos e testes práticos com PHP 8.3, tipagem estrita, conexões PDO seguras, arquitetura MVC e Autoload PSR-4.**

[![Status](https://img.shields.io/badge/Status-70%2B_Tópicos_Estudados-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Estudante](https://img.shields.io/badge/Estudante-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

## 🎯 Visão Geral dos Meus Estudos

Este documento organiza o meu caderno pessoal de anotações, resumos teóricos e experimentos de código nesta especialização dentro do meu repositório de **Estudos**. Estruturei meu aprendizado rigorosamente em **7 Módulos de Investigação**, totalizando **70 tópicos de estudo detalhados**, onde documentei a teoria, armadilhas comuns, macetes corporativos e desenvolvi códigos de laboratório para fixar cada conceito.

---

## 📚 Índice de Resumos & Experimentos

### 🔹 Módulo 1: PHP 8.3+, Sintaxe, Tipagem Estrita e Estruturas (Tópicos 01 a 10)
**Pasta de Resumos e Experimentos:** `/Modulo_01_Fundamentos_e_Sintaxe_PHP/`

- 📌 Tópico 01: O PHP moderno no servidor web e a declaração de tipagem estrita (declare(strict_types=1);)
- 📌 Tópico 02: A estrutura do arquivo .php, tags de abertura e a função echo vs print
- 📌 Tópico 03: Variáveis, tipos escalares (int, float, string, bool) e verificação com var_dump() e is_type()
- 📌 Tópico 04: Operadores aritméticos, lógicos, relacionais e o operador Spaceship (<=>)
- 📌 Tópico 05: O operador Null Coalescing (??) e Null Coalescing Assignment (??=)
- 📌 Tópico 06: Estruturas de controle de fluxo condicionais (if, elseif, else e ternário)
- 📌 Tópico 07: A poderosa estrutura de decisão Match (PHP 8+): Limpa, estrita e com retorno de valor
- 📌 Tópico 08: Laços de repetição (for, while, do-while) e o iterador de arrays foreach
- 📌 Tópico 09: Arrays no PHP: O tipo mais versátil (Arrays indexados vs Arrays associativos chave-valor)
- 📌 Tópico 10: Manipulação avançada de arrays (array_map, array_filter, array_reduce, count, in_array, explode, implode)

### 🔹 Módulo 2: Funções, Orientação a Objetos Moderna e Construtores (Tópicos 11 a 20)
**Pasta de Resumos e Experimentos:** `/Modulo_02_Funcoes_e_Orientacao_a_Objetos/`

- 📌 Tópico 01: Definindo funções em PHP com tipagem de parâmetros e tipagem de retorno
- 📌 Tópico 02: Parâmetros padrão, argumentos nomeados (Named Arguments) e empacotamento variádico (...$args)
- 📌 Tópico 03: Funções anônimas (Closures) e Arrow Functions (fn() => ...) no PHP 8
- 📌 Tópico 04: Introdução à Orientação a Objetos em PHP: Classes, Objetos e a pseudo-variável $this
- 📌 Tópico 05: Propriedades e métodos, modificadores de visibilidade (public, protected, private)
- 📌 Tópico 06: O método construtor (__construct) e a Promoção de Propriedades no Construtor (PHP 8+)
- 📌 Tópico 07: Propriedades somente leitura (readonly properties e readonly classes)
- 📌 Tópico 08: Herança com extends, chamada ao pai com parent:: e sobrescrita de métodos
- 📌 Tópico 09: Polimorfismo, classes e métodos abstratos (abstract) no PHP
- 📌 Tópico 10: Interfaces corporativas em PHP (interface e implements): Garantindo contratos de implementação

### 🔹 Módulo 3: Traits, Enums, Métodos Mágicos e Autoloading PSR-4 (Tópicos 21 a 30)
**Pasta de Resumos e Experimentos:** `/Modulo_03_Recursos_Avancados_de_POO/`

- 📌 Tópico 01: O que são Traits em PHP? Compartilhando comportamentos na ausência de herança múltipla
- 📌 Tópico 02: Enums (Enumerações no PHP 8.1+): Enums puros e Enums de suporte (Backed Enums com valores string/int)
- 📌 Tópico 03: Propriedades e métodos estáticos (static) e o operador de resolução de escopo (::)
- 📌 Tópico 04: O conceito de Late Static Binding (self:: vs static::) em hierarquias
- 📌 Tópico 05: Métodos mágicos fundamentais: __toString(), __get(), __set(), __call()
- 📌 Tópico 06: Clonagem de objetos no PHP com a palavra-chave clone e o método mágico __clone()
- 📌 Tópico 07: Namespaces em PHP: Evitando conflito de nomes e organizando pacotes corporativos
- 📌 Tópico 08: A especificação de Autoloading PSR-4 da PHP-FIG: Carregamento automático de classes sem require/include
- 📌 Tópico 09: Gerenciamento de pacotes profissionais com Composer e o arquivo composer.json
- 📌 Tópico 10: O tratamento moderno de exceções com try, catch, finally e a interface Throwable

### 🔹 Módulo 4: Acesso Seguro ao Banco de Dados Relacional com PDO (Tópicos 31 a 40)
**Pasta de Resumos e Experimentos:** `/Modulo_04_Banco_de_Dados_com_PDO/`

- 📌 Tópico 01: Por que abandonar as funções antigas mysql_* / mysqli e usar exclusivamente a extensão PDO (PHP Data Objects)?
- 📌 Tópico 02: Estabelecendo uma conexão segura com MySQL / PostgreSQL via DSN e tratamento de exceções PDOException
- 📌 Tópico 03: O maior perigo da Web: Injeção de SQL (SQL Injection) e como ela destrói sistemas desprotegidos
- 📌 Tópico 04: A blindagem absoluta: Prepared Statements (Declarações preparadas) com parâmetros posicionais (?) e nomeados (:param)
- 📌 Tópico 05: Executando consultas de seleção (SELECT) com fetch() e fetchAll() e modos de retorno (PDO::FETCH_ASSOC vs PDO::FETCH_OBJ)
- 📌 Tópico 06: Mapeamento Direto Objeto-Relacional: Hidratando instâncias de classes automáticas com PDO::FETCH_CLASS
- 📌 Tópico 07: Executando mutações seguras (INSERT, UPDATE, DELETE) e capturando o ID gerado com lastInsertId()
- 📌 Tópico 08: A importância crítica das Transações de Banco de Dados (ACID): beginTransaction(), commit() e rollBack()
- 📌 Tópico 09: Paginação eficiente de resultados SQL no backend PHP com LIMIT e OFFSET
- 📌 Tópico 10: Construindo uma classe Database Singleton modularizada e à prova de falhas

### 🔹 Módulo 5: Requisições Web, Sessões, Cookies e Segurança OWASP (Tópicos 41 a 50)
**Pasta de Resumos e Experimentos:** `/Modulo_05_Web_Sessoes_Cookies_e_Seguranca/`

- 📌 Tópico 01: A anatomia do protocolo HTTP e as variáveis superglobais do PHP ($_GET, $_POST, $_REQUEST, $_SERVER)
- 📌 Tópico 02: Lendo cabeçalhos, método da requisição e envio de respostas formatadas com header()
- 📌 Tópico 03: Gerenciamento de estado na Web: Configurando, lendo e excluindo Cookies seguros no navegador (setcookie)
- 📌 Tópico 04: Trabalhando com Sessões de usuário ($_SESSION): session_start(), regeneração de ID e destruição
- 📌 Tópico 05: Segurança Web OWASP 1: Prevenção total contra Cross-Site Scripting (XSS) com htmlspecialchars() e escape de saída
- 📌 Tópico 06: Segurança Web OWASP 2: Prevenção contra Cross-Site Request Forgery (CSRF) através de tokens de validação em formulários
- 📌 Tópico 07: Segurança Web OWASP 3: Validação, sanitização e filtragem nativa de dados de entrada com filter_input() e filter_var()
- 📌 Tópico 08: Upload de arquivos seguro no PHP ($_FILES): Verificação de tipo MIME, tamanho, renomeação de hash e destinação segura
- 📌 Tópico 09: O manuseio correto de senhas: Por que NUNCA usar MD5/SHA? Hashing seguro com password_hash() (Bcrypt/Argon2) e password_verify()
- 📌 Tópico 10: Construindo um sistema de autenticação e controle de acesso de usuários completo e à prova de invasões

### 🔹 Módulo 6: Arquitetura MVC, Roteamento Limpo e Criação de APIs REST (Tópicos 51 a 60)
**Pasta de Resumos e Experimentos:** `/Modulo_06_Arquitetura_MVC_e_APIs_REST/`

- 📌 Tópico 01: O padrão arquitetural MVC (Model-View-Controller) no PHP: Separando lógica de dados, apresentação e controle
- 📌 Tópico 02: Construindo o roteador frontal de aplicação (Front Controller via index.php e .htaccess / reescrita de URLs)
- 📌 Tópico 03: O papel do Controller: Interceptando requisições HTTP, delegando ações aos Models e chamando as Views
- 📌 Tópico 04: O papel do Model e dos repositórios: Encapsulando regras de negócio e consultas ao banco PDO
- 📌 Tópico 05: O papel da View: Renderizando HTML limpo com sistemas de templates simples ou integração com o motor Twig
- 📌 Tópico 06: O que é uma API RESTful? Princípios de design, verbos HTTP (GET, POST, PUT, DELETE) e códigos de status HTTP em PHP
- 📌 Tópico 07: Retornando dados estruturados de APIs via JSON (json_encode e a resposta de cabeçalho Content-Type: application/json)
- 📌 Tópico 08: Recebendo e decodificando payloads JSON no corpo da requisição (file_get_contents('php://input') e json_decode)
- 📌 Tópico 09: Autenticação de APIs em PHP via Tokens de Portador (Bearer Token / JWT simples sem sessões estáticas)
- 📌 Tópico 10: Como frameworks modernos como Laravel e Symfony utilizam esses conceitos arquiteturais sob o capô

### 🔹 Módulo 7: Maestria Completa - Construindo um Sistema Backend MVC e API (Tópicos 61 a 70)
**Pasta de Resumos e Experimentos:** `/Modulo_07_Projetos_Reais_e_Maestria_PHP/`

- 📌 Tópico 01: Estruturação de um projeto PHP MVC moderno do zero seguindo o padrão PSR-4 e Autoloading com Composer
- 📌 Tópico 02: Desenvolvimento da classe Roteador interativa com suporte a parâmetros dinâmicos na URL (/livros/{id})
- 📌 Tópico 03: Criação dos Models e DAOs para o ecossistema literário ERP (Livros, Leitores e Empréstimos) integrados ao PDO
- 📌 Tópico 04: Implementação dos Controllers e rotas administrativas protegidas pelo Middleware de verificação de autenticação e sessão
- 📌 Tópico 05: Desenvolvimento da API RESTful simultânea para consumo por aplicações frontend (React / Next.js / Mobile)
- 📌 Tópico 06: Implementação de um sistema de log de auditoria do sistema em arquivos de texto locais com registro de IP e timestamp
- 📌 Tópico 07: Tratamento global de exceções na aplicação convertendo erros fatais em respostas JSON elegantes ou páginas de erro de UX alta
- 📌 Tópico 08: Otimização de desempenho em scripts PHP, cache de configuração e boas práticas para deploy com PHP-FPM / Nginx
- 📌 Tópico 09: Testes unitários e de integração na prática com a ferramenta padrão da indústria PHPUnit (Asserções e Mocks)
- 📌 Tópico 10: Projeto Final: O Backend Corporativo MVC & API RESTful Core PHP 8.3 Carlos Guedes

---

<div align="center">
  <p>💡 <i>"A constância nos estudos e o teste diário no código são os verdadeiros segredos para evoluir na engenharia de software."</i></p>
  <p><b>Caderno e laboratório mantido por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> ❤️🚀</b></p>
</div>
