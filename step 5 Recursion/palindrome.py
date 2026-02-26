def pal(p):
    if len(p) <= 1:
        return True
    if p[0] == p[-1]:
        return pal(p[1:-1])
    else:
        return False
    
def pal2(p):
    if len(p) <= 1:
        return True
    return p[0] == p[-1] and pal2(p[1:-1])

print(pal("madamz"))
print(pal2("madamz"))
pall = "madam"
print(pall[1:-1])