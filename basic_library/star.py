
# * 接任意多個輸入 包成tuple
print("test one : *")
text_batch1 = tuple(["I love Pixar.", "I don't care for Pixar.", "batch1"])
text_batch2 = tuple(["I love Pixar.", "I don't care for Pixar.", "batch2"])
def tt(*ttt):
    print(ttt)
    print(list(zip(*ttt)))
    print(zip(*ttt))
tt(text_batch1,text_batch2)


#
print("\n test two : *")
a1 = (1,2,3)
print(a1)
print(*a1)

print("\n test three : *")
a2 = ((1,2),(3,4),(5,6))
print(a2)
print(*a2)




# ** 接任意多個輸入 包成dic
print("\ntest one : **")
def ttt(**ttt):
    print(ttt)

dictest = {'a':123, 'b':321}
ttt(a = "123", b="321")


print("\ntest two : **:")
def tttt(aa=None,bb=None):
    print(aa)
    print(bb)
b = {'aa': '123', 'bb': '321'}
tttt(**b)
