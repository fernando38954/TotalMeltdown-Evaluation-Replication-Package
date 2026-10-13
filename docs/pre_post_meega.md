# Pré/pós, MEEGA+ e comentários

O snapshot de 44 participantes do Google foi comparado à exportação local usada no artigo. Todos os valores analíticos e IDs coincidiram; timestamps e links de uploads não foram usados na comparação. A ordem da exportação e os IDs 1–44 coincidem; os códigos públicos são P001–P044.

Os motores `pre_post_engine.py` e `meega_engine.py` foram reaproveitados dos scripts fornecidos nas fontes locais, com adaptação mínima para saídas gráficas PNG/SVG. Os adaptadores públicos leem CSV saneado e preservam o gabarito e o cálculo original. Campos de localização em saídas apontam para o CSV distribuído, não para células de uma planilha privada.

O gabarito foi encontrado em `analise_reproduzivel/gabarito.json`, com nota explícita de que foi informado pelo autor. O pacote preserva tanto a redação oficial quanto a redação exportada. Não é uma reconstrução pelo padrão de respostas da turma. As alternativas observadas não substituem o formulário original completo: alternativas nunca selecionadas podem faltar.

Formas A/B: conteúdos correspondentes, cenários diferentes, 14 acertos possíveis. São incluídos todos os pares e ambos os grupos de conhecimento autodeclarado. Nenhum participante foi excluído pelo teto. Não foi demonstrada equivalência psicométrica entre as formas. As análises são descritivas, sem teste inferencial, ganho normalizado, regressão ou atribuição causal.

MEEGA+: 31 itens 1–5, com contagens por categoria, média, mediana e SD amostral por item. Os objetivos específicos Q28–Q31 são itens do estudo, não uma escala MEEGA+ validada. A reprodução não inventa um escore global nem atribui aprendizagem medida a uma resposta de percepção.

Comentários finais: os três campos são mantidos mesmo quando vazios. `results/feedback/coverage.csv` reproduz cobertura 35/44, 32/44 e 31/44. A análise do artigo seleciona relatos para ilustrar problemas e sugestões. Não foi encontrado um codebook de codificação temática com avaliadores independentes; o pacote não afirma prevalência de temas nem concordância.
