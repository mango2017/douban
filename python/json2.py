import json
historyTransactions = [
    {
        'time'   : '20170101070311',  # 交易时间
        'amount' : '3088',            # 交易金额
        'productid' : '45454455555',  # 货号
        'productname' : 'iphone7'     # 货名
    },
    {
        'time'   : '20170101050311',  # 交易时间
        'amount' : '18',              # 交易金额
        'productid' : '453455772955', # 货号
        'productname' : '奥妙洗衣液'   # 货名
    }

]
#对象转json字符串
jsonstr  = json.dumps(historyTransactions,ensure_ascii=False,indent=4)
print(type(jsonstr))
print(type(historyTransactions))
#json字符串转对象
a = json.loads(jsonstr)
print(type(a))