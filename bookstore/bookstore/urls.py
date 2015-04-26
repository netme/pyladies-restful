from django.conf.urls import include, url
from django.contrib import admin

from api.views import BookListView

urlpatterns = [
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^books/$', BookListView.as_view(), name='books'),
    url(r'^admin/', include(admin.site.urls)),
]
