# from django.db import models

# class Division(models.Model):
#     division_id = models.AutoField(primary_key=True)
#     division_name = models.CharField(max_length=255, unique=True)

#     def __str__(self):
#         return self.division_name


# class Product(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=255)
#     sku = models.CharField(max_length=100, null=True, blank=True)
#     product_code = models.CharField(max_length=100, null=True, blank=True)
#     unit = models.CharField(max_length=50, null=True, blank=True)
#     product_division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name="products")
#     sub_division = models.CharField(max_length=100, null=True, blank=True)
#     category_id = models.IntegerField(null=True, blank=True)
#     manufacturer = models.CharField(max_length=255, null=True, blank=True)
#     barcode = models.CharField(max_length=255, null=True, blank=True)
#     shipper_size = models.IntegerField(null=True, blank=True)
#     batch_size = models.IntegerField(null=True, blank=True)
#     hsn_code = models.CharField(max_length=100, null=True, blank=True)
#     ic_code = models.CharField(max_length=100, null=True, blank=True)
#     inventory_days = models.IntegerField(null=True, blank=True)
#     sheme_lot_one_invoice_qnty = models.IntegerField(null=True, blank=True)
#     sheme_lot_one_free_qnty = models.IntegerField(null=True, blank=True)
#     sheme_lot_two_invoice_qnty = models.IntegerField(null=True, blank=True)
#     sheme_lot_two_free_qnty = models.IntegerField(null=True, blank=True)
#     min_inventory_qnty = models.IntegerField(null=True, blank=True)
#     commission = models.FloatField(null=True, blank=True)

#     def __str__(self):
#         return self.product_name


# class Product1(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=255)
#     sku = models.CharField(max_length=100, null=True, blank=True)
#     product_code = models.CharField(max_length=100, null=True, blank=True)
#     unit = models.CharField(max_length=50, null=True, blank=True)
#     product_division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name="products1")
#     sub_division = models.CharField(max_length=100, null=True, blank=True)
#     category_id = models.IntegerField(null=True, blank=True)
#     manufacturer = models.CharField(max_length=255, null=True, blank=True)
#     barcode = models.CharField(max_length=255, null=True, blank=True)
#     shipper_size = models.IntegerField(null=True, blank=True)
#     batch_size = models.IntegerField(null=True, blank=True)
#     hsn_code = models.CharField(max_length=100, null=True, blank=True)
#     ic_code = models.CharField(max_length=100, null=True, blank=True)
#     inventory_days = models.IntegerField(null=True, blank=True)
#     sheme_lot_one_invoice_qnty = models.IntegerField(null=True, blank=True)
#     sheme_lot_one_free_qnty = models.IntegerField(null=True, blank=True)
#     sheme_lot_two_invoice_qnty = models.IntegerField(null=True, blank=True)
#     sheme_lot_two_free_qnty = models.IntegerField(null=True, blank=True)
#     min_inventory_qnty = models.IntegerField(null=True, blank=True)
#     commission = models.FloatField(null=True, blank=True)

#     def __str__(self):
#         return self.product_name

from django.db import models



class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    owner_name = models.TextField(blank=True, null=True)
    mobile_number = models.TextField()
    email = models.TextField()
    password = models.TextField()
    type = models.IntegerField()
    role = models.IntegerField()
    kyc_status = models.CharField(max_length=1)
    approval_status = models.CharField(max_length=1, db_comment='Y -> Approved N -> Declined P->Pending A->Approved by Admin F->Approved by Finance')
    is_block = models.CharField(max_length=1)
    created_on = models.DateTimeField()
    placeorder = models.CharField(max_length=1)
    state_id = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    terms_conditions = models.CharField(max_length=1, db_comment='N - Accepted on Registration\r\nY- Accepted on Mail')
    supplier = models.IntegerField(blank=True, null=True)
    farmer_type = models.CharField(max_length=11, blank=True, null=True)
    dairy_animals = models.IntegerField(blank=True, null=True)
    sheep_goat = models.IntegerField(blank=True, null=True)
    piggery_animals = models.IntegerField(blank=True, null=True)
    layer_birds = models.IntegerField(blank=True, null=True)
    broiler_birds = models.IntegerField(blank=True, null=True)
    reference = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'