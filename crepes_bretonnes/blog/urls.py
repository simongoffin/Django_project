from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^home/$', 'home'), # Accueil du blog
    url(r'^article/(?P<id_article>\d+)/$', 'view_article'), # Vue d'un article
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', 'list_articles'),
    url(r'^redirection/$', 'view_redirection'),
    url(r'^tpl/$', 'tpl'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', 'addition'),
    url(r'^image/$', 'image'),
    url(r'^model/(?P<id>\d+)$', 'lire'),
    url(r'^contact/$', 'contact'),
    url(r'^message/$', 'message'),
    url(r'^formulaire/$', 'formulaire'),
    url(r'^nouveau_contact/$', 'nouveau_contact'),
    url(r'^voir_contacts/$', 'voir_contacts'),
    url(r'^connexion/$', 'connexion'),
    url(r'^deconnexion/$', 'deconnexion'),
    url(r'^confirmation/$', 'confirmation'),
    url(r'^creation/$', 'creation'),
)
