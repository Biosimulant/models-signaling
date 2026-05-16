# models-signaling

> Storage-only repo: each former root model now lives in `labs/<slug>/models/core/` and is wrapped by
> `labs/<slug>/lab.yaml`. This repo has no repo-level import catalog and no composed labs at the root.

Curated collection of **cell signaling** and **signal transduction** simulation models for the **biosim** platform. This repository contains cleaned computational labs for signaling pathways, receptor dynamics, second messengers, and signal transduction cascades.

## What's Inside

### Labs

**Cell Signaling** — signal transduction pathways, receptor activation, and signaling networks:

**Key Areas:** MAPK/ERK pathways, PI3K/AKT signaling, calcium signaling, cAMP/PKA pathways, JAK/STAT, Wnt, Notch, TGF-β, receptor tyrosine kinases (RTKs), G-protein coupled receptors (GPCRs), and crosstalk between signaling networks.

All models use SBML format with tellurium runtime.

## Prerequisites
```bash
pip install "biosim @ git+https://github.com/BioSimulant/biosim.git@main"
```

## License
Dual-licensed: Apache-2.0 (code), CC BY 4.0 (content)
