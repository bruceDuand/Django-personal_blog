from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic import DetailView

from markdown import markdown
import re
import logging

import os
import pickle
import numpy as np

from .vectorizer import vect

from .models import Comment, Article, ImageUpload
from .forms import CommentForm, ArticleForm, ImageUploadForm, ReviewForm



logger = logging.getLogger(__name__)

def project_signin(request):

	return render(request, 'app/project_page/signin_page.html')

def review(request):
	form = ReviewForm(request.POST or None)

	context = {'form': form}
	return render(request, 'app/review.html', context)

def review_result(request):
	review = request.POST['moviereview']
	cur_dir = os.path.dirname(__file__)
	clf = pickle.load(open(os.path.join(cur_dir,
             'pkl_objects',
             'classifier.pkl'), 'rb'))

	label = {0: 'negative', 1: 'positive'}
	X = vect.transform([review])
	y = clf.predict(X)[0]
	proba = np.max(clf.predict_proba(X))
	proba = float('%.4f' % proba)
	y = label[y]

	context = {
		'review': review,
		'probability': proba*100,
		'prediction': y,
	}
 
	return render(request, 'app/review_result.html', context)


def upload_image(request):
	if not request.user.is_superuser:
		return Http404 

	form = ImageUploadForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		messages.success(request, 'image successfully uploaded')
		return redirect('upload_image')

	context = {
		'form': form,
	}
 
	return render(request, 'app/upload_image.html', context)

def article_create(request):
	if not request.user.is_superuser:
		return Http404 

	form = ArticleForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		messages.success(request, 'successfully created')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'form' : form,
	}
 
	return render(request, 'app/article_create.html', context)

def article_update(request, pk=None):
	if not request.user.is_superuser:
		return Http404 

	article = get_object_or_404(Article, id=pk)

	form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		messages.success(request, 'successfully saved')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'title': article.title, 
		'article': article,
		'form': form,
	}

	return render(request, 'app/article_create.html', context)

def article_delete(request, pk=None):
	if not request.user.is_superuser:
		return Http404 

	article = get_object_or_404(Article, id=pk)
	article.delete()
	messages.success(request, 'successfully deleted')
	return redirect('article_list')


# class ProjectIndexView(ListView):
# 	"""docstring for ProjectIndexView"""
# 	template_name = 'app/project_index.html'

# 	context_object_name = 'article_list'

# 	def get_queryset(self):
# 		article_list = Article.objects.filter(status='p')

# 		for article in article_list:
# 			article.body = markdown.markdown(article.body)

# 		return article_list

# 	# def get_context_data(self, **kwargs):
# 	# 	kwargs['category_list'] = Category.objects.all().order_by('name')

# 	# 	return super(ProjectIndexView, self).get_context_data(**kwargs)

# class ArticleListView(ListView):
# 	"""docstring for ArticleListView"""
# 	template_name = 'app/article_list.html'
# 	context_object_name = 'article_list'

# 	def get_queryset(self):
# 		article_list = Article.objects.all()

# 		# for article in article_list:
# 		# 	article.content = markdown.markdown(article.content)

# 		return article_list

def ArticleList(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 10)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = {
    	'contacts': contacts,
		'article_list': article_list    	
    }
    return render(request, 'app/article_list.html', context)


# def article_list(request):
# 	return render(request, 'app/article_list.html')



def article_detail(request, pk):
#	article = get_object_or_404(Article, pk=pk)
	try:
		article = Article.objects.get(id=pk)
		#marked content
		# article.part1 = markdown(article.part1,['codehilite'])
		# article.part2 = markdown(article.part2,['codehilite'])
		# article.part3 = markdown(article.part3,['codehilite'])

	except Article.DoesNotExist:
		raise Http404

	context = {'article' : article}

	return render(request, 'app/article_detail.html', context)


def comment_index(request):
	comments = Comment.objects.order_by('-date')

	context = {'comments' : comments}

	return render(request, 'app/comment_index.html', context)

def comment(request):
	if request.method=='POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
			new_comment.save()
			return redirect('comment_index')

	else:
		form = CommentForm()

	context = {'form' : form}

	return render(request, 'app/comment.html', context)

def base(request):
	return render(request, 'app/index.html')

'''
def test(request):
	return render(request, 'app/test_comment.html')
'''

'''
def index(request):
	return HttpResponse("hello world")

def sign(request):
	return HttpResponse("this is the sign page")
'''