import openai
from agents.safety_agent import content_safety_agent
from agents.logic_agent import logic_analysis_agent
from agents.readability_agent import readability_agent

openai.api_key = "YOUR_API_KEY"

def review_and_optimize(text):
    print("==== 内容安全审查 ====")
    safety_result = content_safety_agent(text)
    print(safety_result)

    print("\n==== 逻辑分析 ====")
    logic_result = logic_analysis_agent(text)
    print(logic_result)

    print("\n==== 可读性优化 ====")
    optimized_text = readability_agent(text)
    print(optimized_text)

    return optimized_text

if __name__ == "__main__":
    sample_text = """
    本项目旨在通过自动化方法提升企业内部文档质量。
    内容可能存在重复描述、逻辑不够清晰以及表达冗长的问题。
    """
    final_text = review_and_optimize(sample_text)
    print("\n==== 最终优化文本 ====")
    print(final_text)
