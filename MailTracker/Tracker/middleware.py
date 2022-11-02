from MailTracking.serializers.trackermodelserializer import MailEventMetricsSerializer, TrackMetricsModelSerializer
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin


class EmailTrackMiddleware(MiddlewareMixin):

    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        # Code that is executed in each request before the view is called
        response = self.get_response(request)
        # Code that is executed in each request after the view is called
        return response
    

    def process_view(self, request, view_func, view_args, view_kwargs):
        """Responsible for saving the incoming request details in DB
        uat : user_access_token
        URL Format : /track_mail?uid={}&frm={from_mail_id}&to={to_mail_id}&fi={from_ip}&id={}&img_id={}
        Action : To set the status of reading mail to True. Both of the embed image should be loaded at the same time.
        """ 
        print("Hoo")
        http_host=request.META.get("HTTP_HOST",None)
        http_user_agent=request.META.get("HTTP_USER_AGENT",None)
        http_content_length=request.META.get("CONTENT_LENGTH",None)
        print(type(request))
        # user_id=self.request.query_params.get("uid",None)
        # from_mail_id=self.request.query_params.get("frm",None)
        # to_mail_id=self.request.query_params.get("to",None)
        # from_mail_ip=self.request.query_params.get("fi",None)
        # mail_id=self.request.query_params.get("id",None)
        # image_id=self.request.query_params.get("img_id",None)
        # to_mail_ip=http_host
        
        # serialized_data = {
        #     "mail_event_metrics_stats": {
        #         "image1": {
        #         "mail_status": "string",
        #         "mail_opened_history": {
        #             "opened_at": datetime.now(),
        #             "opening_user_agent": http_user_agent,
        #             "opening_count_order": 0
        #         },
        #         "image_slug": "string"
        #         },
        #         "image2": {
        #         "mail_status": "string",
        #         "mail_opened_history": {
        #             "opened_at": datetime.now(),
        #             "opening_user_agent": http_user_agent,
        #             "opening_count_order": 0
        #         },
        #         "image_slug": "string"
        #         }
        #     },
        #     "mail_id": mail_id,
        #     "from_mail_user_token": user_id,
        #     "from_mail_address": from_mail_id,
        #     "from_host_address": from_mail_ip,
        #     "from_user_agent": "string",
        #     "to_mail_address": to_mail_id,
        #     "to_host_address": to_mail_ip,
        #     "to_user_agent": http_user_agent,
        #     "to_content_length": http_content_length,
        #     "total_mail_opening_count": 2147483647,
        # }
        # print(serialized_data)
        # serializer=TrackMetricsModelSerializer(data=serialized_data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        ...

    def process_exception(self, request, exception):
        # This code is executed if an exception is raised
        pass

    def process_template_response(self, request, response):
        # This code is executed if the response contains a render() method
        return response