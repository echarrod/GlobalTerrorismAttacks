import pandas as pd
import config
import sys

reload(sys)
sys.setdefaultencoding('utf-8') #Required when using python2 with this dataset

newCSVFileName = 'gtd_converted.csv'

# Data Preparation Function
def excel_to_csv():
    path = config.gtd_filename
    whole = pd.read_excel(path, encoding='utf-8')
    whole.to_csv(newCSVFileName)


if __name__ == "__main__":
    excel_to_csv()
    print "Successfully converted %s to %s." % (config.gtd_filename, newCSVFileName)
