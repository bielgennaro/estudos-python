velocidade = 61
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carrou_passou_radar1 = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (
    LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar1 and velocidade_carrou_passou_radar1

if velocidade_carrou_passou_radar1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar1:
    print('Carro passou radar 1')

if carro_passou_radar1:
    print('Carro multado em radar 1')
