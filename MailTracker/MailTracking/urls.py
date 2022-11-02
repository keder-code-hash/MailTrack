from .views import CountClick,TrackMail,TrackMailModelViewSet,ImageModelViewset
from django.urls import include,path
from rest_framework import routers

router=routers.DefaultRouter()
router.register("track_mail",TrackMailModelViewSet)
router.register("image_details",ImageModelViewset)

urlpatterns=[ 
    path('',include(router.urls)),
    path("test_track",TrackMail.as_view())
]
