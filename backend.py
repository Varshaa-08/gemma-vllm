from fastapi import FastAPI
from pydantic import BaseModel
from vllm import LLM, SamplingParams
import os

# Force vLLM to run on CPU
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["VLLM_USE_CPU"] = "1"

# Initialize FastAPI app
app = FastAPI()

# Load Gemma-3B explicitly in CPU mode
llm = LLM(model="google/gemma-3b-it", tensor_parallel_size=1, enforce_eager=True)

# Define request format
class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

@app.get("/")
def home():
    return {"message": "Gemma-3B-IT vLLM API is running!"}

@app.post("/generate/")
def generate_text(request: PromptRequest):
    sampling_params = SamplingParams(max_tokens=request.max_tokens)
    output = llm.generate(request.prompt, sampling_params)
    
    return {"response": output[0].outputs[0].text}
