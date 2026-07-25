<div align="center">

# 📖 PHP 8.3+, POO, PDO, MVC & Segurança no Desenvolvimento Web - Ementa Completa (70+ Aulas) 🚀

**Trilha completa sobre o motor da web moderna: PHP 8.3, tipagem estrita, banco de dados seguro, arquitetura MVC e Autoload PSR-4.**

[![Status](https://img.shields.io/badge/Status-70%2B_Aulas_Concluídas-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Autor](https://img.shields.io/badge/Autor-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

## 🎯 Visão Geral da Trilha de Especialização

Este documento representa o plano pedagógico e técnico integral desta especialização dentro do hub **Estudos**. O conteúdo foi divido rigorosamente em **7 Módulos de Maestria Progressive**, totalizando **70 aulas detalhadas**, com códigos, fundamentos científicos, melhores práticas da indústria e desafios de engenharia.

---

## 📚 Índice de Módulos & Aulas

### 🔹 Módulo 1: PHP 8.3+, Sintaxe, Tipagem Estrita e Estruturas (Aulas 01 a 10)
**Diretório de Aulas e Práticas:** `/Modulo_01_Fundamentos_e_Sintaxe_PHP/`

- O PHP moderno no servidor web e a declaração de tipagem estrita (declare(strict_types=1);)
- A estrutura do arquivo .php, tags de abertura e a função echo vs print
- Variáveis, tipos escalares (int, float, string, bool) e verificação com var_dump() e is_type()
- Operadores aritméticos, lógicos, relacionais e o operador Spaceship (<=>)
- O operador Null Coalescing (??) e Null Coalescing Assignment (??=)
- Estruturas de controle de fluxo condicionais (if, elseif, else e ternário)
- A poderosa estrutura de decisão Match (PHP 8+): Limpa, estrita e com retorno de valor
- Laços de repetição (for, while, do-while) e o iterador de arrays foreach
- Arrays no PHP: O tipo mais versátil (Arrays indexados vs Arrays associativos chave-valor)
- Manipulação avançada de arrays (array_map, array_filter, array_reduce, count, in_array, explode, implode)

### 🔹 Módulo 2: Funções, Orientação a Objetos Moderna e Construtores (Aulas 11 a 20)
**Diretório de Aulas e Práticas:** `/Modulo_02_Funcoes_e_Orientacao_a_Objetos/`

- Definindo funções em PHP com tipagem de parâmetros e tipagem de retorno
- Parâmetros padrão, argumentos nomeados (Named Arguments) e empacotamento variádico (...$args)
- Funções anônimas (Closures) e Arrow Functions (fn() => ...) no PHP 8
- Introdução à Orientação a Objetos em PHP: Classes, Objetos e a pseudo-variável $this
- Propriedades e métodos, modificadores de visibilidade (public, protected, private)
- O método construtor (__construct) e a Promoção de Propriedades no Construtor (PHP 8+)
- Propriedades somente leitura (readonly properties e readonly classes)
- Herança com extends, chamada ao pai com parent:: e sobrescrita de métodos
- Polimorfismo, classes e métodos abstratos (abstract) no PHP
- Interfaces corporativas em PHP (interface e implements): Garantindo contratos de implementação

### 🔹 Módulo 3: Traits, Enums, Métodos Mágicos e Autoloading PSR-4 (Aulas 21 a 30)
**Diretório de Aulas e Práticas:** `/Modulo_03_Recursos_Avancados_de_POO/`

- O que são Traits em PHP? Compartilhando comportamentos na ausência de herança múltipla
- Enums (Enumerações no PHP 8.1+): Enums puros e Enums de suporte (Backed Enums com valores string/int)
- Propriedades e métodos estáticos (static) e o operador de resolução de escopo (::)
- O conceito de Late Static Binding (self:: vs static::) em hierarquias
- Métodos mágicos fundamentais: __toString(), __get(), __set(), __call()
- Clonagem de objetos no PHP com a palavra-chave clone e o método mágico __clone()
- Namespaces em PHP: Evitando conflito de nomes e organizando pacotes corporativos
- A especificação de Autoloading PSR-4 da PHP-FIG: Carregamento automático de classes sem require/include
- Gerenciamento de pacotes profissionais com Composer e o arquivo composer.json
- O tratamento moderno de exceções com try, catch, finally e a interface Throwable

### 🔹 Módulo 4: Acesso Seguro ao Banco de Dados Relacional com PDO (Aulas 31 a 40)
**Diretório de Aulas e Práticas:** `/Modulo_04_Banco_de_Dados_com_PDO/`

- Por que abandonar as funções antigas mysql_* / mysqli e usar exclusivamente a extensão PDO (PHP Data Objects)?
- Estabelecendo uma conexão segura com MySQL / PostgreSQL via DSN e tratamento de exceções PDOException
- O maior perigo da Web: Injeção de SQL (SQL Injection) e como ela destrói sistemas desprotegidos
- A blindagem absoluta: Prepared Statements (Declarações preparadas) com parâmetros posicionais (?) e nomeados (:param)
- Executando consultas de seleção (SELECT) com fetch() e fetchAll() e modos de retorno (PDO::FETCH_ASSOC vs PDO::FETCH_OBJ)
- Mapeamento Direto Objeto-Relacional: Hidratando instâncias de classes automáticas com PDO::FETCH_CLASS
- Executando mutações seguras (INSERT, UPDATE, DELETE) e capturando o ID gerado com lastInsertId()
- A importância crítica das Transações de Banco de Dados (ACID): beginTransaction(), commit() e rollBack()
- Paginação eficiente de resultados SQL no backend PHP com LIMIT e OFFSET
- Construindo uma classe Database Singleton modularizada e à prova de falhas

### 🔹 Módulo 5: Requisições Web, Sessões, Cookies e Segurança OWASP (Aulas 41 a 50)
**Diretório de Aulas e Práticas:** `/Modulo_05_Web_Sessoes_Cookies_e_Seguranca/`

- A anatomia do protocolo HTTP e as variáveis superglobais do PHP ($_GET, $_POST, $_REQUEST, $_SERVER)
- Lendo cabeçalhos, método da requisição e envio de respostas formatadas com header()
- Gerenciamento de estado na Web: Configurando, lendo e excluindo Cookies seguros no navegador (setcookie)
- Trabalhando com Sessões de usuário ($_SESSION): session_start(), regeneração de ID e destruição
- Segurança Web OWASP 1: Prevenção total contra Cross-Site Scripting (XSS) com htmlspecialchars() e escape de saída
- Segurança Web OWASP 2: Prevenção contra Cross-Site Request Forgery (CSRF) através de tokens de validação em formulários
- Segurança Web OWASP 3: Validação, sanitização e filtragem nativa de dados de entrada com filter_input() e filter_var()
- Upload de arquivos seguro no PHP ($_FILES): Verificação de tipo MIME, tamanho, renomeação de hash e destinação segura
- O manuseio correto de senhas: Por que NUNCA usar MD5/SHA? Hashing seguro com password_hash() (Bcrypt/Argon2) e password_verify()
- Construindo um sistema de autenticação e controle de acesso de usuários completo e à prova de invasões

### 🔹 Módulo 6: Arquitetura MVC, Roteamento Limpo e Criação de APIs REST (Aulas 51 a 60)
**Diretório de Aulas e Práticas:** `/Modulo_06_Arquitetura_MVC_e_APIs_REST/`

- O padrão arquitetural MVC (Model-View-Controller) no PHP: Separando lógica de dados, apresentação e controle
- Construindo o roteador frontal de aplicação (Front Controller via index.php e .htaccess / reescrita de URLs)
- O papel do Controller: Interceptando requisições HTTP, delegando ações aos Models e chamando as Views
- O papel do Model e dos repositórios: Encapsulando regras de negócio e consultas ao banco PDO
- O papel da View: Renderizando HTML limpo com sistemas de templates simples ou integração com o motor Twig
- O que é uma API RESTful? Princípios de design, verbos HTTP (GET, POST, PUT, DELETE) e códigos de status HTTP em PHP
- Retornando dados estruturados de APIs via JSON (json_encode e a resposta de cabeçalho Content-Type: application/json)
- Recebendo e decodificando payloads JSON no corpo da requisição (file_get_contents('php://input') e json_decode)
- Autenticação de APIs em PHP via Tokens de Portador (Bearer Token / JWT simples sem sessões estáticas)
- Como frameworks modernos como Laravel e Symfony utilizam esses conceitos arquiteturais sob o capô

### 🔹 Módulo 7: Maestria Completa - Construindo um Sistema Backend MVC e API (Aulas 61 a 70)
**Diretório de Aulas e Práticas:** `/Modulo_07_Projetos_Reais_e_Maestria_PHP/`

- Estruturação de um projeto PHP MVC moderno do zero seguindo o padrão PSR-4 e Autoloading com Composer
- Desenvolvimento da classe Roteador interativa com suporte a parâmetros dinâmicos na URL (/livros/{id})
- Criação dos Models e DAOs para o ecossistema literário ERP (Livros, Leitores e Empréstimos) integrados ao PDO
- Implementação dos Controllers e rotas administrativas protegidas pelo Middleware de verificação de autenticação e sessão
- Desenvolvimento da API RESTful simultânea para consumo por aplicações frontend (React / Next.js / Mobile)
- Implementação de um sistema de log de auditoria do sistema em arquivos de texto locais com registro de IP e timestamp
- Tratamento global de exceções na aplicação convertendo erros fatais em respostas JSON elegantes ou páginas de erro de UX alta
- Otimização de desempenho em scripts PHP, cache de configuração e boas práticas para deploy com PHP-FPM / Nginx
- Testes unitários e de integração na prática com a ferramenta padrão da indústria PHPUnit (Asserções e Mocks)
- Projeto Final: O Backend Corporativo MVC & API RESTful Core PHP 8.3 Carlos Guedes

---

<div align="center">
  <p>💡 <i>"O estudo metódico, aliado à prática contínua, é o caminho indiscutível para a maestria em engenharia de software."</i></p>
  <p><b>Desenvolvido com precisão tecnológica por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> ❤️🚀</b></p>
</div>
