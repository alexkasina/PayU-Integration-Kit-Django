from django.conf.urls import patterns, include, url

urlpatterns = [
    (r'^order/', include('cart.urls')),
]
