# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
def yw(s,p):
    findIndex=[]
    ps=sorted(p)
    pl=len(p)
    sl=len(s)
    for i in range(0,sl):
        if ps==sorted(s[i:i+pl]):
            findIndex.append(i)
    return findIndex
print(yw("cbaebabacd","abc"))
