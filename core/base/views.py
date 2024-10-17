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

    def get_paginated_response(self, data):
        return Response({"count": self.page.paginator.count, "results": data})


# ModelViewSet kullanarak değişiklik yapıyoruz
class BaseViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == "list" and hasattr(self, "list_serializer"):
            return self.list_serializer
        elif self.action == "retrieve" and hasattr(self, "retrieve_serializer"):
            return self.retrieve_serializer
        elif self.action == "create" and hasattr(self, "create_serializer"):
            return self.create_serializer
        elif self.action == "update" or self.action == "partial_update":
            if hasattr(self, "update_serializer"):
                return self.update_serializer
        return self.serializer_class

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
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return self.success_response(serializer.data)

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

    def success_response(self, data, status_code=200):
        return Response({"status": "success", "data": data}, status=status_code)

    def error_response(self, message, status_code=400):
        return Response({"status": "error", "message": message}, status=status_code)
