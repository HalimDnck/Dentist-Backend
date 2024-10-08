from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "item_per_page"
    max_page_size = 100
    page_query_param = "page"
    ordering_query_param = "ordering"

    def paginate_queryset(self, queryset, request, view=None):
        ordering = request.query_params.get(self.ordering_query_param)
        if ordering:
            queryset = queryset.order_by(ordering)

        return super().paginate_queryset(queryset, request, view)


class BaseViewSet(viewsets.ViewSet):
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == "list" and self.list_serializer is not None:
            return self.list_serializer
        elif self.action == "retrieve" and self.retrieve_serializer is not None:
            return self.retrieve_serializer
        elif self.action == "create" and self.create_serializer is not None:
            return self.create_serializer
        elif self.action == "update" and self.update_serializer is not None:
            return self.update_serializer
        elif self.action == "partial_update" and self.update_serializer is not None:
            return self.update_serializer
        return self.serializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        if hasattr(self, "queryset") and self.queryset is not None:
            return self.queryset
        raise NotImplementedError(
            "get_queryset metodunu implement etmelisiniz ya da queryset tanımlamalısınız."
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        ordering = request.query_params.get("ordering")
        if ordering:
            queryset = queryset.order_by(ordering)

        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def perform_destroy(self, instance):
        # is_deleted flag'ini True yapıyoruz
        instance.is_deleted = True
        instance.deleted_at = timezone.now()  # silinme zamanını ayarlıyoruz
        if hasattr(instance, "deleted_by"):
            # Eğer modelde deleted_by varsa, user'ı set ediyoruz
            instance.deleted_by = self.request.user
        instance.save()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return self.success_response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()
            return self.success_response(serializer.data, status_code=201)

        return self.error_response(serializer.errors, status_code=400)

    def success_response(self, data, status_code=200):
        return Response({"status": "success", "data": data}, status=status_code)

    def error_response(self, message, status_code=400):
        return Response({"status": "error", "message": message}, status=status_code)
