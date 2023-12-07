import os
import sys
import json
from base_logger import logger

def update_settings_file(data: dict):
    try:
        with open(settings_file, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            logger.info('settings.json updated successfully.')
    except Exception as e:
        logger.error(e)
        raise (f'[ERROR] {e}')


def read_settings_file():
    try:
        with open(settings_file, 'r') as f:
            data = json.load(f)
            for d in data:
                if data[d] in ("", " ", []):
                    logger.exception(
                        f"No value in \'{d}\' of settings.json file.")
                    raise json.JSONDecodeError("", "", 0)
            return data
    except FileNotFoundError:
        with open(settings_file, 'w+', encoding='utf-8') as f:
            json.dump(json.loads(DEFATULT_SETTINGS), f, indent=4)
            f.seek(0)
            logger.info('Restoring default settings.json file.')
            return json.load(f)
    except json.JSONDecodeError:
        logger.exception("settings.json file not readable.")
        os.remove(settings_file)
        return read_settings_file()
    except Exception as e:
        logger.error(e)
        sys.exit()
        

# Airport codes file
try: 
    AIRPORT_CODES_FILE = os.path.join(sys._MEIPASS, 'airport_codes.xls.xlsx')
except: 
    AIRPORT_CODES_FILE ='airport_codes.xls.xlsx'
# Settings file and results directory for CSV file
try:
    settings_file = os.path.join(os.getcwd(), 'settings.json')
    results_path = os.path.join(os.getcwd(), 'results', '')
    os.makedirs(results_path, exist_ok=True)
    # chromedriver_path = os.path.join(os.getcwd(), 'chromedriver', 'chromedriver.exe')
except Exception as e:
    logger.error(e)
    raise (f'{e}')


# GoogleFlights XPATH
XP_AIRPORT_CODES = '''//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[3]/span'''
XP_PRICE = '''//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span'''
XP_COMPANY = '''//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[2]/div[2]'''
XP_TYPE = '''//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[6]/div[2]'''
XP_DURATION = '''//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[3]/div'''
XP_STOPS = '''//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div[4]/div[1]/span'''
XP_CLICK_FIRST_SORTED = '''//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]'''
XP_NOT_FOUND = '''//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/p[1]'''
XP_NOT_FOUND_MESSAGE = '''//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/p[2]'''
# Keys and values
XPATH_DICT = { 
    'codes':XP_AIRPORT_CODES,
    'price': XP_PRICE,
    'company':XP_COMPANY,
    'type': XP_TYPE,
    'duration':XP_DURATION,
    'stops':XP_STOPS,
}
XPATH_KEYS = [k for k, v in XPATH_DICT.items()]
XPATH_LIST = [str(v) for v in XPATH_DICT.values()]
# Default settings.json
DEFATULT_SETTINGS = '''
{
    "from": [
        "NAP""
    ],
    "to": [
        "CCU"
    ],
    "outbound": "2023-10-01",
    "delta": 20,
    "flexdays": 4,
    "weekend": false,
    "lastdate": "2024-02-01",
    "fastmode": true,
    "timeout": 10,
}'''

