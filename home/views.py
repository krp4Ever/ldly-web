 # -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
from django.contrib.staticfiles.templatetags.staticfiles import static
def index(request):
	return render_to_response('home/index.html',{
        'sliderContent': [
            {
                'img':static('images/content/slider_pic1.jpg'),
                'desc':'推进国际产能和装备制造合作，是保持我国经济中高速增长和迈向中高端 水平的重大举措'
            },
            {
                'img':static('images/content/slider_pic2.jpg'),
                'desc':'推进国际产能和装备制造合作，是保持我国经济中高速增长和迈向中高端 水平的重大举措'
            }
        ],
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
