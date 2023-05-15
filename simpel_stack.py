stack = [1,2,3,4,5]
print('tumpukan sekarang',stack)

stack.append(6)
print('tumpukan masuk:',6)
print('tumpukan sekarang:',6)

stack.append(6)
print('tumpukan masuk:',7)
print('tumpukan sekarang:',6)

out = stack.pop()
print('tumpukan keluar:',out)
print('tumpukan sekarang:',stack)