
# class UserViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

# class QualityApi(View):
#     def get(self,requst,*args, **kwargs):
#         qd = Quality.objects.all()
#         serializer = QualitySerializer(qd, many=True)
#         return JsonResponse(serializer.data, safe=False)