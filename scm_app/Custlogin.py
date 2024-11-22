from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from scm_app.serializers import CustomerauthLoginSerializer


class CustomerauthLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CustomerauthLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Use raw SQL to fetch customer and role details
            with connection.cursor() as cursor:
                query = """
                SELECT c.customer_id, c.name, c.email, c.role, r.role_name
                FROM customer c
                JOIN customer_roles r ON c.role = r.cust_role_id
                WHERE c.email = %s AND c.password = %s AND c.is_block = 'N'
                """
                cursor.execute(query, [email, password])
                customer = cursor.fetchone()

            if customer:
                # Manually create a RefreshToken
                refresh = RefreshToken()
                refresh['role_name'] = customer[4]  # Adding role to token
                refresh['customer_id'] = customer[0]
                refresh['email'] = customer[2]

                # Generate access token from refresh token
                access_token = refresh.access_token

                return Response({
                    'refresh': str(refresh),
                    'access': str(access_token),
                    'customer_id': customer[0],
                    'name': customer[1],
                    'email': customer[2],
                    'role_name': customer[4],
                }, status=HTTP_200_OK)
            return Response({'error': 'Invalid credentials or account blocked'}, status=HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
