import ccxt
import schedule
import pandas as pd
from telegram.ext.updater import Updater
import warnings
from datetime import datetime
import time
import ta.volatility as ta_vo
import numpy as np

pd.set_option('display.max_rows', None)
desired_width = 320

pd.set_option('display.width', desired_width)

np.set_printoptions(linewidth=desired_width)

pd.set_option('display.max_columns', 10)
warnings.filterwarnings('ignore')

exchange = ccxt.okx({
    'api_key': "5b97a4e2-3c4c-474a-897c-6419b11dbe40",
    'secret': "99ED30747127932E65BE5D573B44B5A0",
    'password': "LD2KAShd3a8qjah@",
    'Permissions': "ReadTrade"
})
updater = Updater('5165684199:AAF9h9lm9GMktnnerdUgIwcALt8V0om8tKw', use_context=True)
dispatcher_ = updater.dispatcher
in_position = False
in_uptrend = False
def run_bot():
    global in_position, in_uptrend
    print(" ------------------------------------- START ----------------------------------------- ")
    print(f"Fetching new bars for {datetime.now().isoformat()}")
    bars = exchange.fetch_ohlcv('BTC/USDT', timeframe='15m', limit=1)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    print(df['volume'][0], df['open'][0], df['close'][0])
    if df['volume'][0] >= 200 and df['open'][0] < df['close'][0]:
        updater.bot.sendMessage(chat_id='-658043138', text="high volume alert  \n current volume : "+str(df['volume'][0]))
        print(" -------------------------------------- END -------------------------------------------- ")


schedule.every(30).seconds.do(run_bot)

while True:
    schedule.run_pending()
    time.sleep(1)
