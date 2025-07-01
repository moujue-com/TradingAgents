from typing import Annotated, Sequence
from datetime import date, timedelta, datetime
from typing_extensions import TypedDict, Optional
from langchain_openai import ChatOpenAI
from tradingagents.agents import *
from langgraph.prebuilt import ToolNode
from langgraph.graph import END, StateGraph, START, MessagesState


# Researcher team state
# 研究员团队状态
class InvestDebateState(TypedDict):
    bull_history: Annotated[
        str, "多头对话历史"
    ]  # 多头对话历史
    bear_history: Annotated[
        str, "空头对话历史"
    ]  # 空头对话历史
    history: Annotated[str, "对话历史"]  # 对话历史
    current_response: Annotated[str, "最新回复"]  # 最新回复
    judge_decision: Annotated[str, "最终评审决策"]  # 最终评审决策
    count: Annotated[int, "当前对话长度"]  # 当前对话长度


# Risk management team state
# 风险管理团队状态
class RiskDebateState(TypedDict):
    risky_history: Annotated[
        str, "激进分析师对话历史"
    ]  # 对话历史
    safe_history: Annotated[
        str, "保守分析师对话历史"
    ]  # 对话历史
    neutral_history: Annotated[
        str, "中性分析师对话历史"
    ]  # 对话历史
    history: Annotated[str, "对话历史"]  # 对话历史
    latest_speaker: Annotated[str, "上次发言分析师"]
    current_risky_response: Annotated[
        str, "激进分析师最新回复"
    ]  # 最新回复
    current_safe_response: Annotated[
        str, "保守分析师最新回复"
    ]  # 最新回复
    current_neutral_response: Annotated[
        str, "中性分析师最新回复"
    ]  # 最新回复
    judge_decision: Annotated[str, "评审决策"]
    count: Annotated[int, "当前对话长度"]  # 当前对话长度


class AgentState(MessagesState):
    company_of_interest: Annotated[str, "关注交易的公司"]
    trade_date: Annotated[str, "交易日期"]

    sender: Annotated[str, "发送消息的智能体"]

    # research step
    # 研究阶段
    market_report: Annotated[str, "市场分析师报告"]
    sentiment_report: Annotated[str, "社交媒体分析师报告"]
    news_report: Annotated[
        str, "新闻研究员报告"
    ]
    fundamentals_report: Annotated[str, "基本面研究员报告"]

    # researcher team discussion step
    # 研究员团队讨论阶段
    investment_debate_state: Annotated[
        InvestDebateState, "当前投资辩论状态"
    ]
    investment_plan: Annotated[str, "分析师生成的方案"]

    trader_investment_plan: Annotated[str, "交易员生成的方案"]

    # risk management team discussion step
    # 风险管理团队讨论阶段
    risk_debate_state: Annotated[
        RiskDebateState, "当前风险评估辩论状态"
    ]
    final_trade_decision: Annotated[str, "风险分析师最终决策"]
