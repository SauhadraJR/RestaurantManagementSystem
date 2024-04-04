from rest_framework import serializers
from .user_management.models import User
from .table_management.models import Table
from .staff_management.models import Employee, Shift, TimeOffRequest, WorkedHours
from .order_management.models import Order, OrderItem
from .menu_management.models import Category, MenuItem, CustomizationOption
from .kitchen_display.models import KitchenDisplay
from .inventory_management.models import Ingredient
from .accounting.models import Bill

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'email']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class TimeOffRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeOffRequest
        fields = '__all__'

class WorkedHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkedHours
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class CustomizationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizationOption
        fields = '__all__'

class KitchenDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenDisplay
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

