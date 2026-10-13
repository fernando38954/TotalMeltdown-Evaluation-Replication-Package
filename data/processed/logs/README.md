# Entradas públicas dos logs

São 44 arquivos JSON, um por participante da avaliação final, com 1.747 eventos. P001–P044 seguem a mesma ordem usada nos dados do pré/pós-teste e do MEEGA+. Todos os eventos estão preservados; as reduções a primeira observação ou conteúdo distinto são operações reproduzidas por `scripts/logs.py`.

Nomes, nomes dos arquivos originais, links, IDs de sessão, datas/horas absolutas e plataforma foram omitidos. `relative_time_seconds` preserva a cronologia em segundos a partir do primeiro evento de cada participante. `header_game_time_seconds` é a conversão do campo `Game Time`, cuja equivalência a tempo ativo não foi confirmada.

O dicionário, as regras de preparação e os limites das medidas estão em `docs/logs.md`. Os arquivos não contêm o mapa de associação às fontes privadas.
