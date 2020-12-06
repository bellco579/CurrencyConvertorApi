from django.urls import include, path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.CurrencyViewSet.as_view()),
]
