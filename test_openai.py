import os
import sys
from langchain_openai import ChatOpenAI

# 设置代理环境变量\os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ['https_proxy'] = 'http://127.0.0.1:7890'

# 打印当前环境变量，检查代理设置
print("HTTP_PROXY:", os.environ.get('http_proxy'))
print("HTTPS_PROXY:", os.environ.get('https_proxy'))

# 尝试连接OpenAI API
try:
    # 确保OPENAI_API_KEY已设置
    if not os.environ.get('OPENAI_API_KEY'):
        print("请先设置OPENAI_API_KEY环境变量")
        sys.exit(1)
    
    # 创建ChatOpenAI实例
    llm = ChatOpenAI(model="gpt-4o")
    
    # 简单的测试消息
    from langchain_core.messages import HumanMessage
    messages = [HumanMessage(content="Hello, world!")]
    
    # 调用模型
    print("尝试连接OpenAI API...")
    response = llm.invoke(messages)
    print("成功连接！响应内容:", response.content)
    
except Exception as e:
    print(f"连接失败: {e}")