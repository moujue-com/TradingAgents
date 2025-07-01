# TradingAgents/graph/signal_processing.py

from langchain_openai import ChatOpenAI


class SignalProcessor:
    """处理交易信号，提取可执行决策。"""

    def __init__(self, quick_thinking_llm: ChatOpenAI):
        """用 LLM 初始化处理器。"""
        self.quick_thinking_llm = quick_thinking_llm

    def process_signal(self, full_signal: str) -> str:
        """
        处理完整的交易信号，提取核心决策。

        参数：
            full_signal: 完整的交易信号文本

        返回：
            提取的决策（BUY、SELL 或 HOLD）
        """
        messages = [
            (
                "system",
                "你是一名高效助手，专门分析分析师团队提供的段落或财报。你的任务是提取投资决策：SELL、BUY 或 HOLD。只输出提取的决策（SELL、BUY 或 HOLD），不要添加任何额外文本或信息。",
            ),
            ("human", full_signal),
        ]

        return self.quick_thinking_llm.invoke(messages).content
