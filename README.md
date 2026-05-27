# A-DAP: Protocolo de Responsabilização de Decisões Auditáveis

A-DAP é um protocolo arquitetônico para tornar as evidências de decisão da IA reconstruíveis de forma independente, falsificáveis e verificáveis externamente.

Este repositório é o principal ponto de acesso público para o trabalho técnico do A-DAP.

Não exige que os leitores confiem no autor.

O teste pede que eles examinem as evidências, reconstruam o processo de custódia da decisão e testem se uma adulteração pode permanecer indetectável.

---

## Tese principal

A governança da IA não pode se basear apenas em explicações, registros, capturas de tela ou documentação posterior.

Para sistemas de IA de alto impacto, a questão central não é apenas:

“Por que o sistema tomou essa decisão?”

A questão mais difícil é:

“Será que uma terceira parte independente consegue reconstruir e verificar as evidências existentes no momento em que a decisão foi tomada?”

A-DAP aborda esse problema por meio de uma arquitetura de custódia de decisões.

O protocolo separa:

- entrada de decisão
- resultado da decisão
- envelope de decisão
- processo de custódia
- evidência de verificação
- veredicto esperado
- tentativas de falsificação
- fronteiras de oráculo

O objetivo não é provar que a decisão foi correta.

O objetivo é tornar as evidências da decisão reconstruíveis de forma independente e estruturalmente difíceis de alterar sem serem detectadas.

---

## O que o A-DAP afirma

O A-DAP não afirma que a adulteração seja impossível.

O A-DAP afirma que adulterações não detectadas devem ter um custo estrutural mensurável.

O A-DAP não substitui responsabilidade legal, revisão institucional ou autoridade regulatória.

Ele fornece uma camada de verificabilidade que pode apoiá-las.

O A-DAP não requer a abertura do modelo interno.

Ele se concentra no conjunto de evidências que envolve uma decisão.

---

## Fronteira de Oráculo

O A-DAP não afirma tornar decisões de IA totalmente trustless.

Seu núcleo verificável se aplica aos registros de decisão, não à verdade da decisão.

Isso significa que o A-DAP pode verificar de forma independente artefatos como:

- envelopes canônicos de decisão
- hashes
- assinaturas
- âncoras de timestamp
- integridade de cadeia de hashes
- hashes de entrada
- hashes de política
- compromissos publicados externamente
- reconstrução determinística do registro

No entanto, o A-DAP não prova, por si só:

- que a entrada era verdadeira no mundo real
- que o modelo realmente executou a decisão
- que o estado do modelo era real
- que a identidade declarada do agente era institucionalmente válida
- que a política era juridicamente válida ou estava em vigor
- que a explicação reflete causalidade interna real
- que a decisão era correta, justa ou legítima

Essas afirmações permanecem dependentes de oráculos, salvo quando apoiadas separadamente por evidência externa.

Essa distinção está formalizada na nota:

[GCD-001 Oracle Boundary Note](./oracle-boundary.md)

Em resumo:

O A-DAP torna registros de decisão reconstruíveis de forma independente enquanto registros.

Ele separa o que pode ser verificado criptograficamente daquilo que continua dependente de oráculos externos.

A afirmação correta não é que o A-DAP prova a verdade da decisão.

A afirmação correta é que o A-DAP prova o que foi comprometido sobre uma decisão, quando foi comprometido, por qual chave criptográfica e se esse compromisso foi alterado depois do fato.

---

## Notas Técnicas Centrais

Este repositório atualmente inclui três notas técnicas centrais que definem o escopo, os limites e o caminho de reconstrução do A-DAP:

- [GCD-001 Oracle Boundary Note](./oracle-boundary.md)  
  Define o que o A-DAP consegue reconstruir de forma independente e o que permanece dependente de oráculos por desenho.

- [GCD-001 Oracle Boundary Note — Short Version](./oracle-boundary-short.md)  
  Fornece uma versão curta em inglês para revisores externos.

- [GCD-001 Reconstruction Specification](./gcd-001-reconstruction-spec.md)  
  Define como um verificador externo deve reconstruir o grafo de custódia de decisão, calcular ou desafiar o NDC alegado e distinguir reconstrução independente de simples execução de scripts fornecidos pelo autor.

Juntos, esses documentos estabelecem uma distinção crítica:

O A-DAP não prova a verdade da decisão.

O A-DAP torna registros de decisão reconstruíveis de forma independente enquanto registros.

Ele separa o que pode ser verificado criptograficamente daquilo que permanece dependente de oráculos externos.

O padrão correto de revisão é:

```text
Não confie no autor.
Reconstrua o grafo.
Calcule o corte.
Desafie o NDC.
Declare a fronteira de oráculo.
