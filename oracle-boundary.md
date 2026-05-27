# GCD-001 Oracle Boundary Note

# Nota de Fronteira de Oráculo GCD-001

## Status

Candidate architectural note.  
Pending external reconstruction review.

Nota arquitetural candidata.  
Pendente de revisão externa por reconstrução independente.

This note defines the boundary between what GCD-001 can independently reconstruct and what remains oracle-bound by design.

Esta nota define a fronteira entre o que o GCD-001 consegue reconstruir de forma independente e o que permanece dependente de oráculos por desenho.

Its purpose is to prevent overclaiming.

Seu objetivo é evitar afirmações excessivas.

GCD-001 does not claim to make AI decisions fully trustless.

O GCD-001 não afirma tornar decisões de IA totalmente trustless.

It claims to make decision records independently reconstructible as records, while explicitly declaring the oracle-bound assumptions required to interpret those records as true descriptions of real-world decision processes.

Ele afirma tornar registros de decisão reconstruíveis de forma independente enquanto registros, declarando explicitamente as premissas dependentes de oráculos necessárias para interpretar esses registros como descrições verdadeiras de processos decisórios no mundo real.

---

## 1. Core Distinction

## 1. Distinção Central

A-DAP does not prove that a decision was true.

O A-DAP não prova que uma decisão era verdadeira.

It proves what was committed about the decision, when it was committed, by which cryptographic key, and whether that commitment was later altered.

Ele prova o que foi comprometido sobre a decisão, quando foi comprometido, por qual chave criptográfica e se esse compromisso foi alterado posteriormente.

This distinction is structural.

Essa distinção é estrutural.

A cryptographic record can prove integrity of bytes.

Um registro criptográfico pode provar a integridade dos bytes.

It cannot, by itself, prove that those bytes faithfully describe reality.

Ele não pode, por si só, provar que esses bytes descrevem fielmente a realidade.

---

## 2. Regime I — Closed-World Trustless Verification

## 2. Regime I — Verificação Trustless de Mundo Fechado

Regime I contains artifacts that can be independently verified without reference to external-world truth.

O Regime I contém artefatos que podem ser verificados de forma independente sem referência à verdade do mundo externo.

These include:

Estes incluem:

- canonical decision envelopes;
- envelopes canônicos de decisão;
- envelope hashes;
- hashes de envelope;
- input hashes;
- hashes de entrada;
- policy hashes;
- hashes de política;
- signature verification;
- verificação de assinatura;
- hash-chain consistency;
- consistência de cadeia de hashes;
- ledger integrity;
- integridade do ledger;
- deterministic reconstruction of digests;
- reconstrução determinística de digests.

A valid Regime I claim is:

Uma afirmação válida de Regime I é:

These bytes match the committed artifact and have not changed after commitment.

Estes bytes correspondem ao artefato comprometido e não foram alterados após o compromisso.

A Regime I claim does not prove:

Uma afirmação de Regime I não prova:

- that the input was true;
- que a entrada era verdadeira;
- that the policy was valid;
- que a política era válida;
- that the model actually executed;
- que o modelo realmente executou;
- that the agent identity was legitimate;
- que a identidade do agente era legítima;
- that the decision was correct.
- que a decisão era correta.

Regime I verifies record integrity, not decision truth.

O Regime I verifica integridade de registro, não verdade da decisão.

---

## 3. Regime II — Externally Anchored Verification

## 3. Regime II — Verificação Ancorada Externamente

Regime II contains artifacts whose verification depends on external anchoring infrastructure.

O Regime II contém artefatos cuja verificação depende de infraestrutura externa de ancoragem.

These may include:

Estes podem incluir:

- RFC 3161 timestamp tokens;
- tokens de timestamp RFC 3161;
- timestamp authority certificate chains;
- cadeias de certificados de autoridades de timestamp;
- OpenTimestamps proofs;
- provas OpenTimestamps;
- public blockchain anchors;
- âncoras em blockchain pública;
- Merkle roots published outside the original system;
- Merkle roots publicadas fora do sistema original;
- multiple independent time anchors.
- múltiplas âncoras independentes de tempo.

A valid Regime II claim is:

Uma afirmação válida de Regime II é:

This commitment existed before or at a verifiable external time boundary.

Este compromisso existia antes ou no momento de uma fronteira temporal externa verificável.

Regime II strengthens temporal integrity.

O Regime II fortalece a integridade temporal.

It does not prove the truth of the committed content.

Ele não prova a verdade do conteúdo comprometido.

The timestamp proves that a commitment existed at a given time.

O timestamp prova que um compromisso existia em determinado momento.

It does not prove that the commitment accurately described a real decision process.

Ele não prova que o compromisso descrevia corretamente um processo decisório real.

---

## 4. Regime III — Oracle-Bound Claims

## 4. Regime III — Afirmações Dependentes de Oráculo

Regime III contains claims that cannot be independently reconstructed from cryptographic artifacts alone.

O Regime III contém afirmações que não podem ser reconstruídas de forma independente apenas a partir de artefatos criptográficos.

These include:

Estas incluem:

- real-world truth of inputs;
- verdade das entradas no mundo real;
- identity of the real agent behind a key;
- identidade do agente real por trás de uma chave;
- key custody and operational control;
- custódia da chave e controle operacional;
- correspondence between a public key and a specific model or agent;
- correspondência entre uma chave pública e um modelo ou agente específico;
- actual model execution;
- execução real do modelo;
- model state at inference time;
- estado do modelo no momento da inferência;
- runtime environment integrity;
- integridade do ambiente de execução;
- causal relation between input, model, policy, and output;
- relação causal entre entrada, modelo, política e saída;
- legal or institutional validity of a policy;
- validade legal ou institucional de uma política;
- correctness, fairness, or legitimacy of the decision;
- correção, justiça ou legitimidade da decisão;
- correspondence between the decision record and the external world.
- correspondência entre o registro da decisão e o mundo externo.

A valid Regime III declaration is:

Uma declaração válida de Regime III é:

This claim depends on an external oracle and is not independently reconstructible from the A-DAP record alone.

Esta afirmação depende de um oráculo externo e não é reconstruível de forma independente apenas a partir do registro A-DAP.

A Regime III declaration is not a reconstruction failure.

Uma declaração de Regime III não é uma falha de reconstrução.

It is a boundary condition.

Ela é uma condição de fronteira.

However, Regime III must not be used as a convenience category.

No entanto, o Regime III não deve ser usado como categoria de conveniência.

A claim may only be classified as Regime III when independent reconstruction is impossible without an external oracle.

Uma afirmação só pode ser classificada como Regime III quando a reconstrução independente for impossível sem um oráculo externo.

If a claim can be migrated into Regime I or Regime II through commitment, anchoring, canonicalization, external custody, or independent publication, it should not be hidden inside Regime III.

Se uma afirmação puder ser migrada para o Regime I ou Regime II por meio de compromisso, ancoragem, canonicalização, custódia externa ou publicação independente, ela não deve ser escondida dentro do Regime III.

---

## 5. Oracle Boundary Criterion

## 5. Critério de Fronteira de Oráculo

A claim belongs to Regime III only if at least one of the following conditions applies:

Uma afirmação pertence ao Regime III apenas se pelo menos uma das seguintes condições se aplicar:

1. The claim depends on correspondence with external-world facts not contained in the committed bytes.

1. A afirmação depende de correspondência com fatos do mundo externo não contidos nos bytes comprometidos.

2. The claim depends on identity, authority, intent, or institutional custody.

2. A afirmação depende de identidade, autoridade, intenção ou custódia institucional.

3. The claim depends on computational state that cannot be deterministically reconstructed by an external verifier.

3. A afirmação depende de estado computacional que não pode ser reconstruído deterministicamente por um verificador externo.

4. The claim depends on internal causality that is not directly observable from the record.

4. A afirmação depende de causalidade interna que não é diretamente observável a partir do registro.

5. The claim requires privileged access to the original execution environment.

5. A afirmação exige acesso privilegiado ao ambiente original de execução.

6. The claim depends on legal, organizational, or human interpretation outside the cryptographic record.

6. A afirmação depende de interpretação legal, organizacional ou humana fora do registro criptográfico.

If none of these conditions applies, the claim should be treated as a candidate for Regime I or Regime II reconstruction.

Se nenhuma dessas condições se aplicar, a afirmação deve ser tratada como candidata à reconstrução em Regime I ou Regime II.

---

## 6. The Trustless Core Is About Records

## 6. O Núcleo Trustless Trata de Registros

GCD-001 contains a real trustless core, but its scope is narrow.

O GCD-001 contém um núcleo trustless real, mas seu escopo é estreito.

The trustless core verifies:

O núcleo trustless verifica:

- record integrity;
- integridade do registro;
- hash consistency;
- consistência de hashes;
- signature validity;
- validade de assinatura;
- commitment structure;
- estrutura do compromisso;
- temporal anchoring, when externally anchored;
- ancoragem temporal, quando houver âncora externa;
- tamper evidence after commitment.
- evidência de adulteração após o compromisso.

The trustless core does not verify:

O núcleo trustless não verifica:

- truth of the input;
- verdade da entrada;
- identity of the real-world actor;
- identidade do ator no mundo real;
- actual model execution;
- execução real do modelo;
- real model state;
- estado real do modelo;
- causal explanation;
- explicação causal;
- decision correctness;
- correção da decisão;
- legal legitimacy.
- legitimidade jurídica.

Therefore, the accurate claim is:

Portanto, a afirmação correta é:

A-DAP has a trustless core for decision records, not for decision truth.

O A-DAP possui um núcleo trustless para registros de decisão, não para a verdade da decisão.

---

## 7. Oracle Cut Principle

## 7. Princípio do Corte de Oráculo

In a decision-custody graph, the global reconstructibility of a claim is limited by the cheapest sufficient verification cut.

Em um grafo de custódia de decisão, a reconstruibilidade global de uma afirmação é limitada pelo corte verificatório suficiente mais barato.

If a claim depends on a single oracle-bound edge in series, that oracle dominates the verification path.

Se uma afirmação depende de uma única aresta dependente de oráculo em série, esse oráculo domina o caminho de verificação.

For example:

Por exemplo:

- a valid signature proves that a key signed the envelope;
- uma assinatura válida prova que uma chave assinou o envelope;
- it does not prove that the declared agent controlled the key;
- ela não prova que o agente declarado controlava a chave;
- therefore, any claim that “agent A made decision X” remains oracle-bound unless key custody and identity are externally established.
- portanto, qualquer afirmação de que “o agente A tomou a decisão X” permanece dependente de oráculo, salvo se a custódia da chave e a identidade forem estabelecidas externamente.

Similarly:

De modo semelhante:

- a model hash may prove the integrity of a model artifact;
- um hash de modelo pode provar a integridade de um artefato de modelo;
- it does not prove that this model actually executed the decision;
- ele não prova que esse modelo realmente executou a decisão;
- therefore, any claim that “model M produced output X” remains oracle-bound unless execution is independently attested.
- portanto, qualquer afirmação de que “o modelo M produziu a saída X” permanece dependente de oráculo, salvo se a execução for atestada de forma independente.

However, oracle dependence can sometimes be reduced through redundancy.

No entanto, a dependência de oráculos pode, em alguns casos, ser reduzida por redundância.

Multiple independent external anchors, independent input sources, external key custody, hardware attestation, public publication, and third-party audits may increase the cost of falsification.

Múltiplas âncoras externas independentes, fontes independentes de entrada, custódia externa de chaves, atestação de hardware, publicação pública e auditorias de terceiros podem aumentar o custo de falsificação.

This does not eliminate the oracle problem.

Isso não elimina o problema do oráculo.

It makes the oracle boundary more explicit and more expensive to compromise.

Isso torna a fronteira de oráculo mais explícita e mais cara de comprometer.

---

## 8. Reconstruction Failure vs. Oracle Boundary

## 8. Falha de Reconstrução vs. Fronteira de Oráculo

A reconstruction failure occurs when a Regime I or Regime II artifact cannot be independently verified.

Uma falha de reconstrução ocorre quando um artefato de Regime I ou Regime II não pode ser verificado de forma independente.

Examples:

Exemplos:

- hash mismatch;
- divergência de hash;
- invalid signature;
- assinatura inválida;
- broken hash chain;
- cadeia de hashes quebrada;
- invalid timestamp token;
- token de timestamp inválido;
- canonicalization ambiguity;
- ambiguidade de canonicalização;
- missing committed artifact;
- artefato comprometido ausente;
- digest mismatch under the published specification.
- divergência de digest sob a especificação publicada.

An oracle boundary occurs when the claim was never independently reconstructible from the record alone.

Uma fronteira de oráculo ocorre quando a afirmação nunca foi reconstruível de forma independente apenas a partir do registro.

Examples:

Exemplos:

- input truth;
- verdade da entrada;
- agent identity;
- identidade do agente;
- real model execution;
- execução real do modelo;
- model state;
- estado do modelo;
- causal explanation;
- explicação causal;
- decision correctness.
- correção da decisão.

These must not be confused.

Essas categorias não devem ser confundidas.

Failure to reconstruct a Regime I or II artifact is a protocol or implementation failure.

Falha ao reconstruir um artefato de Regime I ou II é uma falha de protocolo ou implementação.

Failure to reconstruct a Regime III claim is expected, provided the boundary was explicitly declared.

Falha ao reconstruir uma afirmação de Regime III é esperada, desde que a fronteira tenha sido declarada explicitamente.

Failure to declare a Regime III dependency is an overclaim.

Falhar em declarar uma dependência de Regime III é uma afirmação excessiva.

---

## 9. What External Reviewers Should Reconstruct

## 9. O Que Revisores Externos Devem Reconstruir

External reviewers should attempt to independently reconstruct:

Revisores externos devem tentar reconstruir de forma independente:

- the canonical envelope;
- o envelope canônico;
- the envelope hash;
- o hash do envelope;
- input and policy hashes;
- hashes de entrada e de política;
- signature validity;
- validade da assinatura;
- hash-chain consistency;
- consistência da cadeia de hashes;
- timestamp validity, if present;
- validade do timestamp, se houver;
- Merkle root consistency, if present;
- consistência da Merkle root, se houver;
- any published external anchor;
- qualquer âncora externa publicada;
- whether the declared Regime III boundaries are complete and justified.
- se as fronteiras declaradas de Regime III estão completas e justificadas.

External reviewers should not be expected to reconstruct:

Revisores externos não devem ser esperados a reconstruir:

- whether the input was true;
- se a entrada era verdadeira;
- whether the model actually executed;
- se o modelo realmente executou;
- whether the model state was real;
- se o estado do modelo era real;
- whether the agent identity was institutionally valid;
- se a identidade do agente era institucionalmente válida;
- whether the decision was correct;
- se a decisão era correta;
- whether the explanation reflects true internal causality.
- se a explicação reflete causalidade interna real.

Those are oracle-bound claims unless separately supported by external evidence.

Essas são afirmações dependentes de oráculo, salvo quando apoiadas separadamente por evidência externa.

---

## 10. Minimal Honest Claim

## 10. Afirmação Honesta Mínima

The minimal honest claim of GCD-001 is:

A afirmação honesta mínima do GCD-001 é:

A-DAP makes decision records independently reconstructible as records.

O A-DAP torna registros de decisão reconstruíveis de forma independente enquanto registros.

It does not make the full decision process trustless.

Ele não torna o processo decisório completo trustless.

It separates what can be cryptographically verified from what remains dependent on external oracles.

Ele separa o que pode ser verificado criptograficamente daquilo que permanece dependente de oráculos externos.

---

## 11. Practical Implication

## 11. Implicação Prática

The design goal is not to pretend that all trust has been eliminated.

O objetivo de design não é fingir que toda confiança foi eliminada.

The design goal is to move as much verification load as possible from Regime III into Regime I or Regime II, and to explicitly declare what cannot be migrated.

O objetivo de design é mover o máximo possível da carga verificatória do Regime III para o Regime I ou Regime II, e declarar explicitamente aquilo que não pode ser migrado.

Examples of migration include:

Exemplos de migração incluem:

- committing inputs before action;
- comprometer entradas antes da ação;
- hashing policy versions;
- aplicar hash a versões de política;
- anchoring commitments externally;
- ancorar compromissos externamente;
- publishing Merkle roots;
- publicar Merkle roots;
- using independent timestamp authorities;
- usar autoridades independentes de timestamp;
- separating key custody from model operation;
- separar custódia de chaves da operação do modelo;
- using independent execution attestation where possible;
- usar atestação independente de execução quando possível;
- requiring reviewers to reconstruct digests from specification, not merely run author-provided scripts.
- exigir que revisores reconstruam digests a partir da especificação, e não apenas executem scripts fornecidos pelo autor.

Residual oracle-bound claims should remain visible.

Afirmações residuais dependentes de oráculo devem permanecer visíveis.

They should not be hidden inside the ledger.

Elas não devem ser escondidas dentro do ledger.

---

## 12. Canonical Statement

## 12. Declaração Canônica

A-DAP does not eliminate trust.

O A-DAP não elimina a confiança.

It localizes and names trust.

Ele localiza e nomeia a confiança.

It prices what is structurally verifiable.

Ele precifica o que é estruturalmente verificável.

It declares what remains oracle-bound.

Ele declara o que permanece dependente de oráculos.

GCD-001 is therefore not a proof of decision truth.

Portanto, o GCD-001 não é uma prova da verdade da decisão.

It is a reconstruction protocol for decision records with explicit oracle-boundary disclosure.

Ele é um protocolo de reconstrução de registros de decisão com declaração explícita de fronteiras de oráculo.
