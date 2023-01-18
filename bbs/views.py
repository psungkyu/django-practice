from django.views import View
from django.http import HttpResponse, JsonResponse, Http404
from bbs.models import Article

def hello(request, to):
    return HttpResponse("Hello, {}!" .format(to))

# 모든 컨텐츠를 리스팅하는 함수
def list_contents(request):
    contents = Article.objects.all() # db에서 모든 조회가 일어남
    if len(contents) == 0:
        return HttpResponse("No data")
    elif len(contents) > 0:
        print("1")
        return HttpResponse(contents)
    else:
        raise Http404('nodap')

# 특정 컨텐츠를 눌렀을 때 관련된 데이터가 모두 보이는 함수
def read_content(request, content_id):
    print("2")
    content = Article.objects.get(content_id=content_id)
    return JsonResponse(content)

# 새로운 컨텐츠를 만드는 함수
def create_content(request):
    if request.method == 'POST':
        article = Article.objects.create()
        print("create")
        return HttpResponse(request.POST)

# 기존의 컨텐츠를 수정하는 함수
def update_content(request, content_id):
    if request.method == 'POST':
        article = Article.objects.get(content_id=content_id)
        print("updated article : {}" .format(article))
        return HttpResponse(request.POST)


# 기존의 컨텐츠를 삭제하는 함수
def delete_content(request, content_id):
    Article.objects.get(content_id=content_id).delete()
