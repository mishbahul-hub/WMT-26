# LORA - lower order rank adaptation
# -> Efficient technique for fine-tuning LLMs
# -> Instead of updating all model parameters, it only tracks the changes
# -> Only updates a small number of parameters (the "low-rank" part)
# -> it undergoes matrix-decomposition

# Quantization - ( fp32-bit => 8-bit int )
# 1-bit LLM - ( fp32-bit => 1-bit int )
# -> Reduces memory and computational requirements
from peft import LoraConfig, get_peft_model, TaskType
from load_model import load_model
lora_config = LoraConfig(
    r=16,                # rank
    lora_alpha=32,      # scaling factor
    init_lora_weights="gaussian",  # initialization method
    target_modules=["q_proj", "k_proj", "v_proj", "out_proj"],  # target modules for LoRA
    task_type=TaskType.CAUSAL_LM,  # task type (causal language modeling)
)


# dont try this : 
tokenizer, model = load_model("gpt2")
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()