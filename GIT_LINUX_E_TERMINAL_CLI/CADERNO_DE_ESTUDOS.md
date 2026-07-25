<div align="center">

# 📓 Git, Linux, CLI & Diagnóstico de Ambiente (Meus Comandos & Macetes) - Meu Caderno de Anotações (70+ Tópicos) 🚀

**Meus resumos práticos de terminal: controle de versão com Git, comandos Linux, Shell Scripting, Docker e automação.**

[![Status](https://img.shields.io/badge/Status-70%2B_Tópicos_Estudados-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Estudante](https://img.shields.io/badge/Estudante-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

## 🎯 Visão Geral dos Meus Estudos

Este documento organiza o meu caderno pessoal de anotações, resumos teóricos e experimentos de código nesta especialização dentro do meu repositório de **Estudos**. Estruturei meu aprendizado rigorosamente em **7 Módulos de Investigação**, totalizando **70 tópicos de estudo detalhados**, onde documentei a teoria, armadilhas comuns, macetes corporativos e desenvolvi códigos de laboratório para fixar cada conceito.

---

## 📚 Índice de Resumos & Experimentos

### 🔹 Módulo 1: O Poder do Terminal, Comandos Linux e Navegação no Sistema (Tópicos 01 a 10)
**Pasta de Resumos e Experimentos:** `/Modulo_01_Fundamentos_de_Terminal_e_Linux/`

- 📌 Tópico 01: A filosofia Unix/Linux: Por que a linha de comando (CLI) é a ferramenta mais rápida, flexível e poderosa do engenheiro de software?
- 📌 Tópico 02: A anatomia do Shell (Bash, Zsh, PowerShell): Prompt, caminhos absolutos vs relativos e estruturação de comandos
- 📌 Tópico 03: Navegação com precisão no sistema de arquivos: pwd, ls (e as flags essenciais -la, -lh), cd e árvore de diretórios
- 📌 Tópico 04: Gerenciamento de arquivos e pastas no terminal: mkdir, touch, cp, mv, rm (e os cuidados extremos com rm -rf)
- 📌 Tópico 05: Visualização e inspeção de conteúdo de arquivos na linha de comando: cat, less, more, head e tail (-f para acompanhamento ao vivo)
- 📌 Tópico 06: Redirecionamento de fluxos de entrada e saída (I/O Redirection): O operador > (sobrescrever), >> (anexar) e < (entrada)
- 📌 Tópico 07: O superpoder dos Pipes (|): Conectando a saída de um comando diretamente na entrada de outro para processamento encadeado
- 📌 Tópico 08: Pesquisa textual em tempo real no terminal com grep / ripgrep: Filtrando linhas por padrões e expressões regulares
- 📌 Tópico 09: Busca e localização ultraveloz de arquivos no sistema de arquivos com find e locate e execução de ações em massa com -exec
- 📌 Tópico 10: Permissões de arquivos no Linux/Unix (rwx - Leitura, Escrita, Execução), propriedade e os comandos chmod, chown e sudo

### 🔹 Módulo 2: Automação com Bash / Shell Scripting e Variáveis de Ambiente (Tópicos 11 a 20)
**Pasta de Resumos e Experimentos:** `/Modulo_02_Bash_Scripting_e_Automacao/`

- 📌 Tópico 01: O que é um Shell Script? O Shebang (#!/bin/bash), permissões de execução (+x) e a criação de seu primeiro script automatizado
- 📌 Tópico 02: Variáveis no Bash: Declaração, atribuição sem espaços, leitura e variáveis de ambiente globais ($HOME, $PATH, $USER)
- 📌 Tópico 03: Entrada de dados interativa com o comando read e passagem de argumentos posicionais de linha de comando ($1, $2, $# e $@)
- 📌 Tópico 04: Estruturas condicionais em Bash: A instrução if, then, else, fi e o comando de teste ([ ... ] vs [[ ... ]]) para strings e números
- 📌 Tópico 05: Operadores de verificação de arquivos no Bash (-e existe, -d é diretório, -f é arquivo, -r legível, -x executável)
- 📌 Tópico 06: Laços de repetição no terminal: Automatizando tarefas repetitivas com for, while e interações em listas de arquivos
- 📌 Tópico 07: Funções em Shell Script: Modularizando lógicas de automação, escopo local com 'local' e códigos de status de retorno ($?)
- 📌 Tópico 08: Manipulação e processamento de textos avançado em linha de comando utilizando utilitários nativos unix sed, awk e cut
- 📌 Tópico 09: Agendamento de tarefas em segundo plano no sistema operacional e automação rotineira com o serviço Cron (crontab)
- 📌 Tópico 10: Construindo scripts de automação visualmente profissionais com cores ANSI, ícones e tratamento de erros (set -e)

### 🔹 Módulo 3: Git Essencial, Controle de Versão e o Ciclo de Vida do Código (Tópicos 21 a 30)
**Pasta de Resumos e Experimentos:** `/Modulo_03_Git_Fundamentos_e_Controle/`

- 📌 Tópico 01: Por que o Git é o sistema de controle de versão distribuído padrão da indústria mundial? A arquitetura de snapshots do Git
- 📌 Tópico 02: Configuração inicial profissional do ambiente Git (git config --global user.name / user.email) e chaves SSH para autenticação no GitHub
- 📌 Tópico 03: As 3 áreas fundamentais do Git: Working Directory (Diretório de trabalho), Staging Area (Área de preparação) e Repository (Histórico oficial)
- 📌 Tópico 04: O ciclo de vida de um arquivo no Git (Untracked, Unmodified, Modified, Staged): git init, status, add e commit
- 📌 Tópico 05: Escrevendo o histórico da sua aplicação: Como funciona um Commit no Git e a importância de mensagens descritivas
- 📌 Tópico 06: Inspecionando a evolução do projeto: O log de commits com git log, --oneline, --graph, --all e a visualização das alterações com git diff
- 📌 Tópico 07: O arquivo de exclusão .gitignore: Como blindar seu repositório contra arquivos temporários, credenciais, .env e pastas de dependências (node_modules)
- 📌 Tópico 08: Desfazendo alterações em segurança na área de trabalho e na área de preparação com git restore e git reset --soft / --mixed
- 📌 Tópico 09: Viajando no tempo com git checkout e git switch: Navegando entre commits passados e restaurando estados anteriores da aplicação
- 📌 Tópico 10: O recurso salva-vidas do Git: Armazenando modificações temporariamente sem commitar utilizando git stash e git stash pop

### 🔹 Módulo 4: Ramificações (Branches), Mesclagens (Merge vs Rebase) e Conflitos (Tópicos 31 a 40)
**Pasta de Resumos e Experimentos:** `/Modulo_04_Git_Avancado_Branches_e_Merge/`

- 📌 Tópico 01: O conceito de Ramificação (Branch): Por que desenvolver funcionalidades isoladamente é a regra de ouro em equipes de software?
- 📌 Tópico 02: Criando, listando, navegando e excluindo branches em seu projeto local: O comando git branch, git switch -c e git checkout -b
- 📌 Tópico 03: Mesclando evoluções de código: O funcionamento técnico do git merge (Fast-Forward merge vs 3-Way merge com commit de junção)
- 📌 Tópico 04: O terror dos programadores desmitificado: O que causa um Conflito de Merge (Merge Conflict) no Git e como o terminal o sinaliza
- 📌 Tópico 05: Resolução prática e limpa de conflitos de merge manual ou no Visual Studio Code: Entendendo Current Change, Incoming Change e marcações <<<<<<<
- 📌 Tópico 06: A alternativa de histórico linear: Como funciona o git rebase, em que situações ele brilha e a regra de ouro: 'Nunca faça rebase em branches públicas'
- 📌 Tópico 07: Reescrevendo a história do código localmente: O rebase interativo (git rebase -i) para comprimir (squash), renomear (reword) ou reordenar commits
- 📌 Tópico 08: O comando cirúrgico git cherry-pick: Copiado e aplicando um commit específico de outra branch diretamente na sua ramificação atual
- 📌 Tópico 09: Investigação de bugs no histórico com precisão matemática: Como usar git blame para identificar autores e git bisect para caçar o commit exato que quebrou o código
- 📌 Tópico 10: O botão de emergência do Git: Como utilizar o git reflog para recuperar branches deletadas por engano ou reverter resets desastrosos

### 🔹 Módulo 5: Conventional Commits, Workflows, GitHub e Otimização CLI (Tópicos 41 a 50)
**Pasta de Resumos e Experimentos:** `/Modulo_05_Conventional_Commits_e_GitHub/`

- 📌 Tópico 01: O padrão internacional Conventional Commits (feat, fix, docs, style, refactor, perf, test, chore): Por que padronizar mensagens é obrigatório?
- 📌 Tópico 02: Como o padrão Conventional Commits habilita a geração automática de Changelogs (Semantic Versioning - SemVer 2.0.0 e Semantic Release)
- 📌 Tópico 03: Trabalhando com repositórios remotos no GitHub / GitLab / Bitbucket: Conectando repositórios locais com git remote add origin
- 📌 Tópico 04: Sincronizando código com o mundo: Enviando evoluções com git push -u origin, baixando com git fetch e atualizando com git pull
- 📌 Tópico 05: O fluxo de colaboração profissional na Web: O que é um Pull Request (PR) / Merge Request e como realizar revisões de código (Code Review)
- 📌 Tópico 06: Workflows de Git em equipes corporativas: Comparando GitFlow (develop, feature, release, hotfix) vs Trunk-Based Development vs GitHub Flow
- 📌 Tópico 07: Proteção de branches no GitHub (Branch Protection Rules): Impedindo pushes diretos em main / master e exigindo aprovações em Pull Requests
- 📌 Tópico 08: Automatizando validações antes do commit com Git Hooks locais (pre-commit, commit-msg) utilizando a ferramenta Husky e Lint-Staged
- 📌 Tópico 09: Análise profunda do repositório 'commit-craft-cli' de Carlos Guedes: Como criar um assistente de linha de comando interativo e ultrarrápido para Git
- 📌 Tópico 10: Produtividade extrema no terminal: Criando Aliases poderosos no Git (git st, git lg, git co) e customizando o prompt com Git Status

### 🔹 Módulo 6: Diagnóstico de Ambiente DevEnv Doctor, Redes TCP e Docker Básico (Tópicos 51 a 60)
**Pasta de Resumos e Experimentos:** `/Modulo_06_Diagnosticos_de_Ambiente_e_Docker/`

- 📌 Tópico 01: Gargalos de ambiente de desenvolvimento: Os problemas mais comuns no setup inicial de software e como diagnosticar em milissegundos
- 📌 Tópico 02: Auditoria de rede e portas TCP em conflito no Linux / Windows / macOS: Comandos nativos lsof -i, netstat, ss e resolução com kill -9
- 📌 Tópico 03: Análise profunda do repositório 'dev-env-doctor' de Carlos Guedes: Como auditar variáveis de ambiente, portas e integridade de repositórios ao vivo
- 📌 Tópico 04: Introdução ao mundo dos Contêineres: O problema do 'na minha máquina funciona' e a revolução da virtualização leve com Docker
- 📌 Tópico 05: Diferença entre Imagens Docker (modelos somente leitura) e Contêineres Docker (instâncias em execução na memória e CPU)
- 📌 Tópico 06: Comandos essenciais da CLI Docker: docker pull, docker run (-d, -p, -v, --name), docker ps, docker stop, docker rm e docker rmi
- 📌 Tópico 07: Escrevendo seu primeiro arquivo de receita Dockerfile: FROM, WORKDIR, COPY, RUN, EXPOSE e o comando de inicialização CMD / ENTRYPOINT
- 📌 Tópico 08: Containerização de aplicações modernas: Empacotando uma aplicação web HTML/CSS/JS e um backend em uma imagem customizada
- 📌 Tópico 09: Orquestração local de múltiplos contêineres com Docker Compose e o arquivo docker-compose.yml: Subindo aplicação e Banco de Dados com um único comando (docker compose up -d)
- 📌 Tópico 10: Monitoramento de logs de contêineres em tempo real com docker logs -f e inspeção interna de sistemas em execução com docker exec -it /bash

### 🔹 Módulo 7: Maestria Completa - Construindo uma Suíte CLI de Diagnóstico e Automação (Tópicos 61 a 70)
**Pasta de Resumos e Experimentos:** `/Modulo_07_Projetos_Reais_e_Maestria_DevOps/`

- 📌 Tópico 01: Arquitetura de uma ferramenta de automação e auditoria de ambiente 100% via linha de comando no terminal do desenvolvedor
- 📌 Tópico 02: Módulo 1 do Projeto CLI: Script Bash de verificação automática de dependências essenciais instaladas (Git, Node, Python, Docker, Curl)
- 📌 Tópico 03: Módulo 2 do Projeto CLI: Auditor instantâneo de portas TCP locais abertas com identificação de processo e opção de encerramento programático
- 📌 Tópico 04: Módulo 3 do Projeto CLI: Validador automático de padronização de mensagens Git no padrão Conventional Commits em repositórios locais
- 📌 Tópico 05: Módulo 4 do Projeto CLI: Verificador de integridade de repositórios Git (status de alteração, branch atual, commits não enviados ao remoto)
- 📌 Tópico 06: Módulo 5 do Projeto CLI: Gerador de arquivos estruturados .gitignore e Dockerfile customizados para stacks modernas (Node/Next, Python, PHP, Java)
- 📌 Tópico 07: Interface de terminal interativa e colorida com menus de navegação, ícones visuais e relatórios de auditoria formatados
- 📌 Tópico 08: Empacotamento da suíte CLI como um executável de linha de comando global no sistema operacional (Acessível via comando 'dev-doctor' ou 'agy-tools')
- 📌 Tópico 09: Criação de um pipeline de Integração Contínua (CI/CD) básico com GitHub Actions (.github/workflows) para testar e validar código automaticamente a cada push
- 📌 Tópico 10: Projeto Final: A Suíte de Automação de Terminal, Diagnóstico de Ambiente & Assistente Git (CommitCraft / DevEnv Doctor Core) Carlos Guedes

---

<div align="center">
  <p>💡 <i>"A constância nos estudos e o teste diário no código são os verdadeiros segredos para evoluir na engenharia de software."</i></p>
  <p><b>Caderno e laboratório mantido por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> ❤️🚀</b></p>
</div>
