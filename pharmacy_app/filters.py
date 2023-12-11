import django_filters
from django_filters import DateFilter

from .models import *
from store.models import *
class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created",lookup_expr='gte')#greater than equal gte
    end_date = DateFilter(field_name="date_created",lookup_expr ='lte')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','total_bill','quantity']



class FinaledOrderFilter(django_filters.FilterSet):
    class Meta:
        model = Finaled_order
        fields = '__all__'
        exclude = ['total']

