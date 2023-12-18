from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from . import firebase_settings
from rest_framework.permissions import AllowAny

@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request,*args,**kwargs):
    username = request.data["username"]
    password = request.data["password"]
    try:
        user = firebase_settings.auth.create_user_with_email_and_password(username,password)
        return Response(True)
    except Exception as e:
        if "EMAIL_EXISTS" in str(e):
            return Response({"response":"Email Already Exsist"})
        elif "INVALID_EMAIL" in str(e):
            return Response({"response":"INVALID_EMAIL"})
        else:
            return Response(str(e))


@api_view(["POST"])
@permission_classes([AllowAny])

def signin(request,*args,**kwargs):
    username = request.data["username"]
    password = request.data["password"]
    try:
        user = firebase_settings.auth.sign_in_with_email_and_password(username,password)
        return Response(True)
    except:
        return Response(False)