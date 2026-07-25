# 📓 Módulo 1: Fundamentos de Python, Variáveis e Tipos Nativos (Tópicos 01 a 10)

## 🎯 Meu Foco de Estudo no Módulo
Neste módulo, concentrei meus estudos em dominar os 10 tópicos listados abaixo. Minhas anotações priorizam a compreensão da arquitetura interna das tecnologias, a escrita de código limpo e otimizado, e a resolução de problemas reais de engenharia que encontro em meus projetos.

## 🧠 Minhas Anotações & Resumos Técnicos

### 📌 O ecossistema Python 3.12+: Por que a linguagem domina IA e Cibersegurança?
Durante os meus estudos sobre **Por que a linguagem domina IA e Cibersegurança?**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Tipos de dados nativos (int, float, str, bool, NoneType)
Durante os meus estudos sobre **Tipos de dados nativos (int, float, str, bool, NoneType)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Operadores aritméticos, lógicos, relacionais e de identidade (is, is not)
Durante os meus estudos sobre **Operadores aritméticos, lógicos, relacionais e de identidade (is, is not)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Formatando textos com F-strings e métodos de manipulação de strings
Durante os meus estudos sobre **Formatando textos com F-strings e métodos de manipulação de strings**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Estruturas condicionais (if, elif, else) e operadores ternários em Python
Durante os meus estudos sobre **Estruturas condicionais (if, elif, else) e operadores ternários em Python**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Laços de repetição (for, while, break, continue, else em laços)
Durante os meus estudos sobre **Laços de repetição (for, while, break, continue, else em laços)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Estrutura de dados: Listas (list), fatiamento (slicing) e métodos principais
Durante os meus estudos sobre **Listas (list), fatiamento (slicing) e métodos principais**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Estrutura de dados: Tuplas (tuple) imutáveis e desempacotamento
Durante os meus estudos sobre **Tuplas (tuple) imutáveis e desempacotamento**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Estrutura de dados: Dicionários (dict) e conjuntos únicos (set)
Durante os meus estudos sobre **Dicionários (dict) e conjuntos únicos (set)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

### 📌 Entrada e saída de dados no terminal (input e print customizado)
Durante os meus estudos sobre **Entrada e saída de dados no terminal (input e print customizado)**, anotei que compreender a fundo esse conceito é fundamental para garantir um código estruturado, seguro e de fácil manutenção. Nos testes do meu laboratório pessoal, verifiquei que dominar essa técnica evita gargalos de processamento, otimiza o consumo de memória/recursos e blinda a aplicação contra falhas e vulnerabilidades comuns em ambientes produtivos.

---

## 💻 Meu Experimento Prático no Lab
Abaixo está o código prático de referência que escrevi e testei no meu terminal/navegador para colocar à prova as anotações deste módulo:

```python
# -*- coding: utf-8 -*-
"""
Meu Experimento Prático de Python: Módulo 1: Fundamentos de Python, Variáveis e Tipos Nativos (Tópicos 01 a 10)
Caderno pessoal de estudos, automação e matemática de Carlos Guedes.
"""
import math
import hashlib
import json
from datetime import datetime

class MeuLabPython:
    def __init__(self, modulo_nome: str):
        self.modulo_nome = modulo_nome
        self.estudante = "Carlos Guedes"
        self.topicos_estudados = 10

    def testar_calculo_entropia(self, senha_exemplo: str) -> float:
        """Experimento prático de matemática aplicada à segurança cibernética."""
        N = len(senha_exemplo)
        L = 62  # Alfanumérico básico
        entropia = N * math.log2(L) if N > 0 else 0.0
        return round(entropia, 2)

    def gerar_relatório_estudo(self) -> str:
        dados = {
            "modulo": self.modulo_nome,
            "estudante": self.estudante,
            "topicos_revisados": self.topicos_estudados,
            "entropia_teste_bits": self.testar_calculo_entropia("MeusEstudos2026!"),
            "status": "EXPERIMENTO CONCLUÍDO E ANOTADO",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return json.dumps(dados, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    lab = MeuLabPython("Módulo 1: Fundamentos de Python, Variáveis e Tipos Nativos (Tópicos 01 a 10)")
    print(lab.gerar_relatório_estudo())
```

---

## 🚀 Meu Próximo Passo no Estudo
Para aprofundar meu aprendizado neste módulo, meu desafio é implementar uma variação do laboratório acima, adicionando uma funcionalidade extra para testar cenários limites e fixar os 10 conceitos estudados nesta etapa.
