# Filtragem e desidentificação

O pacote mantém as observações necessárias para repetir as análises. `raw_anonymized` significa uma extração dos valores observados com identificadores removidos, e não a exportação original intacta. As planilhas integrais e a correspondência entre nomes e códigos ficam fora do repositório.

| Fonte | Entrada | Análise | Decisão |
|---|---:|---:|---|
| AHJED | 5 avaliadores, 42 itens | 5, 210 avaliações | Nenhum avaliador excluído. Severidades 0–4 preservadas. |
| IMI/IMMS | 18 respostas no Google | 18 | Última resposta excluída por instrução explícita do autor. A exportação local já contém apenas as 18 incluídas. |
| Pré/pós | 44 pares completos | 44 | Sem exclusão por teto, queda de nota ou mudança pequena. |
| MEEGA+ adaptado | 44 respostas, 31 itens | 44, 1.364 avaliações | Sem exclusão automática por respostas iguais. |
| Comentários finais | 132 campos | Campos respondidos e ausentes preservados | Vazios não viram avaliações negativas. |
| Conversa da heurística | Transcrição da conversa com o autor | 10 unidades parafraseadas | Mensagem repetida, citações em respostas, pontuação solta e mensagens administrativas não duplicam evidência. |


Os códigos `H01–H05`, `M001–M019` e `P001–P044` pertencem a coortes independentes. P001 corresponde ao P1 da avaliação final no artigo, P040 ao P40. Não existe ligação de pessoas entre as três avaliações. Os códigos S1–S3 identificam apenas interlocutores distintos na conversa fornecida, sem presumir sua identidade entre os cinco avaliadores.

Timestamps de formulários, nomes e telefone dos participantes, links de upload e nomes de arquivos de logs foram retirados. Demografia detalhada por pessoa foi substituída por contagens agregadas; conhecimento prévio por participante foi mantido apenas para reproduzir o agrupamento dos testes. Nos logs, tempos absolutos e identificação de sessão são substituídos por offsets relativos. 


A resposta livre de gênero que não corresponde às categorias padronizadas foi resumida como `Other (free-text)`, seguindo a Tabela 5. Não foi convertida em uma identidade de gênero, nem usada para eliminar o participante. Ausência, valor inválido e zero são distintos.

Uma resposta repetida não prova duplicidade de participante. IDs de estudo únicos e consentimento foram conferidos na ingestão. As rotinas interrompem a análise em valores quantitativos inesperados. Não há imputação, remoção por resultado indesejado, dedução de gabarito por frequência ou ajuste de dados para coincidir com o artigo.

Os comentários abertos foram revisados para nomes, contatos e links pessoais. As paráfrases da conversa não são transcrições literais e não devem ser usadas como citações entre aspas. Os comentários do formulário são mantidos como texto da fonte. A síntese editorial não constitui codificação temática com frequência ou concordância entre avaliadores.
