# surveyPaperCollectorPrivate

> **Contributions**
>
> If you want to add your paper or update details like conference info or code URLs, please submit a pull request. You can generate the necessary markdown for each paper by filling out `generate_item.py` and running `python generate_item.py`. We greatly appreciate your contributions. Alternatively, you can email me ([Gmail](fscnkucs@gmail.com)) the links to your paper and code, and I will add your paper to the list as soon as possible.

---
<p align="center">
<img src="assets/taxonomy.png" width = "95%" alt="" align=center />
</p>

### Quick Links
  - [Make Long CoT Short](#Make-Long-CoT-Short)
    - [SFT-based Methods](#SFT-based-Methods)
    - [RL-based Methods](#RL-based-Methods)
    - [Prompt-driven Methods](#Prompt-driven-Methods)
    - [Latent Reasoning](#Latent-Reasoning)
  - [Build SLM with Strong Reasoning Ability](#Build-SLM-with-Strong-Reasoning-Ability)
    - [Distillation](#Distillation)
    - [Quantization and Pruning](#Quantization-and-Pruning)
    - [RL+SLM Methods](#rlslm-methods)
  - [Let Decoding More Efficient](#Let-Decoding-More-Efficient)
    - [Efficient TTS](#Efficient-TTS)
    - [Other Optimal Methods](#Other-Optimal-Methods)
  - [Efficient Multimodal Reasoning](#efficient-agentic-reasoning)
  - [Efficient Agentic Reasoning](#Efficient-Agentic-Reasoning)
  - [Evaluation and Benchmarks](#Evaluation-and-Benchmarks)
  - [Background Papers](#Background-Papers)
  - [Competition](#Competition)

## Full list

### Make Long CoT Short

| Title & Authors | Analogy Summary | Summary | Pipeline | Links |
|:--| :----: | :---: | :---: | :---: |
|[123](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 33 |44||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|

### Build SLM with Strong Reasoning Ability

| Title & Authors | Analogy Summary | Summary | Pipeline | Links |
|:--| :----: | :---: | :---: | :---: |
|[3321](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 23 |2|\[AI generated\] 该方法通过构建一个“思维链”推理框架，让小型语言模型像解谜一样逐步拆解复杂问题，从而显著提升其逻辑推理能力。|**目标/动机**: \[AI generated\] 构建具有强大推理能力的小型语言模型，提升其逻辑分析与问题解决性能。<br>**创新点**: \[AI generated\] 该论文的主要创新点在于提出了一种构建具有强大推理能力的小型语言模型的方法。<br>**方法精炼**: \[AI generated\] 构建小语言模型，提升推理能力。<br>**结论**: \[AI generated\] 该论文旨在构建具备强大推理能力的小型语言模型（SLM）。<br>**局限/展望**: \[AI generated\] 摘要信息不足，无法准确评估论文局限。建议补充研究内容与核心结论。||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[222333](https://ojs.aaai.org/index.php/ICWSM/article/view/35807) <br> 331 |123|\[AI generated\] 通过构建“思维链”脚手架，像为小树苗提供攀爬架一样，系统性地引导小型语言模型逐步完成复杂推理任务。|**目标/动机**: \[AI generated\] 该论文旨在构建具有强大推理能力的小型语言模型。<br>**创新点**: \[AI generated\] 该论文的主要创新点在于构建具有强大推理能力的小型语言模型，以提升其逻辑分析与问题解决效能。<br>**方法精炼**: \[AI generated\] 构建具备强推理能力的小型语言模型。<br>**结论**: \[AI generated\] 该论文旨在构建具备强大推理能力的小型语言模型，但摘要内容过简，无法提炼具体结论。<br>**局限/展望**: \[AI generated\] 摘要内容过简，无法评估模型推理能力的具体表现与验证方法，需补充详细实验设计与结果分析。||[Paper](https://ojs.aaai.org/index.php/ICWSM/article/view/35807)|
|[TamperTok: Forensics\-driven tokenized](https://ieeexplore.ieee.org/document/10246420/) <br> 123 |123|\[AI generated\] 该研究通过为小型语言模型嵌入防篡改的“数字水印”，使其在推理时能像拥有自检能力的精密仪器一样，自动识别并排除被恶意篡改的思维链干扰。|**目标/动机**: \[AI generated\] 研究目标：构建具有强推理能力的小型语言模型，提升其抗篡改性能。<br>**创新点**: \[AI generated\] TamperTok提出基于取证驱动的令牌化方法，旨在构建具备强推理能力的小型语言模型。<br>**方法精炼**: \[AI generated\] 基于令牌化与法证分析，构建具备强推理能力的小型语言模型。<br>**结论**: \[AI generated\] TamperTok通过令牌化增强小型语言模型在数字取证中的推理能力。<br>**局限/展望**: \[AI generated\] 摘要内容过简，无法基于现有信息推断局限性或未来工作。||[Paper](https://ieeexplore.ieee.org/document/10246420/)|
|[TamperTok: Forensics\-driven tokenized](https://ieeexplore.ieee.org/document/10246420/) <br> 123 |123||||[Paper](https://ieeexplore.ieee.org/document/10246420/)|
|[222333](https://ojs.aaai.org/index.php/ICWSM/article/view/35807) <br> 331 |123||||[Paper](https://ojs.aaai.org/index.php/ICWSM/article/view/35807)|
|[3321](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 23 |2||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[222333](https://ojs.aaai.org/index.php/ICWSM/article/view/35807) <br> 331 |123||||[Paper](https://ojs.aaai.org/index.php/ICWSM/article/view/35807)|
|[3321](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 23 |2||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[3321](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 23 |2||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[3321](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 23 |2||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[3321](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 23 |2||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[3321](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 23 |2||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[3321](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 23 |2||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[3321](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 23 |2||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[3321](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 23 |2||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[3321](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 23 |2||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|

### Efficient Multimodal Reasoning

| Title & Authors | Analogy Summary | Summary | Pipeline | Links |
|:--| :----: | :---: | :---: | :---: |
|[123](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 321 |123|\[AI generated\] 该方法通过多模态信息协同推理，如同交响乐团中各乐器声部精准配合，最终高效合成统一决策。|**目标/动机**: \[AI generated\] 研究目标：探索高效多模态推理方法，提升跨模态信息处理能力。<br>**创新点**: \[AI generated\] 本文提出了一种高效的多模态推理方法，旨在提升处理速度与准确性。<br>**方法精炼**: \[AI generated\] 该论文提出了一种高效的多模态推理方法，通过优化模型架构与计算流程，显著提升处理速度与准确性。<br>**结论**: \[AI generated\] 该论文主要探讨了高效多模态推理方法，旨在提升跨模态信息处理与整合的效率。<br>**局限/展望**: \[AI generated\] 摘要内容缺失，无法评估论文局限性。建议补充摘要以明确研究方向与贡献。||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[123](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 321 |123||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[123](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 321 |123||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[123](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 321 |123||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|
|[123](https://dl.acm.org/doi/10.1145/3746027.3754828) <br> 321 |123||||[Paper](https://dl.acm.org/doi/10.1145/3746027.3754828)|

=====List End=====
## Acknowledgement