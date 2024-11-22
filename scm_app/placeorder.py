# from django.http import JsonResponse
# from django.views import View
# from django.db import connection
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# import json


# class PlaceOrder(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def get_user_from_token(self, request):
#         """
#         Extracts user_id and role_name from the access token in the Authorization header.
#         """
#         auth = JWTAuthentication()
#         try:
#             # Extract token from Authorization header
#             token = request.headers.get('Authorization', '').split(' ')[1]
#             validated_token = auth.get_validated_token(token)
#             user_id = validated_token.get('customer_id')
#             role_name = validated_token.get('role_name')
#             if not user_id or not role_name:
#                 return None, None
#             return user_id, role_name

#         except (InvalidToken, TokenError, IndexError):
#             return None, None

#     def put(self, request, *args, **kwargs):
#         """
#         Updates `is_placed_order` to 'Y' and `payment_method` to 'Credit'
#         for a given `order_id` and `order_product_id`.
#         """
#         try:
#             # Authenticate user
#             user_id, role_name = self.get_user_from_token(request)
#             if not user_id or not role_name:
#                 return JsonResponse({'error': 'Authentication failed. Invalid or missing token.'}, status=401)

#             # Parse the request body
#             body = json.loads(request.body)
#             order_id = body.get('order_id')
#             order_product_id = body.get('order_product_id')

#             if not order_id or not order_product_id:
#                 return JsonResponse({'error': 'order_id and order_product_id are required.'}, status=400)

#             # Update the `is_placed_order` and `payment_method`
#             with connection.cursor() as cursor:
#                 update_query = """
#                     UPDATE order_table_product
#                     SET is_placed_order = 'Y', payment_method = 'Credit'
#                     WHERE order_id = %s AND order_product_id = %s
#                 """
#                 cursor.execute(update_query, [order_id, order_product_id])

#                 # Check if the update was successful
#                 if cursor.rowcount == 0:
#                     return JsonResponse({'error': 'No matching records found to update.'}, status=404)

#             # Send success message
#             return JsonResponse({
#                 'message': 'Order placed successfully.',
#                 'updated_details': {
#                     'order_id': order_id,
#                     'order_product_id': order_product_id,
#                     'is_placed_order': 'Y',
#                     'payment_method': 'Credit'
#                 }
#             }, status=200)

#         except Exception as e:
#             return JsonResponse({'error': f"An error occurred: {str(e)}"}, status=500)


# from django.http import JsonResponse
# from django.views import View
# from django.db import connection
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# import json


# class PlaceOrder(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def get_user_from_token(self, request):
#         """
#         Extracts user_id and role_name from the access token in the Authorization header.
#         """
#         auth = JWTAuthentication()
#         try:
#             token = request.headers.get('Authorization', '').split(' ')[1]
#             validated_token = auth.get_validated_token(token)
#             user_id = validated_token.get('customer_id')
#             role_name = validated_token.get('role_name')
#             if not user_id or not role_name:
#                 return None, None
#             return user_id, role_name

#         except (InvalidToken, TokenError, IndexError):
#             return None, None

#     def put(self, request, *args, **kwargs):
#         """
#         Updates `is_placed_order` to 'Y' and `payment_method` for a given `order_id` and `order_product_id`.
#         """
#         try:
#             # Authenticate user
#             user_id, role_name = self.get_user_from_token(request)
#             if not user_id or not role_name:
#                 return JsonResponse({'error': 'Authentication failed. Invalid or missing token.'}, status=401)

#             # Parse the request body
#             body = json.loads(request.body)
#             order_id = body.get('order_id')
#             order_product_id = body.get('order_product_id')
#             product_name = body.get('product_name')
#             sku = body.get('sku')
#             quantity = body.get('quantity')
#             free = body.get('free')
#             scheme_name = body.get('scheme_name')
#             total_amount = body.get('total_amount')
#             payment_method = body.get('payment_method')

#             if not (order_id and order_product_id and payment_method):
#                 return JsonResponse({'error': 'order_id, order_product_id, and payment_method are required.'}, status=400)

#             # Update the `is_placed_order` and `payment_method`
#             with connection.cursor() as cursor:
#                 update_query = """
#                     UPDATE placeorder
#                     SET is_placed_order = 'Y', payment_method = %s
#                     WHERE stockiest_order_id = %s 
#                 """
#                 cursor.execute(update_query, [payment_method, order_id])

#                 if cursor.rowcount == 0:
#                     return JsonResponse({'error': 'No matching records found to update.'}, status=404)

#             # Send success response
#             return JsonResponse({
#                 "message": "Order placed successfully.",
#                 "order_details": {
#                     "order_id": order_id,
#                     "order_product_id": order_product_id,
#                     "product_name": product_name,
#                     "sku": sku,
#                     "quantity": quantity,
#                     "free": free,
#                     "scheme_name": scheme_name,
#                     "total_amount": total_amount,
#                     "payment_method": payment_method,
#                     "is_placed_order": "Y"
#                 }
#             }, status=200)

#         except Exception as e:
#             return JsonResponse({'error': f"An error occurred: {str(e)}"}, status=500)




from django.http import JsonResponse
from django.views import View
from django.db import connection
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
import json


class PlaceOrder(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_user_from_token(self, request):
        """
        Extracts user_id and role_name from the access token in the Authorization header.
        """
        auth = JWTAuthentication()
        try:
            token = request.headers.get('Authorization', '').split(' ')[1]
            validated_token = auth.get_validated_token(token)
            user_id = validated_token.get('customer_id')
            role_name = validated_token.get('role_name')
            if not user_id or not role_name:
                return None, None
            return user_id, role_name

        except (InvalidToken, TokenError, IndexError):
            return None, None

    def put(self, request, *args, **kwargs):
        """
        Updates `is_placed_order` to 'Y' and `payment_method` for a given `order_id` and `order_product_id`.
        """
        try:
            # Authenticate user
            user_id, role_name = self.get_user_from_token(request)
            if not user_id or not role_name:
                return JsonResponse({'error': 'Authentication failed. Invalid or missing token.'}, status=401)

            # Parse the request body
            body = json.loads(request.body)
            order_id = body.get('order_id')
            order_product_id = body.get('order_product_id')
            product_name = body.get('product_name')
            sku = body.get('sku')
            quantity = body.get('quantity')
            free = body.get('free')
            scheme_name = body.get('scheme_name')
            total_amount = body.get('total_amount')
            payment_method = body.get('payment_method')

            if not (order_id and order_product_id and payment_method):
                return JsonResponse({'error': 'order_id, order_product_id, and payment_method are required.'}, status=400)

            # Update the `is_placed_order` and `payment_method`
            with connection.cursor() as cursor:
                update_query = """
                    UPDATE placeorder
                    SET is_placed_order = 'Y', payment_method = %s
                    WHERE stockiest_order_id = %s 
                """
                cursor.execute(update_query, [payment_method, order_id])

                if cursor.rowcount == 0:
                    return JsonResponse({'error': 'No matching records found to update.'}, status=404)

            # Send success response without order details
            return JsonResponse({
                "message": "Order placed successfully."
            }, status=200)

        except Exception as e:
            return JsonResponse({'error': f"An error occurred: {str(e)}"}, status=500)
