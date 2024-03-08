from django.http import JsonResponse, HttpResponse
from app01.models import User, Dish, Canteen, Comment, Reply, Window, Tag
from django.views.decorators.csrf import csrf_exempt
import json, random

def statistics_type():
    Dish.objects.filter()

def statistics_canteen():
    Dish.objects.filter()

def statistics_price():
    Dish.objects.filter()

def dishToJson(dishList, dishInfoList):  # 将dishList转换成dishInfoList
    for dish in dishList:
        tagsNameList = []
        for tag in dish.tags.all():
            tagsNameList.append(tag.tagName)
        d = dict(id=dish.id, name=dish.name, hall=dish.window.canteen.name, window=dish.window.name,
                 type=dish.type, tags=tagsNameList, purchase=dish.numPurchase, comment=dish.numComment,
                 collectNum=dish.collectNum, score=dish.score, price=dish.price)
        dishInfoList.append(d)
    return


@csrf_exempt
def search(request):
    body = request.body
    body_str = body.decode()
    data = json.loads(body_str)  # 将JSON字符串并将其转换为Python字典

    keyword = data["keyword"]
    hall_list = data["hall"]
    order = data["order"]
    filters = data["filters"]  # dict {tag:true/false}
    type = data["type"]
    synonymsList = [["热", "煮", "温", "蒸", "炒", "砂锅", "炖", "烧", "焖", "暖"],
                    ["面食", "饺子", "面条", "包子", "饼", "米线", "馍", "粉"],
                    ["辣", "麻", "辛", "椒"],
                    ["甜", "蜜", "糖"],
                    ["猪", "排骨", "五花", "红烧肉", "卤肉", "肘", "培根", "狮子头"],
                    ["酸", "醋"],
                    ["炸", "烤", "香酥", "鸡排", "鸡柳", "骨肉相连", "油"],
                    ["凉", "冷", "冰"],
                    ["咸", "酱", "卤", "盐"]]
    keyword_synonyms = [keyword]
    if len(keyword):
        for synonyms in synonymsList:
            if keyword in synonyms:
                keyword_synonyms = synonyms

    if len(hall_list) == 0:  # 若为空则全选
        for canteen in Canteen.objects.all():
            hall_list.append(canteen.name)

    if len(type) == 0:
        type = "正餐"

    dishList1 = []

    for dish in Dish.objects.all():
        choose = 1
        for tagName, attitude in filters.items():
            tag = Tag.objects.get(tagName=tagName)
            if attitude:
                if not tag in dish.tags.all():
                    choose = 0
                    break
            else:
                if tag in dish.tags.all():
                    choose = 0
                    break
        if choose and dish.window.canteen.name in hall_list and dish.type == type:
            dishList1.append(dish)

    dishList2 = []
    if len(keyword):
        for dish in dishList1:
            for synonym in keyword_synonyms:
                if synonym in dish.name:
                    dishList2.append(dish)
                    break
    else:  # 若为空则全选
        dishList2 = dishList1

    if order == "score":
        dishList2.sort(key=lambda dish: dish.score, reverse=True)
    elif order == "collect":
        dishList2.sort(key=lambda dish: dish.collectNum, reverse=True)
    elif order == "sales":
        dishList2.sort(key=lambda dish: dish.numPurchase, reverse=True)

    dishInfoList = []
    dishToJson(dishList2, dishInfoList)
    dictionary = {"code": 0, "dishes": dishInfoList}
    return JsonResponse(dictionary, safe=False)  # safe为True则参数只能为字典


@csrf_exempt
def recommendation(request):
    userId = request.POST.get("user_id")
    isMorning = request.POST.get("is_morning")
    n = request.POST.get("n")
    n = int(n)
    user = User.objects.get(userId=userId)
    comments = Comment.objects.filter(author=user).order_by("-id")[0:5]
    recommendTagList = set()
    for comment in comments:
        if comment.score >= 4:
            for tag in comment.dish.tags.all():
                recommendTagList.add(tag)

    dishHateList = set()
    for comment in comments:
        if comment.score <= 2:
            dishHateList.add(comment.dish)

    recommendDishList = []

    if isMorning == "true":
        querySet = Dish.objects.filter(type="早餐")
    else:
        querySet = Dish.objects.exclude(type="早餐")

    querySet = querySet.order_by("?")
    for dish in querySet:
        for tag in recommendTagList:
            if tag in dish.tags.all() and dish not in dishHateList:
                recommendDishList.append(dish)
                break
        if len(recommendDishList) >= n:
            break

    dishInfoList = []
    dishToJson(recommendDishList, dishInfoList)
    dictionary = {"code": 0, "dishes": dishInfoList}
    return JsonResponse(dictionary, safe=False)


@csrf_exempt
def rank(request):
    order = request.POST.get("order")
    n = request.POST.get("n")
    n = int(n)
    querySet = None
    if order == "score":
        querySet = Dish.objects.all().order_by('-score')
    elif order == "collect":
        querySet = Dish.objects.all().order_by('-collectNum')
    elif order == "sales":
        querySet = Dish.objects.all().order_by('-numPurchase')
    dishList = []
    dishInfoList = []
    for dish in querySet:  # 选择前n个返回
        dishList.append(dish)
        n = n - 1
        if n == 0:
            break
    dishToJson(dishList, dishInfoList)
    dictionary = {"code": 0, "dishes": dishInfoList}
    return JsonResponse(dictionary, safe=False)


@csrf_exempt
def deleteComment(request):
    commentId = request.POST.get("commentId")
    Comment.objects.filter(id=commentId).delete()
    return JsonResponse({"code": 0})


@csrf_exempt
def signUp(request):
    userId = request.POST.get("user_id")
    password = request.POST.get("password")
    name = request.POST.get("name")
    stuId = request.POST.get("stuId")
    college = request.POST.get("college")
    if User.objects.filter(userId=userId).exists():
        return JsonResponse({"code": 1})
    else:
        User.objects.create(userId=userId, password=password, name=name, stuId=stuId, college=college)
        return JsonResponse({"code": 0})


@csrf_exempt
def signIn(request):
    userId = request.POST.get("user_id")
    password = request.POST.get("password")
    if User.objects.filter(userId=userId).exists():
        user = User.objects.get(userId=userId)
        if password == user.password:  # 密码正确
            return JsonResponse({"code": 0})
        else:  # 密码错误
            return JsonResponse({"code": 2})
    else:  # 不存在的用户名
        return JsonResponse({"code": 1})


@csrf_exempt
def get_info(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    commentNum = Comment.objects.filter(author=user).count()
    return JsonResponse({"code": 0, "college": user.college, "stuId": user.stuId, "name": user.name,
                         "comments": commentNum, "purchase": user.purchaseDishes.all().count()})


@csrf_exempt
def edit_info(request):
    userId = request.POST.get("user_id")
    college = request.POST.get("college")
    name = request.POST.get("name")
    stuId = request.POST.get("stuId")
    college = request.POST.get("college")
    User.objects.filter(userId=userId).update(name=name, stuId=stuId, college=college)
    return JsonResponse({"code": 0})


@csrf_exempt
def edit_password(request):
    userId = request.POST.get("user_id")
    password = request.POST.get("password")
    User.objects.filter(userId=userId).update(password=password)
    return JsonResponse({"code": 0})


@csrf_exempt
def collect(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    dishInfoList = []
    dishToJson(user.collectDishes.all(), dishInfoList)
    return JsonResponse({"code": 0, "dishes": dishInfoList})


@csrf_exempt
def save_collect(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    dish_id = request.POST.get("dish_id")
    dish = Dish.objects.get(id=dish_id)
    dish.collectNum += 1
    dish.save()
    user.collectDishes.add(dish)
    user.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def delete_collect(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    dish_id = request.POST.get("dish_id")
    dish = Dish.objects.get(id=dish_id)
    user.collectDishes.remove(dish)
    user.save()
    dish.collectNum -= 1
    dish.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def collect_hall(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    canteenList = []
    for canteen in user.collectCanteens.all():
        canteenList.append(canteen.name)
    return JsonResponse({"code": 0, "halls": canteenList})


@csrf_exempt
def save_collect_hall(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    canteenName = request.POST.get("hall")
    canteen = Canteen.objects.get(name=canteenName)
    user.collectCanteens.add(canteen)
    user.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def delete_collect_hall(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    canteenName = request.POST.get("hall")
    canteen = Canteen.objects.get(name=canteenName)
    user.collectCanteens.remove(canteen)
    user.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def collect_window(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    windowList = []
    for window in user.collectWindows.all():
        windowList.append({"hall": window.canteen.name, "window": window.name})
    return JsonResponse({"code": 0, "windows": windowList})


@csrf_exempt
def save_collect_window(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    canteenName = request.POST.get("hall")
    canteen = Canteen.objects.get(name=canteenName)
    windowName = request.POST.get("window")
    window = Window.objects.get(canteen=canteen, name=windowName)
    user.collectWindows.add(window)
    user.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def delete_collect_window(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    canteenName = request.POST.get("hall")
    canteen = Canteen.objects.get(name=canteenName)
    windowName = request.POST.get("window")
    window = Window.objects.get(canteen=canteen, name=windowName)
    user.collectWindows.remove(window)
    user.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def history(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    dishInfoList = []
    dishToJson(user.purchaseDishes.all(), dishInfoList)
    return JsonResponse({"code": 0, "dishes": dishInfoList})


@csrf_exempt
def delete_history(request):
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    dish_id = request.POST.get("dish_id")
    dish = Dish.objects.get(id=dish_id)
    user.purchaseDishes.remove(dish)
    user.save()
    dish.numPurchase -= 1
    dish.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def getHalls(request):
    hallsNameList = []
    for canteen in Canteen.objects.all():
        hallsNameList.append(canteen.name)
    return JsonResponse({"code": 0, "halls": hallsNameList})


@csrf_exempt
def purchase(request):
    dish_id = request.POST.get("dish_id")
    userId = request.POST.get("user_id")
    user = User.objects.get(userId=userId)
    dish = Dish.objects.get(id=dish_id)
    user.purchaseDishes.add(dish)
    user.save()
    dish.numPurchase += 1
    dish.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def dish_get_detail(request):
    dish_id = request.POST.get("dish_id")
    dish = Dish.objects.get(id=dish_id)
    tagsNameList = []
    for tag in dish.tags.all():
        tagsNameList.append(tag.tagName)
    d = dict(id=dish.id, name=dish.name, hall=dish.window.canteen.name, window=dish.window.name,
             type=dish.type, tags=tagsNameList, purchase=dish.numPurchase, comment=dish.numComment,
             collectNum=dish.collectNum, score=dish.score, price=dish.price)
    querySet = Comment.objects.filter(dish=dish)
    commentIdList = []
    for comment in querySet:
        commentIdList.append(comment.id)

    return JsonResponse({"code": 0, "summary": d, "comments": commentIdList})


@csrf_exempt
def dish_random(request):
    n = request.POST.get("n")
    n = int(n)
    if n > Dish.objects.all().count():
        return JsonResponse({"code": 1})
    querySet = Dish.objects.all().order_by("?")[0:n]
    dishInfoList = []
    dishToJson(querySet, dishInfoList)
    dictionary = {"code": 0, "dishes": dishInfoList}
    return JsonResponse(dictionary, safe=False)


@csrf_exempt
def post_comment(request):
    dish_id = request.POST.get("dish_id")
    userId = request.POST.get("user_id")
    content = request.POST.get("content")
    score = request.POST.get("score")
    score = int(score)
    time = request.POST.get("time")
    user = User.objects.get(userId=userId)
    dish = Dish.objects.get(id=dish_id)
    Comment.objects.create(dish=dish, author=user, content=content, score=score, likes=0, time=time, replyNum=0)
    dish.score = (dish.score * dish.numComment + score) / (dish.numComment + 1)
    dish.save()
    dish.numComment += 1
    dish.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def reply_comment(request):
    userId = request.POST.get("user_id")
    receiverId = request.POST.get("receiver_id")
    comment_id = request.POST.get("comment_id")
    content = request.POST.get("content")
    time = request.POST.get("time")
    author = User.objects.get(userId=userId)
    receiver = User.objects.get(userId=receiverId)
    comment = Comment.objects.get(id=comment_id)
    Reply.objects.create(author=author, receiver=receiver, comment=comment, content=content, likes=0, time=time)
    comment.replyNum += 1
    comment.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def support(request):
    comment_id = request.POST.get("id")
    comment = Comment.objects.get(id=comment_id)
    comment.likes += 1
    comment.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def support_reply(request):
    reply_id = request.POST.get("id")
    reply = Reply.objects.get(id=reply_id)
    reply.likes += 1
    reply.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def cancel_support(request):
    comment_id = request.POST.get("id")
    comment = Comment.objects.get(id=comment_id)
    comment.likes -= 1
    comment.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def cancel_support_reply(request):
    reply_id = request.POST.get("id")
    reply = Reply.objects.get(id=reply_id)
    reply.likes -= 1
    reply.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def comment_get_detail(request):
    comment_id = request.POST.get("id")
    comment = Comment.objects.get(id=comment_id)
    summary = dict(id=comment.id, dish_id=comment.dish.id, user_id=comment.author.userId,
                   summary=comment.content[0:50], score=comment.score, likes=comment.likes,
                   comments=comment.replyNum)
    querySet = Reply.objects.filter(comment=comment)
    replyInfoList = []
    for reply in querySet:
        d = dict(id=reply.id, likes=reply.likes, time=reply.time, user_id=reply.author.userId, full_text=reply.content,
                 receiver_id=reply.receiver.userId)
        replyInfoList.append(d)
    return JsonResponse({"code": 0, "summary": summary, "full_text": comment.content, "time": comment.time,
                         "comments": replyInfoList})


@csrf_exempt
def comment_random(request):
    n = request.POST.get("n")
    n = int(n)
    commentList = []
    if n > Comment.objects.all().count():
        return JsonResponse({"code": 1})
    querySet = Comment.objects.all().order_by("?")[0:n]
    commentInfoList = []
    for comment in querySet:
        d = dict(id=comment.id, dish_id=comment.dish.id, user_id=comment.author.userId,
                 summary=comment.content[0:50], score=comment.score, likes=comment.likes,
                 comments=comment.replyNum)
        commentInfoList.append(d)
    dictionary = {"code": 0, "comments": commentInfoList}
    return JsonResponse(dictionary, safe=False)


@csrf_exempt
def init(request):
    f3 = open(r"C:\Users\Administrator\Desktop\python-hw-master\app01\dishData.txt", "r", encoding="UTF-8")
    dataList = f3.readlines()
    for line in dataList:
        print(line)
        if line == "\n":
            continue
        keys = line.split()
        print(keys)
        canteenName = keys[0]
        windowName = keys[1]
        dishName = keys[2]
        price = keys[3]
        type = keys[4]
        tags = keys[5:]
        canteen = Canteen.objects.get(name=canteenName)
        window = Window.objects.get(canteen=canteen, name=windowName)
        dish = Dish.objects.create(name=dishName, window=window, price=price, score=0, numComment=0,
                                   numPurchase=0, collectNum=0, type=type)
        for tagName in tags:
            tag = Tag.objects.get(tagName=tagName)
            dish.tags.add(tag)
    return HttpResponse("682道菜全部添加成功")


@csrf_exempt
def addCanteen(request):
    canteenName = request.POST.get("hall")
    Canteen.objects.create(name=canteenName)
    return JsonResponse({"code": 0})


@csrf_exempt
def addWindow(request):
    canteenName = request.POST.get("hall")
    windowName = request.POST.get("window")
    canteen = Canteen.objects.get(name=canteenName)
    Window.objects.create(name=windowName, canteen=canteen)
    return JsonResponse({"code": 0})


@csrf_exempt
def addDish(request):
    body = request.body
    body_str = body.decode()
    data = json.loads(body_str)  # 将JSON字符串并将其转换为Python字典

    canteenName = data["hall"]
    windowName = data["window"]
    name = data["name"]
    tags = data["tags"]
    type = data["type"]
    price = data["price"]
    canteen = Canteen.objects.get(name=canteenName)
    window = Window.objects.get(canteen=canteen, name=windowName)
    dish = Dish.objects.create(name=name, window=window, price=price, score=0, numComment=0,
                               numPurchase=0, collectNum=0, type=type)
    for tagName in tags:
        tag = Tag.objects.get(tagName=tagName)
        dish.tags.add(tag)
    return JsonResponse({"code": 0})


@csrf_exempt
def addTag(request):
    tagName = request.POST.get("tagName")
    if Tag.objects.filter(tagName=tagName).exists():
        return JsonResponse({"code": 1})
    Tag.objects.create(tagName=tagName)
    return JsonResponse({"code": 0})


@csrf_exempt
def deleteTag(request):
    tagName = request.POST.get("tagName")
    if Tag.objects.filter(tagName=tagName).exists():
        Tag.objects.filter(tagName=tagName).delete()
        return JsonResponse({"code": 0})
    return JsonResponse({"code": 1})


@csrf_exempt
def editCanteen(request):
    newName = request.POST.get("newName")
    canteenName = request.POST.get("hall")
    canteen = Canteen.objects.get(name=canteenName)
    canteen.name = newName
    canteen.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def editWindow(request):
    newName = request.POST.get("newName")
    windowName = request.POST.get("window")
    canteenName = request.POST.get("hall")
    canteen = Canteen.objects.get(name=canteenName)
    window = Window.objects.get(name=windowName, canteen=canteen)
    window.name = newName
    window.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def editDish(request):
    newName = request.POST.get("newName")
    windowName = request.POST.get("window")
    canteenName = request.POST.get("hall")
    dishName = request.POST.get("dish")
    canteen = Canteen.objects.get(name=canteenName)
    window = Window.objects.get(name=windowName, canteen=canteen)
    dish = Dish.objects.get(name=dishName, window=window)
    dish.name = newName
    dish.save()
    return JsonResponse({"code": 0})


@csrf_exempt
def deleteDish(request):
    windowName = request.POST.get("window")
    canteenName = request.POST.get("hall")
    dishName = request.POST.get("dish")
    canteen = Canteen.objects.get(name=canteenName)
    window = Window.objects.get(name=windowName, canteen=canteen)
    Dish.objects.filter(name=dishName, window=window).delete()
    return JsonResponse({"code": 0})


@csrf_exempt
def deleteWindow(request):
    canteenName = request.POST.get("hall")
    windowName = request.POST.get("window")
    canteen = Canteen.objects.get(name=canteenName)
    Window.objects.filter(name=windowName, canteen=canteen).delete()
    return JsonResponse({"code": 0})


@csrf_exempt
def deleteCanteen(request):
    canteenName = request.POST.get("hall")
    Canteen.objects.filter(name=canteenName).delete()
    return JsonResponse({"code": 0})
