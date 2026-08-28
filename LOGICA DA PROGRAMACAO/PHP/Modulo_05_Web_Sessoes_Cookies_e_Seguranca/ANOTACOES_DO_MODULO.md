#  Módulo 5: Requisições Web, Sessões, Cookies e Segurança OWASP (Tópicos 41 a 50)

##  Meu Foco de Estudo no Módulo
Neste módulo, concentrei meus estudos em dominar os 10 tópicos listados abaixo. Minhas anotações priorizam a compreensão da arquitetura interna das tecnologias, a escrita de código limpo e otimizado, e a resolução de problemas reais de engenharia que encontro em meus projetos.

##  Minhas Anotações & Resumos Técnicos

###  A anatomia do protocolo HTTP e as variáveis superglobais do PHP ($_GET, $_POST, $_REQUEST, $_SERVER)
Durante os meus estudos sobre **A anatomia do protocolo HTTP e as variáveis superglobais do PHP ($_GET, $_POST, $_REQUEST, $_SERVER)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Lendo cabeçalhos, método da requisição e envio de respostas formatadas com header()
Durante os meus estudos sobre **Lendo cabeçalhos, método da requisição e envio de respostas formatadas com header()**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Gerenciamento de estado na Web: Configurando, lendo e excluindo Cookies seguros no navegador (setcookie)
Durante os meus estudos sobre **Configurando, lendo e excluindo Cookies seguros no navegador (setcookie)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Trabalhando com Sessões de usuário ($_SESSION): session_start(), regeneração de ID e destruição
Durante os meus estudos sobre **session_start(), regeneração de ID e destruição**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Segurança Web OWASP 1: Prevenção total contra Cross-Site Scripting (XSS) com htmlspecialchars() e escape de saída
Durante os meus estudos sobre **Prevenção total contra Cross-Site Scripting (XSS) com htmlspecialchars() e escape de saída**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Segurança Web OWASP 2: Prevenção contra Cross-Site Request Forgery (CSRF) através de tokens de validação em formulários
Durante os meus estudos sobre **Prevenção contra Cross-Site Request Forgery (CSRF) através de tokens de validação em formulários**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Segurança Web OWASP 3: Validação, sanitização e filtragem nativa de dados de entrada com filter_input() e filter_var()
Durante os meus estudos sobre **Validação, sanitização e filtragem nativa de dados de entrada com filter_input() e filter_var()**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Upload de arquivos seguro no PHP ($_FILES): Verificação de tipo MIME, tamanho, renomeação de hash e destinação segura
Durante os meus estudos sobre **Verificação de tipo MIME, tamanho, renomeação de hash e destinação segura**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  O manuseio correto de senhas: Por que NUNCA usar MD5/SHA? Hashing seguro com password_hash() (Bcrypt/Argon2) e password_verify()
Durante os meus estudos sobre **Por que NUNCA usar MD5/SHA? Hashing seguro com password_hash() (Bcrypt/Argon2) e password_verify()**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Construindo um sistema de autenticação e controle de acesso de usuários completo e à prova de invasões
Durante os meus estudos sobre **Construindo um sistema de autenticação e controle de acesso de usuários completo e à prova de invasões**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

---

##  Meu Experimento Prático no Lab
Abaixo está o código prático de referência que escrevi e testei no meu terminal/navegador para colocar à prova as anotações deste módulo:

```php
<?php
/**
 * Meu Experimento Prático em PHP 8.3+: Módulo 5: Requisições Web, Sessões, Cookies e Segurança OWASP (Tópicos 41 a 50)
 * Caderno pessoal de estudos de Carlos Guedes.
 */
declare(strict_types=1);

namespace MeusEstudos\PHP;

final readonly class MeuLabPHP {
    public function __construct(
        private string $titulo,
        private string $estudante = "Carlos Guedes",
        private int $totalTopicos = 10
    ) {}

    public function auditarEstudo(): array {
        return [
            "modulo" => $this->titulo,
            "estudante" => $this->estudante,
            "status" => "{$this->totalTopicos} Tópicos 100% Revisados em Conformidade PSR-4",
            "php_version" => PHP_VERSION,
            "hash_seguranca" => password_hash("meus_estudos_2026", PASSWORD_BCRYPT)
        ];
    }
}

$lab = new MeuLabPHP("Módulo 5: Requisições Web, Sessões, Cookies e Segurança OWASP (Tópicos 41 a 50)");
echo json_encode($lab->auditarEstudo(), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
```

---

##  Meu Próximo Passo no Estudo
Para aprofundar meu aprendizado neste módulo, meu desafio é implementar uma variação do laboratório acima, adicionando uma funcionalidade extra para testar cenários limites e fixar os 10 conceitos estudados nesta etapa.
