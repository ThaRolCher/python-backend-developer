// Dados dos Capítulos do E-Book
const chapters = {
    cover: {
        progress: 0,
        content: `
            <div class="cover-layout">
                <h1 class="cover-title">O Futuro Híbrido</h1>
                <p class="cover-subtitle">Como Inteligências Artificiais Generativas Estão Redefinindo o Desenvolvimento Backend e a Engenharia de Software</p>
                <img src="assets/cover.png" alt="Capa do E-Book SynthRead" class="cover-image">
                <div class="cover-meta">
                    <p>Autor: <strong>ThaRolCher</strong></p>
                    <p>Tecnologias: <strong>Gemini, Imagen & Vanilla Web</strong></p>
                </div>
            </div>
        `,
        insight: "Sintetizando capa: Este e-book aborda a transição dos engenheiros de software para papéis de arquitetura e curadoria usando IAs Generativas, superando a mecânica repetitiva de digitação de código."
    },
    preface: {
        progress: 20,
        content: `
            <h1>Prefácio: O Novo Paradigma do Desenvolvimento</h1>
            <p>O desenvolvimento de software sempre avançou através de camadas de abstração. Da programação em cartões perfurados ao Assembly, do Assembly para linguagens de alto nível estruturadas, e depois para frameworks modernos e computação em nuvem.</p>
            <p>Cada salto de abstração aumentou a produtividade humana, permitindo-nos focar mais nas regras de negócio e menos na sintaxe e infraestrutura mecânica.</p>
            <p>Hoje, estamos diante do próximo grande salto: a <strong>Inteligência Artificial Generativa</strong>. Não se trata de substituir o desenvolvedor, mas de elevá-lo a um papel de arquitetura e curadoria. Este e-book explora como essa simbiose está redefinindo as engrenagens invisíveis do software — o backend.</p>
        `,
        insight: "Insight do Prefácio: A IA atua como uma nova camada de abstração de linguagem natural. Os profissionais que melhor se adaptarem focando em curadoria técnica obterão um ganho substancial de produtividade."
    },
    cap1: {
        progress: 40,
        content: `
            <h1>Capítulo 1: A Revolução Silenciosa no Design de APIs</h1>
            <img src="assets/cap1.png" alt="Fluxo de dados holográfico de APIs">
            <p>A criação de APIs tradicionalmente envolve planejamento rigoroso de estruturas de dados, roteamento, códigos de status HTTP e documentação como OpenAPI/Swagger. Embora essencial, esse processo exige muito trabalho braçal e repetitivo.</p>
            <p>Com o auxílio de Modelos de Linguagem de Grande Porte (LLMs), o design de APIs torna-se declarativo. O desenvolvedor backend descreve em linguagem natural o propósito do domínio de negócio (ex: 'Necessito de uma API de comércio eletrônico com rotas para listagem, filtros de preço e tratamento de transações concorrentes'). A IA então propõe contratos OpenAPI estruturados, esquemas de validação JSON e rotas do FastAPI/Express limpas e otimizadas em segundos.</p>
            <p>A inteligência da IA não reside em criar códigos arbitrários, mas na capacidade de consolidar boas práticas de design (RESTful, tratamento correto de cabeçalhos, paginação) de forma instantânea, permitindo ao engenheiro validar e refinar a arquitetura ao invés de digitar sintaxes triviais.</p>
        `,
        insight: "Insight do Capítulo 1: O design de APIs assistido por IA reduz o tempo de prototipagem em até 80%. A validação humana foca em consistência lógica e alinhamento com os requisitos de negócio."
    },
    cap2: {
        progress: 60,
        content: `
            <h1>Capítulo 2: Banco de Dados Inteligente e Assistido</h1>
            <p>No centro de qualquer sistema backend robusto reside o banco de dados. Seja SQL ou NoSQL, otimizar consultas complexas, estruturar indexação e desenhar relacionamentos performáticos são desafios clássicos.</p>
            <p>A IA Generativa atua aqui como um DBA especialista disponível 24 horas por dia. O uso prático inclui:</p>
            <ul>
                <li><strong>Tradutores Natural-to-SQL:</strong> Permitir que analistas de dados consultem bancos convertendo perguntas humanas em queries complexas com múltiplos JOINs de forma segura.</li>
                <li><strong>Otimização de Consultas:</strong> Ao passar um comando EXPLAIN de uma query lenta para uma IA, ela consegue diagnosticar gargalos, sugerir a criação de índices compostos apropriados ou propor a reescrita da consulta para evitar varreduras de tabela inteira (full table scans).</li>
                <li><strong>Migração de Schemas:</strong> Facilitação na conversão de bancos relacionais para NoSQL, propondo estratégias de desnormalização ideais de acordo com os padrões de acesso descritos.</li>
            </ul>
        `,
        insight: "Insight do Capítulo 2: A IA acelera tarefas de banco de dados, mas a tomada de decisão sobre integridade referencial, concorrência e custos de nuvem continua exigindo supervisão humana experiente."
    },
    cap3: {
        progress: 80,
        content: `
            <h1>Capítulo 3: TDD Aumentado com IAs Generativas</h1>
            <img src="assets/cap3.png" alt="Dashboard digital de TDD e Testes">
            <p>O <strong>Desenvolvimento Orientado a Testes (TDD)</strong> é o padrão ouro para construir sistemas confiáveis. No entanto, muitos desenvolvedores ignoram ou reduzem a cobertura de testes devido ao tempo necessário para criar mocks de bancos de dados, simular chamadas de rede e prever todos os fluxos de exceção.</p>
            <p>IAs Generativas são aliadas perfeitas para a escrita de testes unitários e de integração. Ao fornecer a assinatura de uma função ou usecase, a IA consegue:</p>
            <ul>
                <li>Prever caminhos felizes (happy paths) e, mais importante, caminhos de exceção (edge cases) que o programador humano poderia esquecer.</li>
                <li>Gerar fábricas de dados de teste (factories) realistas de forma automática.</li>
                <li>Desenvolver scripts de monkeypatching e mocking robustos para drivers de banco de dados assíncronos e clientes HTTP.</li>
            </ul>
            <p>Com a IA escrevendo a mecânica dos testes, o desenvolvedor backend adota o TDD com muito mais facilidade e prazer, gerando softwares mais seguros e resilientes.</p>
        `,
        insight: "Insight do Capítulo 3: Escrever testes assistido por IA remove a maior barreira para a adoção do TDD: o esforço de codificar estruturas de mock complexas. Foco na segurança de ponta a ponta."
    },
    cap4: {
        progress: 100,
        content: `
            <h1>Capítulo 4: Reflexão Prática: O Código "Natty" vs "Fake"</h1>
            <p>Inspirado no meme 'Natty or Not' do fisiculturismo, no desenvolvimento de software hoje enfrentamos a mesma pergunta: o código é <strong>"Natty"</strong> (escrito puramente à mão por inteligência humana) ou <strong>"Fake/Juiced"</strong> (gerado com o auxílio de IA)?</p>
            <p>A verdade é que o futuro pertence ao desenvolvimento híbrido. Um programador purista 'natty' que rejeita o uso de IAs corre o risco de tornar-se obsoleto devido à velocidade de entrega menor. Por outro lado, um programador puramente 'fake' que apenas copia e cola códigos gerados por IA sem entendê-los criará sistemas instáveis, inseguros e difíceis de depurar.</p>
            <p>O backend de alta performance exige <strong>curadoria humana</strong>. A IA gera a matéria-prima sintética; o desenvolvedor inspeciona, valida, testa e assegura que a arquitetura respeita os limites de segurança, concorrência e manutenibilidade.</p>
            <p>O software do futuro não é 'natty' nem 'fake', mas sim a sinergia perfeita entre a criatividade e o rigor humanos potencializados pela escala de conhecimento artificial.</p>
        `,
        insight: "Insight do Capítulo 4: O papel do programador evoluiu da digitação para a validação crítica. O desenvolvedor híbrido lidera o mercado ao orquestrar IAs Generativas com sabedoria e ética."
    }
};

let currentChapterId = 'cover';
let isTyping = false;

// Inicializa a aplicação
document.addEventListener('DOMContentLoaded', () => {
    loadChapter('cover');
});

// Carrega um capítulo dinamicamente
function loadChapter(chapterId) {
    if (!chapters[chapterId]) return;
    
    currentChapterId = chapterId;
    const chapter = chapters[chapterId];
    
    // Atualiza a Viewport do Livro com animação suave
    const bookViewport = document.getElementById('book-viewport');
    bookViewport.style.opacity = '0';
    bookViewport.style.transform = 'translateY(10px)';
    
    setTimeout(() => {
        bookViewport.innerHTML = chapter.content;
        bookViewport.style.opacity = '1';
        bookViewport.style.transform = 'translateY(0)';
    }, 200);

    // Atualiza Barra de Progresso
    const progressFill = document.getElementById('reading-progress');
    progressFill.style.width = `${chapter.progress}%`;

    // Atualiza itens ativos da navegação
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    
    const activeBtn = document.getElementById(`nav-btn-${chapterId}`);
    if (activeBtn) {
        activeBtn.classList.add('active');
    }

    // Reseta o painel de insights
    const insightText = document.getElementById('insight-text');
    insightText.innerHTML = 'Clique no botão acima para sintetizar os principais insights técnicos e filosóficos do capítulo com nossa Inteligência Artificial.';
    insightText.className = 'copilot-placeholder';

    // Fecha a sidebar mobile se aberta
    const sidebar = document.getElementById('sidebar-nav');
    if (sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
    }
}

// Controla a exibição da barra lateral no Mobile
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar-nav');
    sidebar.classList.toggle('open');
}

// Simula a geração de insights via IA com efeito Typewriter
function generateInsight() {
    if (isTyping) return;
    
    const insightTextElement = document.getElementById('insight-text');
    const targetText = chapters[currentChapterId].insight;
    
    insightTextElement.innerHTML = '';
    insightTextElement.className = 'copilot-insight';
    isTyping = true;
    
    let index = 0;
    
    function typeEffect() {
        if (index < targetText.length) {
            insightTextElement.innerHTML += targetText.charAt(index);
            index++;
            setTimeout(typeEffect, 20); // Velocidade de digitação rápida
        } else {
            isTyping = false;
        }
    }
    
    typeEffect();
}
