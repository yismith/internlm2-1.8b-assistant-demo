import gradio as gr
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel

# download internlm2-1.8b-assistant-demo to the base_path directory using git tool
base_path = './internlm2-1.8b-assistant-demo'
model_base_path = './internlm2-assistant-demo'
os.system(f'git clone https://code.openxlab.org.cn/yismith/internlm2-1.8b-assistant-demo.git {base_path}')
os.system(f'cd {base_path} && git lfs pull && cd ..')
os.system(f'mv {base_path} {model_base_path}')

tokenizer = AutoTokenizer.from_pretrained(model_base_path,trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_base_path,trust_remote_code=True, torch_dtype=torch.float16).cuda()

def chat(message,history):
    for response,history in model.stream_chat(tokenizer,message,history,max_length=2048,top_p=0.7,temperature=1):
        yield response

gr.ChatInterface(chat,
                 title="internlm2-1.8b-assistant-demo",
                 description="""
internlm2-1.8b微调后的个人小助理demo
                 """,
                 ).queue(1).launch()
