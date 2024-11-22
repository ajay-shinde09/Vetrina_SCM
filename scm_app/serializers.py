# # serializers.py
# from rest_framework import serializers
# from .models import Product, Product1

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['product_id', 'product_name']

# class Product1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product1
#         fields = ['product_id', 'product_name']


from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from .models import Customer
from django.core.cache import cache
from django.utils import timezone
    
class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Cache keys for account locking
        lock_key = f"{email}_lock"
        attempts_key = f"{email}_attempts"
        lock_until_key = f"{email}_lock_until"

        # Check if the account exists
        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            raise serializers.ValidationError("Invalid email.")

        # Check if the account is locked
        is_locked = cache.get(lock_key, False)
        lock_until = cache.get(lock_until_key)

        if is_locked:
            if timezone.now() < lock_until:
                raise serializers.ValidationError("Account is locked due to multiple failed login attempts. Please try again later.")
            else:
                # Unlock the account after the lock period expires
                cache.delete(lock_key)
                cache.delete(attempts_key)
                cache.delete(lock_until_key)
        else:
            # Check if the password is correct
            if not check_password(password, customer.password):
                # Increment failed attempts
                failed_attempts = cache.get(attempts_key, 0) + 1
                cache.set(attempts_key, failed_attempts, timeout=None)

                if failed_attempts >= 5:
                    # Lock the account if 5 failed attempts
                    lock_until = timezone.now() + timezone.timedelta(hours=1)
                    cache.set(lock_key, True, timeout=None)
                    cache.set(lock_until_key, lock_until, timeout=None)
                    raise serializers.ValidationError("Too many failed attempts. Account locked for 1 hour.")
                else:
                    raise serializers.ValidationError("Invalid email or password.")
            else:
                # On successful login, reset attempts and unlock if necessary
                cache.delete(lock_key)
                cache.delete(attempts_key)
                cache.delete(lock_until_key)
        
        data['customer'] = customer
        return data

from rest_framework import serializers

class CustomerauthLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
