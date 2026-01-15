"""
分类配置文件

重要说明：
1. unique_name字段是分类的唯一标识符，不可重复
2. order字段决定分类在Excel和README中的显示顺序，必须唯一
3. enabled=false的分类会被系统忽略，相关论文不会出现在该分类下
"""

CATEGORIES_CONFIG = {
    "config_version": "2.0",
    "last_updated": "2026-01-14",
    
    # 分类列表，按order排序
    "categories": [

        # ============一级分类===============
        {
            "unique_name": "Uncategorized",
            "order": 0,                     # 排序顺序，0为第一个
            "name": "Uncategorized",  # 显示名称
            "primary_category": None,# 所属一级分类，None表示本身为一级分类
            "enabled": True,                # 是否启用该分类
        },
        {
            "unique_name": "Base Techniques",
            "order": 99,                     # 排序顺序，0为第一个
            "name": "Base Techniques",  # 显示名称
            "primary_category": None,# None表示本身为1级分类
            "enabled": True,                # 是否启用该分类
        },
        {
            "unique_name": "Perception and Classification",
            "order": 100,                     # 排序顺序，0为第一个
            "name": "Perception and Classification",  # 显示名称
            "primary_category": None,# None表示本身为1级分类
            "enabled": True,                # 是否启用该分类
        },
        {
            "unique_name": "Cognition and Generation",
            "order": 101,                     # 排序顺序，0为第一个
            "name": "Cognition and Generation",  # 显示名称
            "primary_category": None,# None表示本身为1级分类
            "enabled": True,                # 是否启用该分类
        },
        {
            "unique_name": "Simulation and Deduction",
            "order": 102,                     # 排序顺序，0为第一个
            "name": "Simulation and Deduction",  # 显示名称
            "primary_category": None,# None表示本身为1级分类
            "enabled": True,                # 是否启用该分类
        },
        {
            "unique_name": "Social Media Security",
            "order": 103,                     # 排序顺序，0为第一个
            "name": "Social Media Security",  # 显示名称
            "primary_category": None,# None表示本身为1级分类
            "enabled": True,                # 是否启用该分类
        },
        {
            "unique_name": "Other",
            "order": 200,
            "name": "Other",
            "primary_category": None,# None表示本身为1级分类
            "enabled": True,
        },
        
        # ============二级分类===============
        {
            "unique_name": "Hate Speech Analysis",
            "order": 1,                     
            "name": "Hate Speech Analysis",  # 显示名称
            "primary_category": 100,# 所属一级分类，用一级分类的order表示
            "enabled": True,                # 是否启用该分类
        },
        {
            "unique_name": "Sentiment Analysis",
            "order": 2,
            "name": "Sentiment Analysis",
            "primary_category": 100,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Misinformation Analysis",
            "order": 3,
            "name": "Misinformation Analysis",
            "primary_category": 100,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Multimodal Analysis",
            "order": 4,
            "name": "Meme Analysis",
            "primary_category": 100,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Steganography Detection",
            "order": 5,
            "name": "Steganography Detection",
            "primary_category": 100,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Event Extraction",
            "order": 6,
            "name": "Event Extraction",
            "primary_category": 100,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Topic Modeling",
            "order": 7,
            "name": "Topic Modeling",
            "primary_category": 101,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "User Opinion Mining",
            "order": 8,
            "name": "User Opinion Mining",
            "primary_category": 100,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "User Profiling",
            "order": 9,
            "name": "User Profiling",
            "primary_category": 101,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "User Behavior Prediction",
            "order": 10,
            "name": "User Behavior Prediction",
            "primary_category": 100,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Social Content Generation",
            "order": 11,
            "name": "Social Content Generation",
            "primary_category": 101,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Information Diffusion Analysis",
            "order": 12,
            "name": "Information Diffusion Analysis",
            "primary_category": 102,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Macrosocial Phenomena Analysis",
            "order": 13,
            "name": "Macrosocial Phenomena Analysis",
            "primary_category": 102,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Social Simulation",
            "order": 14,
            "name": "Social Simulation",
            "primary_category": 102,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Malicious Bot Detection",
            "order": 15,
            "name": "Malicious Bot Detection",
            "primary_category": 100,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Community Detection",
            "order": 16,
            "name": "Community Detection",
            "primary_category": 100,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Dynamic Community Analysis",
            "order": 17,
            "name": "Dynamic Community Analysis",
            "primary_category": 102,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },
        {
            "unique_name": "Social Psychological Phenomena Analysis",
            "order": 18,
            "name": "Social Psychological Phenomena Analysis",
            "primary_category": 101,# 所属一级分类，用一级分类的order表示
            "enabled": True,
        },

    ]
}

# 验证函数
def validate_categories_config():
    """
    验证分类配置的有效性
    
    返回: (是否有效, 错误信息列表)
    """
    errors = []
    
    # 检查unique_name唯一性
    unique_names = {}
    for category in CATEGORIES_CONFIG["categories"]:
        unique_name = category.get("unique_name")
        if unique_name is None:
            errors.append(f"分类缺少unique_name字段: {category}")
            continue
            
        if unique_name in unique_names:
            errors.append(f"unique_name {unique_name} 重复")
        else:
            unique_names[unique_name] = True
    
    # 检查order唯一性，并建立order->category映射
    orders = {}
    categories_by_order = {}
    for category in CATEGORIES_CONFIG["categories"]:
        order = category.get("order")
        if order is None:
            errors.append(f"分类 {category.get('unique_name')} 缺少order字段")
            continue
            
        if order in orders:
            errors.append(f"order {order} 重复: {orders[order]} 和 {category['unique_name']}")
        else:
            orders[order] = category["unique_name"]
            categories_by_order[order] = category
    
    # 检查 primary_category 合法性：
    # - 一级分类（primary_category 为 None）只能为 None
    # - 二级分类（primary_category 非 None）必须引用存在的一级分类（用 order 表示），且被引用的分类的 primary_category 必须为 None
    for category in CATEGORIES_CONFIG["categories"]:
        pc = category.get("primary_category", None)
        if pc is None:
            # 本身为一级分类，确保显式为 None（允许缺失或 None）——已满足
            continue
        # 如果 primary_category 非 None，则应为整数并且存在于 categories_by_order
        if not isinstance(pc, int):
            errors.append(f"分类 {category.get('unique_name')} 的 primary_category 应为一级分类的 order(int)，当前为 {pc!r}")
            continue
        if pc not in categories_by_order:
            errors.append(f"分类 {category.get('unique_name')} 的 primary_category {pc} 不存在")
            continue
        parent = categories_by_order[pc]
        if parent.get('primary_category') is not None:
            errors.append(f"分类 {category.get('unique_name')} 的 primary_category {pc} 指向的不是一级分类 ({parent.get('unique_name')})")

    # 检查name不为空
    for category in CATEGORIES_CONFIG["categories"]:
        name = category.get("name", "").strip()
        if not name:
            errors.append(f"分类 {category.get('unique_name')} 的name不能为空")
    
    return len(errors) == 0, errors

# 配置验证
if __name__ == "__main__":
    is_valid, error_list = validate_categories_config()
    if is_valid:
        print("✅ 分类配置验证通过")
    else:
        print("❌ 分类配置验证失败:")
        for error in error_list:
            print(f"   - {error}")
        exit(1)