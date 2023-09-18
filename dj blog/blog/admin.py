#from django.contrib import admin
#from .models import Post

#admin.site.register(Post)
# Register your models here.
from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','author','title','content','date_posted')

admin.site.register(Post,PostAdmin)
