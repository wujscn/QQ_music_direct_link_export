import QQ

import QQ


qq = QQ.QQ()


# 搜索
search_result = qq.search('李健')
print(search_result)
# 解析
audio_url = qq.get_audio_url('001Liwq92gKerW', '320')
print(audio_url)
# ###
# http://streamoc.music.tc.qq.com/M800001Liwq92gKerW.mp3?vkey=17E517E90215EB25F6DD717CE479C6E9573EB9505EA633F4909A32725B490ACDF5A934BB8674363A90C8C076104C2412E6FCADCF58FB5DC0&guid=DreamWalkerXZ&uin=123456&fromtag=8
# ###