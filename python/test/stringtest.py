s =  "A1A2A3"

g = []

for x in s:
    if x.isdigit():
	    g.append(x)
print("".join(g))