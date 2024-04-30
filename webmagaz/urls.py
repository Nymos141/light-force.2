from django.contrib import admin
from django.urls import path
from game.views import (hello_views, jokes_views,
                        main_views, product_list, detail_product, create, add_feedback)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_views),
    path("jokes/", jokes_views),
    path("", main_views),
    path("products/", product_list, name="product_list"),
    path("products/<int:product_id>/", detail_product),
    path("more/", detail_product),
    path("append/", create),
    path('add_feedback/<int:product_id>/', add_feedback, name='add_feedback')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
