from django.urls import include, path
from rest_framework import routers
from backend.locations import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register('movies', views.MovieViewSet)
router.register('cities', views.CityViewSet)
router.register('countries', views.CountryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]