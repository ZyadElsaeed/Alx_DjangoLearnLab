from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

from rest_framework import permissions

class UserListView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = CustomUser.objects.get(id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"message": f"Following {user_to_follow.username}"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = CustomUser.objects.get(id=user_id)
    if user_to_follow != request.user:
        request.user.following.add(user_to_follow)
        return Response({"message": f"Now following {user_to_follow.username}"}, status=status.HTTP_200_OK)
    return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = CustomUser.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({"message": f"Unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
