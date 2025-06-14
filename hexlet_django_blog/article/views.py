from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from .forms import ArticleCommentForm
from .models import ArticleComment, Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )
    

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )
    

class ArticleCommentsView(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(
            ArticleComment, id=kwargs["id"], article__id=kwargs["article_id"]
        )

        return render(...)
    

class CommentArticleView(View):
    # если метод POST, то мы обрабатываем данные
    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данные формы на корректность
            comment = form.save(commit=False)  # Получаем заполненную модель
            # Дополнительно обрабатываем модель
            comment.content = check_for_spam(form.data["content"])
            comment.save()

    # если метод GET, то создаем пустую форму
    def get(self, request, *args, **kwargs):
        form = ArticleCommentForm()  # Создаем экземпляр нашей формы
        return render(
            request, "comment.html", {"form": form}
        )  # Передаем нашу форму в контексте