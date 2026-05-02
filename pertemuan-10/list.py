stack = []
stack.append("Pildun 2026")
stack.append("Ronaldo juara")
stack.append("Pildun 2030")
stack.append("wasit barca")

print("Stack: ",stack)

isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

popelement = stack.pop()
print("pop: ",popelement)

topelement = stack[-1]
print("peek: ",topelement)

print("riwayat terbaru: ",stack)

print("Jumlah riwayat: ", len(stack))
