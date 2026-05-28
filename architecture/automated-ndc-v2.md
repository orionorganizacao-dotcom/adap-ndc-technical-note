# Automated NDC v2: Custody-Graph Analysis

This document defines the intended direction for A-DAP v2 regarding automated NDC analysis.

It incorporates a critical constraint:

An automated NDC solver can compute over a custody graph, but it cannot make the custody graph true.

Therefore, A-DAP v2 must not be presented as a final automated NDC validator.

It should be presented as a custody-graph solver for self-reported NDC analysis.

---

## 1. Purpose

The purpose of A-DAP v2 is to model decision custody as a graph and compute where custody collapses, where independence is claimed, where independence is evidenced, and where independence remains unknown.

The v2 solver should help answer:

```txt
Given a declared custody graph, what is the minimum set of control domains that must collude for a falsified decision record to pass without evidence?
