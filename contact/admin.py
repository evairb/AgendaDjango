from django.contrib import admin
from contact import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id','name',
    ordering = '-id',


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    #lista colunas na area administrativa
    list_display = 'id', 'first_name', 'last_name', 'phone','show',
    #ordena por id ou outro campo pode usar (-) para inverter a ordem
    ordering = '-id',
    #campo de pesquisa
    search_fields = 'id', 'first_name', 'last_name',
    #paginacao
    list_per_page = 10
    #controle para maximo na pagina
    list_max_show_all = 200
    #habilita forma de edicao direto na tela
    list_editable = 'first_name', 'last_name','show',
    #criar um link
    list_display_links = 'id', 'phone',

