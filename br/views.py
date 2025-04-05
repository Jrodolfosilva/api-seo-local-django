import traceback
from django.db import DatabaseError, IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from br.models import Estado
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http.request import HttpRequest
from rest_framework import status

class estadoSerializes (serializers.ModelSerializer):
    class Meta :
        model =  Estado
        fields =  '__all__'


class SerializeDataRequest(serializers.Serializer):
    slug = serializers.CharField()
    uf =  serializers.CharField()
    name = serializers.CharField(max_length=5000)
    full_name = serializers.CharField(max_length=5000)
    uf = serializers.CharField()
    population = serializers.IntegerField()
    area_km2 = serializers.FloatField()
    population_density = serializers.FloatField()
    demonym = serializers.CharField(max_length=5000)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    ibge_code = serializers.IntegerField()
    main_zip_code = serializers.CharField(max_length=150000)
    zip_code_range = serializers.CharField(max_length=5000)
    seo_title = serializers.CharField(max_length=1500060)
    meta_description = serializers.CharField()
    appropriate_preposition = serializers.CharField(max_length=5000)
    description_text = serializers.CharField()
    map_embed = serializers.URLField()
    gdp = serializers.CharField()  
    hdi = serializers.FloatField()
    climate = serializers.CharField(max_length=5000)
    history = serializers.CharField()
    main_activities = serializers.JSONField()
    tourist_attractions = serializers.JSONField()


    def get(self, request:HttpRequest):

        try:
            data = Estado.objects.all()
            
            serial =  estadoSerializes(data, many= True)
            return Response(serial.data, status=200)
            
        except:
            return Response(status=404)
        

class GetEstados (APIView):
    permission_classes = [AllowAny] 

    def get(self,request:HttpRequest):

         try:
            serial =  estadoSerializes(Estado.objects.all(),many=True)
            return Response(serial.data,status=200)
         
         except:
             return Response(status=404)


class GetEstadosSlug (APIView):

    def get(self,request:HttpRequest):

         try:
            parms = request.query_params.get("slug")
            serial = estadoSerializes(Estado.objects.get(slug = parms))
            return Response(serial.data,status=200)
         
         except:
             return Response({"msg":"Not found Estado"},status=404)


class CreateEstados(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request: HttpRequest):
        try:
            serial = SerializeDataRequest(data=request.data)

            if serial.is_valid():
                dataEstado = serial.validated_data

                try:
                    Estado.objects.create(**dataEstado)
                    return Response({"msg": "Estado criado com sucesso!"}, status=status.HTTP_201_CREATED)
                except (DatabaseError, IntegrityError) as db_error:
                    print("Erro ao salvar no banco:", db_error)
                    traceback.print_exc()
                    return Response(
                        {"msg": "Erro ao salvar no banco de dados", "erro": str(db_error)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )

            else:
                return Response(
                    {"msg": "Dados inválidos", "erros": serial.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            print("Erro inesperado:", e)
            traceback.print_exc()
            return Response(
                {"msg": "Erro inesperado", "erro": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )