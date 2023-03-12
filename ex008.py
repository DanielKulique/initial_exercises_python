#conversor de unidades


print('Conversor de Metros para Centímetros e Milímetros')
m = float(input('Digite o valor em metros:'))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('O valor de {} metros equivale a \n'
      '{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm' .format(m, km, hm, dam, dm, cm, mm))
