vendas = 17_000
vendas_empresa = 60_000
meta_empresa = 50_000

if vendas > 15_000 and vendas_empresa > meta_empresa:
    bonus= 800

elif vendas > 10_000 and vendas_empresa > meta_empresa:
    bonus= 600

elif vendas > 5_000 and vendas_empresa > meta_empresa:
    bonus = 180
 
else :
     bonus = 0

print("bonus", bonus)
