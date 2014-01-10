# -*- coding: utf-8 -*-
"""
 ***All Rights Reserved
 @author frankiezhu
 @data 20140106
 ***
"""
###################################CONFIG START##################################

#账户信息
#user='frankiezhu@foxmail.com'
user='frankiezhu@foxmail.com'
passwd='sky123'

#想买的车次,为空的话会进入交互阶段，需要手动输入车次,建议设置上
g_buy_list =  ["K1017", "K729",]

#忽略的车次
g_ingnore_list = []


#买票查询条件：时间、站点
g_query_data = [
             ("leftTicketDTO.train_date", "2014-01-28"),
             ("leftTicketDTO.from_station", "SZQ"),
             ("leftTicketDTO.to_station", "JJG"),
             ("purpose_codes", "ADULT"),
            ]
#乘客信息
g_passengers = [
                {
                "name": u"孙敬",
                "id": "42112719900715085X",
                "tel": "13430680458",
                },             
            ]

'''
g_str_seat_types = {
                    "gg_num":u"GG类型",  
                    "gr_num":u"高级软卧",#6 
                    "qt_num":u"QT类型",
                    "rw_num":u"软卧",   #4 
                    "rz_num":u"软座",   #2
                    "tz_num":u"特等座", #P
                    "wz_num":u"无座",  #WZ
                    "yb_num":u"YB类型", 
                    "yw_num":u"硬卧",   #3 
                    "yz_num":u"硬座",   #1
                    "ze_num":u"二等座", #O
                    "zy_num":u"一等座", #M
                    "swz_num":u"商务座",#9
            }
'''
#座位类型,类型名在g_str_seat_types里有对应
g_care_seat_types = ["yz_num", "rw_num", "yw_num", "wz_num"]

#自动识别验证码次数，验证码无重叠无背景时候识别率高，基于tesseract的OCR
#目前仅仅遇到过一次，几个小时，dns更新后连接到的服务器有背景干扰
#可以找到这种服务器并修改host让其一直连接此服务器
#或者做更多的图像相关处理，去除噪点再做OCR
g_max_auto_times = 0

#刷新间隔
g_query_sleep_time = 0.6

###################################End##################################


