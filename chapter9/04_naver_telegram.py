import telegram
import time
import requests
from bs4 import BeautifulSoup as bs

bot = telegram.Bot(token='Telegram:botToken')

res = requests.get('http://naver.com')
soup = bs(res.text, 'lxml')
top_list = soup.select('.PM_CL_realtimeKeyword_rolling span.ah_k')
result = ''
for top in top_list:
    result += top.text
bot.sendMessage(chat_id='17261014', text=result)

