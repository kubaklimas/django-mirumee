# from django.urls import include, path

# from rest_framework import routers

# from books.views import BookViewSet

# router = routers.DefaultRouter()
# router.register("books", BookViewSet)

# urlpatterns = [path(r"^", include(router.urls))]
from django.urls import path,include
from books.api.views import BookViewSet,OpinionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('opinions', OpinionViewSet)


urlpatterns = [
     path('', include(router.urls)),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
 ]

