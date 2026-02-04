"""
完整的分类提取功能验证
验证从Zotero Meta到Paper对象的完整流程
"""
from src.process_zotero_meta import ZoteroProcessor

print("=" * 70)
print("分类提取功能 - 完整验证报告")
print("=" * 70)

processor = ZoteroProcessor()

# 测试用例1：标准格式
print("\n✅ 测试1: 标准格式 - 多个标签")
test1 = {
    "title": "Test Paper 1",
    "tags": [
        {"tag": "cat Social Media Security"},
        {"tag": "cat Humor Generation"},
        {"tag": "cat Sentiment Analysis"}
    ]
}
paper1 = processor.process_meta_data(test1)[0]
expected1 = "Social Media Security;Humor Generation;Sentiment Analysis"
status1 = "✓" if paper1.category == expected1 else "✗"
print(f"   {status1} 结果: '{paper1.category}'")
print(f"   {status1} 预期: '{expected1}'")
print(f"   {status1} 类型: {type(paper1.category).__name__}")

# 测试用例2：分号分隔格式
print("\n✅ 测试2: 分号分隔格式 - 单个标签")
test2 = {
    "title": "Test Paper 2",
    "tags": [
        {"tag": "cat Social Media Security;Humor Generation;Sentiment Analysis"}
    ]
}
paper2 = processor.process_meta_data(test2)[0]
expected2 = "Social Media Security;Humor Generation;Sentiment Analysis"
status2 = "✓" if paper2.category == expected2 else "✗"
print(f"   {status2} 结果: '{paper2.category}'")
print(f"   {status2} 预期: '{expected2}'")

# 测试用例3：混合格式
print("\n✅ 测试3: 混合格式")
test3 = {
    "title": "Test Paper 3",
    "tags": [
        {"tag": "cat Social Media Security"},
        {"tag": "cat Humor Generation;Sentiment Analysis"},
        {"tag": "regular tag"},
        {"tag": "cat Misinformation Analysis"}
    ]
}
paper3 = processor.process_meta_data(test3)[0]
expected3 = "Social Media Security;Humor Generation;Sentiment Analysis;Misinformation Analysis"
status3 = "✓" if paper3.category == expected3 else "✗"
print(f"   {status3} 结果: '{paper3.category}'")
print(f"   {status3} 预期: '{expected3}'")

# 测试用例4：空分类
print("\n✅ 测试4: 空分类")
test4 = {
    "title": "Test Paper 4",
    "tags": [{"tag": "keyword1"}, {"tag": "keyword2"}]
}
paper4 = processor.process_meta_data(test4)[0]
expected4 = ""
status4 = "✓" if paper4.category == expected4 else "✗"
print(f"   {status4} 结果: '{paper4.category}'")
print(f"   {status4} 预期: '{expected4}'")

# 测试用例5：去重功能
print("\n✅ 测试5: 去重功能")
test5 = {
    "title": "Test Paper 5",
    "tags": [
        {"tag": "cat Social Media Security"},
        {"tag": "cat Social Media Security"},
        {"tag": "cat Humor Generation"},
        {"tag": "cat Social Media Security"}
    ]
}
paper5 = processor.process_meta_data(test5)[0]
expected5 = "Social Media Security;Humor Generation"
status5 = "✓" if paper5.category == expected5 else "✗"
print(f"   {status5} 结果: '{paper5.category}'")
print(f"   {status5} 预期: '{expected5}'")

# 验证分割功能（GUI会使用）
print("\n✅ 测试6: 验证分割功能（GUI兼容性）")
if paper1.category:
    categories_list = paper1.category.split(";")
    print(f"   ✓ 分割成功: {categories_list}")
    print(f"   ✓ 分类数量: {len(categories_list)}")
    print(f"   ✓ 第一个分类: '{categories_list[0]}'")
else:
    print(f"   ✗ 分割失败")

# 总结
print("\n" + "=" * 70)
all_passed = all([
    paper1.category == expected1,
    paper2.category == expected2,
    paper3.category == expected3,
    paper4.category == expected4,
    paper5.category == expected5
])

if all_passed:
    print("🎉 所有测试通过！分类提取功能正常工作")
    print("\n关键特性:")
    print("  ✓ 分类以分号分隔的字符串形式存储")
    print("  ✓ 支持多个标签和分号分隔")
    print("  ✓ 自动去重")
    print("  ✓ 可通过 .split(';') 转换为列表")
    print("  ✓ 与GUI兼容")
else:
    print("❌ 部分测试失败，请检查实现")

print("=" * 70)
