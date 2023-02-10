from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
import requests

from .serializers import UserSerializer

from accounts.models import CustomUser, Feedback

# getting api routes exists


class getRoutes(APIView):
    def get(self, request):
        routes = [
            '/api/'
        ]
        return Response(routes)

# creating users


class SignupView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data, many=False)
        if serializer.is_valid():
            new_user = serializer.save()
            # sending post request for getting tokens for this user
            res = requests.post('http://127.0.0.1:8000/auth/token/', data={
                'username': new_user.email,
                # password in serializer is hashed,
                # so get it from request itself
                'password': request.data['password'],
                'client_id': 'dSd1sOYrR8nATOgjWrsdZNd49zk5JVxiGkel3y1S',
                'client_secret': 'kmPDtehwAsC5ozNyC46HCdw7hbOjiqEC4oORapW5pTEuSUkmQ1N5QLhPh0m1EMR0405UqK28791PUCIuRDD3mPU5Qf2DjrBgpnCAEJdsAat25SQWcIft4Yj54K20Ts9c',
                'grant_type': 'password'
            })
            # returning tokens to react
            return Response(res.json(), status=status.HTTP_200_OK)

        # when email already exists
        return Response({
            'message': 'Something went wrong',
        }, status=status.HTTP_400_BAD_REQUEST)

# fetching all user details


class AllUsers(generics.ListAPIView):
    # everyone can access
    permission_classes = [permissions.AllowAny]

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# fetching current user loggedin


class CurrentUser(APIView):
    # only Authenticated users can access
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(self.request.user)

        return Response(serializer.data)

# change user password


class changePasswordView(APIView):
    def post(self, request):
        user = request.user
        data = request.data
        current_password = data['current_password']
        new_password = data['new_password']

        return Response(current_password, new_password)


# new feedback from users
class NewFeedback(APIView):
    def post(self, request):
        try:
            user = request.user
            data = request.data

            feedback = Feedback.objects.create(
                user=user,
                body=data['body']
            )

            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
