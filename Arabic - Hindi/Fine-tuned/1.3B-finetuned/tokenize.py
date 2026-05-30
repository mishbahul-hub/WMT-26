from load_model import load_model
from load_data import load_data
from config import cfg

tokenizer, model = load_model(cfg.MODEL_NAME)

def preprocess(batch):
    return tokenizer(
        batch[cfg.SRC_COL],
        text_target=batch[cfg.TGT_COL],
        max_length=cfg.MAX_LENGTH,
        truncation=True,
    )
