from django.contrib import admin

# Register your models here.

from .  models import Proce, Graph, Ram, Gab, Marca_Proce, Marca_Graph, Marca_Gab

admin.site.register(Proce)
admin.site.register(Graph)
admin.site.register(Ram)
admin.site.register(Gab)
admin.site.register(Marca_Proce)
admin.site.register(Marca_Graph)
admin.site.register(Marca_Gab)