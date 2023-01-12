from .views import WorkViewSet, GoalViewSet
from rest_framework import routers


app_name = 'api'

router = routers.SimpleRouter()
router.register(r'works', WorkViewSet)
router.register(r'goals', GoalViewSet)
urlpatterns = router.urls


