# str = "hello world"
# a = len("hi")
# print(str)

members= {
    'account1':13,
    'account2':12
}
members['account3'] = 14
print(members)
# members.pop('account1')
# print(members)

if 'account1' in members:
    print('account1 在字典中存在')
else:
    print('account1 不在字典中存在')

for account,level in members.items():
    print(f'{account},{level}')

members1 = {
    'account1'  : 13 ,
    'account2'  : 12 ,
    'account3'  : 15 ,
}

another1 =  {
    'account4'  : 13 ,
    'account5'  : 12 ,
}

members1.update(another1)

print(members1)