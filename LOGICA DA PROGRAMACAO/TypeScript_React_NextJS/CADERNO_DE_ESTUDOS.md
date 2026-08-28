<div align="center">

#  TypeScript, React 19 & Next.js App Router (Meus Cadernos de Estudo) - Meu Caderno de Anotações (70+ Tópicos) 

**Meus estudos práticos sobre tipagem estática, Server Components, Server Actions, Hooks e arquitetura ERP.**

[![Status](https://img.shields.io/badge/Status-70%2B_Tópicos_Estudados-00ff88?style=for-the-badge)](https://github.com/carlosguedes-dev)
[![Estudante](https://img.shields.io/badge/Estudante-Carlos_Guedes_Dev-38bdf8?style=for-the-badge)](https://github.com/carlosguedes-dev)

</div>

---

##  Visão Geral dos Meus Estudos

Este documento organiza o meu caderno pessoal de anotações, resumos teóricos e experimentos de código nesta especialização dentro do meu repositório de **Estudos**. Estruturei meu aprendizado rigorosamente em **7 Módulos de Investigação**, totalizando **70 tópicos de estudo detalhados**, onde documentei a teoria, armadilhas comuns, macetes corporativos e desenvolvi códigos de laboratório para fixar cada conceito.

---

##  Índice de Resumos & Experimentos

###  Módulo 1: TypeScript Esencial, Tipagem Estática e Interfaces (Tópicos 01 a 10)
**Pasta de Resumos e Experimentos:** `/Modulo_01_TypeScript_Fundamentos/`

-  Tópico 01: Por que o TypeScript é obrigatório no desenvolvimento corporativo moderno?
-  Tópico 02: Tipagem de variáveis fundamentais (string, number, boolean, any, unknown, never)
-  Tópico 03: Arrays, Tuplas e Enums no TypeScript
-  Tópico 04: Tipagem de funções, parâmetros opcionais e retorno de funções
-  Tópico 05: Interfaces vs Type Aliases: Quando utilizar cada um?
-  Tópico 06: Propriedades opcionais (?) e somente-leitura (readonly)
-  Tópico 07: Union Types (|) e Intersection Types (&)
-  Tópico 08: Type Guards e Narrowing (typeof, instanceof, in)
-  Tópico 09: Tipagem de Objetos complexos e Index Signatures
-  Tópico 10: Configuração do tsconfig.json para projetos de alta exigência

###  Módulo 2: Generics, Utility Types e Tipagem Avançada (Tópicos 11 a 20)
**Pasta de Resumos e Experimentos:** `/Modulo_02_TypeScript_Avancado_e_Generics/`

-  Tópico 01: O poder dos Generics (<T>): Código tipado e 100% reutilizável
-  Tópico 02: Generics em Funções, Interfaces e Classes
-  Tópico 03: Restrições em Generics (extends)
-  Tópico 04: Utility Types Nativos: Partial<T>, Required<T>, Readonly<T>
-  Tópico 05: Utility Types Nativos: Record<K, T>, Pick<T, K>, Omit<T, K>
-  Tópico 06: Template Literal Types e manipulação de tipos por string
-  Tópico 07: Conditional Types (T extends U ? X : Y)
-  Tópico 08: Mapped Types para transformação de esquemas de dados
-  Tópico 09: Tipagem de Promises e chamadas assíncronas no TS
-  Tópico 10: Criando bibliotecas de tipos limpas sem dependências externas

###  Módulo 3: React 19, JSX/TSX, Componentes e Hooks Fundamentais (Tópicos 21 a 30)
**Pasta de Resumos e Experimentos:** `/Modulo_03_React_Fundamentos_e_Hooks/`

-  Tópico 01: O Virtual DOM e a arquitetura orientada a componentes
-  Tópico 02: Sintaxe JSX/TSX e renderização condicional elegante
-  Tópico 03: Passagem e tipagem de Props no TypeScript
-  Tópico 04: Gerenciamento de estado local com useState<T>
-  Tópico 05: Efeitos colaterais, ciclo de vida e limpeza com useEffect
-  Tópico 06: Acesso a elementos do DOM e referências mútuas com useRef
-  Tópico 07: Otimização de performance com useMemo e useCallback
-  Tópico 08: Evitando prop drilling através da Context API (createContext e useContext)
-  Tópico 09: Hooks customizados (Custom Hooks): Encapsulando lógica complexa
-  Tópico 10: As novidades do React 19: Actions, use() hook e melhorias de concorrência

###  Módulo 4: Arquitetura de Componentes e Gerenciamento de Estado Avançado (Tópicos 31 a 40)
**Pasta de Resumos e Experimentos:** `/Modulo_04_Arquitetura_e_Gerenciamento_Estado/`

-  Tópico 01: Padrão de projeto: Componentes de Apresentação vs Componentes de Contêiner
-  Tópico 02: Composição de componentes com children e Slots no React
-  Tópico 03: Gerenciamento de estado complexo com useReducer
-  Tópico 04: Integração de formulários avançados no React com validação tipada
-  Tópico 05: Tratamento de erros globais com Error Boundaries no React
-  Tópico 06: Otimização de re-renderizações com React.memo e comparação profunda
-  Tópico 07: Carregamento sob demanda com React.lazy e Suspense
-  Tópico 08: Portal API: Renderizando Modais e Toasts fora da árvore DOM principal
-  Tópico 09: Integração do React com bibliotecas externas (Three.js / Gráficos Canvas)
-  Tópico 10: Padrões limpos de testes de componentes com React Testing Library

###  Módulo 5: Next.js App Router, React Server Components (RSC) e SSR (Tópicos 41 a 50)
**Pasta de Resumos e Experimentos:** `/Modulo_05_NextJS_App_Router_e_RSC/`

-  Tópico 01: Evolução do Next.js: Pages Router vs App Router (Diretório /app)
-  Tópico 02: React Server Components (RSC): Por que rodar componentes no servidor?
-  Tópico 03: Server Components vs Client Components ('use client'): Diretrizes de uso
-  Tópico 04: Roteamento baseado em arquivos, Layouts aninhados e Templates
-  Tópico 05: Rotas dinâmicas ([id]), Parâmetros de rota e busca (Search Params)
-  Tópico 06: Carregamento elegante com loading.tsx e Suspense boundaries
-  Tópico 07: Páginas de erro personalizadas (error.tsx e not-found.tsx)
-  Tópico 08: Server Actions ('use server'): Mutações no servidor sem criar endpoints API REST
-  Tópico 09: Estratégias de Cache no Next.js (Force-cache, Revalidate, No-store)
-  Tópico 10: Otimização nativa de Imagens, Fontes e Metadados SEO no Next.js

###  Módulo 6: Integração Backend, Banco de Dados (Prisma ORM) e Auth (Tópicos 51 a 60)
**Pasta de Resumos e Experimentos:** `/Modulo_06_Integracao_Prisma_ORM_e_Banco/`

-  Tópico 01: Modelagem de dados com Prisma Schema (Modelos, Relacionamentos 1:N e N:N)
-  Tópico 02: Geração de cliente tipado (Prisma Client) com TypeScript
-  Tópico 03: Realizando consultas CRUD (Create, Read, Update, Delete) no Server Component
-  Tópico 04: Consultas relacionais avançadas com include e select no Prisma
-  Tópico 05: Mutações seguras de dados utilizando Server Actions e Prisma
-  Tópico 06: Autenticação moderna no Next.js com NextAuth.js / Auth.js (JWT e Sessões)
-  Tópico 07: Proteção de rotas com Middleware no Next.js (middleware.ts)
-  Tópico 08: Validação de esquemas de dados de entrada com Zod e TypeScript
-  Tópico 09: Manipulação de Upload de arquivos e armazenamento de mídia
-  Tópico 10: Tratamento de transações no banco de dados e reversão de falhas (Rollback)

###  Módulo 7: Maestria Completa - Construindo um Sistema ERP Literário (Tópicos 61 a 70)
**Pasta de Resumos e Experimentos:** `/Modulo_07_Projetos_Reais_ERP_e_Maestria/`

-  Tópico 01: Arquitetura de sistema completo: Estudo de caso do ERP Biblioteca
-  Tópico 02: Criação do layout de dashboard administrativo moderno (Dark Mode & Glassmorphism)
-  Tópico 03: Desenvolvimento do módulo de gestão do acervo literário com paginação e busca
-  Tópico 04: Sistema de registro de empréstimos e devoluções com validação de regras de negócio
-  Tópico 05: Gráficos estatísticos interativos e relatórios em tempo real no dashboard
-  Tópico 06: Exportação de dados para relatórios gerenciais PDF / CSV
-  Tópico 07: Otimização extrema de requisições ao banco com índices no Prisma e cache do Next
-  Tópico 08: Auditoria de segurança contra injeções SQL, XSS e CSRF no Next.js
-  Tópico 09: Deploy profissional contínuo (Vercel / Docker) e variáveis de ambiente em produção
-  Tópico 10: Projeto Final: O Sistema de Gestão Empresarial (ERP) 2026 Carlos Guedes

---

<div align="center">
  <p> <i>"A constância nos estudos e o teste diário no código são os verdadeiros segredos para evoluir na engenharia de software."</i></p>
  <p><b>Caderno e laboratório mantido por <a href="https://github.com/carlosguedes-dev">Carlos Guedes</a> </b></p>
</div>
