from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
