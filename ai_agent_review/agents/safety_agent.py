import openai

def content_safety_agent(text, model="gpt-4"):
    prompt = f"请检查以下文本是否包含敏感、不当或违规内容，并列出改进建议：\n{text}"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role":"user", "content": prompt}],
        temperature=0
    )
    return response['choices'][0]['message']['content']
