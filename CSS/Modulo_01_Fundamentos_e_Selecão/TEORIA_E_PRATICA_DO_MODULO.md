# Módulo 1: Seletor, Cascata, Especificidade e Box Model (Aulas 01 a 10)

## 📌 Objetivos de Aprendizagem do Módulo
Neste módulo, você dominará os conceitos técnicos que sustentam as 10 aulas desta etapa. A abordagem de Carlos Guedes prioriza a clareza arquitetural, a eficiência computacional e a aplicação direta em projetos de nível profissional.

## 🧠 Resumo Teórico & Boas Práticas da Indústria

### Anatomia de uma regra CSS e importação
O domínio de **Anatomia de uma regra CSS e importação** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Seletores de tipo, classe e ID
O domínio de **Seletores de tipo, classe e ID** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### A matemática da Especificidade e o perigo do !important
O domínio de **A matemática da Especificidade e o perigo do !important** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Box Model (margin, border, padding, content)
O domínio de **Box Model (margin, border, padding, content)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Box-sizing: border-box vs content-box
O domínio de **border-box vs content-box** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Cores em CSS (HEX, RGB, RGBA, HSL, HSLA)
O domínio de **Cores em CSS (HEX, RGB, RGBA, HSL, HSLA)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Unidades de medida absolutas (px) vs relativas (rem, em, vh, vw, %)
O domínio de **Unidades de medida absolutas (px) vs relativas (rem, em, vh, vw, %)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Tipografia web moderna e carregamento de fontes (Google Fonts)
O domínio de **Tipografia web moderna e carregamento de fontes (Google Fonts)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Alinhamento básico de textos e propriedades de fonte
O domínio de **Alinhamento básico de textos e propriedades de fonte** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

### Normalização de estilos (Reset CSS vs Normalize)
O domínio de **Normalização de estilos (Reset CSS vs Normalize)** é fundamental para garantir código limpo, escalável, seguro e de fácil manutenção. Em ambientes corporativos modernos (como visto nos sistemas de alto desempenho de Carlos Guedes), essa prática reduz gargalos, otimiza o consumo de memória/rede e previne vulnerabilidades críticas de segurança.

---

## 💻 Laboratório de Código Prático
Abaixo está a implementação prática de referência que consolida os aprendizados deste módulo:

```css
/* Laboratório Prático: Módulo 1: Seletor, Cascata, Especificidade e Box Model (Aulas 01 a 10) | Autor: Carlos Guedes */
:root {
    --primary-color: #00ff88;
    --bg-dark: #0f172a;
    --surface: #1e293b;
    --text-main: #f8fafc;
}

.card-modulo {
    background: var(--surface);
    border-left: 4px solid var(--primary-color);
    padding: 2rem;
    border-radius: 12px;
    color: var(--text-main);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card-modulo:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0, 255, 136, 0.2);
}
```

---

## 🚀 Desafio Prático de Conclusão do Módulo
Para validar sua certificação interna neste módulo, implemente uma variação do laboratório acima que adicione uma funcionalidade extra à sua escolha, aplicando rigorosamente os 10 conceitos teóricos apresentados nas aulas.
