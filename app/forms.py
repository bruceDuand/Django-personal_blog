from django import forms

from pagedown.widgets import PagedownWidget

from .models import Article, ImageUpload, Review

class CommentForm(forms.Form):
	name = forms.CharField(max_length=20,
		widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Name'}))
	comment = forms.CharField(
		widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Comment'}))


class ArticleForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget)
	class Meta:
		model = Article
		fields = [
			'title',
			'content', 
			'image',
		]

class ImageUploadForm(forms.ModelForm):
	class Meta:
		model = ImageUpload
		fields = [
			'image',
		]

class ReviewForm(forms.ModelForm):
	# date = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Review
		fields = [
			'moviereview',
		]
