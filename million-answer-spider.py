# -*- coding: utf-8 -*-
# 本脚本实现 收集百万英雄 历次答题的题库
# writed by Zhengxuan Zhang
# More visit  http://blog.mindcont.com
#

import requests
import json
from datetime import datetime
import urllib
import codecs
import sys
import re
import time
import urlparse


reload(sys)
sys.setdefaultencoding('utf-8')

def getAndSave():

    # file =codecs.open("百万英雄题库.txt","a+","utf-8")
    saveName = "百万英雄题库-" + datetime.now().strftime("%Y%m%d") + ".txt"
    file =codecs.open(saveName,"w","utf-8")
    host = 'http://answer.sm.cn/answer/detail?format=json&activity=million'

    for sid_num in range(18,300):
        url = host + '&sid=' + str(sid_num)
        rawData = requests.post(url)
        mjson = json.loads(rawData.text)
        question = mjson['data']['question']

        if question:
            print "now spider location: " + url
            # print rawData.text
            q_info = mjson['data']['info']

            # 保存日期、场次、奖金池信息
            print >>file, "2018年".decode("utf-8") + q_info['date']+ '\t' + q_info['order'] +' '+ q_info['reward']
            print >>file, "===================================================="

            # 遍历 12个问题及其答案
            for q_id in range(0,len(question)):
                q_question_answer = question[q_id]['answer']

                # 由于个性化题目存在多个答案，需要根据特定情况调整输出后，再保存到txt
                if isinstance(q_question_answer, list):
                    person_anwser = ''
                    for person_num in range(0,len(q_question_answer)):
                         person_anwser += q_question_answer[person_num] + "、"
                    # print person_anwser[:-1]
                    print >>file, str(question[q_id]['id']) + '\t' + question[q_id]['title'] + '\t' + person_anwser[:-1]

                else:
                    print >>file, str(question[q_id]['id']) + '\t' + question[q_id]['title'] + '\t' + q_question_answer

            print >>file, "====================================================" +'\n'

    file.close()
    print 'done!'

if __name__ == '__main__':

    getAndSave()
