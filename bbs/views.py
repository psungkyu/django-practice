from django.views import View
from django.http import HttpResponse, JsonResponse, Http404
from bbs.models import Article
from django.views.generic import TemplateView

def hello(request, to):
    return HttpResponse("Hello, {}!" .format(to))

class ArticleListView(TemplateView):
    template_name = 'base.html'
    queryset = Article.objects.all()
    
    # 모든 데이터를 읽어와서 ctx dictionary에 넣어준다. 이 때, 필요한 데이터만 보여준다.
    def get(self, request, *args, **kwargs):
        ctx = {}    # 탬플릿에 전달할 데이터
        return self.render_to_response(ctx)

class ArticleDetailView(TemplateView):
    template_name = 'article_detail.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return self.render_to_response(ctx)

class ArticleCreateUpdateView(TemplateView):
    template_name = 'article_detail.html'


class ArticleDeleteView(TemplateView):
    # 삭제 버튼을 누르면 삭제가 되도록 만들 것. 삭제 버튼은 메인 페이지와 디테일 페이지 모두에 있어야 한다.