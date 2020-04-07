"""
reading logs today for statistic and graphics
"""
import datetime

def logs_reading():
    date = datetime.date.today()

    try:
        with open('{} .txt'.format(date), 'r+') as f:
            logs_origin = f.read()
            logs = logs_origin.split('\n')

    except (OSError, IOError):

        logs = str("{} .txt [CNTTOREAD] cant to read ".format(date))

    return logs

def count_event(log_text):
    count_warning = 0
    count_unnorm = 0
    count_error = 0
    for keyword in log_text:

      if 'WARNING' in keyword:
          count_warning += 1  # do something

      elif 'UnNORM' in keyword:
          count_unnorm +=  1
      elif 'ERROR' in keyword:
          count_error += 1
      elif 'CNTTOREAD' in keyword:                  # WARNING!!!!!!!не могу обработать     except (OSError, IOError):

                                                     # logs = str("{} .txt [CNTTOREAD] cant to read ".format(date))
          count_warning = "can't to read "  #переделать
          count_unnorm = "can't to read"
          count_error = "can't to read"
    return  count_warning, count_unnorm, count_error



# log_text = logs_reading()
# log = count_event(log_text)
# warning= 'Кол-во WARNING = {}'.format(count_warning)
# unnorm= 'Кол-во UnNORM = {}'.format(count_unnorm)
# error = 'Кол-во UnNORM = {}'.format(count_error)
# print('-------------',log [0],log [1], log [2] , type(log),log)
#print('=======', log_text, type(log_text))
