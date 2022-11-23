from django.urls import include, re_path

accounts_urlpatterns = [
    re_path(r'^api/v1/', include('djoser.urls')),
    re_path(r'^api/v1/', include('djoser.urls.authtoken')),
    re_path(r'^api/v1/', include('drfpasswordless.urls')),
]

