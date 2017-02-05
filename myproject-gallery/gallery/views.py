from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from gallery.models import Imginfo
from operator import itemgetter, attrgetter
from gallery.forms import ImgForm,UserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

@csrf_exempt
def cal_date_list():
    img_list = Imginfo.objects.order_by('-year')
    date_list = []
    if len(img_list) > 0:
        for i in img_list:
            if [i.year,i.month] not in date_list:
                date_list.append([i.year,i.month])
        for i in date_list:
            temp = 0;
            for j in img_list:
                if j.year == i[0] and j.month == i[1]:
                    temp += 1
            i.append(temp)
    return date_list

@csrf_exempt
@login_required
def add_img(request):
    date_list = cal_date_list()
    if request.method == 'POST':
        form = ImgForm(request.POST)
        print(1)
        if form.is_valid():
            form.save(commit = True)
            print(2)
            return index(request)
        else:
            context = {
                'form' : form,
                'date_list' : date_list,
            }

            print(form.errors)

    else:
        form = ImgForm()

        context = {
            'form' : form,
            'date_list' : date_list,

        }

    return render(request,'gallery/addimg.html',context)



@csrf_exempt
# Create your views here.
def index(request):

    date_list = cal_date_list()
        # date_list.append([img_list[0].year,img_list[0].month,1])
        # for i in img_list:
        #     length = len(date_list)
        #     for j in range(length):
        #         if ((date_list[j][0] == i.year) and (date_list[j][1] == i.month)):
        #             date_list[j][2] += 1
        #         else:
        #             date_list.append([i.year,i.month,1])
        #             break
        # if [i.year,i.month] not in date_list:

    sorted(date_list,key=itemgetter(0,1))

    # print(date_list)

    # don't need to reorder all the objects
    # reorder_list = []
    #
    # for j in date_list:
    #     list_temp = []
    #     for i in img_list:
    #         if j[0] == i.year and j[1] == i.month:
    #             list_temp.append(i)
    #     reorder_list.append(list_temp)
    #
    #
    context = {
        'info' : date_list,
    }
    return render(request, 'gallery/index.html',context)

@login_required
@csrf_exempt
def viewimg(request,year,month):
    path = request.path
    print(path)
    path = path.split('/')
    # ['','gallery','viewimg','2016','11','']
    yearinfo = path[-3]
    monthinfo = path[-2]
    print(yearinfo,monthinfo)
    img_list = Imginfo.objects.filter(year = yearinfo,month = monthinfo)
    date_list = cal_date_list()

    context = {
        'img_list': img_list,
        'date_list': date_list,
    }
    # should have at least one img because the first one
    return render(request, 'gallery/viewimg.html', context)

@login_required
@csrf_exempt
def detail(request):
    path = request.path
    path = path.split('/')
    url = "http://" + "/".join(path[6:])
    print(path,url)
    img = Imginfo.objects.filter(qiniu_url = url)
    print(len(img))
    date_list = cal_date_list()
    context = {
        'img' : img,
        'date_list': date_list,
    }

    return render(request, 'gallery/detail.html', context)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password,"哈哈哈哈")
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                print('pass')
                return HttpResponseRedirect('/gallery/')

            else:
                print("deactive")


        else:
            print("invalid login details!",username,password)
            return HttpResponse("invalid login")

    else:
        print("not post")
        return render(request,'gallery/login.html',{})

@csrf_exempt
@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/gallery/')
# @csrf_exempt
# def restricted(request):
#     return HttpResponse("Since you're logged in, you can see this text!")
#
