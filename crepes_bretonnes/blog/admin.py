# -*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import Categorie, Article, Contact

class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'categorie', 'auteur', 'date', 'apercu_contenu')
    list_filter    = ('auteur','categorie',)
    date_hierarchy = 'date'
    ordering       = ('date',)
    search_fields  = ('titre', 'contenu')
    
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            'classes': ['collapse',],
            'fields': ('titre', 'auteur', 'categorie')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
            'description':u'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields': ('contenu', )
        }),
    )

    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article. S'il
        y a plus de 40 caractères, il faut ajouter des points de suspension. 
        """
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s...' % text
        else:
            return text
            
    # En-tête de notre colonne
    apercu_contenu.short_description = u'Aperçu du contenu'
            
class ContactAdmin(admin.ModelAdmin):
    list_display   = ('nom','adresse','photo')


admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Contact,ContactAdmin)


