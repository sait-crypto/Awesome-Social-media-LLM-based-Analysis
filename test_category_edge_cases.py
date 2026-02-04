"""
测试分类提取的边界情况
"""
from src.process_zotero_meta import ZoteroProcessor

processor = ZoteroProcessor()

print("=" * 60)
print("边界情况测试")
print("=" * 60)

# 测试1: 空tags数组
test1 = {"title": "Test 1", "tags": []}
papers1 = processor.process_meta_data(test1)
print(f"\n测试1 - 空tags数组:")
print(f"  结果: '{papers1[0].category if papers1 else 'N/A'}'")
print(f"  预期: '' (空字符串)")

# 测试2: 没有tags字段
test2 = {"title": "Test 2"}
papers2 = processor.process_meta_data(test2)
print(f"\n测试2 - 没有tags字段:")
print(f"  结果: '{papers2[0].category if papers2 else 'N/A'}'")
print(f"  预期: '' (空字符串)")

# 测试3: tags中没有分类标签
test3 = {"title": "Test 3", "tags": [{"tag": "keyword1"}, {"tag": "keyword2"}]}
papers3 = processor.process_meta_data(test3)
print(f"\n测试3 - 没有分类标签:")
print(f"  结果: '{papers3[0].category if papers3 else 'N/A'}'")
print(f"  预期: '' (空字符串)")

# 测试4: 重复的分类（应去重）
test4 = {
    "title": "Test 4",
    "tags": [
        {"tag": "cat Social Media Security"},
        {"tag": "cat Social Media Security"},
        {"tag": "cat Humor Generation"}
    ]
}
papers4 = processor.process_meta_data(test4)
print(f"\n测试4 - 重复分类:")
print(f"  结果: '{papers4[0].category if papers4 else 'N/A'}'")
print(f"  预期: 'Social Media Security;Humor Generation'")

# 测试5: 分号分隔的分类带空格
test5 = {
    "title": "Test 5",
    "tags": [
        {"tag": "cat Social Media Security ; Humor Generation ; Sentiment Analysis"}
    ]
}
papers5 = processor.process_meta_data(test5)
print(f"\n测试5 - 分号分隔带空格:")
print(f"  结果: '{papers5[0].category if papers5 else 'N/A'}'")
print(f"  预期: 'Social Media Security;Humor Generation;Sentiment Analysis'")

# 测试6: 混合大小写的"cat"前缀
test6 = {
    "title": "Test 6",
    "tags": [
        {"tag": "cat Social Media Security"},
        {"tag": "CAT Humor Generation"},  # 大写CAT
        {"tag": "Cat Sentiment Analysis"}  # 首字母大写
    ]
}
papers6 = processor.process_meta_data(test6)
print(f"\n测试6 - 不同大小写的cat前缀:")
print(f"  结果: '{papers6[0].category if papers6 else 'N/A'}'")
print(f"  预期: 'Social Media Security;Humor Generation;Sentiment Analysis'")

# 测试7: tag字段为空字符串
test7 = {
    "title": "Test 7",
    "tags": [
        {"tag": ""},
        {"tag": "cat Social Media Security"}
    ]
}
papers7 = processor.process_meta_data(test7)
print(f"\n测试7 - 包含空tag:")
print(f"  结果: '{papers7[0].category if papers7 else 'N/A'}'")
print(f"  预期: 'Social Media Security'")

print("\n" + "=" * 60)
print("所有边界测试完成")
print("=" * 60)
