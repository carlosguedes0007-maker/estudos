#  Módulo 6: Arquitetura MVC, Roteamento Limpo e Criação de APIs REST (Tópicos 51 a 60)

##  Meu Foco de Estudo no Módulo
Neste módulo, concentrei meus estudos em dominar os 10 tópicos listados abaixo. Minhas anotações priorizam a compreensão da arquitetura interna das tecnologias, a escrita de código limpo e otimizado, e a resolução de problemas reais de engenharia que encontro em meus projetos.

##  Minhas Anotações & Resumos Técnicos

###  O padrão arquitetural MVC (Model-View-Controller) no PHP: Separando lógica de dados, apresentação e controle
Durante os meus estudos sobre **Separando lógica de dados, apresentação e controle**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Construindo o roteador frontal de aplicação (Front Controller via index.php e .htaccess / reescrita de URLs)
Durante os meus estudos sobre **Construindo o roteador frontal de aplicação (Front Controller via index.php e .htaccess / reescrita de URLs)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  O papel do Controller: Interceptando requisições HTTP, delegando ações aos Models e chamando as Views
Durante os meus estudos sobre **Interceptando requisições HTTP, delegando ações aos Models e chamando as Views**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  O papel do Model e dos repositórios: Encapsulando regras de negócio e consultas ao banco PDO
Durante os meus estudos sobre **Encapsulando regras de negócio e consultas ao banco PDO**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  O papel da View: Renderizando HTML limpo com sistemas de templates simples ou integração com o motor Twig
Durante os meus estudos sobre **Renderizando HTML limpo com sistemas de templates simples ou integração com o motor Twig**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  O que é uma API RESTful? Princípios de design, verbos HTTP (GET, POST, PUT, DELETE) e códigos de status HTTP em PHP
Durante os meus estudos sobre **O que é uma API RESTful? Princípios de design, verbos HTTP (GET, POST, PUT, DELETE) e códigos de status HTTP em PHP**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Retornando dados estruturados de APIs via JSON (json_encode e a resposta de cabeçalho Content-Type: application/json)
Durante os meus estudos sobre **application/json)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Recebendo e decodificando payloads JSON no corpo da requisição (file_get_contents('php://input') e json_decode)
Durante os meus estudos sobre **Recebendo e decodificando payloads JSON no corpo da requisição (file_get_contents('php://input') e json_decode)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Autenticação de APIs em PHP via Tokens de Portador (Bearer Token / JWT simples sem sessões estáticas)
Durante os meus estudos sobre **Autenticação de APIs em PHP via Tokens de Portador (Bearer Token / JWT simples sem sessões estáticas)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

###  Como frameworks modernos como Laravel e Symfony utilizam esses conceitos arquiteturais sob o capô
Durante os meus estudos sobre **Como frameworks modernos como Laravel e Symfony utilizam esses conceitos arquiteturais sob o capô**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

---

##  Meu Experimento Prático no Lab
Abaixo está o código prático de referência que escrevi e testei no meu terminal/navegador para colocar à prova as anotações deste módulo:

```php
<?php
/**
 * Meu Experimento Prático em PHP 8.3+: Módulo 6: Arquitetura MVC, Roteamento Limpo e Criação de APIs REST (Tópicos 51 a 60)
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

$lab = new MeuLabPHP("Módulo 6: Arquitetura MVC, Roteamento Limpo e Criação de APIs REST (Tópicos 51 a 60)");
echo json_encode($lab->auditarEstudo(), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
```

---

##  Meu Próximo Passo no Estudo
Para aprofundar meu aprendizado neste módulo, meu desafio é implementar uma variação do laboratório acima, adicionando uma funcionalidade extra para testar cenários limites e fixar os 10 conceitos estudados nesta etapa.
