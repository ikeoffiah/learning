from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import LLMMathChain
from langchain.tools import Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools.retriever import create_retriever_tool
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
import os
from langchain.agents import create_openai_tools_agent


# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-functions-agent")
# print(prompt.messages)



os.environ["OPENAI_API_KEY"] = ""

# search = TavilySearchResults()
# print(search.invoke("who is Ghana President?"))

# loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
# doc = loader.load()

# documents = RecursiveCharacterTextSplitter(
#     chunk_size=1000, chunk_overlap=200
# ).split_documents(doc)

# vector = FAISS.from_documents(documents, OpenAIEmbeddings())
# retriever = vector.as_retriever()

# print(retriever.invoke("how to upload a dataset")[0])

# retriever_tool = create_retriever_tool(
#     retriever,
#     "langchain_search_tool",
#     "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
# )

def say_my_age(*args):
    return "26 years"


def say_time(*args):
    return "11 am"

age_tool = Tool.from_function(
func=say_my_age,
name = "Age",
description= "This should be used to get age, any question on age should be gotten using this"
)

time_tool = Tool.from_function(
func=say_time,
name = "time",
description= "This should be used to get time, any question on time should be gotten using this"
)

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

tools = [age_tool, time_tool]

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
print(agent_executor.invoke({"input": "What is China's President's age ?"}))

# print(say_my_age())

# llm = OpenAI(
#     openai_api_key = "98613bce-75a6-49c3-9c7a-fdaa18db54d1",
#     temperature = 0,
#     model_name = "gpt-3.5-turbo-0125"
# )
#
# llm_math = LLMMathChain(llm=llm)
#
# math_tool = Tool(
#     name= 'Calculator',
#     func = llm_math.run,
#     description= 'Userful for when you need to answer questions about math.'
# )
#
# tools = [math_tool]
#
# agent = create_tool_calling_agent(llm, tools, prompt)
#
# zero_shot_agent = initialize_agent(
#     agent= "zero-shot-react-description",
#     tools = tools,
#     llm=llm,
#     verbose = True,
#     max_iterations = 2
# )
