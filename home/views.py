 # -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render_to_response('home/index.html',{
        'channelList':{
            'title':'国别投资报告',
            'dataArray': [
                {
                    'date': '2016-12-18',
                    'content': '外资法规、投资手续'
                },
                {
                    'date': '2016-12-19',
                    'content': '地理环境、政治环境、社会文化、经济概况'
                },
                {
                    'date': '2016-12-19',
                    'content': '理事会、联盟章程、联盟宣言、批复文件'
                },
                {
                    'date': '2016-12-19',
                    'content': '参与“一带一路”战略的金融、保险企业联盟。'
                }
            ]
        }

    })
