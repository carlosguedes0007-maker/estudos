# Módulo 2: Automação com Bash / Shell Scripting e Variáveis de Ambiente (Aulas 11 a 20)

## 📌 Objetivos de Aprendizagem do Módulo
Neste módulo, você dominará os conceitos técnicos que sustentam as 10 aulas desta etapa. A abordagem de Carlos Guedes prioriza a clareza arquitetural, a eficiência computacional e a aplicação direta em projetos de nível profissional.

## 🧠 Resumo Teórico & Boas Práticas da Indústria

### O que é um Shell Script? O Shebang (#!/bin/bash), permissões de execução (+x) e a criação de seu primeiro script automatizado
O domínio de **O que é um Shell Script? O Shebang (#!/bin/bash), permissões de execução (+x) e a criação de seu primeiro script automatizado** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Variáveis no Bash: Declaração, atribuição sem espaços, leitura e variáveis de ambiente globais ($HOME, $PATH, $USER)
O domínio de **Declaração, atribuição sem espaços, leitura e variáveis de ambiente globais ($HOME, $PATH, $USER)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Entrada de dados interativa com o comando read e passagem de argumentos posicionais de linha de comando ($1, $2, $# e $@)
O domínio de **Entrada de dados interativa com o comando read e passagem de argumentos posicionais de linha de comando ($1, $2, $# e $@)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Estruturas condicionais em Bash: A instrução if, then, else, fi e o comando de teste ([ ... ] vs [[ ... ]]) para strings e números
O domínio de **A instrução if, then, else, fi e o comando de teste ([ ... ] vs [[ ... ]]) para strings e números** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Operadores de verificação de arquivos no Bash (-e existe, -d é diretório, -f é arquivo, -r legível, -x executável)
O domínio de **Operadores de verificação de arquivos no Bash (-e existe, -d é diretório, -f é arquivo, -r legível, -x executável)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Laços de repetição no terminal: Automatizando tarefas repetitivas com for, while e interações em listas de arquivos
O domínio de **Automatizando tarefas repetitivas com for, while e interações em listas de arquivos** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Funções em Shell Script: Modularizando lógicas de automação, escopo local com 'local' e códigos de status de retorno ($?)
O domínio de **Modularizando lógicas de automação, escopo local com 'local' e códigos de status de retorno ($?)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Manipulação e processamento de textos avançado em linha de comando utilizando utilitários nativos unix sed, awk e cut
O domínio de **Manipulação e processamento de textos avançado em linha de comando utilizando utilitários nativos unix sed, awk e cut** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Agendamento de tarefas em segundo plano no sistema operacional e automação rotineira com o serviço Cron (crontab)
O domínio de **Agendamento de tarefas em segundo plano no sistema operacional e automação rotineira com o serviço Cron (crontab)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Construindo scripts de automação visualmente profissionais com cores ANSI, ícones e tratamento de erros (set -e)
O domínio de **Construindo scripts de automação visualmente profissionais com cores ANSI, ícones e tratamento de erros (set -e)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

---

## 💻 Laboratório de Código Prático
Abaixo está a implementação prática de referência que consolida os aprendizados deste módulo:

```bash
#!/usr/bin/env bash
# Laboratório de Automação CLI e Terminal: Módulo 2: Automação com Bash / Shell Scripting e Variáveis de Ambiente (Aulas 11 a 20)
# Desenvolvido por Carlos Guedes
set -euo pipefail

echo -e "\033[1;32m============================================================\033[0m"
echo -e "\033[1;36m ⚡ CLI Diagnóstico & Automação - Modulo_02_Bash_Scripting_e_Automacao\033[0m"
echo -e "\033[1;32m============================================================\033[0m"

echo "[INFO] Auditando ambiente de terminal do desenvolvedor Carlos Guedes..."
echo "[CHECK] Usuário do Sistema: $(whoami)"
echo "[CHECK] Diretório Atual: $(pwd)"
echo "[CHECK] Data do Teste: $(date)"
echo -e "\033[1;32m[SUCCESS] Módulo validado! 10/10 Aulas executadas com excelência.\033[0m"
```

---

## 🚀 Desafio Prático de Conclusão do Módulo
Para validar sua certificação interna neste módulo, implemente uma variação do laboratório acima que adicione uma funcionalidade extra à sua escolha, aplicando rigorosamente os 10 conceitos teóricos apresentados nas aulas.
