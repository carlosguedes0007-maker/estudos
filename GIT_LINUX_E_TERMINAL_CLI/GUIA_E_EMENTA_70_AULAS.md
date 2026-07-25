<div align="center">

# 📖 Git, Conventional Commits, Linux, CLI & Diagnóstico de Ambiente - Ementa Completa (70+ Aulas) 🚀

**Trilha essencial para o desenvolvedor de alta performance: controle de versão, Linux, Shell Scripting, Docker e automação de terminal.**

[![Status](https://img.shields.io/badge/Status-70%2B_Aulas_Concluídas-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Autor](https://img.shields.io/badge/Autor-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

## 🎯 Visão Geral da Trilha de Especialização

Este documento representa o plano pedagógico e técnico integral desta especialização dentro do hub **Estudos**. O conteúdo foi divido rigorosamente em **7 Módulos de Maestria Progressive**, totalizando **70 aulas detalhadas**, com códigos, fundamentos científicos, melhores práticas da indústria e desafios de engenharia.

---

## 📚 Índice de Módulos & Aulas

### 🔹 Módulo 1: O Poder do Terminal, Comandos Linux e Navegação no Sistema (Aulas 01 a 10)
**Diretório de Aulas e Práticas:** `/Modulo_01_Fundamentos_de_Terminal_e_Linux/`

- A filosofia Unix/Linux: Por que a linha de comando (CLI) é a ferramenta mais rápida, flexível e poderosa do engenheiro de software?
- A anatomia do Shell (Bash, Zsh, PowerShell): Prompt, caminhos absolutos vs relativos e estruturação de comandos
- Navegação com precisão no sistema de arquivos: pwd, ls (e as flags essenciais -la, -lh), cd e árvore de diretórios
- Gerenciamento de arquivos e pastas no terminal: mkdir, touch, cp, mv, rm (e os cuidados extremos com rm -rf)
- Visualização e inspeção de conteúdo de arquivos na linha de comando: cat, less, more, head e tail (-f para acompanhamento ao vivo)
- Redirecionamento de fluxos de entrada e saída (I/O Redirection): O operador > (sobrescrever), >> (anexar) e < (entrada)
- O superpoder dos Pipes (|): Conectando a saída de um comando diretamente na entrada de outro para processamento encadeado
- Pesquisa textual em tempo real no terminal com grep / ripgrep: Filtrando linhas por padrões e expressões regulares
- Busca e localização ultraveloz de arquivos no sistema de arquivos com find e locate e execução de ações em massa com -exec
- Permissões de arquivos no Linux/Unix (rwx - Leitura, Escrita, Execução), propriedade e os comandos chmod, chown e sudo

### 🔹 Módulo 2: Automação com Bash / Shell Scripting e Variáveis de Ambiente (Aulas 11 a 20)
**Diretório de Aulas e Práticas:** `/Modulo_02_Bash_Scripting_e_Automacao/`

- O que é um Shell Script? O Shebang (#!/bin/bash), permissões de execução (+x) e a criação de seu primeiro script automatizado
- Variáveis no Bash: Declaração, atribuição sem espaços, leitura e variáveis de ambiente globais ($HOME, $PATH, $USER)
- Entrada de dados interativa com o comando read e passagem de argumentos posicionais de linha de comando ($1, $2, $# e $@)
- Estruturas condicionais em Bash: A instrução if, then, else, fi e o comando de teste ([ ... ] vs [[ ... ]]) para strings e números
- Operadores de verificação de arquivos no Bash (-e existe, -d é diretório, -f é arquivo, -r legível, -x executável)
- Laços de repetição no terminal: Automatizando tarefas repetitivas com for, while e interações em listas de arquivos
- Funções em Shell Script: Modularizando lógicas de automação, escopo local com 'local' e códigos de status de retorno ($?)
- Manipulação e processamento de textos avançado em linha de comando utilizando utilitários nativos unix sed, awk e cut
- Agendamento de tarefas em segundo plano no sistema operacional e automação rotineira com o serviço Cron (crontab)
- Construindo scripts de automação visualmente profissionais com cores ANSI, ícones e tratamento de erros (set -e)

### 🔹 Módulo 3: Git Essencial, Controle de Versão e o Ciclo de Vida do Código (Aulas 21 a 30)
**Diretório de Aulas e Práticas:** `/Modulo_03_Git_Fundamentos_e_Controle/`

- Por que o Git é o sistema de controle de versão distribuído padrão da indústria mundial? A arquitetura de snapshots do Git
- Configuração inicial profissional do ambiente Git (git config --global user.name / user.email) e chaves SSH para autenticação no GitHub
- As 3 áreas fundamentais do Git: Working Directory (Diretório de trabalho), Staging Area (Área de preparação) e Repository (Histórico oficial)
- O ciclo de vida de um arquivo no Git (Untracked, Unmodified, Modified, Staged): git init, status, add e commit
- Escrevendo o histórico da sua aplicação: Como funciona um Commit no Git e a importância de mensagens descritivas
- Inspecionando a evolução do projeto: O log de commits com git log, --oneline, --graph, --all e a visualização das alterações com git diff
- O arquivo de exclusão .gitignore: Como blindar seu repositório contra arquivos temporários, credenciais, .env e pastas de dependências (node_modules)
- Desfazendo alterações em segurança na área de trabalho e na área de preparação com git restore e git reset --soft / --mixed
- Viajando no tempo com git checkout e git switch: Navegando entre commits passados e restaurando estados anteriores da aplicação
- O recurso salva-vidas do Git: Armazenando modificações temporariamente sem commitar utilizando git stash e git stash pop

### 🔹 Módulo 4: Ramificações (Branches), Mesclagens (Merge vs Rebase) e Conflitos (Aulas 31 a 40)
**Diretório de Aulas e Práticas:** `/Modulo_04_Git_Avancado_Branches_e_Merge/`

- O conceito de Ramificação (Branch): Por que desenvolver funcionalidades isoladamente é a regra de ouro em equipes de software?
- Criando, listando, navegando e excluindo branches em seu projeto local: O comando git branch, git switch -c e git checkout -b
- Mesclando evoluções de código: O funcionamento técnico do git merge (Fast-Forward merge vs 3-Way merge com commit de junção)
- O terror dos programadores desmitificado: O que causa um Conflito de Merge (Merge Conflict) no Git e como o terminal o sinaliza
- Resolução prática e limpa de conflitos de merge manual ou no Visual Studio Code: Entendendo Current Change, Incoming Change e marcações <<<<<<<
- A alternativa de histórico linear: Como funciona o git rebase, em que situações ele brilha e a regra de ouro: 'Nunca faça rebase em branches públicas'
- Reescrevendo a história do código localmente: O rebase interativo (git rebase -i) para comprimir (squash), renomear (reword) ou reordenar commits
- O comando cirúrgico git cherry-pick: Copiado e aplicando um commit específico de outra branch diretamente na sua ramificação atual
- Investigação de bugs no histórico com precisão matemática: Como usar git blame para identificar autores e git bisect para caçar o commit exato que quebrou o código
- O botão de emergência do Git: Como utilizar o git reflog para recuperar branches deletadas por engano ou reverter resets desastrosos

### 🔹 Módulo 5: Conventional Commits, Workflows, GitHub e Otimização CLI (Aulas 41 a 50)
**Diretório de Aulas e Práticas:** `/Modulo_05_Conventional_Commits_e_GitHub/`

- O padrão internacional Conventional Commits (feat, fix, docs, style, refactor, perf, test, chore): Por que padronizar mensagens é obrigatório?
- Como o padrão Conventional Commits habilita a geração automática de Changelogs (Semantic Versioning - SemVer 2.0.0 e Semantic Release)
- Trabalhando com repositórios remotos no GitHub / GitLab / Bitbucket: Conectando repositórios locais com git remote add origin
- Sincronizando código com o mundo: Enviando evoluções com git push -u origin, baixando com git fetch e atualizando com git pull
- O fluxo de colaboração profissional na Web: O que é um Pull Request (PR) / Merge Request e como realizar revisões de código (Code Review)
- Workflows de Git em equipes corporativas: Comparando GitFlow (develop, feature, release, hotfix) vs Trunk-Based Development vs GitHub Flow
- Proteção de branches no GitHub (Branch Protection Rules): Impedindo pushes diretos em main / master e exigindo aprovações em Pull Requests
- Automatizando validações antes do commit com Git Hooks locais (pre-commit, commit-msg) utilizando a ferramenta Husky e Lint-Staged
- Análise profunda do repositório 'commit-craft-cli' de Carlos Guedes: Como criar um assistente de linha de comando interativo e ultrarrápido para Git
- Produtividade extrema no terminal: Criando Aliases poderosos no Git (git st, git lg, git co) e customizando o prompt com Git Status

### 🔹 Módulo 6: Diagnóstico de Ambiente DevEnv Doctor, Redes TCP e Docker Básico (Aulas 51 a 60)
**Diretório de Aulas e Práticas:** `/Modulo_06_Diagnosticos_de_Ambiente_e_Docker/`

- Gargalos de ambiente de desenvolvimento: Os problemas mais comuns no setup inicial de software e como diagnosticar em milissegundos
- Auditoria de rede e portas TCP em conflito no Linux / Windows / macOS: Comandos nativos lsof -i, netstat, ss e resolução com kill -9
- Análise profunda do repositório 'dev-env-doctor' de Carlos Guedes: Como auditar variáveis de ambiente, portas e integridade de repositórios ao vivo
- Introdução ao mundo dos Contêineres: O problema do 'na minha máquina funciona' e a revolução da virtualização leve com Docker
- Diferença entre Imagens Docker (modelos somente leitura) e Contêineres Docker (instâncias em execução na memória e CPU)
- Comandos essenciais da CLI Docker: docker pull, docker run (-d, -p, -v, --name), docker ps, docker stop, docker rm e docker rmi
- Escrevendo seu primeiro arquivo de receita Dockerfile: FROM, WORKDIR, COPY, RUN, EXPOSE e o comando de inicialização CMD / ENTRYPOINT
- Containerização de aplicações modernas: Empacotando uma aplicação web HTML/CSS/JS e um backend em uma imagem customizada
- Orquestração local de múltiplos contêineres com Docker Compose e o arquivo docker-compose.yml: Subindo aplicação e Banco de Dados com um único comando (docker compose up -d)
- Monitoramento de logs de contêineres em tempo real com docker logs -f e inspeção interna de sistemas em execução com docker exec -it /bash

### 🔹 Módulo 7: Maestria Completa - Construindo uma Suíte CLI de Diagnóstico e Automação (Aulas 61 a 70)
**Diretório de Aulas e Práticas:** `/Modulo_07_Projetos_Reais_e_Maestria_DevOps/`

- Arquitetura de uma ferramenta de automação e auditoria de ambiente 100% via linha de comando no terminal do desenvolvedor
- Módulo 1 do Projeto CLI: Script Bash de verificação automática de dependências essenciais instaladas (Git, Node, Python, Docker, Curl)
- Módulo 2 do Projeto CLI: Auditor instantâneo de portas TCP locais abertas com identificação de processo e opção de encerramento programático
- Módulo 3 do Projeto CLI: Validador automático de padronização de mensagens Git no padrão Conventional Commits em repositórios locais
- Módulo 4 do Projeto CLI: Verificador de integridade de repositórios Git (status de alteração, branch atual, commits não enviados ao remoto)
- Módulo 5 do Projeto CLI: Gerador de arquivos estruturados .gitignore e Dockerfile customizados para stacks modernas (Node/Next, Python, PHP, Java)
- Interface de terminal interativa e colorida com menus de navegação, ícones visuais e relatórios de auditoria formatados
- Empacotamento da suíte CLI como um executável de linha de comando global no sistema operacional (Acessível via comando 'dev-doctor' ou 'agy-tools')
- Criação de um pipeline de Integração Contínua (CI/CD) básico com GitHub Actions (.github/workflows) para testar e validar código automaticamente a cada push
- Projeto Final: A Suíte de Automação de Terminal, Diagnóstico de Ambiente & Assistente Git (CommitCraft / DevEnv Doctor Core) Carlos Guedes

---

<div align="center">
  <p>💡 <i>"O estudo metódico, aliado à prática contínua, é o caminho indiscutível para a maestria em engenharia de software."</i></p>
  <p><b>Desenvolvido com precisão tecnológica por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> ❤️🚀</b></p>
</div>
