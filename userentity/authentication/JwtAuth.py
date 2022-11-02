from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJwtAuthentication(JWTAuthentication ,BasicAuthentication):

    # split the Bearer token and split the JWT part from it.
    def authenticate(self, request):

        token_str = self.authenticate_header(request=request).decode('UTF-8')
        token = token_str.split(" ") 

        if not token or token[0]!="Bearer":
            return None
        
        if len(token)==1:
            msg = _('Invalid basic header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(token)>2:
            msg = _('Invalid basic header. Credentials string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)
        
        try :
            # get validated token from raw token
            validated_token = self.get_validated_token(raw_token= token[1])
            return self.authenticate_credentials(validated_token=validated_token)

        except (TypeError, UnicodeDecodeError):
            msg = _('Invalid basic header. Credentials not correctly base64 encoded.')
            raise exceptions.AuthenticationFailed(msg)

    # authenticate the token and extract user_name from it.
    def authenticate_credentials(self, validated_token, request=None):

        user = self.get_user(validated_token=validated_token)
         
        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
        
        return (user, None)

    # Access Auth header and return it from here.
    def authenticate_header(self, request):
        bearer_tok = get_authorization_header(request) 
        return bearer_tok
