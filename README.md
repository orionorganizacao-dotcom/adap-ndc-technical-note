# A-DAP: Protocolo de Responsabilização de Decisões Auditáveis

A-DAP é um protocolo arquitetônico para tornar as evidências de decisão da IA reconstruíveis de forma independente, falsificáveis e verificáveis externamente.

Este repositório é o principal ponto de acesso público para o trabalho técnico do A-DAP.

Não exige que os leitores confiem no autor.

O teste pede que eles examinem as evidências, reconstruam o processo de tomada de decisão e testem se a adulteração pode permanecer indetectável.

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

O objetivo não é provar que a decisão foi correta.

O objetivo é tornar as evidências da decisão reconstruíveis de forma independente e estruturalmente difíceis de alterar sem serem detectadas.

---

## O que a A-DAP afirma

A A-DAP não afirma que a adulteração seja impossível.

A A-DAP afirma que adulterações não detectadas devem ter um custo estrutural mensurável.

O A-DAP não substitui a responsabilidade legal, a revisão institucional ou a autoridade regulatória.

Ele fornece uma camada de verificabilidade que pode suportá-los.

O A-DAP não requer a abertura do modelo interno.

Concentra-se no conjunto de evidências que envolvem uma decisão.

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

[Leia a GCD-001 Oracle Boundary Note](./oracle-boundary.md)

Em resumo:

O A-DAP torna registros de decisão reconstruíveis de forma independente enquanto registros.

Ele separa o que pode ser verificado criptograficamente daquilo que continua dependente de oráculos externos.

A afirmação correta não é que o A-DAP prova a verdade da decisão.

A afirmação correta é que o A-DAP prova o que foi comprometido sobre uma decisão, quando foi comprometido, por qual chave criptográfica e se esse compromisso foi alterado depois do fato.

---

## Por que isso é importante?

Muitas abordagens de governança de IA dependem de registros internos, explicações de modelos, relatórios de auditoria ou confiança institucional.

Esses mecanismos podem ser úteis, mas muitas vezes permanecem dentro do sistema ou sob o controle da mesma organização que tomou a decisão.

O A-DAP foi projetado com base em um princípio diferente:

A verificação não deve depender apenas da confiança no sistema que tomou a decisão.

Para IA de alto risco, as evidências em torno de uma decisão devem ser reconstruíveis fora dos limites originais do sistema.

---

## O que é verificado

O A-DAP permite verificar:

- se o envelope de decisão foi preservado
- se os hashes correspondem aos artefatos originais
- se a cadeia de custódia permanece consistente
- se uma assinatura criptográfica é válida
- se um commitment foi alterado depois do registro
- se a evidência reconstruída corresponde ao veredicto esperado
- se uma tentativa de adulteração muda o resultado da verificação

O A-DAP não verifica automaticamente:

- verdade factual do mundo externo
- legitimidade jurídica da decisão
- intenção humana
- validade institucional completa
- causalidade interna total do modelo
- justiça moral da decisão

Esses elementos podem exigir revisão humana, institucional, jurídica ou regulatória.

O papel do A-DAP é tornar a camada técnica de evidência mais verificável, menos dependente de confiança e mais resistente à adulteração silenciosa.

---

## NDC: Custo de Não Detecção

O conceito central deste repositório é o NDC:

Non-Detection Cost.

NDC mede o custo estrutural necessário para adulterar um grafo de custódia de decisão sem que a adulteração seja detectada.

Em vez de perguntar apenas se um registro existe, o NDC pergunta:

“Quanto teria que ser alterado para que uma falsificação permanecesse consistente?”

Quanto maior o custo estrutural de falsificação indetectável, mais forte é a custódia da decisão.

Quanto menor o custo, mais frágil é a alegação de auditabilidade.

---

## A-DAP e Proof-of-Work

Existe uma analogia limitada, mas útil, entre A-DAP e proof-of-work.

No Bitcoin, a segurança vem do custo de reescrever o histórico sem ser detectado.

No A-DAP, o NDC mede o custo estrutural de alterar a custódia de uma decisão sem quebrar a consistência verificável.

Mas há uma diferença essencial:

Bitcoin verifica um universo fechado.

O ledger do Bitcoin não precisa provar que uma transação corresponde a uma verdade externa. Ele só precisa verificar se a transação é válida dentro do próprio ledger.

O A-DAP opera em um mundo aberto.

Decisões de IA envolvem entradas, agentes, políticas, modelos, estados, ambientes de execução e fatos externos.

Por isso, o A-DAP não herda a trustlessness completa do Bitcoin.

O A-DAP herda apenas a intuição estrutural:

aumentar o custo de falsificação indetectável.

A fronteira entre registro verificável e verdade externa deve ser declarada explicitamente.

---

## Regimes de verificação

O A-DAP separa três regimes:

### Regime I — Verificação fechada

Artefatos que podem ser verificados sem referência ao mundo externo.

Exemplos:

- hashes
- assinaturas
- envelopes canônicos
- cadeias de hash
- integridade de ledger
- reconstrução determinística de digests

Esse regime verifica integridade de registro.

Não verifica verdade da decisão.

### Regime II — Verificação ancorada externamente

Artefatos cuja força depende de uma âncora externa.

Exemplos:

- RFC 3161 timestamp
- OpenTimestamps
- âncoras em blockchain pública
- publicação externa de Merkle roots
- múltiplas autoridades independentes de tempo

Esse regime fortalece anterioridade e integridade temporal.

Não prova a verdade do conteúdo registrado.

### Regime III — Afirmações dependentes de oráculo

Afirmações que não podem ser reconstruídas apenas a partir de artefatos criptográficos.

Exemplos:

- verdade do input no mundo real
- identidade real do agente
- custódia operacional da chave
- execução real do modelo
- estado real do modelo
- causalidade interna da inferência
- validade jurídica da política
- legitimidade ou correção da decisão

Essas afirmações devem ser declaradas como fronteiras de oráculo.

Não devem ser escondidas dentro do ledger.

---

## O que este repositório contém

Este repositório reúne os materiais técnicos públicos do A-DAP, incluindo:

- nota técnica principal
- modelo conceitual do protocolo
- estrutura de verificação
- análise de NDC
- mapa de fronteiras de oráculo
- exemplos de reconstrução
- desafio público de verificabilidade
- materiais para revisão externa

O objetivo é permitir que terceiros avaliem a arquitetura sem depender da autoridade do autor.

---

## Estado do repositório

Versão pública atual:

```text
A-DAP Public Challenge v0.4
