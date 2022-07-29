# Criacao de Rotas Otimizadas para o Problema LTL
Repositório para entrega da solução do desafio proposto pela empresa Linear na disciplina PO-207 – Resolução de Problemas via Modelagem Matemática do PPGMAT/PPGPO

Para o problema se tem como variaveis os diferentes tipos de veiculo com suas respetivas capacidades e tempo de carregamento/descarregamento, as diferentes demandas com seus destinos e origem, prazos, tamanho em kg e horarios de coleta e entrega; os custos de viagem com carga ou vazio nos diferentes arcos dependendo dos veiculos disponiveis; e finalmente as filiais com seu tipo, identificação e capacidades de recebimento e expedição. Se quer minimizar o custo de transferência das demandas entre as filiais de final de linha.

Na resolução do problema se considera uma adaptação do algorithmo de Clarke para a criação das rotas de viagem, baixo as considerações seguintes:

-As demandas tem que chegar antes dos prazos
-As capacidades não podem ser maiores que do veiculo que leva as demandas
-Se tem os diferentes tipos de veiculo e custos
-Se considera a assimetria no fluxo das demandas
-Se tem fluxo zero dos veiculos
-Não se tem limite de veiculos
-Não se consideraram capacidades de recebimento e expedição
-Não se tem janela de tempo entre a coleta e entrega
-Não se considera o tipo de filial


Dadas as premisas anteriores, foram criadas as rotas iniciais de fluxo zero considerando as demandas das diferentes filiais, o menor custo de translado sem exceder a capacidade e tomando demandas como indivisíveis. Posteriormente, se fizeram combinações de rotas para minimizar os custos de transferência.
