from transformers import AutoTokenizer, AutoModelForCausalLM 

def load_model(model_name):
    print(f"--- loading model: {model_name} ---")
    # loads tokenizer and model from huggingface hub (or local cache)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    print(f"Loaded {model_name}  ({sum(p.numel() for p in model.parameters())/1e6:.1f}M params)")
    return tokenizer, model