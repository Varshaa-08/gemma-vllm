import os
import uvicorn
from fastapi import FastAPI
from vllm import LLM

# Force vLLM to run on CPU
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["VLLM_USE_CPU"] = "1"

app = FastAPI()

# Load Gemma-3B explicitly in CPU mode
llm = LLM(model="google/gemma-3b-it", tensor_parallel_size=1, enforce_eager=True)

@app.get("/")
def read_root():
    return {"message": "FastAPI with vLLM is running!"}

# Ensure server runs on Render's assigned port
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
