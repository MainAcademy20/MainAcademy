"""
create data settings for testing
"""

def create_write_setings(sets_text):


    try:
        sets = open('Settings.txt', '+w',)
        sets.write(str(sets_text))
        sets.close()
    except (OSError, IOError):

        sets = open('Settings.txt', '+r')
        sets.read()
        sets.close()
    return sets




air_temp_min = 'air_temp_min'
air_temp_max = 'air_temp_max'
water_temp_min = 'water_temp_min'
water_temp_max = 'water_temp_max'
ground_temp_min = 'ground_temp_min'
ground_temp_max = 'ground_temp_max'
lightOn = 'LightOn'
waterOn = 'WaterOn'                                     #может лучше было Диктами сделать : ключ - значение
sets_text = [
                air_temp_min, 0,
                air_temp_max, 0,
                water_temp_min, 0,
                water_temp_max, 0,
                ground_temp_min, 0,
                ground_temp_max, 0,
                lightOn, False,
                waterOn, False
            ]

test = create_write_setings(sets_text)
# print(sets_text, type(sets_text))
# print(sets_text, type(sets_text))
# print(test,type(test))
# print(sets_text)
#print('##########',sets_text[3][0])
