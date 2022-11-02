from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from MailTracking.serializers.trackermodelserializer import TrackMetricsModelSerializer
from .models.trackermodel import Track
from .models.trackermodel import TrackMetricsModel
from rest_framework import viewsets
from bson import ObjectId
from django.shortcuts import get_object_or_404
from rest_framework import exceptions
from MailTracking.serializers.imagemodelserializer import ImageDeatilsModelSerializer
from MailTracking.models.imagemodel import ImageDeatilsModel

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from datetime import datetime
from rest_framework import mixins


uid = openapi.Parameter(
    "keyword", openapi.IN_QUERY, description="User Id", type=openapi.TYPE_STRING
)
frm = openapi.Parameter(
    "frm", openapi.IN_QUERY, description="sender email", type=openapi.TYPE_STRING
)
to = openapi.Parameter(
    "to", openapi.IN_QUERY, description="reciever email", type=openapi.TYPE_STRING
)
fi = openapi.Parameter(
    "fi", openapi.IN_QUERY, description="sender IP Address", type=openapi.TYPE_STRING
)
id = openapi.Parameter(
    "id", openapi.IN_QUERY, description="Mail Id", type=openapi.TYPE_STRING
)
img_id = openapi.Parameter(
    "img_id", openapi.IN_QUERY, description="Mail tracker Image slug", type=openapi.TYPE_STRING
)


class CountClick(APIView):
    def get(self,request,format=None):
        track=Track.objects.create(count=1)
        track.save()
        click_count=Track.objects.filter().count()
        return Response(click_count,status=status.HTTP_200_OK)

class TrackMail(APIView):
    def get(self,request,format=None):
        print(request.META.get("HTTP_HOST"))
        print(request.META.get("HTTP_USER_AGENT"))
        print(request.META.get("CONTENT_LENGTH"))
        track=Track.objects.create(count=1)
        track.save()
        # read image 
        file='saticfiles/mail_tracker.jpg'
        try:
            with open(file,'rb') as tracking_image:
                response=HttpResponse(tracking_image.read()
                                ,content_type='image/jpg')
                return response
        except:
            return Response("Image can't be loaded.",status=status.HTTP_200_OK)

class ImageModelViewset(viewsets.ModelViewSet):
    serializer_class=ImageDeatilsModelSerializer
    queryset=ImageDeatilsModel.objects.all()
    lookup_field="_id"
    http_method_names = ['get','put','delete','post']

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        try:
            filter_kwargs = {self.lookup_field: ObjectId(self.kwargs[lookup_url_kwarg])}
            queryset = self.filter_queryset(self.get_queryset())
            track_obj = get_object_or_404(queryset, **filter_kwargs)
            self.check_object_permissions(self.request,track_obj)
            return track_obj
        except:
            msg=f'Object with ObjectId {self.kwargs[lookup_url_kwarg]} does not exist.'
            raise exceptions.APIException(detail=msg)


class TrackMailModelViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):

    serializer_class=TrackMetricsModelSerializer
    queryset=TrackMetricsModel.objects.all()
    lookup_field="_id"
    http_method_names = ['get','put','delete','post']

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        try:
            filter_kwargs = {self.lookup_field: ObjectId(self.kwargs[lookup_url_kwarg])}
            queryset = self.filter_queryset(self.get_queryset())
            track_obj = get_object_or_404(queryset, **filter_kwargs)
            self.check_object_permissions(self.request,track_obj)
            return track_obj
        except:
            msg=f'Object with ObjectId {self.kwargs[lookup_url_kwarg]} does not exist.'
            raise exceptions.APIException(detail=msg)


    @action(
        methods=["POST"],
        detail=False,
        url_path=r"sendmail",
        serializer_class=None,
    )
    @swagger_auto_schema(manual_parameters=[uid,frm,to,fi,id,img_id])
    def sendmail(self, request, *args, **kwargs):
        http_host=request.META.get("HTTP_HOST",None)
        http_user_agent=request.META.get("HTTP_USER_AGENT",None)
        http_content_length=request.META.get("CONTENT_LENGTH",None)

        user_id=self.request.query_params.get("uid",None)
        from_mail_id=self.request.query_params.get("frm",None)
        to_mail_id=self.request.query_params.get("to",None)
        from_mail_ip=self.request.query_params.get("fi",None)
        mail_id=self.request.query_params.get("id",None)
        image_id=self.request.query_params.get("img_id",None)
        to_mail_ip=http_host
        
        serialized_data = {
            "mail_event_metrics_stats": {
                "image1": {
                "mail_status": "string",
                "mail_opened_history": {
                    "opened_at": datetime.now(),
                    "opening_user_agent": http_user_agent,
                    "opening_count_order": 0
                },
                "image_slug": "string"
                },
                "image2": {
                "mail_status": "string",
                "mail_opened_history": {
                    "opened_at": datetime.now(),
                    "opening_user_agent": http_user_agent,
                    "opening_count_order": 0
                },
                "image_slug": "string"
                }
            },
            "mail_id": mail_id,
            "from_mail_user_token": user_id,
            "from_mail_address": from_mail_id,
            "from_host_address": from_mail_ip,
            "from_user_agent": "string",
            "to_mail_address": to_mail_id,
            "to_host_address": to_mail_ip,
            "to_user_agent": http_user_agent,
            "to_content_length": http_content_length,
            "total_mail_opening_count": 2147483647,
        }
        serializer=TrackMetricsModelSerializer(data=serialized_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        try:
            image=ImageDeatilsModel.objects.get(_id=ObjectId(image_id))
            file='saticfiles/'+image.image_name
            try:
                with open(file,'rb') as tracking_image:
                    response=HttpResponse(tracking_image.read()
                                    ,content_type='image/jpg')
                    return response
            except:
                return Response("Image can't be loaded.",status=status.HTTP_404_NOT_FOUND)
        except:
            message=f'Image does not exist with Image Id {img_id}'
            Response(message,status=status.HTTP_404_NOT_FOUND)
    