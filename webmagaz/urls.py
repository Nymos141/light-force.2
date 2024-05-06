from django.contrib import admin
from django.urls import path
from game.views import (hello_views, jokes_views,
                        main_views, product_list, detail_product, create_product, add_feedback, update_product,
                        Hello,  JokesView, ProductListView, ProductDetailView, AddFeedbackView,
                        CreateProductView, UpdateProductView, MainView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_views),
    path("jokes/", jokes_views),
    path("", main_views, name="main_view"),
    path("products/", product_list, name="product_list"),
    path("products/<int:product_id>/", detail_product, name="detail_product"),
    path("append/", create_product, name="append"),
    path('add_feedback/<int:product_id>/', add_feedback, name='add_feedback'),
    path('products/<int:product_id>/edit/', update_product, name='update_product'),

    path("", MainView.as_view(), name='Main'),

    path('Hello2/', Hello.as_view()),
    path('Jokes2/', JokesView.as_view(), name="jokes_view"),
    path('Product2/', ProductListView.as_view(), name="product_list2"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('Create2', CreateProductView.as_view, name='create_view'),
    path('products/<int:pk>/edit/', UpdateProductView.as_view(), name='update_product')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
