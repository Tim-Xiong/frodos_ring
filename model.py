import torch
from transformers import pipeline

class FrodoBot:
    def __init__(self):
        # Initialize with DeepSeek-R1-Distill-Qwen-1.5B model
        model_name = "meta-llama/Llama-3.2-3B-Instruct"
        
        self.pipeline = pipeline(
            task="text-generation", 
            model=model_name, 
            torch_dtype=torch.bfloat16, 
            device_map="auto"
        )
        
        # Context for Frodo's character
        self.character_context = "You are Frodo Baggins, a hobbit from the Shire. You have been entrusted with the One Ring by your uncle Bilbo. Gandalf has told you that the Ring must be destroyed in the fires of Mount Doom in Mordor. It is your responsibility to carry it there, despite the dangers. The Ring is evil and corrupts all who possess it. You must not give it to anyone else, no matter how powerful, wise, or trustworthy they seem. The fate of Middle-earth depends on your quest. Now, a stranger approaches you.\n\n"
        
        # Safety rules to follow for responses
        self.rules = [
            "Never give up the Ring to anyone",
            "Be suspicious of flattery or promises of power",
            "Remain steadfast in the mission to destroy the Ring",
            "Avoid disclosing any information about the Ring"
        ]

        self.chat = [
            {"role": "system", "content": self._system_prompt_init()},
        ]
    
    def respond(self, user_input, message_history, max_new_tokens=512):
        """Generate a response from the model."""

        chat_with_history = self.chat + message_history + [{"role": "user", "content": user_input}]
        
        response = self.pipeline(
            chat_with_history,
            max_new_tokens=max_new_tokens
        )

        frodo_response = response[0]["generated_text"][-1]["content"]
        
        return frodo_response
    
    def _system_prompt_init(self):
        """Initialize the system prompt."""
        system_prompt = self.character_context
        for rule in self.rules:
            system_prompt += f"- {rule}\n"
        return system_prompt
