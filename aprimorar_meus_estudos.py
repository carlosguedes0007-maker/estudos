# -*- coding: utf-8 -*-
"""
Script de Aprimoramento dos Meus Experimentos Legados (Aprimorar Meus Estudos)
Formata meus experimentos antigos em HTML, CSS e scripts, aplicando um design premium
de caderno de estudos e removendo termos docentes.
"""

import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_UPGRADES = {
    "experimento_01_comecando_html.html": """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Experimento 01 - Começando com HTML5 | Carlos Guedes</title>
    <style>
        body { font-family: 'Inter', system-ui, sans-serif; background: #0f172a; color: #f8fafc; padding: 2rem; line-height: 1.6; }
        .header { border-bottom: 2px solid #00ff88; padding-bottom: 1rem; margin-bottom: 2rem; }
        h1 { color: #00ff88; font-size: 2.5rem; margin: 0; }
        .conceito { background: #1e293b; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #38bdf8; margin: 1rem 0; }
        h1, h2, h3, h4, h5, h6 { color: #fff; }
        .highlight { color: #00ff88; font-weight: bold; }
    </style>
</head>
<body>
    <header class="header">
        <h1>Experimento 01: Estrutura Básica e Títulos (H1 ao H6)</h1>
        <p>Caderno de estudos e testes práticos de <span class="highlight">Carlos Guedes</span>.</p>
    </header>
    
    <main>
        <div class="conceito">
            <h2>🧠 Minhas anotações: Por que usamos títulos no HTML5?</h2>
            <p>Anotei que os elementos <strong>&lt;h1&gt;</strong> a <strong>&lt;h6&gt;</strong> definem a hierarquia semântica da informação. Os motores de busca e leitores de tela utilizam esses títulos para compreender a estrutura de tópicos da página.</p>
        </div>

        <section>
            <h1>H1: Título Principal (Apenas UM por página para SEO)</h1>
            <h2>H2: Subtítulo de Seção</h2>
            <h3>H3: Tópico Específico</h3>
            <h4>H4: Detalhe do Tópico</h4>
            <h5>H5: Sub-detalhe</h5>
            <h6>H6: Menor Nível de Hierarquia</h6>
        </section>
    </main>
</body>
</html>""",
    "experimento_02_textos.html": """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Experimento 02 - Formatação de Textos | Carlos Guedes</title>
    <style>
        body { font-family: sans-serif; background: #0f172a; color: #e2e8f0; padding: 2rem; }
        .box { background: #1e293b; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #00ff88; }
        strong { color: #00ff88; } em { color: #38bdf8; }
    </style>
</head>
<body>
    <h1>Experimento 02: Parágrafos e Formatação Semântica de Texto</h1>
    <div class="box">
        <p>No HTML5 moderno que estou estudando, evito tags antigas como &lt;b&gt; e &lt;i&gt;. Utilizo:</p>
        <ul>
            <li><strong>&lt;strong&gt;</strong> para dar <strong>importância semântica e destaque forte</strong>.</li>
            <li><em>&lt;em&gt;</em> para dar <em>ênfase vocal ou tom de leitura</em>.</li>
            <li><mark style="background: #eab308; color: #000; padding: 2px 6px; border-radius: 4px;">&lt;mark&gt;</mark> para destacar trechos relevantes em amarelo.</li>
        </ul>
    </div>
</body>
</html>""",
    "experimento_03_imagens.html": """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Experimento 03 - Imagens e Acessibilidade | Carlos Guedes</title>
    <style>
        body { font-family: sans-serif; background: #0b0f19; color: #fff; padding: 2rem; }
        figure { background: #151e2f; border: 1px solid #1e293b; padding: 1rem; border-radius: 12px; max-width: 600px; }
        img { width: 100%; height: auto; border-radius: 8px; }
        figcaption { color: #00ff88; margin-top: 0.5rem; text-align: center; font-style: italic; }
    </style>
</head>
<body>
    <h1>Experimento 03: Inserção de Imagens, Atributo ALT e Tag Figure</h1>
    <p>A tag <strong>&lt;figure&gt;</strong> encapsula uma mídia e sua legenda <strong>&lt;figcaption&gt;</strong>, criando uma estrutura semântica perfeita nos meus testes:</p>
    <figure>
        <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600" alt="Tela de computador exibindo código de programação verde" loading="lazy">
        <figcaption>Figura 3.1: Ambiente de desenvolvimento otimizado no meu setup de estudos.</figcaption>
    </figure>
</body>
</html>"""
}

CSS_UPGRADES = {
    "experimento_01_comecando_css.html": """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Experimento 01 - Introdução ao CSS3 | Carlos Guedes</title>
    <style>
        :root { --primary: #00ff88; --bg: #0f172a; --card: #1e293b; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: #f8fafc; padding: 3rem; text-align: center; }
        .hero { background: var(--card); border: 2px solid var(--primary); padding: 3rem; border-radius: 16px; box-shadow: 0 0 30px rgba(0,255,136,0.2); max-width: 600px; margin: 0 auto; }
        h1 { color: var(--primary); font-size: 2.5rem; margin-bottom: 1rem; }
        p { color: #94a3b8; font-size: 1.1rem; }
    </style>
</head>
<body>
    <div class="hero">
        <h1>✨ Olá, Mundo CSS3!</h1>
        <p>Bem-vindo ao meu laboratório pessoal de estilização. Aqui eu testo variáveis, box model e design interativo!</p>
    </div>
</body>
</html>"""
}

def aprimorar_meus_estudos():
    print("[APRIMORAMENTO] Atualizando meus experimentos no diretório HTML...")
    html_dir = os.path.join(BASE_DIR, "HTML")
    for fname, content in HTML_UPGRADES.items():
        fpath = os.path.join(html_dir, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f" -> Atualizado no meu caderno: {fname}")

    print("[APRIMORAMENTO] Atualizando meus experimentos no diretório CSS...")
    css_dir = os.path.join(BASE_DIR, "CSS")
    for fname, content in CSS_UPGRADES.items():
        fpath = os.path.join(css_dir, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f" -> Atualizado no meu caderno: {fname}")

    print("[SUCESSO] Aprimoramento dos experimentos finalizado!")

if __name__ == "__main__":
    aprimorar_meus_estudos()
