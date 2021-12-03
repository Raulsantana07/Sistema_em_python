#### Ajuda ao usuário ####
print('Auxilio ao usuário:')
print('Sistema para calculo de um ângulo qualquer, trazendo o resultado de SENO,COSSENO E TANGENTE')
print('Digitar o ângulo em grau, exemplo 45º, digita-se no sistema 45')

### funcionamento do sistema ###
import math
an = float(input('Digite o ângulo que deseja calcular:'))
seno = math.sin(math.radians(an))
print(' O ângulo de {}, tem o SENO de {:.2f}'.format(an, seno))
cos = math.cos(math.radians(an))
print(' O ângulo de {}, tem o COSSENO de {:.2f}'.format(an, cos))
tang = math.tan(math.radians(an))
print(' O ângulo de {}, tem a TANGENTE de {:.2f}'.format(an, tang))

exit()
