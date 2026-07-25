<div align="center">

# 📓 Hacking Ético, Cibersegurança, InfoSec & Pentest (Meus Labs de Defesa) - Meu Caderno de Anotações (70+ Tópicos) 🚀

**Minhas anotações e laboratórios controlados sobre segurança cibernética, Wi-Fi WPA2/WPA3, OWASP Top 10 e análise de redes.**

[![Status](https://img.shields.io/badge/Status-70%2B_Tópicos_Estudados-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Estudante](https://img.shields.io/badge/Estudante-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

## 🎯 Visão Geral dos Meus Estudos

Este documento organiza o meu caderno pessoal de anotações, resumos teóricos e experimentos de código nesta especialização dentro do meu repositório de **Estudos**. Estruturei meu aprendizado rigorosamente em **7 Módulos de Investigação**, totalizando **70 tópicos de estudo detalhados**, onde documentei a teoria, armadilhas comuns, macetes corporativos e desenvolvi códigos de laboratório para fixar cada conceito.

---

## 📚 Índice de Resumos & Experimentos

### 🔹 Módulo 1: Fundamentos de InfoSec, O Código de Ética e Kali Linux (Tópicos 01 a 10)
**Pasta de Resumos e Experimentos:** `/Modulo_01_Fundamentos_e_Etica_InfoSec/`

- 📌 Tópico 01: O que é Hacking Ético? A diferença fundamental entre White Hat, Grey Hat e Black Hat Hacker
- 📌 Tópico 02: A Lei, a Ética e as Regras de Engajamento: Por que nunca devemos testar sistemas sem autorização formal e escrita por contrato (RoE)
- 📌 Tópico 03: Os três pilares fundamentais da Segurança da Informação: Confidencialidade, Integridade e Disponibilidade (A Tríade CIA)
- 📌 Tópico 04: Metodologias e fases padrão de um Teste de Intrusão (Pentest): Reconhecimento, Varredura, Exploração, Pós-Exploração e Relatório
- 📌 Tópico 05: O sistema operacional do hacker ético: Introdução ao Kali Linux e sua suíte de mais de 600 ferramentas pré-instaladas de segurança
- 📌 Tópico 06: Configuração de um laboratório de testes seguro e isolado em máquina virtual (VirtualBox / VMware) com redes exclusivas de host
- 📌 Tópico 07: Navegação e administração de sistemas Kali Linux via terminal: Comandos de rede essenciais (ifconfig, ip a, ping, traceroute, netstat)
- 📌 Tópico 08: O que é Anonimato na Web? Como funcionam endereços IP, MAC Address, servidores Proxy e a rede de roteamento em cebola Tor
- 📌 Tópico 09: Mascaramento de identidade em testes de rede locais: Como e por que alterar o endereço MAC de placas de rede com macchanger
- 📌 Tópico 10: OSINT (Open Source Intelligence): Conceitos e técnicas de coleta de informações públicas sobre alvos através de fontes abertas na Internet

### 🔹 Módulo 2: Segurança e Análise de Redes Wi-Fi (WPA2/WPA3 e Aircrack-ng) (Tópicos 11 a 20)
**Pasta de Resumos e Experimentos:** `/Modulo_02_Redes_Wifi_e_Monitoramento/`

- 📌 Tópico 01: A anatomia das redes sem fio (IEEE 802.11): Frequências de 2.4GHz vs 5GHz, canais de rádio, SSIDs, pontos de acesso (AP) e clientes
- 📌 Tópico 02: Modo Gerenciado (Managed Mode) vs Modo Monitor (Monitor Mode): A placa de rede wi-fi como ouvinte passivo de todo o tráfego de rádio
- 📌 Tópico 03: Colocando a interface de rede wireless em Modo Monitor com segurança utilizando o utilitário nativo airmon-ng start wlan0
- 📌 Tópico 04: Escaneamento de redes ao redor, identificação de SSIDs, endereços MAC (BSSID), canais de rádio e força de sinal com airodump-ng
- 📌 Tópico 05: Focando a captura de dados de rádio em um ponto de acesso específico e gravando pacotes de rede em arquivo .cap com airodump-ng -c -w
- 📌 Tópico 06: O Handshake WPA/WPA2 de 4 vias (4-Way Handshake): O momento exato em que a autenticação da senha acontece no ar
- 📌 Tópico 07: Forçando a captura do Handshake através do envio de pacotes de desautenticação (Deauth Attack) direcionados com aireplay-ng -0
- 📌 Tópico 08: Análise off-line de arquivos de captura e teste educacional de força de senha WPA2 utilizando dicionários com aircrack-ng e hashcat
- 📌 Tópico 09: Evolução da segurança wireless: Como o WPA3 e o protocolo SAE (Simultaneous Authentication of Equals) eliminam ataques offline de handshake
- 📌 Tópico 10: Defesa wireless de redes corporativas e residenciais: Segmentação de VLANs, desativação de WPS e políticas de senhas de alta entropia

### 🔹 Módulo 3: Reconhecimento de Redes, Port Scanning e Enumeração (Tópicos 21 a 30)
**Pasta de Resumos e Experimentos:** `/Modulo_03_Reconhecimento_e_Scanner_de_Redes/`

- 📌 Tópico 01: A fase de Varredura (Scanning): Identificando dispositivos ativos, portas abertas, serviços em execução e sistemas operacionais em uma rede
- 📌 Tópico 02: O padrão de ouro mundial para escaneamento de redes: Introdução ao Nmap (Network Mapper) e sua sintaxe fundamental
- 📌 Tópico 03: Técnicas de varredura no Nmap 1: Ping Scan (-sn) para descoberta de hosts e TCP Connect Scan (-sT) para conexões completas
- 📌 Tópico 04: Técnicas de varredura no Nmap 2: O furtivo TCP SYN Scan (-sS / Half-Open scan) e varredura de portas UDP (-sU)
- 📌 Tópico 05: Enumeração e identificação precisa de versões de serviços em execução nas portas abertas com a flag -sV do Nmap
- 📌 Tópico 06: Detecção remota do Sistema Operacional do alvo (OS Detection) com a flag -O e varredura agressiva combinada (-A)
- 📌 Tópico 07: O poder da automação de scanner: O Nmap Scripting Engine (NSE) e scripts de detecção de vulnerabilidades (nmap --script vuln)
- 📌 Tópico 08: Interceptação, inspeção e análise profunda de pacotes de rede em tempo real com o analisador de protocolos Wireshark / tshark
- 📌 Tópico 09: Entendendo o fluxo do protocolo TCP/IP, o Handshake TCP de 3 vias (SYN, SYN-ACK, ACK) e as bandeiras (Flags) de controle de rede
- 📌 Tópico 10: Identificação de vulnerabilidades conhecidas (CVEs) associadas às versões de software enumeradas durante a fase de varredura de rede

### 🔹 Módulo 4: Teste de Intrusão em Aplicações Web (OWASP Top 10) (Tópicos 31 a 40)
**Pasta de Resumos e Experimentos:** `/Modulo_04_Pentest_Web_OWASP_Top_10/`

- 📌 Tópico 01: A anatomia de uma aplicação Web moderna e a importância do projeto OWASP (Open Web Application Security Project) para desenvolvedores
- 📌 Tópico 02: OWASP A01 - Quebra de Controle de Acesso (Broken Access Control): IDOR (Insecure Direct Object References) e escalada de privilégios em APIs
- 📌 Tópico 03: OWASP A02 - Falhas Criptográficas (Cryptographic Failures): Transmissão de dados sensíveis sem criptografia forte e armazenamento inseguro
- 📌 Tópico 04: OWASP A03 - Injeção (Injection 1): SQL Injection na prática — Como identificar entradas vulneráveis e extrair bancos de dados com SQLMap
- 📌 Tópico 05: OWASP A03 - Injeção (Injection 2): Cross-Site Scripting (XSS Refletido, Armazenado e DOM-based) — Como scripts maliciosos roubam sessões
- 📌 Tópico 06: OWASP A03 - Injeção (Injection 3): Command Injection — Executando comandos arbitrários do sistema operacional na máquina do servidor web
- 📌 Tópico 07: OWASP A04 & A05 - Design Inseguro e Configuração Incorreta de Segurança (Security Misconfiguration): Diretórios abertos, senhas padrão e CORS desprotegido
- 📌 Tópico 08: OWASP A07 - Falhas de Identificação e Autenticação (Identification and Authentication Failures): Força bruta, Session Fixation e falta de Rate Limiting
- 📌 Tópico 09: OWASP A10 - Falsificação de Requisição do Lado do Servidor (SSRF - Server-Side Request Forgery): Fazendo o servidor atacar sua própria rede interna
- 📌 Tópico 10: A ferramenta canivete suíço do pentester web: Como utilizar o Burp Suite Community para interceptar, modificar e analisar requisições HTTP

### 🔹 Módulo 5: Criptografia, Entropia de Senhas e o Repositório 'senhas-logaritmo' (Tópicos 41 a 50)
**Pasta de Resumos e Experimentos:** `/Modulo_05_Criptografia_Logaritmos_e_Entropia/`

- 📌 Tópico 01: Os fundamentos matemáticos da criptografia: Por que a segurança digital mundial depende da complexidade de problemas matemáticos assintóticos?
- 📌 Tópico 02: Diferença entre Codificação (Base64, Hex), Hashing Criptográfico (MD5, SHA-1, SHA-256, SHA-512) e Criptografia (AES, RSA)
- 📌 Tópico 03: O conceito de Hash Colision (Colisão de Hash): Por que algoritmos antigos como MD5 e SHA-1 foram descontinuados para segurança de alto nível
- 📌 Tópico 04: A matemática do roubo de senhas: O que são Rainbow Tables (Tabelas arco-íris) e como o Salt (Salgado aleatório) inutiliza esse ataque
- 📌 Tópico 05: Estudo prático do repositório 'senhas-logaritmo' de Carlos Guedes: A aplicação de logaritmos na mensuração de força de credenciais
- 📌 Tópico 06: A fórmula de Entropia de Shannon (H = N * log2(L)): Calculando quantos bits reais de segurança uma senha possui no universo computacional
- 📌 Tópico 07: Simulação matemática de tempo para quebra de senhas por força bruta: Como GPUs modernas (RTX / ASICs) testam bilhões de hashes por segundo
- 📌 Tópico 08: Algoritmos modernos para armazenamento de senhas em bancos de dados: Por que Bcrypt, PBKDF2 e Argon2 possuem custo computacional (Work Factor) configurável
- 📌 Tópico 09: Criptografia assimétrica moderna na Web: O funcionamento de certificados digitais SSL/TLS, infraestrutura de chaves públicas (PKI) e HTTPS
- 📌 Tópico 10: Esteganografia digital: Os conceitos e técnicas de ocultação de arquivos secretos e dados criptografados dentro de imagens e áudios

### 🔹 Módulo 6: Engenharia Social, Exploração de Sistemas e Pós-Exploração (Tópicos 51 a 60)
**Pasta de Resumos e Experimentos:** `/Modulo_06_Engenharia_Social_e_Exploracao/`

- 📌 Tópico 01: A vulnerabilidade humana: O que é Engenharia Social e por que o fator humano continua sendo o elo mais fraco da segurança cibernética
- 📌 Tópico 02: Vetores de ataque de Engenharia Social: Phishing (e-mail enganoso), Spear Phishing (alvo direcionado), Vishing (voz) e Baiting (isca física)
- 📌 Tópico 03: Conceitos de Exploração de Vulnerabilidades: O que é um Exploit, um Payload e a diferença entre Bind Shell e Reverse Shell
- 📌 Tópico 04: O framework de penetração mais famoso do planeta: Introdução ao Metasploit Framework (msfconsole), busca de módulos e configuração de opções
- 📌 Tópico 05: Executando um teste educacional em sistema vulnerável (Metasploitable 2 / 3) com Metasploit: Selecionando exploit, configurando payload e obtendo shell
- 📌 Tópico 06: Pós-exploração no sistema invadido: O que fazer após obter acesso? Coleta de informações locais, escalada de privilégios e persistência
- 📌 Tópico 07: O que são Malwares? A classificação e comportamento dos principais tipos: Vírus, Worms, Trojans (Cavalo de Troia), Spywares e Rootkits
- 📌 Tópico 08: A maior ameaça cibernética da década: Como funcionam os Ransomwares (Sequestro de dados com criptografia de alta resistência e extorsão)
- 📌 Tópico 09: Conceitos de Evasão de Antivírus e Firewalls: Como os sistemas de defesa detectam ameaças por Assinatura (Hash) vs Comportamento (Heurística)
- 📌 Tópico 10: Metodologias de Hardening de Servidores Linux e Windows: Fechamento de portas, desativação de serviços inúteis e aplicação de patches de segurança

### 🔹 Módulo 7: Maestria em InfoSec - Laboratório Prático e Blue Team (Defesa) (Tópicos 61 a 70)
**Pasta de Resumos e Experimentos:** `/Modulo_07_Projetos_Reais_e_Defesa_Cibernetica/`

- 📌 Tópico 01: A transição do ataque para a defesa: Diferença entre Red Team (Ataque ofensivo), Blue Team (Defesa e monitoramento) e Purple Team (Colaboração integrada)
- 📌 Tópico 02: O que são sistemas de detecção e prevenção de intrusões de rede (IDS / IPS)? Introdução aos conceitos do Snort e Suricata na proteção do tráfego
- 📌 Tópico 03: Centralização e correlação de logs de segurança em tempo real: O papel dos sistemas SIEM (Security Information and Event Management) corporativos
- 📌 Tópico 04: Análise forense computacional básica: Como coletar evidências digitais em memória RAM e discos rígidos sem alterar os metadados dos arquivos (Cadeia de custódia)
- 📌 Tópico 05: Resposta a Incidentes de Segurança (Incident Response): Os 6 passos cruciais na contenção, erradicação e recuperação de um sistema hackeado
- 📌 Tópico 06: Projeto Prático de Segurança 1: Construindo um Script Python / CLI de auditoria de senhas e cálculo de entropia logarítmica com relatórios
- 📌 Tópico 07: Projeto Prático de Segurança 2: Configurando um laboratório de teste web local vulnerável (DVWA - Damn Vulnerable Web Application / OWASP Juice Shop)
- 📌 Tópico 08: Projeto Prático de Segurança 3: Executando um relatório completo de auditoria de vulnerabilidades em uma aplicação web de testes seguindo o OWASP Top 10
- 📌 Tópico 09: Escrita profissional de um Relatório Executivo de Teste de Intrusão (Pentest Report): Classificação de risco por CVSS (Common Vulnerability Scoring System) e remediação
- 📌 Tópico 10: Projeto Final: O Guia Definitivo do Hacker Ético, Engenharia de Defesa & Auditoria Cibernética Carlos Guedes

---

<div align="center">
  <p>💡 <i>"A constância nos estudos e o teste diário no código são os verdadeiros segredos para evoluir na engenharia de software."</i></p>
  <p><b>Caderno e laboratório mantido por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> ❤️🚀</b></p>
</div>
