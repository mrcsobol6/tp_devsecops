import logging.handlers
from dotenv import load_dotenv
import os
import requests
import logging
from datetime import datetime

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

def hide(source: str, target: str):
    return source.replace(target, len(target) * '*')

if os.path.exists('logs'):
    print("Le sous dossier 'logs' existe")
    os.chdir('logs')
    if os.path.isfile('monitor.log'):
        print("Le fichier 'monitor.log existe dans le sous dossier logs.")

exit()

logging.basicConfig(
       level=logging.INFO,
#       format="%(asctime)s [%(levelname)s] %(message)s Data: %(args)s",
       format="%(asctime)s [%(levelname)s] %(message)s",
       handlers=[logging.FileHandler('logs/monitor.log'),
                 #logging.StreamHandler() # Standard Output
       ]
)

logger = logging.getLogger(__name__)
handler = logging.handlers.RotatingFileHandler("logs/monitor.log", maxBytes=2000, backupCount=10)
logger.addHandler(handler)

logging.info('Début du script')

url = os.getenv('API_URL')
status=f"{url}/status?{API_TOKEN}"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

date = datetime.now().strftime('%Y-%m-%d')
json_report = f'reports/{date}-App.json'

try:

    token = os.environ.get("API_TOKEN")
    if not token:
        raise ValueError('Token vide')
        
except KeyError as k:
    logging.error('API_TOKEN non défini dans l\'environnement : %s', k)

try:

    r = requests.get(status, headers=headers, timeout=30)
    json = r.json()
    jsn = open(f"reports/{date}-App.json", 'a+')
    jsn.write(str(json))
    jsn.write('\n')
    logging.info(f"HTTP response from {hide(r.url, API_TOKEN)} with status {r.status_code}")

except ConnectionError as c:

    logging.error(c)

logging.info('Fin du script')
