from rest_framework import serializers
from .models import Cliente2
<<<<<<< HEAD
from .models import OfertaProducto, PseudoJoin
from tienda_almacen.models import Producto
from tienda_almacen.serializer import ProductoSerializer
=======
from .models import OfertaProducto
from tienda_almacen.models import Producto
>>>>>>> b33096b293b252160e6f4f3ea609da2e58199d33



from rest_framework.fields import CurrentUserDefault

class Cliente2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente2
        fields = ('cedula','nombre','url','lastname','email','phone','seller','contra')





class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = '__all__'

   


<<<<<<< HEAD
=======
       


class getProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
   


>>>>>>> b33096b293b252160e6f4f3ea609da2e58199d33
class OfertaSerializer(serializers.ModelSerializer):
    producto = getProductsSerializer(read_only=True)
    class Meta:
<<<<<<< HEAD
        model = PseudoJoin
        fields = '__all__'


class JoinFalso(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PseudoJoin
        fields = ('id','url','vendedor','productos')

class JoinFalso2(serializers.ModelSerializer):
    vendedor = LoginSerializer()
    productos = ProductoSerializer()
    class Meta:
        model = PseudoJoin
        fields = ('id','url','vendedor','productos')
=======
        model = OfertaProducto
        fields = '__all__'
>>>>>>> b33096b293b252160e6f4f3ea609da2e58199d33
