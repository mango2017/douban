# import save
from save import savetofile,aa
from bb import aa as aa2
fee = input('请输入午餐费用：')
members = input('请输入聚餐人姓名，以英文逗号,分隔：')

# 将人员放入一个列表
memberlist = members.split(',')
# 得到人数
headcount = len(memberlist)

# 计算人均费用
avgfee = int (fee) / headcount
# save.savetofile(memberlist,avgfee)

savetofile(memberlist,avgfee)
aa()
aa2()