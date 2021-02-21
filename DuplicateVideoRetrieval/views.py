from django.shortcuts import render


def runoob(request):
    views_list = ['wx-视屏相关性检索', '2333', '33444', '5566']
    import datetime
    now = datetime.datetime.now()  # 访问时间
    views_goRunoob = "<a href='http://www.runoob.com/'>菜鸟教程</a>"
    return render(request, 'runoob.html', {"views_list": views_list, "time": now, "runoob": views_goRunoob})


def textExtend(request):
    return render(request, 'testextend.html')
