<!-- ====================== HEADER ====================== -->
<div align="center">

<h1>
  <samp>· WMT &mdash; 26 ·</samp>
</h1>

<h3><em>Low-Resource Neural Machine Translation</em></h3>

<p>
  <a href="#-getting-started"><b>Getting Started</b></a> &nbsp;|&nbsp;
  <a href="#-repository-structure"><b>Structure</b></a> &nbsp;|&nbsp;
  <a href="#-models"><b>Models</b></a> &nbsp;|&nbsp;
  <a href="#-usage"><b>Usage</b></a> &nbsp;|&nbsp;
  <a href="#-results"><b>Results</b></a> &nbsp;|&nbsp;
  <a href="#-license"><b>License</b></a>
</p>

<p>
  <a href="https://github.com/mishbahul-hub/WMT-26/stargazers">
    <img src="https://img.shields.io/github/stars/mishbahul-hub/WMT-26?style=for-the-badge&color=ffd166" alt="Stars"/></a>
  <a href="https://github.com/mishbahul-hub/WMT-26/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/mishbahul-hub/WMT-26?style=for-the-badge&color=06d6a0" alt="License: MIT"/></a>
  <a href="https://github.com/mishbahul-hub/WMT-26/commits/main">
    <img src="https://img.shields.io/github/last-commit/mishbahul-hub/WMT-26?style=for-the-badge&color=118ab2" alt="Last commit"/></a>
</p>

<p>
  <img src="https://img.shields.io/badge/python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Transformers-FFD21E?style=flat-square" alt="HuggingFace Transformers"/>
  <img src="https://img.shields.io/badge/PEFT%20%C2%B7%20LoRA-7C3AED?style=flat-square" alt="PEFT / LoRA"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/>
</p>

<p>
  <img src="https://img.shields.io/badge/WMT-2026%20Shared%20Task-1e2327?style=flat-square" alt="WMT 2026"/>
  <img src="https://img.shields.io/badge/Arabic%20%E2%86%94%20English-success?style=flat-square" alt="Arabic-English"/>
  <img src="https://img.shields.io/badge/Arabic%20%E2%86%94%20Hindi-success?style=flat-square" alt="Arabic-Hindi"/>
  <img src="https://img.shields.io/badge/metrics-BLEU%20%C2%B7%20chrF++%20%C2%B7%20COMET-blueviolet?style=flat-square" alt="Metrics"/>
</p>

</div>

<hr/>

# WMT-26

**WMT-26** is a research codebase for **machine translation on low-resource language pairs**, built for the [WMT 2026](https://www2.statmt.org/wmt26/) (Conference on Machine Translation) shared-task setting. It benchmarks and fine-tunes modern open multilingual models across two directions in each pair:

1. **Arabic &harr; English**
2. **Arabic &harr; Hindi**

The repository is organized as a set of reproducible Jupyter notebooks (one per model/direction) plus a small, modular Python package for **parameter-efficient fine-tuning (LoRA)**. Every experiment is scored with the three metrics standard in MT evaluation today — **BLEU**, **chrF++**, and **COMET** — so zero-shot baselines and fine-tuned checkpoints can be compared on equal footing.

> **Why this matters.** Arabic&ndash;Hindi in particular is a genuinely low-resource direction with little high-quality parallel data. This repo treats it as a first-class problem: it establishes strong zero-shot baselines from large pretrained models, then measures how much LoRA fine-tuning on a modest parallel corpus closes the gap.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Models](#-models)
- [Evaluation Metrics](#-evaluation-metrics)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Results](#-results)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## 🔭 Overview

The project is split by **language pair**, and within each pair by **approach**:

| Language pair | Approach | Backbone family | Notebooks / code |
| :--- | :--- | :--- | :--- |
| Arabic &harr; English | Pretrained inference | Helsinki-NLP **OPUS-MT** | `Arabic - English/` |
| Arabic &harr; Hindi | **Zero-shot** | Meta **NLLB-200**, Google **MADLAD-400** | `Arabic - Hindi/Zero-shot/` |
| Arabic &harr; Hindi | **Fine-tuned** | **NLLB-200** (600M, 1.3B + LoRA) | `Arabic - Hindi/Fine-tuned/` |
| Arabic &rarr; Hindi | Challenge-set evaluation | NLLB-200-distilled-600M | `challenge test/` |
| Indic directions | Toolkit integration *(WIP)* | **IndicTrans** | `indic-trans/` |

Each notebook follows the same modular pipeline so results are directly comparable:

```text
Install & Imports → Config → Data Loading → Model Loading
       → Translation Function → Evaluation (BLEU / chrF++ / COMET) → Main
```

---

## 📁 Repository Structure

```text
WMT-26/
├── Arabic - English/                      # OPUS-MT pretrained baselines
│   ├── ar-en-wmt-helsinki-428m.ipynb      # Helsinki-NLP/opus-mt-tc-big-ar-en
│   └── en-ar-wmt-helsinki-241m.ipynb      # Helsinki-NLP/opus-mt-tc-big-en-ar
│
├── Arabic - Hindi/
│   ├── Zero-shot/                         # No fine-tuning — pretrained models as-is
│   │   ├── nllb-600m-zeroshot.ipynb       # facebook/nllb-200-distilled-600M
│   │   ├── nllb-1-3b-zeroshot.ipynb       # facebook/nllb-200-distilled-1.3B
│   │   ├── nllb-3-3b-zeroshot.ipynb       # facebook/nllb-200-3.3B
│   │   └── madlad-3b-zeroshot.ipynb       # google/madlad400-3b-mt
│   │
│   └── Fine-tuned/
│       ├── ar-hi-finetne-nllb-600M.ipynb  # AR→HI fine-tuning (NLLB-600M)
│       ├── hi-ar-finetne-nllb-600M.ipynb  # HI→AR fine-tuning (NLLB-600M)
│       ├── 170k-ar-hi-finetne-nllb.ipynb  # Fine-tuning on the 170k corpus
│       └── 1.3B-finetuned/                # Modular LoRA pipeline (NLLB-1.3B)
│           ├── config.py                  # Dataclass: paths, lang codes, hyperparams, LoRA
│           ├── load_data.py               # CSV → 🤗 datasets.Dataset
│           ├── load_model.py              # Tokenizer + model from the Hub
│           ├── tokenize.py                # Source/target preprocessing
│           ├── lora.py                    # PEFT LoraConfig + get_peft_model
│           └── requirements.txt
│
├── challenge test/                        # Hard-case evaluation
│   ├── ar-hi-challenge-set.ipynb
│   └── 170k/ar_hi_170k.csv                # AR source + HI reference (≈1.5k rows)
│
├── indic-trans/                           # IndicTransToolkit integration (scaffolding)
│   ├── main.py
│   ├── new.py
│   └── requirements.txt
│
├── LICENSE                                # MIT
└── README.md
```

---

## 🤖 Models

| Model | Params | Pair / Direction | Mode | Source |
| :--- | :--- | :--- | :--- | :--- |
| `opus-mt-tc-big-ar-en` | ~428M | AR → EN | Pretrained | Helsinki-NLP |
| `opus-mt-tc-big-en-ar` | ~241M | EN → AR | Pretrained | Helsinki-NLP |
| `nllb-200-distilled-600M` | 600M | AR &harr; HI | Zero-shot **+ fine-tuned** | Meta AI |
| `nllb-200-distilled-1.3B` | 1.3B | AR &harr; HI | Zero-shot **+ LoRA fine-tuned** | Meta AI |
| `nllb-200-3.3B` | 3.3B | AR &harr; HI | Zero-shot | Meta AI |
| `madlad400-3b-mt` | 3B | AR &harr; HI | Zero-shot | Google |
| `IndicTrans` | — | Indic directions | *Planned* | AI4Bharat |

> **NLLB language codes used:** Arabic = `arb_Arab`, Hindi = `hin_Deva`.

---

## 📊 Evaluation Metrics

All experiments report the same three metrics so scores are comparable across models and approaches:

- **BLEU** — n-gram precision against the reference (`sacrebleu`).
- **chrF++** — character-level F-score; more reliable than BLEU for morphologically rich languages like Arabic (`sacrebleu`).
- **COMET** — learned, embedding-based quality estimate that correlates better with human judgement (`unbabel-comet`).

For low-resource and morphologically rich pairs, **chrF++ and COMET are the headline numbers** — BLEU alone tends to under-credit valid lexical/morphological variation.

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10+**
- A CUDA-capable GPU is strongly recommended (the 1.3B/3.3B models and COMET both need substantial memory).
- The notebooks are written to run on **Kaggle/Colab** — enable the **GPU accelerator** and **internet** so NLLB, MADLAD, and COMET can download from the Hugging Face Hub.

### Installation

```bash
# Clone the repository
git clone https://github.com/mishbahul-hub/WMT-26.git
cd WMT-26

# (Recommended) create an isolated environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies for the LoRA fine-tuning pipeline
pip install -r "Arabic - Hindi/Fine-tuned/1.3B-finetuned/requirements.txt"
```

Core dependencies: `torch`, `transformers`, `datasets`, `accelerate`, `peft`, `sentencepiece`, `sacrebleu`, `unbabel-comet`, `pandas`, `numpy`.

---

## 🛠 Usage

### 1. Run a zero-shot baseline

Open any notebook under `Arabic - Hindi/Zero-shot/` (e.g. `nllb-600m-zeroshot.ipynb`), select a GPU runtime, and **Run All**. Each notebook loads the model, translates the evaluation set, and prints BLEU / chrF++ / COMET.

### 2. Fine-tune with the modular LoRA pipeline

The `1.3B-finetuned/` package keeps configuration and logic separate so experiments are easy to reproduce. Point the config at your data and run:

```python
from config import cfg                 # central hyperparameters + LoRA settings
from load_data import load_data
from load_model import load_model
from peft import get_peft_model, LoraConfig, TaskType

# 1) Configure (edit config.py or override at runtime)
cfg.DATA_PATH  = "path/to/ar_hi_train.csv"   # columns: 'ar', 'hi'
cfg.OUTPUT_DIR = "checkpoints/nllb-1.3b-lora"

# 2) Load parallel data → 🤗 Dataset
df, train_ds = load_data(cfg.DATA_PATH)

# 3) Load backbone + tokenizer
tokenizer, model = load_model(cfg.MODEL_NAME)   # facebook/nllb-200-distilled-1.3B

# 4) Wrap with LoRA adapters (only a small % of params are trained)
lora_config = LoraConfig(
    r=cfg.LORA_R, lora_alpha=cfg.LORA_ALPHA, lora_dropout=cfg.LORA_DROPOUT,
    target_modules=list(cfg.LORA_TARGETS), task_type=TaskType.SEQ_2_SEQ_LM,
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
```

**Default training configuration** (`config.py`): `MAX_LENGTH=128`, `BATCH_SIZE=8`, `LR=2e-4`, `EPOCHS=3`, `NUM_BEAMS=5`, LoRA `r=16 / α=32 / dropout=0.05` on the attention projections (`q/k/v/out_proj`).

### 3. Evaluate on the challenge set

`challenge test/ar-hi-challenge-set.ipynb` runs the model against `170k/ar_hi_170k.csv` (Arabic source + Hindi reference, ~1.5k hard examples) to stress-test robustness beyond the standard test split.

---

## 📈 Results


### Arabic &harr; Hindi

| Model | Mode | Direction | BLEU | chrF++ | COMET |
| :--- | :--- | :---: | :---: | :---: | :---: |
| NLLB-200-distilled-600M | Zero-shot | AR→HI | 21.03 | 45.63 | 0.6954 |
| NLLB-200-distilled-1.3B | Zero-shot | AR→HI | 23.09 | 47.09 | 0,7126 |
| NLLB-200-3.3B | Zero-shot | AR→HI | 24.37 | 48.03 | 0.7149 |
| NLLB-200-distilled-600M | Fine-tuned | AR→HI | 28.22 | 50.69 | 0.7191 |

### Hindi &harr; Arabic

| Model | Mode | Direction | BLEU | chrF++ | COMET |
| :--- | :--- | :---: | :---: | :---: | :---: |
| NLLB-200-distilled-600M | Zero-shot | HI→AR | 10.79 | 41.85 | 0.8266 |
| NLLB-200-distilled-1.3B | Zero-shot | HI→AR | 12.63 | 44.67 | 0.8487 |
| NLLB-200-3.3B | Zero-shot | HI→AR | 13.49 | 45.07 | 0.8529 |
| NLLB-200-distilled-600M | Fine-tuned | HI→AR | 13.33 | 43.15 | 0.8351 |

### Arabic &harr; English

| Model | Mode | Direction | BLEU | chrF++ | COMET |
| :--- | :--- | :---: | :---: | :---: | :---: |
| OPUS-MT-tc-big-ar-en | Pretrained | AR→EN | 32.23 | 54.77 | — |
| OPUS-MT-tc-big-en-ar | Pretrained | EN→AR | 24.25 | 49.35 | — |

---


## 🤝 Contributing

Contributions are welcome. To keep results reproducible:

1. **Fork** the repo and create a branch: `git checkout -b feat/your-experiment`.
2. Keep each experiment in its **own notebook** following the existing pipeline sections (Config → Data → Model → Translate → Evaluate).
3. Report **BLEU, chrF++, and COMET** for any new model or checkpoint.
4. For Python code, prefer the modular style in `1.3B-finetuned/` (config in `config.py`, no hard-coded paths).
5. Open a **pull request** describing the setup, data, and scores.

Found a bug or have a question? Please [open an issue](https://github.com/mishbahul-hub/WMT-26/issues).

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
© 2026 Mishbahul.

---

## 🙏 Acknowledgements

- [**WMT — Conference on Machine Translation**](https://www2.statmt.org/wmt26/) for the shared-task framing.
- [**Meta AI — NLLB-200**](https://huggingface.co/facebook/nllb-200-distilled-600M) (*No Language Left Behind*).
- [**Google — MADLAD-400**](https://huggingface.co/google/madlad400-3b-mt).
- [**Helsinki-NLP — OPUS-MT**](https://huggingface.co/Helsinki-NLP) and the OPUS project.
- [**AI4Bharat — IndicTrans**](https://github.com/AI4Bharat/IndicTrans2).
- [**Unbabel — COMET**](https://github.com/Unbabel/COMET) and [**sacreBLEU**](https://github.com/mjpost/sacrebleu) for evaluation.

<div align="center">
<sub>Built for low-resource MT research · Arabic &harr; English · Arabic &harr; Hindi</sub>
</div>
