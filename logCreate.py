"""
create data logs for testing
"""
from datetime import datetime
import datetime
# from datetime import datetime

def data_time_decor(f):
	msg_datatime = f.strftime('%Y/%m/%d %H:%M:%S')
	return msg_datatime

def create_write_log(logs_text):
    date = datetime.date.today()
                                              #time = data_time_decor(datetime.now()) ERROR
    try:
        logs = open('{} .txt'.format(  date))
        logs.write(logs_text)
        logs.close()
    except (OSError, IOError):

        logs = open('{} .txt'.format( date), 'w')
        logs.write(logs_text)
        logs.close()
    return logs_text
logs_text = """33.[2020.03.29 - 17:30:12][WARNING] no signal air_temperature_sensor
34.[2020.03.29 - 16:30:21][WARNING] no signal water_temperature_sensor
35.[2020.03.29 - 16:30:33][WARNING] no signal ground_temperature_sensor
36.[2020.03.29 - 16:31:22][UnNORM]  low or high signal water_temperature_sensor
37.[2020.03.29 - 16:31:25][UnNORM]  low or high signal air_temperature_sensor
38.[2020.03.29 - 16:31:44][UnNORM]  low or high signal ground_temperature_sensor
39.[2020.03.29 - 16:35:34][ERROR]  no connection
40.[2020.03.29 - 16:36:23][WARNING] no signal air_temperature_sensor
41.[2020.03.29 - 16:36:24][WARNING] no signal water_temperature_sensor
42.[2020.03.29 - 17:36:28][WARNING] no signal ground_temperature_sensor
43.[2020.03.29 - 17:38:30][UnNORM]  low or high signal water_temperature_sensor
44.[2020.03.29 - 17:38:34][UnNORM]  low or high signal air_temperature_sensor
45.[2020.03.29 - 17:39:12][UnNORM]  low or high signal ground_temperature_sensor
46.[2020.03.29 - 17:40:23][ERROR]  no connection
47.[2020.03.29 - 17:41:34][WARNING] no signal air_temperature_sensor
48.[2020.03.29 - 17:42:45][WARNING] no signal water_temperature_sensor
49.[2020.03.29 - 17:42:50][WARNING] no signal ground_temperature_sensor
50.[2020.03.29 - 17:43:23][UnNORM]  low or high signal water_temperature_sensor
51.[2020.03.29 - 17:43:34][UnNORM]  low or high signal air_temperature_sensor
52.[2020.03.29 - 17:44:45][UnNORM]  low or high signal ground_temperature_sensor
53.[2020.03.29 - 17:45:23][ERROR]  no connection
54.[2020.03.29 - 17:46:12][WARNING] no signal ground_temperature_sensor
55.[2020.03.29 - 17:46:23][UnNORM]  low or high signal water_temperature_sensor
56.[2020.03.29 - 17:46:34][UnNORM]  low or high signal air_temperature_sensor
57.[2020.03.29 - 17:47:12][WARNING] no signal ground_temperature_sensor
58.[2020.03.29 - 17:47:23][UnNORM]  low or high signal water_temperature_sensor
59.[2020.03.29 - 17:47:34][UnNORM]  low or high signal air_temperature_sensor    
    """
test = create_write_log(logs_text)
