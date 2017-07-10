import pandas as pd
import config
import sys

reload(sys)
sys.setdefaultencoding('utf-8') #Required when using python2 with this dataset


# Data Preparation Function
def excel_to_csv():
    path = config.gtd_filename
    whole = pd.read_excel(path, encoding='utf-8')
    whole.to_csv('gtd_converted.csv')


if __name__ == "__main__":
    excel_to_csv()
