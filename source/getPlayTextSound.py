# getPlayTextSound
# 利用百度云AI服务进行语音合成播报(一般来说，第三方提供的云AI服务超过一定调用频率会收取一定的费用)


from aip import AipSpeech
from playsound import playsound

def getPlayText(text):
    """ 直接拷贝百度申请注册的 APPID API_KEY SECRET_KEY """
    APP_ID = '19610626'
    API_KEY = 'm8ayfZMs7yQtVXAK3QH3Ywl4'
    SECRET_KEY = 'R4z6xOhCy3x5pmsbkFwy7r9hM1r6VeNX'

    #初始化百度云服务客户端
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 进行文字转语音 ，设置语音、语速、男声女声
    result = client.synthesis(text,    #text: 合成的文本,使用UTF-8编码,请注意文本长度必须小于1024字节
                               'zh',    ## lang: 语言，中文:zh 英文:en
                               1,       # 用户唯一标志号，目前写1
                               {'per':0,  # 发音人选择,0为女生，1为男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
                                'vol':15,  # 合成音频文件的准音量
                                'pit':9,   # 语调音调,取值0-9,默认为5 中语调
                                'spd':5   # 语速 取值0-9，默认为5 中语速
                                }
                               )


    # 识别正确返回语音二进制 错误则返回dict
    if not isinstance(result, dict):
        with open('.\data\empChecked.mp3', 'wb') as f:
            f.write(result)
            f.close()


    # 播放转换后的语音文件
    playsound(".\data\empChecked.mp3")
