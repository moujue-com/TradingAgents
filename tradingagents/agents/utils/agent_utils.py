from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage, AIMessage
from typing import List
from typing import Annotated
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import RemoveMessage
from langchain_core.tools import tool
from datetime import date, timedelta, datetime
import functools
import pandas as pd
import os
from dateutil.relativedelta import relativedelta
from langchain_openai import ChatOpenAI
import tradingagents.dataflows.interface as interface
from tradingagents.default_config import DEFAULT_CONFIG
from langchain_core.messages import HumanMessage


def create_msg_delete():
    def delete_messages(state):
        """清空消息并添加占位符，兼容 Anthropic。"""
        messages = state["messages"]
        
        # 移除所有消息
        removal_operations = [RemoveMessage(id=m.id) for m in messages]
        
        # 添加最小占位消息
        placeholder = HumanMessage(content="Continue")
        
        return {"messages": removal_operations + [placeholder]}
    
    return delete_messages


class Toolkit:
    _config = DEFAULT_CONFIG.copy()

    @classmethod
    def update_config(cls, config):
        """更新类级别配置。"""
        cls._config.update(config)

    @property
    def config(self):
        """访问配置。"""
        return self._config

    def __init__(self, config=None):
        if config:
            self.update_config(config)

    @staticmethod
    @tool
    def get_reddit_news(
        curr_date: Annotated[str, "Date you want to get news for in yyyy-mm-dd format"],
    ) -> str:
        """
        在指定时间范围内获取 Reddit 全球新闻。
        参数：
            curr_date (str): 你想获取新闻的日期，格式为 yyyy-mm-dd
        返回：
            str: 指定时间范围内 Reddit 最新全球新闻的格式化数据框
        """
        
        global_news_result = interface.get_reddit_global_news(curr_date, 7, 5)

        return global_news_result

    @staticmethod
    @tool
    def get_finnhub_news(
        ticker: Annotated[
            str,
            "Search query of a company, e.g. 'AAPL, TSM, etc.",
        ],
        start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
        end_date: Annotated[str, "End date in yyyy-mm-dd format"],
    ):
        """
        在指定日期范围内获取 Finnhub 关于某股票的最新新闻
        参数：
            ticker (str): 公司股票代码，如 AAPL, TSM
            start_date (str): 开始日期，格式 yyyy-mm-dd
            end_date (str): 结束日期，格式 yyyy-mm-dd
        返回：
            str: 指定日期范围内关于该公司的新闻格式化数据框
        """

        end_date_str = end_date

        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        look_back_days = (end_date - start_date).days

        finnhub_news_result = interface.get_finnhub_news(
            ticker, end_date_str, look_back_days
        )

        return finnhub_news_result

    @staticmethod
    @tool
    def get_reddit_stock_info(
        ticker: Annotated[
            str,
            "Ticker of a company. e.g. AAPL, TSM",
        ],
        curr_date: Annotated[str, "Current date you want to get news for"],
    ) -> str:
        """
        获取指定日期 Reddit 关于某股票的最新新闻。
        参数：
            ticker (str): 公司股票代码，如 AAPL, TSM
            curr_date (str): 你想获取新闻的当前日期，格式 yyyy-mm-dd
        返回：
            str: 指定日期该公司最新新闻的格式化数据框
        """

        stock_news_results = interface.get_reddit_company_news(ticker, curr_date, 7, 5)

        return stock_news_results

    @staticmethod
    @tool
    def get_YFin_data(
        symbol: Annotated[str, "ticker symbol of the company"],
        start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
        end_date: Annotated[str, "End date in yyyy-mm-dd format"],
    ) -> str:
        """
        获取 Yahoo Finance 某股票的价格数据。
        参数：
            symbol (str): 公司股票代码，如 AAPL, TSM
            start_date (str): 开始日期，格式 yyyy-mm-dd
            end_date (str): 结束日期，格式 yyyy-mm-dd
        返回：
            str: 指定日期范围内该股票价格数据的格式化数据框
        """

        result_data = interface.get_YFin_data(symbol, start_date, end_date)

        return result_data

    @staticmethod
    @tool
    def get_YFin_data_online(
        symbol: Annotated[str, "ticker symbol of the company"],
        start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
        end_date: Annotated[str, "End date in yyyy-mm-dd format"],
    ) -> str:
        """
        获取 Yahoo Finance 某股票的价格数据（在线）。
        参数：
            symbol (str): 公司股票代码，如 AAPL, TSM
            start_date (str): 开始日期，格式 yyyy-mm-dd
            end_date (str): 结束日期，格式 yyyy-mm-dd
        返回：
            str: 指定日期范围内该股票价格数据的格式化数据框
        """

        result_data = interface.get_YFin_data_online(symbol, start_date, end_date)

        return result_data

    @staticmethod
    @tool
    def get_stockstats_indicators_report(
        symbol: Annotated[str, "ticker symbol of the company"],
        indicator: Annotated[
            str, "technical indicator to get the analysis and report of"
        ],
        curr_date: Annotated[
            str, "The current trading date you are trading on, YYYY-mm-dd"
        ],
        look_back_days: Annotated[int, "how many days to look back"] = 30,
    ) -> str:
        """
        获取某股票指定技术指标的分析报告。
        参数：
            symbol (str): 公司股票代码，如 AAPL, TSM
            indicator (str): 技术指标
            curr_date (str): 当前交易日期，格式 YYYY-mm-dd
            look_back_days (int): 回溯天数，默认 30
        返回：
            str: 指定股票和指标的格式化分析报告
        """

        result_stockstats = interface.get_stock_stats_indicators_window(
            symbol, indicator, curr_date, look_back_days, False
        )

        return result_stockstats

    @staticmethod
    @tool
    def get_stockstats_indicators_report_online(
        symbol: Annotated[str, "ticker symbol of the company"],
        indicator: Annotated[
            str, "technical indicator to get the analysis and report of"
        ],
        curr_date: Annotated[
            str, "The current trading date you are trading on, YYYY-mm-dd"
        ],
        look_back_days: Annotated[int, "how many days to look back"] = 30,
    ) -> str:
        """
        获取某股票指定技术指标的分析报告（在线）。
        参数：
            symbol (str): 公司股票代码，如 AAPL, TSM
            indicator (str): 技术指标
            curr_date (str): 当前交易日期，格式 YYYY-mm-dd
            look_back_days (int): 回溯天数，默认 30
        返回：
            str: 指定股票和指标的格式化分析报告
        """

        result_stockstats = interface.get_stock_stats_indicators_window(
            symbol, indicator, curr_date, look_back_days, True
        )

        return result_stockstats

    @staticmethod
    @tool
    def get_finnhub_company_insider_sentiment(
        ticker: Annotated[str, "ticker symbol for the company"],
        curr_date: Annotated[
            str,
            "current date of you are trading at, yyyy-mm-dd",
        ],
    ):
        """
        获取公司近 30 天内部人情绪信息（来自 SEC 公共信息）。
        参数：
            ticker (str): 公司股票代码
            curr_date (str): 当前交易日期，格式 yyyy-mm-dd
        返回：
            str: 以 curr_date 为起点的近 30 天情绪报告
        """

        data_sentiment = interface.get_finnhub_company_insider_sentiment(
            ticker, curr_date, 30
        )

        return data_sentiment

    @staticmethod
    @tool
    def get_finnhub_company_insider_transactions(
        ticker: Annotated[str, "ticker symbol"],
        curr_date: Annotated[
            str,
            "current date you are trading at, yyyy-mm-dd",
        ],
    ):
        """
        获取公司近 30 天内部人交易信息（来自 SEC 公共信息）。
        参数：
            ticker (str): 公司股票代码
            curr_date (str): 当前交易日期，格式 yyyy-mm-dd
        返回：
            str: 以 curr_date 为起点的近 30 天内部人交易报告
        """

        data_trans = interface.get_finnhub_company_insider_transactions(
            ticker, curr_date, 30
        )

        return data_trans

    @staticmethod
    @tool
    def get_simfin_balance_sheet(
        ticker: Annotated[str, "ticker symbol"],
        freq: Annotated[
            str,
            "reporting frequency of the company's financial history: annual/quarterly",
        ],
        curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    ):
        """
        获取公司最新资产负债表。
        参数：
            ticker (str): 公司股票代码
            freq (str): 财报频率 annual / quarterly
            curr_date (str): 当前交易日期，格式 yyyy-mm-dd
        返回：
            str: 公司最新资产负债表报告
        """

        data_balance_sheet = interface.get_simfin_balance_sheet(ticker, freq, curr_date)

        return data_balance_sheet

    @staticmethod
    @tool
    def get_simfin_cashflow(
        ticker: Annotated[str, "ticker symbol"],
        freq: Annotated[
            str,
            "reporting frequency of the company's financial history: annual/quarterly",
        ],
        curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    ):
        """
        获取公司最新现金流量表。
        参数：
            ticker (str): 公司股票代码
            freq (str): 财报频率 annual / quarterly
            curr_date (str): 当前交易日期，格式 yyyy-mm-dd
        返回：
            str: 公司最新现金流量表报告
        """

        data_cashflow = interface.get_simfin_cashflow(ticker, freq, curr_date)

        return data_cashflow

    @staticmethod
    @tool
    def get_simfin_income_stmt(
        ticker: Annotated[str, "ticker symbol"],
        freq: Annotated[
            str,
            "reporting frequency of the company's financial history: annual/quarterly",
        ],
        curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
    ):
        """
        获取公司最新利润表。
        参数：
            ticker (str): 公司股票代码
            freq (str): 财报频率 annual / quarterly
            curr_date (str): 当前交易日期，格式 yyyy-mm-dd
        返回：
            str: 公司最新利润表报告
        """

        data_income_stmt = interface.get_simfin_income_statements(
            ticker, freq, curr_date
        )

        return data_income_stmt

    @staticmethod
    @tool
    def get_google_news(
        query: Annotated[str, "Query to search with"],
        curr_date: Annotated[str, "Curr date in yyyy-mm-dd format"],
    ):
        """
        获取 Google News 指定关键词和日期范围的最新新闻。
        参数：
            query (str): 查询关键词
            curr_date (str): 当前日期，格式 yyyy-mm-dd
            look_back_days (int): 回溯天数
        返回：
            str: 指定条件下 Google News 最新新闻的格式化字符串
        """

        google_news_results = interface.get_google_news(query, curr_date, 7)

        return google_news_results

    @staticmethod
    @tool
    def get_stock_news_openai(
        ticker: Annotated[str, "the company's ticker"],
        curr_date: Annotated[str, "Current date in yyyy-mm-dd format"],
    ):
        """
        使用 OpenAI 新闻 API 获取某股票指定日期的最新新闻。
        参数：
            ticker (str): 公司股票代码，如 AAPL, TSM
            curr_date (str): 当前日期，格式 yyyy-mm-dd
        返回：
            str: 指定日期该公司最新新闻的格式化字符串
        """

        openai_news_results = interface.get_stock_news_openai(ticker, curr_date)

        return openai_news_results

    @staticmethod
    @tool
    def get_global_news_openai(
        curr_date: Annotated[str, "Current date in yyyy-mm-dd format"],
    ):
        """
        使用 OpenAI 宏观经济新闻 API 获取指定日期的最新宏观新闻。
        参数：
            curr_date (str): 当前日期，格式 yyyy-mm-dd
        返回：
            str: 指定日期最新宏观新闻的格式化字符串
        """

        openai_news_results = interface.get_global_news_openai(curr_date)

        return openai_news_results

    @staticmethod
    @tool
    def get_fundamentals_openai(
        ticker: Annotated[str, "the company's ticker"],
        curr_date: Annotated[str, "Current date in yyyy-mm-dd format"],
    ):
        """
        使用 OpenAI 新闻 API 获取某股票指定日期的最新基本面信息。
        参数：
            ticker (str): 公司股票代码，如 AAPL, TSM
            curr_date (str): 当前日期，格式 yyyy-mm-dd
        返回：
            str: 指定日期该公司最新基本面信息的格式化字符串
        """

        openai_fundamentals_results = interface.get_fundamentals_openai(
            ticker, curr_date
        )

        return openai_fundamentals_results
