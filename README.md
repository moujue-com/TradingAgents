<p align="center">
  <img src="assets/TauricResearch.png" style="width: 60%; height: auto;">
</p>

<div align="center" style="line-height: 1;">
  <a href="https://arxiv.org/abs/2412.20138" target="_blank"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-2412.20138-B31B1B?logo=arxiv"/></a>
  <a href="https://discord.com/invite/hk9PGKShPK" target="_blank"><img alt="Discord" src="https://img.shields.io/badge/Discord-TradingResearch-7289da?logo=discord&logoColor=white&color=7289da"/></a>
  <a href="./assets/wechat.png" target="_blank"><img alt="WeChat" src="https://img.shields.io/badge/WeChat-TauricResearch-brightgreen?logo=wechat&logoColor=white"/></a>
  <a href="https://x.com/TauricResearch" target="_blank"><img alt="X Follow" src="https://img.shields.io/badge/X-TauricResearch-white?logo=x&logoColor=white"/></a>
  <br>
  <a href="https://github.com/TauricResearch/" target="_blank"><img alt="Community" src="https://img.shields.io/badge/Join_GitHub_Community-TauricResearch-14C290?logo=discourse"/></a>
</div>

<div align="center">
  <!-- 保留这些链接。翻译会自动同步到 README。 -->
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=de">Deutsch</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=es">Español</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=fr">français</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ja">日本語</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ko">한국어</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=pt">Português</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ru">Русский</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=zh">中文</a>
</div>

---

# TradingAgents：多智能体大模型金融交易框架

> 🎉 **TradingAgents** 正式发布！我们收到了许多关于本项目的咨询，感谢社区的热情支持。
>
> 因此我们决定完全开源该框架。期待与你一起打造有影响力的项目！

<div align="center">
<a href="https://www.star-history.com/#TauricResearch/TradingAgents&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date" />
   <img alt="TradingAgents Star History" src="https://api.star-history.com/svg?repos=TauricResearch/TradingAgents&type=Date" style="width: 80%; height: auto;" />
 </picture>
</a>
</div>

<div align="center">

🚀 [TradingAgents](#tradingagents-framework) | ⚡ [安装与CLI](#installation-and-cli) | 🎬 [演示](https://www.youtube.com/watch?v=90gr5lwjIho) | 📦 [包用法](#tradingagents-package) | 🤝 [贡献](#contributing) | 📄 [引用](#citation)

</div>

## TradingAgents 框架

TradingAgents 是一个多智能体交易框架，模拟真实交易公司的运作。通过部署由大模型驱动的专业智能体：包括基本面分析师、情绪分析师、技术分析师、交易员、风险管理团队等，平台协作评估市场状况并给出交易决策。此外，这些智能体还会动态讨论以确定最优策略。

<p align="center">
  <img src="assets/schema.png" style="width: 100%; height: auto;">
</p>

> TradingAgents 框架仅供学术研究使用。交易表现受多种因素影响，包括所选大模型、模型温度、交易周期、数据质量及其他不确定因素。[本项目不构成任何金融、投资或交易建议。](https://tauric.ai/disclaimer/)

我们的框架将复杂的交易任务分解为专业角色，确保系统实现稳健、可扩展的市场分析与决策。

### 分析师团队
- 基本面分析师：评估公司财务和业绩指标，识别内在价值和潜在风险。
- 情绪分析师：利用情绪打分算法分析社交媒体和公众情绪，判断短期市场情绪。
- 新闻分析师：监控全球新闻和宏观经济指标，解读事件对市场的影响。
- 技术分析师：利用技术指标（如MACD和RSI）识别交易模式并预测价格走势。

<p align="center">
  <img src="assets/analyst.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

### 研究员团队
- 由多头和空头研究员组成，批判性地评估分析师团队的见解。通过结构化辩论，平衡潜在收益与固有风险。

<p align="center">
  <img src="assets/researcher.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### 交易员智能体
- 汇总分析师和研究员的报告，做出明智的交易决策。根据全面的市场洞察决定交易时机和规模。

<p align="center">
  <img src="assets/trader.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### 风险管理与投资组合经理
- 持续评估投资组合风险，包括市场波动性、流动性等因素。风险管理团队评估并调整交易策略，向投资组合经理提供评估报告以供最终决策。
- 投资组合经理批准/拒绝交易提案。若批准，订单将发送至模拟交易所并执行。

<p align="center">
  <img src="assets/risk.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

## 安装与CLI

### 安装

克隆 TradingAgents：
```bash
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents
```

在你喜欢的环境管理器中创建虚拟环境：
```bash
conda create -n tradingagents python=3.13
conda activate tradingagents
```

安装依赖：
```bash
pip install -r requirements.txt
```

### 必需的API

你还需要 FinnHub API 获取金融数据。我们的代码全部基于免费额度实现。
```bash
export FINNHUB_API_KEY=$YOUR_FINNHUB_API_KEY
```

所有智能体需要 OpenAI API。
```bash
export OPENAI_API_KEY=$YOUR_OPENAI_API_KEY
```

### CLI 用法

你也可以直接运行 CLI：
```bash
python -m cli.main
```
你会看到一个界面，可以选择股票代码、日期、LLM、研究深度等。

<p align="center">
  <img src="assets/cli/cli_init.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

界面会实时显示结果，让你跟踪智能体的执行进度。

<p align="center">
  <img src="assets/cli/cli_news.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

<p align="center">
  <img src="assets/cli/cli_transaction.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

## TradingAgents 包

### 实现细节

我们基于 LangGraph 构建 TradingAgents，以确保灵活性和模块化。实验中我们使用 `o1-preview` 和 `gpt-4o` 作为深度思考和快速思考的大模型。但测试时建议用 `o4-mini` 和 `gpt-4.1-mini`，因为本框架会频繁调用API。

### Python 用法

你可以在代码中导入 `tradingagents` 模块并初始化 `TradingAgentsGraph()` 对象。`.propagate()` 方法会返回决策。你也可以直接运行 `main.py`，示例：

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())

# 正向推理
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)
```

你也可以调整默认配置，自定义大模型、辩论轮数等：

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 创建自定义配置
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "gpt-4.1-nano"  # 使用不同模型
config["quick_think_llm"] = "gpt-4.1-nano"  # 使用不同模型
config["max_debate_rounds"] = 1  # 增加辩论轮数
config["online_tools"] = True # 使用在线工具或缓存数据

# 用自定义配置初始化
ta = TradingAgentsGraph(debug=True, config=config)

# 正向推理
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)
```

> 对于 `online_tools`，建议实验时开启，可获取实时数据。离线工具依赖我们自建的 **Tauric TradingDB** 缓存数据集，主要用于回测。我们正在完善该数据集，未来会随新项目一同发布，敬请期待！

你可以在 `tradingagents/default_config.py` 查看全部配置项。

## 贡献

欢迎社区贡献！无论是修复bug、完善文档还是提出新特性建议，你的参与都能让项目更好。如果你对金融AI研究感兴趣，欢迎加入我们的开源社区 [Tauric Research](https://tauric.ai/)。

## 引用

如果 *TradingAgents* 对你有帮助，请引用我们的工作：

```
@misc{xiao2025tradingagentsmultiagentsllmfinancial,
      title={TradingAgents: Multi-Agents LLM Financial Trading Framework}, 
      author={Yijia Xiao and Edward Sun and Di Luo and Wei Wang},
      year={2025},
      eprint={2412.20138},
      archivePrefix={arXiv},
      primaryClass={q-fin.TR},
      url={https://arxiv.org/abs/2412.20138}, 
}
```
