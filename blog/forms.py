from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post


class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        widgets = {'title': forms.TextInput(attrs={'placeholder': 'Введите название'}),}
        fields = ('title', 'image', 'content')
