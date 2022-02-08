'''
    IGOR TEIXEIRA BRASILIANO
    @igortbr
'''

import requests
import time
import tweepy
from datetime import datetime

def get_emojis():
    d = {
    'Cloudy': ['cloud'],
    'Scattered Thunderstorms': ['sun behind rain cloud'],
    'Rain': ['cloud with rain'],
    'Thunderstorm': ,
    'Mostly Sunny': ['sun behind small cloud'],
    'Mostly Clear Night': ['crescent moon','cloud'],
    'Scattered Thunderstorms Night': ['cloud with lightning and rain'],
    'Partly Cloudy': ['sun behind large cloud'],
    'Sunny': ['sun'],
    'Clear Night': ['crescent moon'],
    'Partly Cloudy Night': ['cloud','crescent moon'],
    'Heavy Rain': ['cloud with rain'],
    'Isolated Thunderstorms': ['cloud with lightning and rain','sun']
    }


def requisicao():
    url = 'https://weather.com/pt-BR/clima/hoje/l/e86aa3b42b7b0b66dd22be0fe50322a1c482da521465cbfefda27fb98062c2ba'
    res = requests.get(url)

    html_page = res.text
    # HTML PAGE ME DEVOLVE A PÁGINA INTEIRA EM HTML
    '''
    <!doctype html><html dir="ltr" lang="pt-BR"><head>
      <meta data-react-helmet="true" charset="utf-8"/><meta data-react-helmet="true" name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"/><meta data-react-helmet="true" name="robots" content="max-image-preview:large"/><meta data-react-helmet="true" name="robots" content="index, follow"/><meta data-react-helmet="true" name="referrer" content="origin"/><meta data-react-helmet="true" name="description" content="Alertas climáticos para hoje e para a noite, condições climáticas e radar Doppler para Viçosa, Minas Gerais do The Weather Channel e Weather.com"/><meta data-react-helmet="true" name="msapplication-TileColor" content="#ffffff"/><meta data-react-helmet="true" name="msapplication-TileImage" content="/daybreak-today/assets/ms-icon-144x144.d353af.png"/><meta data-react-helmet="true" name="theme-color" content="#ffffff"/><meta data-react-helmet="true" property="og:title" content="Condições e previsões climáticas para Viçosa, Minas Gerais - The Weather Channel | Weather.com"/><meta data-react-helmet="true" property="og:image" content="https://s.w-x.co/240x180_twc_default.png"/><meta data-react-helmet="true" property="og:image:url" content="https://s.w-x.co/240x180_twc_default.png"/><meta data-react-helmet="true" property="og:image:secure_url" content="https://s.w-x.co/240x180_twc_default.png"/><meta data-react-helmet="true" property="og:site_name" content="The Weather Channel"/><meta data-react-helmet="true" property="og:type" content="article"/><meta data-react-helmet="true" property="og:locale" content="pt_BR"/><meta data-react-helmet="true" property="og:description" content="Alertas climáticos para hoje e para a noite, condições climáticas e radar Doppler para Viçosa, Minas Gerais do The Weather Channel e Weather.com"/><meta data-react-helmet="true" property="og:url" content="https://weather.com/pt-BR/clima/hoje/l/Viçosa+Minas+Gerais?canonicalCityId=cf65fe754e97c453fe9b96b586705ba08a8f217ceb288e81f09e35e3a5d6f244"/>
      . . . 
             if (registration.active && registration.active.scriptURL && registration.active.scriptURL.endsWith('weather.com/sw.js')) {
              registration.unregister();
            }
          }
        });
      });
    }</script><div id="dpr-manager"></div></body></html>
    '''

    return html_page

# devolve uma lista com 4 temperaturas: [manhã, tarde, noite, madrugada]
def get_temperaturasDia(soup):
    # div onde fica a temperatura do dia
    div = soup.find('div', {'class':'TodayWeatherCard--TableWrapper--2kEPM'}) 

    # lista com as temperaturas do dia
    temps = []
    emoj = []
    for i in div.findChildren('li'):
        temps.append(i.find('span', {'data-testid':'TemperatureValue'}).text)
        emoj.append(i.find('svg', {'data-testid':'Icon'}).text)
    # div.findChildren('li') devolve todos os item da lista de div
    '''
    [<li class=" Column--column--1p659 "><a class="Column--innerWrapper--1vUk1 Column--past--3pX1J Button--default--3zkvy" href="/pt-BR/clima/horaria/l/e86aa3b42b7b0b66dd22be0fe50322a1c482da521465cbfefda27fb98062c2ba" target="_self"><h3 class="Column--label--3QyFS Column--small--3yLq9"><span class="Ellipsis--ellipsis--1sNTm" style="-webkit-line-clamp:2">Manhã</span></h3><div class="Column--temp--5hqI_" data-testid="SegmentHighTemp"><span data-testid="TemperatureValue">23°</span></div><div class="Column--icon--1MoS8 "><svg aria-hidden="true" class="Icon--icon--3wCKh Icon--fullTheme--3ns8p" data-testid="Icon" role="img" set="weather" skycode="26" theme="full" viewbox="0 0 200 200"><title>Cloudy</title><use xlink:href="#svg-symbol-cloud"></use></svg></div><div class="Column--precip--2ck8J" data-testid="SegmentPrecipPercentage"><span class="Column--precip--2ck8J">--</span></div></a></li>,
    <li class=" Column--column--1p659 Column--active--3vpgg "><a class="Column--innerWrapper--1vUk1 Button--default--3zkvy" href="/pt-BR/clima/horaria/l/e86aa3b42b7b0b66dd22be0fe50322a1c482da521465cbfefda27fb98062c2ba" target="_self"><h3 class="Column--label--3QyFS Column--small--3yLq9"><span class="Ellipsis--ellipsis--1sNTm" style="-webkit-line-clamp:2">Tarde</span></h3><div class="Column--temp--5hqI_" data-testid="SegmentHighTemp"><span data-testid="TemperatureValue">24°</span></div><div class="Column--icon--1MoS8 "><svg aria-hidden="true" class="Icon--icon--3wCKh Icon--fullTheme--3ns8p" data-testid="Icon" role="img" set="weather" skycode="38" theme="full" viewbox="0 0 200 200"><title>Scattered Thunderstorms</title><g transform="translate(0 -16)"><use mask="url(#scattered-thunderstorms-mask)" transform="matrix(.56 0 0 .56 11.2 16.8)" xlink:href="#svg-symbol-sun"></use><use transform="matrix(.95 0 0 .95 7.6 5.7)" xlink:href="#svg-symbol-cloud"></use></g><use transform="matrix(.67 0 0 .67 30 61)" xlink:href="#svg-symbol-lightning-bolt"></use><use transform="translate(57 21)" xlink:href="#svg-symbol-drop"></use><use transform="translate(23 43)" xlink:href="#svg-symbol-drop"></use></svg></div><div class="Column--precip--2ck8J" data-testid="SegmentPrecipPercentage"><svg aria-hidden="true" class="Icon--icon--3wCKh Icon--fullTheme--3ns8p" data-testid="Icon" name="precip-rain-single" role="img" set="heads-up" theme="full" viewbox="0 -2 5 10"><title>Rain</title><path d="M4.7329.0217c-.1848-.059-.3855.0064-.4803.148L.2731 5.1191c-.0814.0922-.1501.1961-.196.3108-.2469.6009.1185 1.2697.8156 1.4943.6914.226 1.447-.0712 1.7-.6585L4.9662.4987l.0111-.0282c.073-.1807-.036-.379-.2444-.4488z"></path></svg><span class="Column--precip--2ck8J"><span class="Accessibility--visuallyHidden--2uGW3">Probabilidade de chuva</span>57%</span></div></a></li>,
    <li class=" Column--column--1p659 "><a class="Column--innerWrapper--1vUk1 Button--default--3zkvy" href="/pt-BR/clima/horaria/l/e86aa3b42b7b0b66dd22be0fe50322a1c482da521465cbfefda27fb98062c2ba" target="_self"><h3 class="Column--label--3QyFS Column--small--3yLq9"><span class="Ellipsis--ellipsis--1sNTm" style="-webkit-line-clamp:2">Noite</span></h3><div class="Column--temp--5hqI_" data-testid="SegmentHighTemp"><span data-testid="TemperatureValue">21°</span></div><div class="Column--icon--1MoS8 "><svg aria-hidden="true" class="Icon--icon--3wCKh Icon--fullTheme--3ns8p" data-testid="Icon" role="img" set="weather" skycode="12" theme="full" viewbox="0 0 200 200"><title>Rain</title><use transform="translate(0 -41)" xlink:href="#svg-symbol-cloud"></use><use xlink:href="#svg-symbol-drop"></use><use transform="matrix(1.7 0 0 2 -27 -120)" xlink:href="#svg-symbol-drop"></use><use transform="translate(60)" xlink:href="#svg-symbol-drop"></use></svg></div><div class="Column--precip--2ck8J" data-testid="SegmentPrecipPercentage"><svg aria-hidden="true" class="Icon--icon--3wCKh Icon--fullTheme--3ns8p" data-testid="Icon" name="precip-rain-single" role="img" set="heads-up" theme="full" viewbox="0 -2 5 10"><title>Rain</title><path d="M4.7329.0217c-.1848-.059-.3855.0064-.4803.148L.2731 5.1191c-.0814.0922-.1501.1961-.196.3108-.2469.6009.1185 1.2697.8156 1.4943.6914.226 1.447-.0712 1.7-.6585L4.9662.4987l.0111-.0282c.073-.1807-.036-.379-.2444-.4488z"></path></svg><span class="Column--precip--2ck8J"><span class="Accessibility--visuallyHidden--2uGW3">Probabilidade de chuva</span>86%</span></div></a></li>,
    <li class=" Column--column--1p659 "><a class="Column--innerWrapper--1vUk1 Button--default--3zkvy" href="/pt-BR/clima/horaria/l/e86aa3b42b7b0b66dd22be0fe50322a1c482da521465cbfefda27fb98062c2ba" target="_self"><h3 class="Column--label--3QyFS Column--small--3yLq9"><span class="Ellipsis--ellipsis--1sNTm" style="-webkit-line-clamp:2">A noite</span></h3><div class="Column--temp--5hqI_" data-testid="SegmentHighTemp"><span data-testid="TemperatureValue">20°</span></div><div class="Column--icon--1MoS8 "><svg aria-hidden="true" class="Icon--icon--3wCKh Icon--fullTheme--3ns8p" data-testid="Icon" role="img" set="weather" skycode="12" theme="full" viewbox="0 0 200 200"><title>Rain</title><use transform="translate(0 -41)" xlink:href="#svg-symbol-cloud"></use><use xlink:href="#svg-symbol-drop"></use><use transform="matrix(1.7 0 0 2 -27 -120)" xlink:href="#svg-symbol-drop"></use><use transform="translate(60)" xlink:href="#svg-symbol-drop"></use></svg></div><div class="Column--precip--2ck8J" data-testid="SegmentPrecipPercentage"><svg aria-hidden="true" class="Icon--icon--3wCKh Icon--fullTheme--3ns8p" data-testid="Icon" name="precip-rain-single" role="img" set="heads-up" theme="full" viewbox="0 -2 5 10"><title>Rain</title><path d="M4.7329.0217c-.1848-.059-.3855.0064-.4803.148L.2731 5.1191c-.0814.0922-.1501.1961-.196.3108-.2469.6009.1185 1.2697.8156 1.4943.6914.226 1.447-.0712 1.7-.6585L4.9662.4987l.0111-.0282c.073-.1807-.036-.379-.2444-.4488z"></path></svg><span class="Column--precip--2ck8J"><span class="Accessibility--visuallyHidden--2uGW3">Probabilidade de chuva</span>79%</span></div></a></li>]
    '''

    # preciso pegar esse <span data-testid="TemperatureValue">
    # então para cada item de div.findChildren('li'), pego os valores das tags <span> que têm classe 'TemperatureValue'
    '''
    print('Manhã:', temps[0])
    print('Tarde:', temps[1])
    print('Noite:', temps[2])
    print('Madrugada:', temps[3])
    '''
    
    return temps, emoj

def get_temperaturaAtual(soup):
    div = soup.find('div',{'class':'CurrentConditions--columns--3KgfN'})

    temp = div.find('span',{'data-testid':'TemperatureValue'}).text
    status = div.find('div',{'data-testid':'wxPhrase'}).text

    return temp, status

def fazTweet(temp,status=None,s=''):
    # se for maior que 1, são as temperaturas do dia
    if isinstance(temp,list):
        dias = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
        hoje = datetime.today()
        twitter_API.update_status('Previsões ' + str(hoje.day) + '/' + str(hoje.month) + '/' + str(hoje.year) + ', ' + dias[hoje.weekday()]
        + '\n Manhã: ' + temp[0] + '\n Tarde: ' + temp[1] + '\n Noite: ' + temp[2] + '\n Madrugada: ' + temp[3])
    
    else: # temperatura atual
        hora = datetime.now()
        twitter_API.update_status('Agora ' + str(hora.hour - 3) + ':' + str(hora.minute) + ' ' + str(hoje.day) + '/' + str(hoje.month) + '/' + str(hoje.year)
        + '\n' + s + temp + ' - ' + status)
        


html_page = requisicao()
soup = BeautifulSoup(html_page, 'html.parser')
while (true):
    #if (datetime.now().hour - 3) == 7:
    temperaturas_dia, status_atual = get_temperaturasDia(soup)
    fazTweet(temperaturas_dia,status_atual)

    time.sleep(7200) # acorda 9hrs

    temperatura_atual, status_atual = get_temperaturaAtual(soup)
    fazTweet(temperatura_atual,status_atual)

    time.sleep(7200) # acorda 11hrs
    temperatura_atual, status_atual = get_temperaturaAtual(soup)
    fazTweet(temperatura_atual,status_atual,s='Previsão para pegar comida no RU\n')

    time.sleep(7200) # acorda 13
    temperatura_atual, status_atual = get_temperaturaAtual(soup)
    fazTweet(temperatura_atual,status_atual,s='Previsão para tarde\n')

    time.sleep(18000) # acroda 18hrs
    temperatura_atual, status_atual = get_temperaturaAtual(soup)
    fazTweet(temperatura_atual,status_atual,s='Previsão para noite\n')

    time.sleep(468000)
