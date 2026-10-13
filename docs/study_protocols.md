# Protocolos reconstruídos a partir do manuscrito

Este documento descreve os procedimentos relatados em [`article.pdf`](article.pdf), com referências às páginas numeradas do artigo, e identifica materiais posteriormente fornecidos pelo autor. Foi reconstruído em 13 de outubro de 2026 para tornar o pacote compreensível. **Este documento não é o protocolo original aprovado ou aplicado**, um TCLE original, um guia histórico de exploração ou uma ata histórica de consolidação. Os textos de consentimento e o snapshot do guia são preservados separadamente, com sua proveniência.

O artigo descreve duas versões: V1 foi objeto da inspeção heurística; V2 foi usada no estudo motivacional e na avaliação final. São três coortes independentes, de conveniência, com participação voluntária. Os códigos do pacote são específicos de cada coorte: H para heurística, M para motivação e P para avaliação final. Não se deve ligá-los entre estudos nem assumir que as pessoas são as mesmas.

## Consentimento e tratamento dos dados

Segundo §3.3, p4, antes da participação foram apresentados objetivos, procedimentos e coleta de dados, com concordância ao Termo de Consentimento Livre e Esclarecido (ICF/TCLE). As exportações contêm campos de concordância. O autor forneceu os três textos integrais durante a preparação deste pacote, preservados em `instruments/consent/heuristics.md`, `instruments/consent/motivation.md` e `instruments/consent/final_evaluation.md`. São textos fornecidos pelo autor, e não termos assinados recuperados de cada participante. Não foi fornecido número de comitê ou aprovação ética; esses dados não são inferidos ou inventados.

Na avaliação final, nomes nos arquivos de log permitiram a associação com o questionário, portanto a coleta não foi anônima segundo o artigo. O texto de TCLE dessa avaliação descreve coleta anônima. Essa é uma divergência entre a descrição do termo e a descrição histórica no manuscrito; o pacote preserva ambas, sem reescrever o termo ou concluir uma aprovação ética. O artigo informa a substituição dos identificadores por códigos antes da análise e a distribuição pública somente de dados desidentificados. O pacote preserva a associação dentro dessa coorte sem distribuir a chave nominal. Campos pessoais e arquivos originais são mantidos fora do repositório público; características demográficas são fornecidas de forma agregada.

## 1. Inspeção heurística — V1, N=5

**Participantes (§5, p5–6).** Cinco estudantes de mestrado em Computação com experiência profissional em desenvolvimento de software. Quatro tinham aproximadamente dois a quatro anos de experiência; o quinto também atuava como pesquisador de Educação em Computação, com experiência docente.

**Sequência descrita no artigo:**

1. Fornecer treinamento introdutório nas heurísticas AHJED e um guia de exploração do jogo.
2. Cada avaliador examinar V1 de forma independente e registrar problemas e severidades segundo o procedimento AHJED adotado.
3. Revisar e consolidar achados sobrepostos em conjunto com os avaliadores.
4. Priorizar achados de severidade 3 ou 4 para o planejamento do redesign.

O artigo não informa duração das sessões, uma ordem obrigatória de telas/atividades, formato das reuniões de consolidação ou regra adicional para resolver discordâncias. O TCLE fornecido pelo autor prevê **30 a 40 minutos de participação total**, que não é uma medida observada de tempo de jogo. O autor identificou o documento preservado em `instruments/heuristic_guide.pdf` como o guia de exploração fornecido aos avaliadores. O material separado de treinamento AHJED e os registros contemporâneos da consolidação não foram localizados.

**Tarefas do guia fornecido pelo autor, na ordem em que aparecem:**

1. **Consultar o Notebook:** localizar e abrir o recurso e buscar a descrição técnica de um padrão, como Microservices ou Event-Driven.
2. **Contratar um desenvolvedor:** acessar a Feira de Recrutamento, comparar atributos e realizar uma contratação.
3. **Aprender um novo padrão:** acessar a Sessão de Estudo, percorrer a explicação e selecionar uma arquitetura.
4. **Gerir recursos:** consultar o Painel de Desenvolvedor, a distribuição de pontos da equipe e as informações do contrato em andamento.
5. **Executar um contrato:** interpretar os requisitos, selecionar e arrastar padrão e desenvolvedores, e assinar o contrato.

O guia também descreve as três regiões da interface, os eventos de recrutamento/estudo/contrato, as interações de seleção e remoção e a fórmula de combinação dos atributos. O PDF preserva três páginas e três imagens; `instruments/heuristic_guide.txt` contém o texto português exportado e `instruments/heuristic_guide_metadata.json` registra a proveniência. Os termos do guia original são mantidos, sem corrigir retroativamente a nomenclatura científica ou adaptar o documento para fazê-lo coincidir com o manuscrito. A identificação do autor estabelece qual documento ele reconhece como guia; a data e os bytes do snapshot atual não comprovam que sejam idênticos aos entregues na avaliação histórica. A lista de tarefas tampouco comprova que todos os avaliadores tenham completado todas elas em ordem obrigatória.

**Material recuperado.** Os 42 enunciados aplicados estão em `instruments/heuristic_items.csv`; as 210 notas individuais, em `data/raw_anonymized/heuristics.csv`. O mapa de IDs traduz ED→EE, JG→GP, HJ→NR e AE→EA para os nomes empregados no artigo; IN permanece IN. O arquivo `data/processed/heuristic_redesign_trace.csv` associa os nove itens da Tabela 3 às respostas de redesign descritas no texto, calculando separadamente notas positivas e notas ≥3. Ele é uma consolidação reconstruída agora, com proveniência, e não um registro histórico da discussão com os avaliadores.

## 2. Estudo motivacional — V2, N=18 incluídos

**Participantes e contexto (§7, p8–10).** Estudantes de graduação e pós-graduação em Computação, com familiaridade ao menos básica com Engenharia de Software e desenvolvimento. Recrutamento voluntário em grupos on-line de Computação. Aplicação remota por formulário.

**Cinco partes, na ordem relatada:**

1. Explicação do experimento: objetivos, consentimento, instruções de jogo e procedimento de avaliação.
2. Questionário demográfico: formação, hábitos de jogo e experiência prévia com conceitos de Engenharia de Software.
3. Sessão de jogo livre por aproximadamente **20 a 30 minutos**, com instrução para explorar os três trimestres do jogo, pois introduzem mecânicas diferentes.
4. Avaliação motivacional: preenchimento de IMI e IMMS. O texto os apresenta nessa ordem, mas não especifica se havia contrabalanceamento ou outra randomização.
5. Comentários abertos opcionais sobre a experiência.

As instruções relatadas enfatizavam que não havia uma forma correta de jogar, que a avaliação se concentrava na experiência e não no desempenho individual, que as mecânicas podiam ser exploradas livremente e que a avaliação deveria continuar mesmo sem concluir todos os desafios. Recomendavam ambiente com poucas distrações e, preferencialmente, fones de ouvido. A aplicação remota não controlava equipamentos, conectividade ou distrações. O TCLE prevê **30 a 60 minutos de participação total**; esse intervalo não substitui os 20 a 30 minutos de jogo descritos no manuscrito.

**Filtro reconstruído.** A exportação fornecida tem 19 registros. A instrução atual do autor determina que o último respondente não foi considerado. O pacote identifica esse registro como `M019`, marca `included=false` e mantém seus itens para tornar a exclusão auditável, sem seus dados pessoais. Não foi fornecido outro motivo para exclusão. Os 18 incluídos coincidem item a item com a planilha histórica de análise. Esse filtro não deve ser inferido da qualidade das notas nem estendido às outras coortes.

**Instrumentos e pontuação (§7.2, p8–9).** IMI: 37 itens, respostas 1–7, agrupados em Interest/Enjoyment, Perceived Competence, Effort/Importance, Pressure/Tension, Perceived Choice e Value/Usefulness. IMMS: 36 itens, respostas 1–5, agrupados na aplicação/figura em Confidence, Attention, Satisfaction e Relevance. A correspondência exata de enunciados, dimensões e itens reversos está em `instruments/motivation_items.csv`; a ordem canônica de outra versão dos instrumentos não deve substituir esse mapa.

O artigo descreve reversão de itens negativos antes da análise, média aritmética dos itens de cada dimensão por participante e resumo por média e desvio padrão **amostral** desses escores. Pressure/Tension continua sendo uma dimensão de orientação negativa: valor baixo é favorável. `instruments/motivation_scoring.json` distingue `8−x` para IMI e a correção `6−x` para IMMS do `5−x` impresso no artigo. A análise literal é uma sensibilidade documentada; não se deve alterar a publicação silenciosamente. Ausência ou valor inválido interrompe a análise atual, sem imputação; essa regra é do pacote, pois o manuscrito não especifica política de dados faltantes.

## 3. Avaliação final — V2, N=44

**Participantes e contexto (§8, p10).** Uma turma de Engenharia da Computação, com 44 estudantes de graduação e pós-graduação, predominantemente de graduação. Aplicação em sala de aula. A Tabela 5 informa características agregadas.

**Sequência descrita no artigo:**

1. Consentimento informado.
2. Questionário demográfico.
3. Pré-teste de conhecimento: **Formulário A, 14 itens**.
4. Breve introdução ao TotalMeltdown.
5. Jogo por **até 50 minutos**, com possibilidade de parar antes. Não se deve atribuir 50 minutos a todos como duração observada.
6. Imediatamente após o jogo, pós-teste: **Formulário B, 14 itens**.
7. Questionário de experiência do jogador.
8. Respostas abertas.

O TCLE prevê **45 a 70 minutos de participação total**. Esse intervalo inclui as atividades de pesquisa e não substitui o limite de até 50 minutos de jogo relatado no artigo.

### Testes de conhecimento

Os formulários abordam conceitos correspondentes através de cenários diferentes. Os autores revisaram conteúdo e dificuldade pretendida antes da aplicação; **não estabeleceram equivalência empírica de dificuldade entre A e B**. Um ponto é atribuído a cada resposta correta, total máximo 14. Todos os 44 participantes forneceram respostas pareadas completas. O gabarito e o mapa entre as respostas exportadas e os itens estão em `instruments/pre_post_key.json`; os dados, em `data/raw_anonymized/pre_post.csv`.

O artigo examina totais por participante, contagens de acerto por par correspondente, transições incorreto→correto/correto→incorreto e mudanças por conhecimento prévio autorrelatado. Os grupos são nenhum/básico (N=30) e intermediário/avançado (N=14). Respostas desconhecidas ou ausentes interrompem a análise atual; não são resolvidas pela alternativa mais frequente. A exportação não recupera automaticamente todos os distratores não escolhidos do formulário original.

### Questionário de experiência

O instrumento tem 31 afirmações com cinco categorias de resposta. Combina itens adaptados do MEEGA+, um item geral de aprendizagem percebida e quatro itens próprios para os objetivos educacionais do jogo. Os itens originais de interação social foram omitidos porque a atividade era individual. O mapa em `instruments/meega_items.json` registra Q01–Q09 como usabilidade, Q10–Q26 como experiência do jogador e Q27–Q31 como aprendizagem percebida. Q28–Q31 abordam identificação de atributos relevantes, vantagens e desvantagens dos padrões, análise de trade-offs e adequação arquitetural.

A análise relatada é por item: distribuição das cinco categorias e proporção que escolheu 4 ou 5. **Não foi atribuída uma classificação global de qualidade MEEGA+.** Não converter esse questionário adaptado em um escore global validado sem outra justificativa.

### Logs e medidas de participação

Todos os 44 participantes têm logs associados aos questionários. O §8.2, p10, descreve metadados de sessão e eventos com timestamp, categoria e campos próprios. O pacote distribui logs tratados, usando o mesmo código da avaliação final, e documenta sua interpretação em `docs/logs.md`.

| Medida relatada | Operação | Limite |
|---|---|---|
| Contratos distintos iniciados | Contar nomes distintos em eventos de início de contrato por participante; repetição conta uma vez | Início não comprova conclusão. |
| Padrões com contato registrado | Contar padrões distintos em eventos de conclusão do minigame por participante; repetição conta uma vez | O registro comprova contato com a atividade, não compreensão do conceito. |
| Uso do Notebook | Contar eventos de fechamento e somar a duração informada nesses eventos | Sem fechamento não há duração observada pela regra. Não presumir leitura ou aprendizagem. |

O artigo registra Notebook para 42 participantes; os dois sem eventos de fechamento são omitidos da Figura 12. O destaque P40 do artigo corresponde à observação de dez fechamentos e 10,38 minutos acumulados. Esse exemplo contextualiza um depoimento, sem estimar o efeito de aprendizagem do Notebook. O deslocamento vertical dos pontos na figura serve apenas para reduzir sobreposição.

Eventos adicionais incluem respostas de quiz, correção e tempo de resposta, além de resumos do trimestre com finanças, contratações e duração. A disponibilidade desses eventos não implica que todos foram usados em análises no artigo.

### Comentários abertos

O §8.6, p13–14, informa exame descritivo das respostas para contextualizar os números e identificar melhorias. Os trechos selecionados são exemplos, sem codificação formal de prevalência relatada. As citações foram traduzidas de português para inglês no artigo e mantêm os códigos daquela avaliação. A reprodução deve distinguir comentário original, tradução e interpretação do pesquisador.

## Alcance da reconstrução

As análises descritas são descritivas e exploratórias. Os estudos não incluíram controle, alocação aleatória a versões do jogo ou avaliação tardia. Não atribuir causalidade ao aumento pré/pós nem interpretar diferenças entre itens A/B como ganhos ou perdas conceituais estabelecidos. Escores iniciais altos limitam aumentos observáveis, e os grupos de conhecimento prévio são pequenos e desiguais. Percepções positivas, conclusão de puzzles e duração registrada não equivalem a aprendizagem transferível.

O conteúdo JSON recuperado documenta a representação do jogo. Um arquivo-fonte Godot foi localizado e tem proveniência registrada em `game/source-provenance.json`, mas sua correspondência com a build V2 avaliada não está estabelecida; o projeto completo e as builds não são distribuídos no pacote de avaliação. Os três textos de TCLE e o documento identificado como guia dos avaliadores são fornecidos pelo autor. O material separado de treinamento AHJED e a consolidação contemporânea dos avaliadores não foram localizados.

A tabela conceitual fornecida pelo autor, preservada em `game/pattern-attribute-conceptual.csv`, contém 63 sinais qualitativos e chaves de referência por padrão. `docs/pattern_traceability.md` distingue essa tabela dos multiplicadores do jogo. As quatro chaves têm entradas bibliográficas fornecidas, incluindo `Liu2021`, *A Survey of Operating System Microkernel*. A consulta independente a essa fonte ficou indisponível; a identificação bibliográfica fornecida não estabelece suporte verificado para cada sinal, nem para a transposição de microkernel de sistema operacional ao contexto de arquitetura de aplicação do jogo. Os sinais e a direção dos pesos não coincidem em todas as relações, e não foi fornecida justificativa específica para converter cada relação em um peso quantitativo. Essas fontes melhoram a rastreabilidade sem estabelecer, por si só, a validade de todos os vínculos acadêmicos ou o modelo de calibragem dos pesos. Esses limites são preservados em `docs/article_requirements.md`; nenhum documento novo é apresentado como um original ausente.
