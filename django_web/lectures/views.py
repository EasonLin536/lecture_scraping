from django.shortcuts import render, get_object_or_404, redirect

from .models import Lecture
from .forms import LectureForm

# Create your views here.
def lecture_detail_view(request):
    obj = Lecture.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "lectures/detail.html", context)




def dynamic_lookup_view(request, id):
    # obj = Lecture.objects.get(id=id)
    obj = get_object_or_404(Lecture, id=id)
    context = {
        'object': obj
    }
    return render(request, "lectures/detail.html", context)


def lecture_list_view(request):
    queryset = Lecture.objects.all() #list of objects
    context = {
        'object_list': queryset
    }
    return render(request, "lectures/list.html", context)


# Search keyword in certain column
def search_str(mode, target, lecture_list):
    new_list = []
    for instance in lecture_list:
        tmp = ""
        if mode == 'A':
            tmp = instance.department
        elif mode == 'B':
            tmp = instance.number
        elif mode == 'C':
            tmp = instance.name
        elif mode == 'D':
            tmp = instance.teacher
        elif mode == 'E':
            tmp = instance.time_and_room
        elif mode == 'F':
            tmp = instance.remark

        if tmp != None:
            if tmp.find(target) != -1:
                new_list.append(instance)

    return new_list


# Functions for search time
# Turn 一 to 1 ,etc
def chin_to_num(chin_day):
    if chin_day == "一": return 1
    elif chin_day == "二": return 2
    elif chin_day == "三": return 3
    elif chin_day == "四": return 4
    elif chin_day == "五": return 5
    else: 
        print("Illegal time!")
        return False
    

# Turn 一6,7,8 into [6,7,8]
def extract_time(time_str, day=0):
    if len(time_str) == 1: return ['1','2','3','4','5','6','7','8','9','10','A','B','C','D']
    if day != 0: # Looking for cirtain day
        if day == 1: str = "一"
        elif day == 2: str = "二"
        elif day == 3: str = "三"
        elif day == 4: str = "四"
        else: str = "五"
    
        begin = time_str.find(str)
        end = time_str.find("(", begin)
        time_str = time_str[begin:end]
    
    return time_str[1:].split(',')


# Clear the room to avoid mistake
def process_str(time_str):
    begin = 0
    end = 0
    tmp = ""
    while True:
        begin = time_str.find("(", begin) + 1
        tmp += time_str[end:begin]
        end = time_str.find(")", end) + 1
        if end == 0: break
    
    return tmp
# End for funcs. of search time


# return a new list of rows that fits certain time
def search_time(time, lecture_list):
    day = chin_to_num(time[0])
    if day is False: main()

    new_list = []
    for instance in lecture_list:

        time_str = process_str(instance.time_and_room)

        all_times = extract_time(time)
        # class_times = extract_time(ws[cell_name].value, day)
        class_times = extract_time(time_str, day)
                
        if set(class_times).issubset(set(all_times)):
            new_list.append(instance)

    return new_list


def lecture_search_view(request):
    # if request.method == 'POST':
    form = LectureForm(request.POST or None)
    
    if form.is_valid():
        department = form.cleaned_data['department']
        number = form.cleaned_data['number']
        name = form.cleaned_data['name']
        teacher = form.cleaned_data['teacher']
        time = form.cleaned_data['time']
        room = form.cleaned_data['room']
        remark = form.cleaned_data['remark']
        
        lecture_list = Lecture.objects.all()

        # remark
        if remark:
            print("Searching \"{}\" in remarks...".format(remark))
            lecture_list = search_str("F", remark, lecture_list)
        # time: 一6,7,8
        if time:
            print("Searching {} on 星期{}...".format(time[1:], time[0]))
            lecture_list = search_time(time, lecture_list)
        # name
        if name:
            print("Searching lecture: {}...".format(name))
            lecture_list = search_str("C", name, lecture_list)
        # teacher
        if teacher:
            print("Searching teacher: {}...".format(teacher))
            lecture_list = search_str("D", teacher, lecture_list)
        # number
        if number:
            print("Searching number: {}...".format(number))
            lecture_list = search_str("B", number, lecture_list)
        # room
        if room:
            print("Searching room: {}...".format(room))
            lecture_list = search_str("E", room, lecture_list)
        # department
        if department:
            print("Searching department: {}...".format(department))
            lecture_list = search_str("A", department, lecture_list)
        
        form = LectureForm()    
        context = {
            'form': form,
            'object_list': lecture_list
        }
       
        return render(request, "lectures/search.html", context)
    
    form = LectureForm()
    context = {
        'form': form
    }

    return render(request, "lectures/search.html", context)


# def lecture_delete_view(request, id):
#     obj = get_object_or_404(id=id)
#     if request.method == "POST":
#         obj.delete()
#         return redirect('../')
#     context = {
#         'object': obj
#     }
#     return render(request, "lectures/delete.html", context)


# def lecture_create_view(request):
#     form = LectureForm(request.POST or None)
#     if form.is_valid(): form.save()

#     context = {
#         'form' :form
#     }

#     return render(request, "lectures/create.html", context)