#1 import the OS, Bedrock, ConversationChain, ConversationBufferMemory Langchain Modules

import os
# from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory

from langchain_aws import BedrockLLM
from langchain.chains import ConversationChain

#2a Write a function for invoking model- client connection with Bedrock with profile, model_id & Inference paramsmodel_kwargs
def demo_chatbot():
    demo_llm = BedrockLLM(
        credentials_profile_name='Ishfaq',
        model_id= 'meta.llama2-70b-chat-v1',
        model_kwargs= {
            "temperature": 0.5,
            "top_p": 0.9,
            "max_gen_len": 512},
            region_name= 'us-east-1')
    #2b Test out the LLM with Predict method
    return demo_llm

# response = demo_chatbot('hi, what is your name')
# print(response)
#3 Create a Function for ConversationBufferMemory (llm and max token limit)

def demo_memory():
    llm_data = demo_chatbot()
    memory=ConversationBufferMemory(llm=llm_data,max_token_limit=300)
    return memory
#4 Create a Function for Conversation Chain - Input text + Memory
def demo_conv(input_text, memory):
    llm_chain_data = demo_chatbot()
    llm_convo= ConversationChain(llm= llm_chain_data, memory=memory, verbose= True)
    
#5 Chat response using Predict (Prompt template)
    chat_reply = llm_convo.invoke(input_text)
    return chat_reply['response']

#Links :
#1 https://python.langchain.com/docs/integrations/llms/bedrock
#2b Chains - Combine LLMs and Prompts 
