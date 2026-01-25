# Awesome Social Media Analysis with LLM Method

> **Contributions**
>
> If you want to add your paper or update details like conference info or code URLs, please submit a pull request. You can generate the necessary markdown for each paper by filling out `generate_item.py` and running `python generate_item.py`. We greatly appreciate your contributions. Alternatively, you can email me ([Gmail](fscnkucs@gmail.com)) the links to your paper and code, and I will add your paper to the list as soon as possible.

---
<p align="center">
<img src="assets/taxonomy.png" width = "95%" alt="" align=center />
</p>

>For complete paper information, please refer to the paper_database.xlsx file.
><br>完整论文信息可以查看paper_database.xlsx文件

**Key Points for Table Usage**
- <b>Paper Link</b>: Please click the paper title
- <b>Paper Project Link</b>: Please click the GitHub icon or Project icon above the paper title
- <b>Summary</b> and <b>Notes</b> can be expanded by clicking

**表格使用要点**
- <b>论文链接</b>:请点击论文标题
- <b>论文项目链接</b>:请点击论文标题上方的github标或project标
- <b>Summary</b>和<b>Notes</b>可以点击展开

## Full paper list (2 papers)
### Quick Links

  - [Uncategorized](#-Uncategorized-0-papers) (0 papers)
  - [Base Techniques](#-Base-Techniques-1-papers) (1 papers)
  - [Perception and Classification](#-Perception-and-Classification-1-papers) (1 papers)
    - [Hate Speech Analysis](#Hate-Speech-Analysis-0-papers) (0 papers)
    - [Misinformation Analysis](#Misinformation-Analysis-0-papers) (0 papers)
    - [Sentiment Analysis](#Sentiment-Analysis-1-papers) (1 papers)
    - [Meme Analysis](#Meme-Analysis-0-papers) (0 papers)
    - [Steganography Detection](#Steganography-Detection-0-papers) (0 papers)
    - [User Stance Detection](#User-Stance-Detection-0-papers) (0 papers)
    - [Malicious Bot Detection](#Malicious-Bot-Detection-0-papers) (0 papers)
    - [User Behavior Prediction](#User-Behavior-Prediction-0-papers) (0 papers)
  - [Understanding](#-Understanding-0-papers) (0 papers)
    - [Event Extraction](#Event-Extraction-0-papers) (0 papers)
    - [Topic Modeling](#Topic-Modeling-0-papers) (0 papers)
    - [Social Psychological Phenomena Analysis](#Social-Psychological-Phenomena-Analysis-0-papers) (0 papers)
    - [Social Popularity Prediction](#Social-Popularity-Prediction-0-papers) (0 papers)
    - [User Identity Understanding](#User-Identity-Understanding-0-papers) (0 papers)
    - [User Profiling](#User-Profiling-0-papers) (0 papers)
  - [Generation](#-Generation-0-papers) (0 papers)
    - [Comment Generation](#Comment-Generation-0-papers) (0 papers)
    - [Debate Generation](#Debate-Generation-0-papers) (0 papers)
    - [Rumor Refutation Generation](#Rumor-Refutation-Generation-0-papers) (0 papers)
    - [Psychological Healing](#Psychological-Healing-0-papers) (0 papers)
    - [Misinformation Generation](#Misinformation-Generation-0-papers) (0 papers)
    - [Social Bots](#Social-Bots-0-papers) (0 papers)
  - [Simulation and Deduction](#-Simulation-and-Deduction-0-papers) (0 papers)
    - [Dynamic Community Analysis](#Dynamic-Community-Analysis-0-papers) (0 papers)
    - [Information Diffusion Analysis](#Information-Diffusion-Analysis-0-papers) (0 papers)
    - [Social Simulation](#Social-Simulation-0-papers) (0 papers)
    - [Social Network Simulation](#Social-Network-Simulation-0-papers) (0 papers)
    - [Town/Community Simulation](#TownCommunity-Simulation-0-papers) (0 papers)
    - [Game Simulation](#Game-Simulation-0-papers) (0 papers)
    - [Family Simulation](#Family-Simulation-0-papers) (0 papers)
    - [Macrosocial Phenomena Analysis](#Macrosocial-Phenomena-Analysis-0-papers) (0 papers)
    - [Frontier Applications](#Frontier-Applications-0-papers) (0 papers)
  - [Social Media Security](#-Social-Media-Security-0-papers) (0 papers)
  - [Other](#-Other-0-papers) (0 papers)


### | Base Techniques (1 papers)

| Title & Info | Analogy Summary | Pipeline | Summary |
|:--| :---: | :----: | :---: |
|[![Star](https://img.shields.io/github/stars/OpenBMB/IoA.svg?style=social&label=Star)](https://github.com/OpenBMB/IoA) [![Publish](https://img.shields.io/badge/Conference-The%20Thirteenth%20International%20Conference%20on%20Learning%20Representations-blue)]()<br>[Internet of agents: Weaving a web of heterogeneous agents for collaborative intelligence](https://openreview.net/forum?id=o1Et3MogPw) <br> Weize Chen\*, Ziming You\*, Ran Li\*, Yitong Guan\*, Chen Qian, Chenyang Zhao Cheng Yang, Ruobing Xie, Zhiyuan Liu, Maosong Sun <br> 2024-10-04|agent互联网，升级版ABM系统，采用类似互联网思想，C/S架构，分布化、服务化、平台化|<div style="display:flex;flex-direction:column;gap:6px;align-items:center"><img width="1000" style="display:block;margin:6px auto" alt="pipeline" src="figures/IoA.png"><img width="1000" style="display:block;margin:6px auto" alt="pipeline" src="figures/IoA2.png"></div>| <div style="line-height: 1.05;font-size: 0.8em"> <details><summary title="**[motivation]** 先前的multi-agent系统的局限性，系统化平台化程度不足（缺乏第三方集成支持，无法分布式，通信协议和状态转换依赖于硬编码） **[innovation]** 将互联网的开放、分布式、服务化思想引入，构建一种标准化、可扩展的支持分布式、异构的智能体集成与通信协议。 **[method]** 服务器：智能体注册（分发系统提示词）、管理已注册智能体（专家）、专家发现服务、群聊管理和消息传递；客户端：包装具体智能体，提供通信接口；三层结构；通信即可嵌套灵活群聊；群聊采用**有限状态机**管理流程；平台初始化与注册-&gt;任务触发团队形成-&gt;内部嵌套协作 **[conclusion/contribution]** 在 GAIA 基准测试中，仅使用四个基础 ReAct 智能体即达到最佳性能；在 RAG 任务中，基于 GPT-3.5 的 IoA 达到或超过 GPT-4 的性能 **[limitation/future]** 实验中存在冗余消息，通信 Token 消耗增加近一倍，这证明agent作为对话者而非执行者的本质能力区别；单点服务器可能存在瓶颈；智能体通过注册获取提示词成为不同专家，仍高度依赖人工实验设计，且这种专家的能力是否可靠">**[summary]**</summary><div style="margin-top:6px">**[motivation]** 先前的multi-agent系统的局限性，系统化平台化程度不足（缺乏第三方集成支持，无法分布式，通信协议和状态转换依赖于硬编码）<br>**[innovation]** 将互联网的开放、分布式、服务化思想引入，构建一种标准化、可扩展的支持分布式、异构的智能体集成与通信协议。<br>**[method]** 服务器：智能体注册（分发系统提示词）、管理已注册智能体（专家）、专家发现服务、群聊管理和消息传递；客户端：包装具体智能体，提供通信接口；三层结构；通信即可嵌套灵活群聊；群聊采用**有限状态机**管理流程；平台初始化与注册->任务触发团队形成->内部嵌套协作<br>**[conclusion/contribution]** 在 GAIA 基准测试中，仅使用四个基础 ReAct 智能体即达到最佳性能；在 RAG 任务中，基于 GPT-3.5 的 IoA 达到或超过 GPT-4 的性能<br>**[limitation/future]** 实验中存在冗余消息，通信 Token 消耗增加近一倍，这证明agent作为对话者而非执行者的本质能力区别；单点服务器可能存在瓶颈；智能体通过注册获取提示词成为不同专家，仍高度依赖人工实验设计，且这种专家的能力是否可靠</div></details><div style="margin-top:6px"><details><summary>**[notes]**</summary><div style="margin-top:6px">每个agent被一个客户端包装；服务器不是agent，它只做四件事：注册、发现、建群、路由；相对于传统ABM，这是一个更大型的服务系统，该方法通过基于任务的“群聊”方式组织问题解决，相对传统回合制方式更加自由。本身也是一个高度可扩展系统。问题在于智能体通过注册获取提示词成为不同专家，仍依赖手工设计，且这种专家的能力是否可靠。对于社会模拟任务相对于传统方法有何决定性优势仍未可知</div></details></div></div>|

### | Perception and Classification (1 papers)


### Sentiment Analysis (1 papers)

| Title & Info | Analogy Summary | Pipeline | Summary |
|:--| :---: | :----: | :---: |
|[![Star](https://img.shields.io/github/stars/neuralnaresh/multimodal-emotion-recognition.svg?style=social&label=Star)](https://github.com/neuralnaresh/multimodal-emotion-recognition) [![Publish](https://img.shields.io/badge/Conference-Proceedings%20of%20the%2031st%20ACM%20International%20Conference%20on%20Multimedia-blue)]()<br>[Multi-label emotion analysis in conversation via multimodal knowledge distillation](https://dl.acm.org/doi/10.1145/3581783.3612517) <br> Sidharth Anand∗,Naresh Kumar Devulapally∗,Sreyasee Das Bhattacharjee,Junsong Yuan <br> 2023-10-27|三个专家分别处理一个模态，训练的同时将能力蒸馏给融合分支，最终形成一个整体模型，教师（分支专家）与学生（融合专家）一同处理多模态内容，得到情感分类|<img width="1200" alt="pipeline" src="figures/SeMuL-PCD.png">| <div style="line-height: 1.05;font-size: 0.8em"> <details><summary title="**[motivation]** Addresses the limitations of single-dominant emotion assumptions by tackling the challenge of multi-label emotion co-occurrence and generalization across diverse socio-demographic groups, particularly varying age populations. \[翻译\] 针对现有多模态方法主要关注单一主导情感的局限性，该研究致力于解决情感标签共现的识别难题，并提升模型在不同社会人口统计学群体（特别是不同年龄段人群）中的泛化能力。 **[innovation]** 将多模态知识蒸馏与标签一致性校准损失（LCC）相结合，减轻了模型对简单标签的过拟合（保证置信度相近）；构建了一个利用蒸馏方法的整体框架，其目的是为了融合各模态能力 **[method]** Employing a Multimodal Transformer Network where mode-specific peer branches \(visual, audio, textual\) collaboratively distill learned probabilistic uncertainty into a fusion branch via cross-network attention and noise contrastive estimation.…… \[翻译\] 将三个特定模态的对等分支通过跨网络注意力和噪声对比估计，协同地将其学习到的概率蒸馏到融合分支中，构建了一个拥有四个分支的整体预测模型。\[值得关注\]视频使用Tubelet embedding技术，将视频切分为时空小块（Spatial-Temporal Tubes），保留时空信息 **[conclusion/contribution]** Demonstrates state-of-the-art performance on MOSEI, EmoReact, and ElderReact datasets, achieving an approximate 17% improvement in weighted F1-score during cross-dataset evaluations, thereby validating robustness in age-diverse scenarios. \[翻译\] 在MOSEI、EmoReact和ElderReact数据集上最先进的性能，跨数据集评估有约17%的加权F1提升，在跨年龄场景下具有鲁棒性。 **[limitation/future]** The approach necessitates the reduction of complex emotion categories to basic subsets for cross-dataset consistency and entails significant computational overhead due to the spatiotemporal tubelet embedding mechanism. \[翻译\] 为了保持跨数据集一致性，要将复杂情感类归约为基础子集，由于采用时空Tubelet嵌入机制，导致了显著的计算开销">**[summary]**</summary><div style="margin-top:6px">**[motivation]** Addresses the limitations of single-dominant emotion assumptions by tackling the challenge of multi-label emotion co-occurrence and generalization across diverse socio-demographic groups, particularly varying age populations.<br>\[翻译\] 针对现有多模态方法主要关注单一主导情感的局限性，该研究致力于解决情感标签共现的识别难题，并提升模型在不同社会人口统计学群体（特别是不同年龄段人群）中的泛化能力。<br>**[innovation]** 将多模态知识蒸馏与标签一致性校准损失（LCC）相结合，减轻了模型对简单标签的过拟合（保证置信度相近）；构建了一个利用蒸馏方法的整体框架，其目的是为了融合各模态能力<br>**[method]** Employing a Multimodal Transformer Network where mode-specific peer branches \(visual, audio, textual\) collaboratively distill learned probabilistic uncertainty into a fusion branch via cross-network attention and noise contrastive estimation.……<br>\[翻译\] 将三个特定模态的对等分支通过跨网络注意力和噪声对比估计，协同地将其学习到的概率蒸馏到融合分支中，构建了一个拥有四个分支的整体预测模型。\[值得关注\]视频使用Tubelet embedding技术，将视频切分为时空小块（Spatial-Temporal Tubes），保留时空信息<br>**[conclusion/contribution]** Demonstrates state-of-the-art performance on MOSEI, EmoReact, and ElderReact datasets, achieving an approximate 17% improvement in weighted F1-score during cross-dataset evaluations, thereby validating robustness in age-diverse scenarios.<br>\[翻译\] 在MOSEI、EmoReact和ElderReact数据集上最先进的性能，跨数据集评估有约17%的加权F1提升，在跨年龄场景下具有鲁棒性。<br>**[limitation/future]** The approach necessitates the reduction of complex emotion categories to basic subsets for cross-dataset consistency and entails significant computational overhead due to the spatiotemporal tubelet embedding mechanism.<br>\[翻译\] 为了保持跨数据集一致性，要将复杂情感类归约为基础子集，由于采用时空Tubelet嵌入机制，导致了显著的计算开销</div></details><div style="margin-top:6px"><details><summary>**[notes]**</summary><div style="margin-top:6px">【面向结果模型训练】\[引用句\]"Transscending the traditional paradigm of identifying single dominant emotions, Anand et al. \[2023\] proposed SeMuL-PCD to enhance the granularity of affective perception in diverse social contexts; by leveraging a collaborative distillation mechanism that calibrates mode-specific feedback, their model robustly disentangles multi-label emotional co-occurrences across varying demographic backgrounds \(e.g., children and the elderly\), thereby providing a more nuanced foundation for socially adaptive agents."<br>\[翻译\] “为了超越识别单一主导情感的传统范式，Anand等人\[2023\]提出了SeMuL-PCD，旨在增强不同社会语境下情感感知的粒度；通过利用一种校准模态特定反馈的协作蒸馏机制，该模型能够在不同的人口统计背景（如儿童和老人）下鲁棒地解耦多标签情感的共现关系，从而为具备社会适应能力的智能体提供了更精细的情感理解基础。”</div></details></div></div>|

=====List End=====
## Acknowledgement