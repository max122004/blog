from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    # ist_display позволяет задавать поля модели, которые вы хотите показывать на странице списка объектов администрирования
    list_filter = ['status', 'created', 'publish', 'author']
    # страница списка содержит правую боковую панель, которая позволяет фильтровать результаты по полям, включенным в атрибут list_filter
    search_fields = ['title', 'body']
    # строка поиска. Это вызвано тем, что мы опреде- лили список полей, по которым можно выполнять поиск, используя атрибут search_fields
    prepopulated_fields = {'slug': ('title',)}
    # Вы сообщили Django, что нужно предзаполнять поле slug данными, вводимыми в поле title, используя атрибут prepopulated_fields:
    raw_id_fields = ['author']
    # поле author отображается поисковым виджетом, кото- рый будет более приемлемым, чем выбор из выпадающего списка, когда у вас тысячи пользователей. Это достигается с помощью атрибута raw_id_fields и выглядит следующим образом:
    date_hierarchy = 'publish'
    # навигационные ссылки для навигации по иерархии дат; это определено атрибутом date_hierarchy
    ordering = ['status', 'publish']
    # умолчанию посты упорядочены по столбцам STA- TUS (Статус) и PUBLISH (Опубликован). С помощью атрибута ordering были заданы критерии сортировки, которые будут использоваться по умолчанию.