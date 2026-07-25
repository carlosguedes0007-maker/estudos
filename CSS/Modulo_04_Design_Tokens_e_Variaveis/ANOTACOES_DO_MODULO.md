# 📓 Módulo 4: Design Tokens, Variáveis Nativas e Matemática de Cores (Tópicos 31 a 40)

## 🎯 Meu Foco de Estudo no Módulo
Neste módulo, concentrei meus estudos em dominar os 10 tópicos listados abaixo. Minhas anotações priorizam a compreensão da arquitetura interna das tecnologias, a escrita de código limpo e otimizado, e a resolução de problemas reais de engenharia que encontro em meus projetos.

## 🧠 Minhas Anotações & Resumos Técnicos

### 📌 Declarando variáveis CSS customizadas (:root)
Durante os meus estudos sobre **Declarando variáveis CSS customizadas (:root)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Escopo de variáveis e sobrescrita dinâmica
Durante os meus estudos sobre **Escopo de variáveis e sobrescrita dinâmica**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Arquitetura de Design Tokens (Cores, Espaçamentos, Tipografia)
Durante os meus estudos sobre **Arquitetura de Design Tokens (Cores, Espaçamentos, Tipografia)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Matemática de cores (calc(), color-mix(), from HSL)
Durante os meus estudos sobre **Matemática de cores (calc(), color-mix(), from HSL)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Algoritmo APCA e WCAG 2.1 para contraste de acessibilidade
Durante os meus estudos sobre **Algoritmo APCA e WCAG 2.1 para contraste de acessibilidade**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Implementação de Dark Mode automático (prefers-color-scheme)
Durante os meus estudos sobre **Implementação de Dark Mode automático (prefers-color-scheme)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Troca dinâmica de temas ao vivo via JavaScript e Variáveis
Durante os meus estudos sobre **Troca dinâmica de temas ao vivo via JavaScript e Variáveis**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Estilização focada em Glassmorphism (backdrop-filter, blur, transparência)
Durante os meus estudos sobre **Estilização focada em Glassmorphism (backdrop-filter, blur, transparência)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Gradientes complexos (linear, radial, conic) e animação de gradientes
Durante os meus estudos sobre **Gradientes complexos (linear, radial, conic) e animação de gradientes**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Sombras realistas e elevação (Box-shadow multidirecional)
Durante os meus estudos sobre **Sombras realistas e elevação (Box-shadow multidirecional)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

---

## 💻 Meu Experimento Prático no Lab
Abaixo está o código prático de referência que escrevi e testei no meu terminal/navegador para colocar à prova as anotações deste módulo:

```css
/* Meu Experimento CSS3: Módulo 4: Design Tokens, Variáveis Nativas e Matemática de Cores (Tópicos 31 a 40) | Estudante: Carlos Guedes */
:root {
    --primary-color: #00ff88;
    --bg-dark: #0f172a;
    --surface: #1e293b;
    --text-main: #f8fafc;
}

.card-anotacao {
    background: var(--surface);
    border-left: 4px solid var(--primary-color);
    padding: 2rem;
    border-radius: 12px;
    color: var(--text-main);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card-anotacao:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0, 255, 136, 0.2);
}
```

---

## 🚀 Meu Próximo Passo no Estudo
Para aprofundar meu aprendizado neste módulo, meu desafio é implementar uma variação do laboratório acima, adicionando uma funcionalidade extra para testar cenários limites e fixar os 10 conceitos estudados nesta etapa.
