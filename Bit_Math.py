def CLR_BIT(var,bit):
    re=int(int(var) & (~(1<<int(bit))))
    return re
def SET_BIT(var,bit):
    re=int(int(var)|(1<<int(bit)))
    return re
def TOG_BIT(var,bit):
    re=int(int(var)^(1<<int(bit)))
    return re
def GET_BIT(var,bit):
    re=int(((int(var)>>int(bit))&1))
    return re