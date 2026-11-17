# Jobs da esteira

Cada arquivo `.json` nesta pasta é uma ordem de serviço para a Nuvemshop.
Ao enviar um job novo para a branch `main`, o GitHub Actions executa o job
(`.github/workflows/esteira.yml`) e grava o resultado em `relatorios/`.

O token da loja fica no secret `NUVEMSHOP_TOKEN` e nunca aparece no código nem nos logs.
