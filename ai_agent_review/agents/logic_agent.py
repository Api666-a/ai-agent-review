import openai

def logic_analysis_agent(text, model="gpt-4"):
    prompt = f"请分析以下文本的逻辑结构是否清晰，有无重复或不连贯的地方，并提出优化建议：\n{text}"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role":"user", "content": prompt}],
        temperature=0
    )
    return response['choices'][0]['message']['content']
