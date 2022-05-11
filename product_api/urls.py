from django.urls import path
from .import views

urlpatterns = [
    #path('',views.apiOverview,name='apiOverview'),
    path('grocery-list/',views.GroceryProducts,name='grocery-list'),
    path('product-detail/<int:pk>/',views.SingleProduct,name='detail'),
    path('product-create/',views.CreateProduct,name='product-create'),
    path('product-update/<int:pk>/',views.updateProduct,name='product-update'),
    path('product-delete/<int:pk>/',views.deleteProduct,name='product-delete'),
]