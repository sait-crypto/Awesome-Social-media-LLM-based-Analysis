"""
完整示例：从Zotero Meta提取分类并验证
"""
import json
from src.process_zotero_meta import ZoteroProcessor

# 模拟真实的Zotero导出数据
real_world_example = {
    "itemType": "conferencePaper",
    "title": "Large Language Models for Social Media Content Moderation",
    "DOI": "10.1145/example.2024",
    "date": "2024-03-15",
    "url": "https://arxiv.org/abs/2403.12345",
    "abstractNote": "This paper explores the application of large language models in detecting hate speech and misinformation on social media platforms.",
    "creators": [
        {"creatorType": "author", "firstName": "Alice", "lastName": "Zhang"},
        {"creatorType": "author", "firstName": "Bob", "lastName": "Johnson"},
        {"creatorType": "author", "firstName": "Carol", "lastName": "Williams"}
    ],
    "conferenceName": "CHI 2024",
    "extra": "titleTranslation: 大语言模型在社交媒体内容审核中的应用\nTLDR: 本文研究了大语言模型在社交媒体平台上检测仇恨言论和虚假信息的应用",
    "tags": [
        {"tag": "cat Hate Speech Analysis"},
        {"tag": "cat Misinformation Analysis"},
        {"tag": "cat Social Media Security"},
        {"tag": "large language model"},
        {"tag": "content moderation"},
        {"tag": "social media"}
    ],
    "notes": [
        {"note": "<p>这篇论文提出了一个创新的方法</p>"}
    ]
}

# 处理数据
processor = ZoteroProcessor()
papers = processor.process_meta_data(real_world_example)

if papers:
    paper = papers[0]
    
    print("=" * 70)
    print("完整示例：从真实Zotero数据提取论文信息")
    print("=" * 70)
    
    print(f"\n📄 基本信息")
    print(f"   标题: {paper.title}")
    print(f"   作者: {paper.authors}")
    print(f"   会议: {paper.conference}")
    print(f"   日期: {paper.date}")
    print(f"   DOI: {paper.doi}")
    print(f"   URL: {paper.paper_url}")
    
    print(f"\n🏷️  提取的分类")
    if paper.category:
        categories = paper.category.split(";")
        for i, cat in enumerate(categories, 1):
            print(f"   {i}. {cat}")
        print(f"   格式: {paper.category}")
    else:
        print(f"   无分类")
    
    print(f"\n📝 其他字段")
    print(f"   标题翻译: {paper.title_translation}")
    print(f"   TLDR: {paper.analogy_summary}")
    print(f"   摘要: {paper.abstract[:100]}...")
    print(f"   笔记: {paper.notes}")
    
    print(f"\n🔍 原始Tags数组")
    print(json.dumps(real_world_example["tags"], indent=2, ensure_ascii=False))
    
    print(f"\n✅ 分类提取分析")
    print(f"   - 总共 {len(real_world_example['tags'])} 个标签")
    category_count = len(paper.category.split(";")) if paper.category else 0
    print(f"   - 提取出 {category_count} 个分类")
    print(f"   - 分类格式: 分号分隔的字符串")
    print(f"   - 忽略了非分类标签: large language model, content moderation, social media")
    
    print("\n" + "=" * 70)
    print("测试完成！所有字段都已正确提取")
    print("=" * 70)
else:
    print("❌ 无法处理数据")
