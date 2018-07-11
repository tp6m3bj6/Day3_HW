#  carbon_foot
print('r_bus=',0.03,end='/')
print('r_car=',0.24,end='/')
print('r_moto=',0.06)

def maker(n):
    def action(x):
        return n*x
    return action


way=maker(0.03)
print('carbion_foot of bus is ',way(100))

way=maker(0.24)
print('carbion_foot of car is ',way(100))

way=maker(0.06)
print('carbion_foot of moto is ',way(100))