import copy

# 原始列表
original_list = [1, 2, [3, 4]]

# 浅拷贝
shallow_copy = copy.copy(original_list)
print("浅拷贝：", shallow_copy)

# 修改原始列表中的子列表
original_list[2][0] = 99
print("修改后的原始列表：", original_list)
print("浅拷贝后的对象：", shallow_copy)

original_list[0]=100
print("修改后的原始列表：", original_list)
print("浅拷贝后的对象：", shallow_copy)
# 修改原始列表中子列表的子元素
original_list[2][1] = 88
print("再次修改后的原始列表：", original_list)
print("浅拷贝后的对象：", shallow_copy)

# 深拷贝
deep_copy = copy.deepcopy(original_list)
print("深拷贝：", deep_copy)

# 修改原始列表中的子列表
original_list[2][0] = 77
print("修改后的原始列表：", original_list)
print("深拷贝后的对象：", deep_copy)

# 修改原始列表中子列表的子元素
original_list[2][1] = 66
print("再次修改后的原始列表：", original_list)
print("深拷贝后的对象：", deep_copy)

original_list[1] = 66
print("再次修改后的原始列表：", original_list)
print("深拷贝后的对象：", deep_copy)