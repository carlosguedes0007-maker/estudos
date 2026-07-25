<div align="center">

# 📖 Hacking Ético, Cibersegurança, InfoSec & Pentest Web - Ementa Completa (70+ Aulas) 🚀

**Trilha imersiva de segurança cibernética: análise de redes, Wi-Fi WPA2/WPA3, OWASP Top 10, entropia e defesa computacional.**

[![Status](https://img.shields.io/badge/Status-70%2B_Aulas_Concluídas-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Autor](https://img.shields.io/badge/Autor-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

## 🎯 Visão Geral da Trilha de Especialização

Este documento representa o plano pedagógico e técnico integral desta especialização dentro do hub **Estudos**. O conteúdo foi divido rigorosamente em **7 Módulos de Maestria Progressive**, totalizando **70 aulas detalhadas**, com códigos, fundamentos científicos, melhores práticas da indústria e desafios de engenharia.

---

## 📚 Índice de Módulos & Aulas

### 🔹 Módulo 1: Fundamentos de InfoSec, O Código de Ética e Kali Linux (Aulas 01 a 10)
**Diretório de Aulas e Práticas:** `/Modulo_01_Fundamentos_e_Etica_InfoSec/`

- O que é Hacking Ético? A diferença fundamental entre White Hat, Grey Hat e Black Hat Hacker
- A Lei, a Ética e as Regras de Engajamento: Por que nunca devemos testar sistemas sem autorização formal e escrita por contrato (RoE)
- Os três pilares fundamentais da Segurança da Informação: Confidencialidade, Integridade e Disponibilidade (A Tríade CIA)
- Metodologias e fases padrão de um Teste de Intrusão (Pentest): Reconhecimento, Varredura, Exploração, Pós-Exploração e Relatório
- O sistema operacional do hacker ético: Introdução ao Kali Linux e sua suíte de mais de 600 ferramentas pré-instaladas de segurança
- Configuração de um laboratório de testes seguro e isolado em máquina virtual (VirtualBox / VMware) com redes exclusivas de host
- Navegação e administração de sistemas Kali Linux via terminal: Comandos de rede essenciais (ifconfig, ip a, ping, traceroute, netstat)
- O que é Anonimato na Web? Como funcionam endereços IP, MAC Address, servidores Proxy e a rede de roteamento em cebola Tor
- Mascaramento de identidade em testes de rede locais: Como e por que alterar o endereço MAC de placas de rede com macchanger
- OSINT (Open Source Intelligence): Conceitos e técnicas de coleta de informações públicas sobre alvos através de fontes abertas na Internet

### 🔹 Módulo 2: Segurança e Análise de Redes Wi-Fi (WPA2/WPA3 e Aircrack-ng) (Aulas 11 a 20)
**Diretório de Aulas e Práticas:** `/Modulo_02_Redes_Wifi_e_Monitoramento/`

- A anatomia das redes sem fio (IEEE 802.11): Frequências de 2.4GHz vs 5GHz, canais de rádio, SSIDs, pontos de acesso (AP) e clientes
- Modo Gerenciado (Managed Mode) vs Modo Monitor (Monitor Mode): A placa de rede wi-fi como ouvinte passivo de todo o tráfego de rádio
- Colocando a interface de rede wireless em Modo Monitor com segurança utilizando o utilitário nativo airmon-ng start wlan0
- Escaneamento de redes ao redor, identificação de SSIDs, endereços MAC (BSSID), canais de rádio e força de sinal com airodump-ng
- Focando a captura de dados de rádio em um ponto de acesso específico e gravando pacotes de rede em arquivo .cap com airodump-ng -c -w
- O Handshake WPA/WPA2 de 4 vias (4-Way Handshake): O momento exato em que a autenticação da senha acontece no ar
- Forçando a captura do Handshake através do envio de pacotes de desautenticação (Deauth Attack) direcionados com aireplay-ng -0
- Análise off-line de arquivos de captura e teste educacional de força de senha WPA2 utilizando dicionários com aircrack-ng e hashcat
- Evolução da segurança wireless: Como o WPA3 e o protocolo SAE (Simultaneous Authentication of Equals) eliminam ataques offline de handshake
- Defesa wireless de redes corporativas e residenciais: Segmentação de VLANs, desativação de WPS e políticas de senhas de alta entropia

### 🔹 Módulo 3: Reconhecimento de Redes, Port Scanning e Enumeração (Aulas 21 a 30)
**Diretório de Aulas e Práticas:** `/Modulo_03_Reconhecimento_e_Scanner_de_Redes/`

- A fase de Varredura (Scanning): Identificando dispositivos ativos, portas abertas, serviços em execução e sistemas operacionais em uma rede
- O padrão de ouro mundial para escaneamento de redes: Introdução ao Nmap (Network Mapper) e sua sintaxe fundamental
- Técnicas de varredura no Nmap 1: Ping Scan (-sn) para descoberta de hosts e TCP Connect Scan (-sT) para conexões completas
- Técnicas de varredura no Nmap 2: O furtivo TCP SYN Scan (-sS / Half-Open scan) e varredura de portas UDP (-sU)
- Enumeração e identificação precisa de versões de serviços em execução nas portas abertas com a flag -sV do Nmap
- Detecção remota do Sistema Operacional do alvo (OS Detection) com a flag -O e varredura agressiva combinada (-A)
- O poder da automação de scanner: O Nmap Scripting Engine (NSE) e scripts de detecção de vulnerabilidades (nmap --script vuln)
- Interceptação, inspeção e análise profunda de pacotes de rede em tempo real com o analisador de protocolos Wireshark / tshark
- Entendendo o fluxo do protocolo TCP/IP, o Handshake TCP de 3 vias (SYN, SYN-ACK, ACK) e as bandeiras (Flags) de controle de rede
- Identificação de vulnerabilidades conhecidas (CVEs) associadas às versões de software enumeradas durante a fase de varredura de rede

### 🔹 Módulo 4: Teste de Intrusão em Aplicações Web (OWASP Top 10) (Aulas 31 a 40)
**Diretório de Aulas e Práticas:** `/Modulo_04_Pentest_Web_OWASP_Top_10/`

- A anatomia de uma aplicação Web moderna e a importância do projeto OWASP (Open Web Application Security Project) para desenvolvedores
- OWASP A01 - Quebra de Controle de Acesso (Broken Access Control): IDOR (Insecure Direct Object References) e escalada de privilégios em APIs
- OWASP A02 - Falhas Criptográficas (Cryptographic Failures): Transmissão de dados sensíveis sem criptografia forte e armazenamento inseguro
- OWASP A03 - Injeção (Injection 1): SQL Injection na prática — Como identificar entradas vulneráveis e extrair bancos de dados com SQLMap
- OWASP A03 - Injeção (Injection 2): Cross-Site Scripting (XSS Refletido, Armazenado e DOM-based) — Como scripts maliciosos roubam sessões
- OWASP A03 - Injeção (Injection 3): Command Injection — Executando comandos arbitrários do sistema operacional na máquina do servidor web
- OWASP A04 & A05 - Design Inseguro e Configuração Incorreta de Segurança (Security Misconfiguration): Diretórios abertos, senhas padrão e CORS desprotegido
- OWASP A07 - Falhas de Identificação e Autenticação (Identification and Authentication Failures): Força bruta, Session Fixation e falta de Rate Limiting
- OWASP A10 - Falsificação de Requisição do Lado do Servidor (SSRF - Server-Side Request Forgery): Fazendo o servidor atacar sua própria rede interna
- A ferramenta canivete suíço do pentester web: Como utilizar o Burp Suite Community para interceptar, modificar e analisar requisições HTTP

### 🔹 Módulo 5: Criptografia, Entropia de Senhas e o Repositório 'senhas-logaritmo' (Aulas 41 a 50)
**Diretório de Aulas e Práticas:** `/Modulo_05_Criptografia_Logaritmos_e_Entropia/`

- Os fundamentos matemáticos da criptografia: Por que a segurança digital mundial depende da complexidade de problemas matemáticos assintóticos?
- Diferença entre Codificação (Base64, Hex), Hashing Criptográfico (MD5, SHA-1, SHA-256, SHA-512) e Criptografia (AES, RSA)
- O conceito de Hash Colision (Colisão de Hash): Por que algoritmos antigos como MD5 e SHA-1 foram descontinuados para segurança de alto nível
- A matemática do roubo de senhas: O que são Rainbow Tables (Tabelas arco-íris) e como o Salt (Salgado aleatório) inutiliza esse ataque
- Estudo prático do repositório 'senhas-logaritmo' de Carlos Guedes: A aplicação de logaritmos na mensuração de força de credenciais
- A fórmula de Entropia de Shannon (H = N * log2(L)): Calculando quantos bits reais de segurança uma senha possui no universo computacional
- Simulação matemática de tempo para quebra de senhas por força bruta: Como GPUs modernas (RTX / ASICs) testam bilhões de hashes por segundo
- Algoritmos modernos para armazenamento de senhas em bancos de dados: Por que Bcrypt, PBKDF2 e Argon2 possuem custo computacional (Work Factor) configurável
- Criptografia assimétrica moderna na Web: O funcionamento de certificados digitais SSL/TLS, infraestrutura de chaves públicas (PKI) e HTTPS
- Esteganografia digital: Os conceitos e técnicas de ocultação de arquivos secretos e dados criptografados dentro de imagens e áudios

### 🔹 Módulo 6: Engenharia Social, Exploração de Sistemas e Pós-Exploração (Aulas 51 a 60)
**Diretório de Aulas e Práticas:** `/Modulo_06_Engenharia_Social_e_Exploracao/`

- A vulnerabilidade humana: O que é Engenharia Social e por que o fator humano continua sendo o elo mais fraco da segurança cibernética
- Vetores de ataque de Engenharia Social: Phishing (e-mail enganoso), Spear Phishing (alvo direcionado), Vishing (voz) e Baiting (isca física)
- Conceitos de Exploração de Vulnerabilidades: O que é um Exploit, um Payload e a diferença entre Bind Shell e Reverse Shell
- O framework de penetração mais famoso do planeta: Introdução ao Metasploit Framework (msfconsole), busca de módulos e configuração de opções
- Executando um teste educacional em sistema vulnerável (Metasploitable 2 / 3) com Metasploit: Selecionando exploit, configurando payload e obtendo shell
- Pós-exploração no sistema invadido: O que fazer após obter acesso? Coleta de informações locais, escalada de privilégios e persistência
- O que são Malwares? A classificação e comportamento dos principais tipos: Vírus, Worms, Trojans (Cavalo de Troia), Spywares e Rootkits
- A maior ameaça cibernética da década: Como funcionam os Ransomwares (Sequestro de dados com criptografia de alta resistência e extorsão)
- Conceitos de Evasão de Antivírus e Firewalls: Como os sistemas de defesa detectam ameaças por Assinatura (Hash) vs Comportamento (Heurística)
- Metodologias de Hardening de Servidores Linux e Windows: Fechamento de portas, desativação de serviços inúteis e aplicação de patches de segurança

### 🔹 Módulo 7: Maestria em InfoSec - Laboratório Prático e Blue Team (Defesa) (Aulas 61 a 70)
**Diretório de Aulas e Práticas:** `/Modulo_07_Projetos_Reais_e_Defesa_Cibernetica/`

- A transição do ataque para a defesa: Diferença entre Red Team (Ataque ofensivo), Blue Team (Defesa e monitoramento) e Purple Team (Colaboração integrada)
- O que são sistemas de detecção e prevenção de intrusões de rede (IDS / IPS)? Introdução aos conceitos do Snort e Suricata na proteção do tráfego
- Centralização e correlação de logs de segurança em tempo real: O papel dos sistemas SIEM (Security Information and Event Management) corporativos
- Análise forense computacional básica: Como coletar evidências digitais em memória RAM e discos rígidos sem alterar os metadados dos arquivos (Cadeia de custódia)
- Resposta a Incidentes de Segurança (Incident Response): Os 6 passos cruciais na contenção, erradicação e recuperação de um sistema hackeado
- Projeto Prático de Segurança 1: Construindo um Script Python / CLI de auditoria de senhas e cálculo de entropia logarítmica com relatórios
- Projeto Prático de Segurança 2: Configurando um laboratório de teste web local vulnerável (DVWA - Damn Vulnerable Web Application / OWASP Juice Shop)
- Projeto Prático de Segurança 3: Executando um relatório completo de auditoria de vulnerabilidades em uma aplicação web de testes seguindo o OWASP Top 10
- Escrita profissional de um Relatório Executivo de Teste de Intrusão (Pentest Report): Classificação de risco por CVSS (Common Vulnerability Scoring System) e remediação
- Projeto Final: O Guia Definitivo do Hacker Ético, Engenharia de Defesa & Auditoria Cibernética Carlos Guedes

---

<div align="center">
  <p>💡 <i>"O estudo metódico, aliado à prática contínua, é o caminho indiscutível para a maestria em engenharia de software."</i></p>
  <p><b>Desenvolvido com precisão tecnológica por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> ❤️🚀</b></p>
</div>
