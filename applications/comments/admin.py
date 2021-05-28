from django.contrib import admin

#app
from .models import CategoryComment, Comment, CommentOfUser

class CategoryCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'category_comment')

class CommentOfUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'candidate')


admin.site.register(CategoryComment, CategoryCommentAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentOfUser, CommentOfUserAdmin)





