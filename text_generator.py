# text_generator.py

import warnings
import os
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer


class TextGenerator:
    def __init__(self, model_name="gpt2"):
        # Suppress warnings and TensorFlow logs
        warnings.filterwarnings("ignore", category=FutureWarning)
        warnings.filterwarnings("ignore", category=UserWarning)
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

        # Load model and tokenizer
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = TFGPT2LMHeadModel.from_pretrained(model_name)

    def generate_text(self, input_text, max_length=100, temperature=0.2, top_k=30, top_p=0.9):
        # Encode input text
        input_ids = self.tokenizer.encode(input_text, return_tensors='tf')

        # Generate text
        output = self.model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            pad_token_id=self.tokenizer.eos_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
            no_repeat_ngram_size=2,  # Avoid repeating n-grams of length 2
            early_stopping=True  # Stop generation when the end of sequence token is generated
        )

        # Decode and return result
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)

        # Remove the prompt from the beginning of the generated text
        return generated_text[len(input_text):].strip()
