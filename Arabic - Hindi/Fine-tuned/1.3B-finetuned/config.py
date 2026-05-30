from dataclasses import dataclass, fields

@dataclass
class Config:

    # data paths
    DATA_PATH: str = ""
    OUTPUT_DIR: str = ""
    ADAPTER_DIR: str = ""

    # columns in dataset
    SRC_COL: str = "ar"
    TGT_COL: str = "hi"

    # --- model + NLLB language codes ---
    MODEL_NAME: str = "facebook/nllb-200-distilled-1.3B"
    SRC_LANG:   str = "arb_Arab"
    TGT_LANG:   str = "hin_Deva"

    # --- split sizes ---
    N_TRAIN: int = 20100
    N_EVAL:  int = 0

    # --- training ---
    SEED:         int   = 42
    MAX_LENGTH:   int   = 128
    BATCH_SIZE:   int   = 8
    GRAD_ACCUM:   int   = 1
    LR:           float = 2e-4   # LoRA tolerates higher LR than full FT
    EPOCHS:       int   = 3
    WARMUP_RATIO: float = 0.1
    WEIGHT_DECAY: float = 0.01

    # --- LoRA ---
    LORA_R:       int   = 16
    LORA_ALPHA:   int   = 32
    LORA_DROPOUT: float = 0.05
    LORA_TARGETS: tuple = ("q_proj", "k_proj", "v_proj", "out_proj")

    # --- inference ---
    NUM_BEAMS: int = 5


cfg = Config()
print({field.name: getattr(cfg, field.name) for field in fields(cfg)})