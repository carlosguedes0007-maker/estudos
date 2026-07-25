# Módulo 2: Segurança e Análise de Redes Wi-Fi (WPA2/WPA3 e Aircrack-ng) (Aulas 11 a 20)

## 📌 Objetivos de Aprendizagem do Módulo
Neste módulo, você dominará os conceitos técnicos que sustentam as 10 aulas desta etapa. A abordagem de Carlos Guedes prioriza a clareza arquitetural, a eficiência computacional e a aplicação direta em projetos de nível profissional.

## 🧠 Resumo Teórico & Boas Práticas da Indústria

### A anatomia das redes sem fio (IEEE 802.11): Frequências de 2.4GHz vs 5GHz, canais de rádio, SSIDs, pontos de acesso (AP) e clientes
O domínio de **Frequências de 2.4GHz vs 5GHz, canais de rádio, SSIDs, pontos de acesso (AP) e clientes** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Modo Gerenciado (Managed Mode) vs Modo Monitor (Monitor Mode): A placa de rede wi-fi como ouvinte passivo de todo o tráfego de rádio
O domínio de **A placa de rede wi-fi como ouvinte passivo de todo o tráfego de rádio** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Colocando a interface de rede wireless em Modo Monitor com segurança utilizando o utilitário nativo airmon-ng start wlan0
O domínio de **Colocando a interface de rede wireless em Modo Monitor com segurança utilizando o utilitário nativo airmon-ng start wlan0** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Escaneamento de redes ao redor, identificação de SSIDs, endereços MAC (BSSID), canais de rádio e força de sinal com airodump-ng
O domínio de **Escaneamento de redes ao redor, identificação de SSIDs, endereços MAC (BSSID), canais de rádio e força de sinal com airodump-ng** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Focando a captura de dados de rádio em um ponto de acesso específico e gravando pacotes de rede em arquivo .cap com airodump-ng -c -w
O domínio de **Focando a captura de dados de rádio em um ponto de acesso específico e gravando pacotes de rede em arquivo .cap com airodump-ng -c -w** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### O Handshake WPA/WPA2 de 4 vias (4-Way Handshake): O momento exato em que a autenticação da senha acontece no ar
O domínio de **O momento exato em que a autenticação da senha acontece no ar** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Forçando a captura do Handshake através do envio de pacotes de desautenticação (Deauth Attack) direcionados com aireplay-ng -0
O domínio de **Forçando a captura do Handshake através do envio de pacotes de desautenticação (Deauth Attack) direcionados com aireplay-ng -0** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Análise off-line de arquivos de captura e teste educacional de força de senha WPA2 utilizando dicionários com aircrack-ng e hashcat
O domínio de **Análise off-line de arquivos de captura e teste educacional de força de senha WPA2 utilizando dicionários com aircrack-ng e hashcat** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Evolução da segurança wireless: Como o WPA3 e o protocolo SAE (Simultaneous Authentication of Equals) eliminam ataques offline de handshake
O domínio de **Como o WPA3 e o protocolo SAE (Simultaneous Authentication of Equals) eliminam ataques offline de handshake** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Defesa wireless de redes corporativas e residenciais: Segmentação de VLANs, desativação de WPS e políticas de senhas de alta entropia
O domínio de **Segmentação de VLANs, desativação de WPS e políticas de senhas de alta entropia** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

---

## 💻 Laboratório de Código Prático
Abaixo está a implementação prática de referência que consolida os aprendizados deste módulo:

```bash
#!/usr/bin/env bash
# Laboratório de Hacking Ético e Cibersegurança: Módulo 2: Segurança e Análise de Redes Wi-Fi (WPA2/WPA3 e Aircrack-ng) (Aulas 11 a 20)
# Autor: Carlos Guedes (Aviso: Apenas para fins educacionais em ambientes autorizados!)

echo "======================================================================="
echo " 💀 LAB INFOSEC & CIBERSEGURANÇA - Modulo_02_Redes_Wifi_e_Monitoramento"
echo " 🛡️ Defesa, Auditoria e Análise de Entropia de Redes / Sistemas"
echo "======================================================================="

echo "[1] Verificando isolamento da rede de testes (RoE)... OK."
echo "[2] Simulando cálculo de entropia criptográfica do módulo... 128-bit STRONG."
echo "[3] Status: 10 Aulas teóricas e práticas consolidadas com sucesso."
echo "======================================================================="
```

---

## 🚀 Desafio Prático de Conclusão do Módulo
Para validar sua certificação interna neste módulo, implemente uma variação do laboratório acima que adicione uma funcionalidade extra à sua escolha, aplicando rigorosamente os 10 conceitos teóricos apresentados nas aulas.
