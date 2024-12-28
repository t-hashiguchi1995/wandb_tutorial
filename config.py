from dotenv import load_dotenv
load_dotenv()


import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
WANDB_API_KEY = os.getenv("WANDB_API_KEY")

