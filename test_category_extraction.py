"""
测试从Zotero Meta中提取分类功能
"""
import json
from src.process_zotero_meta import ZoteroProcessor

# 测试数据
test_data = {
    "DOI": "10.1234/test.2024",
    "title": "Test Paper Title",
    "date": "2024-01-01",
    "url": "https://example.com/paper",
    "abstractNote": "This is a test abstract.",
    "creators": [
        {"creatorType": "author", "firstName": "John", "lastName": "Doe"},
        {"creatorType": "author", "firstName": "Jane", "lastName": "Smith"}
    ],
    "conferenceName": "Test Conference 2024",
    "tags": [
        {"tag": "cat Social Media Security"},
        {"tag": "cat Humor Generation;Frontier Applications"},
        {"tag": "regular tag"},  # 非分类标签，应被忽略
        {"tag": "cat Sentiment Analysis"}
    ]
}

# 创建处理器并处理数据
processor = ZoteroProcessor()
papers = processor.process_meta_data(test_data)

# 验证结果
if papers:
    paper = papers[0]
    print("=" * 60)
    print("测试结果")
    print("=" * 60)
    print(f"标题: {paper.title}")
    print(f"作者: {paper.authors}")
    print(f"会议: {paper.conference}")
    print(f"分类: {paper.category}")
    print("=" * 60)
    
    # 验证分类提取是否正确
    expected_categories = "Social Media Security;Humor Generation;Frontier Applications;Sentiment Analysis"
    if paper.category == expected_categories:
        print("✅ 分类提取成功！")
        print(f"   提取到的分类: {paper.category}")
        print(f"   格式: 分号分隔的字符串")
    else:
        print("❌ 分类提取失败！")
        print(f"   期望: {expected_categories}")
        print(f"   实际: {paper.category}")
else:
    print("❌ 无法处理测试数据")

print("\n" + "=" * 60)
print("测试用例说明")
print("=" * 60)
print("输入的tags数组:")
print(json.dumps(test_data["tags"], indent=2, ensure_ascii=False))
print("\n应该提取出4个分类:")
print("  1. Social Media Security")
print("  2. Humor Generation")
print("  3. Frontier Applications")
print("  4. Sentiment Analysis")
print("\n注意: 'regular tag' 不以 'cat ' 开头，应被忽略")
