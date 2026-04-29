import openai

def readability_agent(text, model="gpt-4"):
    prompt = f"请优化以下文本的语言表达，使其更专业、简洁、可读性更高：\n{text}"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role":"user", "content": prompt}],
        temperature=0
    )
    return response['choices'][0]['message']['content']
