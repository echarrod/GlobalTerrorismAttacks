import pandas as pd
import config
import sys

import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.ini')

reload(sys)
sys.setdefaultencoding('utf-8') #Required when using python2 with this dataset

newCSVFileName = 'gtd_converted.csv'


# Data Preparation Function
def excel_to_csv():
    filename = config.get('Constants', 'Gtd_filename').strip('""')
    whole = pd.read_excel(filename, encoding='utf-8')
    whole.to_csv(newCSVFileName)


if __name__ == "__main__":
    excel_to_csv()
    print("Successfully converted %s to %s." % (config.get('Constants', 'Gtd_filename'), newCSVFileName)
