# A-DAP: Verificação por Grafo de Custódia e NDC

Este repositório contém uma nota técnica inicial sobre o A-DAP, um modelo de verificação por grafo de custódia para sistemas opacos de decisão em IA.

O A-DAP não afirma provar a causalidade interna oculta de um sistema de IA. Em vez disso, ele vincula artefatos observáveis de decisão antes da ação, modela sua custódia como um grafo temporal e define o Número de Disjunção de Custódia (NDC) como uma medida conservadora do custo estrutural necessário para falsificar registros observáveis de decisão sem detecção.

## Status atual

Rascunho de trabalho: Nota Técnica v0.3.1

Este rascunho é formal e arquitetural. Ele ainda não fornece validação empírica em implantações reais, nem apresenta uma implementação completa de solver min-cut para cálculo do NDC.

## Tese central

O A-DAP não prova por que um sistema de IA decidiu.

Ele prova o que foi observavelmente comprometido antes da ação, mede quantos domínios efetivos de custódia precisariam coludir, falhar ou ser comprometidos para que uma história observável falsa permanecesse aceitável para um verificador declarado, e identifica o limite em que a falsificação deixa de ser apenas registral e se torna causalmente indistinguível.

## Conceitos-chave

- Envelope de decisão pré-ação
- Grafo temporal de custódia
- Colapso conservador de domínios de custódia
- Número de Disjunção de Custódia (NDC)
- Compromisso de escopo
- Evidência de geração
- Evidência de execução
- Insuficiência de ancoragem temporal
- Vitrine causal observacionalmente completa
- Gargalo do Envelope
- Camada pública de custódia técnica

## Afirmação principal

Carimbo de tempo externo, hashing, assinaturas ou ancoragem Merkle, isoladamente, não elevam o NDC acima de 1 contra um operador interno capaz de construir um estado demonstrativo coerente antes da ancoragem.

NDC maior que 1 exige disjunção de custódia na origem da geração, não apenas ancoragem posterior.

Em outras palavras, um sistema não se torna estruturalmente verificável apenas porque seus outputs são carimbados após a criação. A verificabilidade estrutural exige que as camadas de criação, compromisso, custódia e verificação sejam separadas de modo que a falsificação retroativa exija comprometimento de domínios disjuntos.

## O que o A-DAP não afirma

O A-DAP não prova:

- causalidade interna oculta;
- legitimidade moral;
- justiça/fairness;
- correção da decisão;
- accountability jurídica por si só;
- a verdade das razões declaradas.

O A-DAP fornece um substrato forense. A accountability institucional ainda exige uma autoridade externa ao gerador.

## Gargalo do Envelope

O A-DAP prova principalmente a não adulteração retroativa após o compromisso e a ancoragem.

Ele não prova, por si só, que o envelope inicial representou fielmente tudo o que ocorreu no momento da decisão. Se o registro inicial nasce falso, incompleto ou manipulado no instante da escrita, o A-DAP pode preservar esse registro com integridade, mas não transforma falsidade original em verdade.

Esse é o Gargalo do Envelope.

Portanto, o objetivo do A-DAP não é eliminar totalmente a confiança, mas relocalizar e distribuir a confiança entre camadas públicas, auditáveis e verificáveis de forma independente.

## Fé pública vs. verificabilidade estrutural

O A-DAP não deve ser confundido com um sistema notarial ou cartorial.

Um cartório digital prova por fé pública. O A-DAP verifica por arquitetura distribuída.

O primeiro concentra confiança em uma autoridade juridicamente sancionada. O segundo distribui confiança entre premissas técnicas públicas e auditáveis.

O A-DAP não substitui tribunais, reguladores, cartórios ou autoridades institucionais. Ele fornece uma camada pré-forense de verificabilidade, permitindo que um auditor independente reconstrua evidências técnicas antes que essas evidências sejam levadas a um foro institucional.

A distinção é:

- sistemas notariais respondem à pergunta jurídica sobre admissibilidade, autoridade e reconhecimento formal;
- o A-DAP responde à pergunta técnica adversarial sobre se um registro observável de decisão poderia ter sido adulterado retroativamente sem atravessar domínios disjuntos de custódia.

Essas são camadas complementares, não sistemas concorrentes.

## Camada Pública de Custódia Técnica

Este repositório não é um cartório jurídico.

Ele fornece uma camada pública de custódia técnica para artefatos A-DAP por meio de:

- versionamento público;
- manifestos SHA-256 de release;
- instruções de verificação de commits assinados;
- documentação de reivindicação de carimbo de tempo;
- ancoragem RFC 3161 / ICP-Brasil planejada;
- ancoragem OpenTimestamps planejada;
- futura reconstrução independente por verificação baseada em solver.

O objetivo não é eliminar a confiança, mas relocalizá-la e distribuí-la entre camadas públicas, auditáveis e verificáveis de forma independente.

## Artefatos de prova

O diretório `proofs/` contém a estrutura inicial para custódia pública e artefatos de verificação externa.

Estrutura atual de prova:

- `proofs/public-key.asc` — placeholder da chave pública para verificação de commits e artefatos;
- `proofs/release-v0.3.1.sha256` — placeholder do manifesto SHA-256 da release;
- `proofs/signed-commit-instructions.md` — instruções para verificação offline de assinatura de commit;
- `proofs/timestamp-claim.md` — status de carimbo de tempo e camada de ancoragem planejada;
- `proofs/ots-proof/` — diretório de provas OpenTimestamps planejado;
- `proofs/rfc3161-proof/` — diretório de provas RFC 3161 / ICP-Brasil planejado.

Esses arquivos ainda não constituem uma prova externa completa. Eles definem a superfície de prova e declaram as camadas de verificação pretendidas.

## Modelo de verificação

O A-DAP distingue entre confiança visível na plataforma e prova reconstruível de forma independente.

Por exemplo, o selo “Verified” do GitHub é uma camada de conveniência. A evidência verificável de forma independente é a assinatura criptográfica anexada ao commit, que pode ser verificada fora do GitHub usando a chave pública correspondente.

Um futuro auditor deverá ser capaz de verificar:

```bash
git verify-commit <commit_hash>
