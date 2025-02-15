import os

from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv('ALIM_API_KEY')
api_secret = os.getenv('ALIM_API_SECRET')

protocol = os.getenv('PROTOCOL', 'https')  
domain = os.getenv('DOMAIN', 'api.solapi.com')  
prefix = os.getenv('PREFIX', '')

# URL 생성 함수
def get_url(path):
    url = f"{protocol}://{domain}"
    if prefix:
        url += prefix
    return url + path



# import configparser
# lib_dir = os.path.dirname(__file__)
# env_config = configparser.ConfigParser()
# env_config.read(lib_dir + '/config.ini')

# api_key = env_config['AUTH']['api_key']
# api_secret = env_config['AUTH']['api_secret']
# protocol = env_config['SERVER']['protocol']
# domain = env_config['SERVER']['domain']
# prefix = env_config['SERVER']['prefix'] and env_config['SERVER']['prefix'] or ''


# def get_url(path):
#     url = '%s://%s' % (protocol, domain)
#     if prefix != '':
#         url = url + prefix
#     url = url + path
#     return url
