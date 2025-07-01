# TradingAgents/graph/reflection.py

from typing import Dict, Any
from langchain_openai import ChatOpenAI


class Reflector:
    """处理决策反思与记忆更新。"""

    def __init__(self, quick_thinking_llm: ChatOpenAI):
        """用 LLM 初始化反思器。"""
        self.quick_thinking_llm = quick_thinking_llm
        self.reflection_system_prompt = self._get_reflection_prompt()

    def _get_reflection_prompt(self) -> str:
        """获取反思用的系统提示词。"""
        return """
你是一名专家级金融分析师，负责回顾交易决策/分析并给出全面、分步骤的分析。
你的目标是对投资决策提供详细见解，突出改进机会，严格遵循以下准则：

1. 推理：
   - 对每个交易决策，判断其正确与否。正确的决策带来收益增长，错误的则相反。
   - 分析每次成功或失误的影响因素，包括：
     - 市场情报。
     - 技术指标。
     - 技术信号。
     - 价格走势分析。
     - 整体市场数据分析。
     - 新闻分析。
     - 社交媒体与情绪分析。
     - 基本面数据分析。
     - 权衡各因素在决策中的重要性。

2. 改进：
   - 对错误决策，提出修正建议以最大化收益。
   - 给出详细的改进措施清单，包括具体建议（如将某日决策从 HOLD 改为 BUY）。

3. 总结：
   - 总结成功与失误的经验教训。
   - 强调这些经验如何应用于未来交易场景，并联系类似情形以迁移知识。

4. 摘要：
   - 从总结中提炼关键信息，形成不超过 1000 tokens 的简明句子。
   - 确保该句子高度凝练经验与推理，便于快速参考。

严格遵循上述要求，确保输出详细、准确、可操作。你还会获得市场价格、技术指标、新闻、情绪等客观描述以辅助分析。
"""

    def _extract_current_situation(self, current_state: Dict[str, Any]) -> str:
        """从状态中提取当前市场情形。"""
        curr_market_report = current_state["market_report"]
        curr_sentiment_report = current_state["sentiment_report"]
        curr_news_report = current_state["news_report"]
        curr_fundamentals_report = current_state["fundamentals_report"]

        return f"{curr_market_report}\n\n{curr_sentiment_report}\n\n{curr_news_report}\n\n{curr_fundamentals_report}"

    def _reflect_on_component(
        self, component_type: str, report: str, situation: str, returns_losses
    ) -> str:
        """为某一组件生成反思。"""
        messages = [
            ("system", self.reflection_system_prompt),
            (
                "human",
                f"Returns: {returns_losses}\n\nAnalysis/Decision: {report}\n\nObjective Market Reports for Reference: {situation}",
            ),
        ]

        result = self.quick_thinking_llm.invoke(messages).content
        return result

    def reflect_bull_researcher(self, current_state, returns_losses, bull_memory):
        """反思多头研究员分析并更新记忆。"""
        situation = self._extract_current_situation(current_state)
        bull_debate_history = current_state["investment_debate_state"]["bull_history"]

        result = self._reflect_on_component(
            "BULL", bull_debate_history, situation, returns_losses
        )
        bull_memory.add_situations([(situation, result)])

    def reflect_bear_researcher(self, current_state, returns_losses, bear_memory):
        """反思空头研究员分析并更新记忆。"""
        situation = self._extract_current_situation(current_state)
        bear_debate_history = current_state["investment_debate_state"]["bear_history"]

        result = self._reflect_on_component(
            "BEAR", bear_debate_history, situation, returns_losses
        )
        bear_memory.add_situations([(situation, result)])

    def reflect_trader(self, current_state, returns_losses, trader_memory):
        """反思交易员决策并更新记忆。"""
        situation = self._extract_current_situation(current_state)
        trader_decision = current_state["trader_investment_plan"]

        result = self._reflect_on_component(
            "TRADER", trader_decision, situation, returns_losses
        )
        trader_memory.add_situations([(situation, result)])

    def reflect_invest_judge(self, current_state, returns_losses, invest_judge_memory):
        """反思投资评审决策并更新记忆。"""
        situation = self._extract_current_situation(current_state)
        judge_decision = current_state["investment_debate_state"]["judge_decision"]

        result = self._reflect_on_component(
            "INVEST JUDGE", judge_decision, situation, returns_losses
        )
        invest_judge_memory.add_situations([(situation, result)])

    def reflect_risk_manager(self, current_state, returns_losses, risk_manager_memory):
        """反思风险管理决策并更新记忆。"""
        situation = self._extract_current_situation(current_state)
        judge_decision = current_state["risk_debate_state"]["judge_decision"]

        result = self._reflect_on_component(
            "RISK JUDGE", judge_decision, situation, returns_losses
        )
        risk_manager_memory.add_situations([(situation, result)])
