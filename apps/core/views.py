import http
import json

from django import views
from django.http import JsonResponse

from .forms import BookForm
from .models import Book
from django.shortcuts import render

from .serializers import Utils

# temp
class Home(views.View):
    def get(self, request):
        return render(request, 'index.html')

class BookView(views.View):

    def get(self, request, book_id=None):
        if book_id is None:
            search_query = request.GET.get('q', None)
            book_list = Book.get_book_list(search_query)
            return JsonResponse(
                data=Utils.serialize_array(book_list),
                status=http.HTTPStatus.OK,
                safe=False
            )
        else:
            try:
                book = Book.get_book_by_id(id=book_id)
            except Book.DoesNotExist:
                return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
            return JsonResponse(
                data=book.to_dict(),
                status=http.HTTPStatus.OK
            )

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        form = BookForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse(
                data={},
                status=http.HTTPStatus.CREATED
            )
        else:
            return JsonResponse(
                data=form.errors,
                status=http.HTTPStatus.BAD_REQUEST
            )

    def put(self, request, book_id):
        try:
            book = Book.get_book_by_id(id=book_id)
            data = json.loads(request.body.decode('utf-8'))
            form = BookForm(data, instance=book)
            if form.is_valid():
                form.save()
                return JsonResponse(
                    data={},
                    status=http.HTTPStatus.OK
                )
            else:
                return JsonResponse(
                    data=form.errors,
                    status=http.HTTPStatus.BAD_REQUEST
                )

        except Book.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)

    def delete(self, request, book_id):
        try:
            book = Book.get_book_by_id(id=book_id)
        except Book.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
        book.delete()
        return JsonResponse(
            data={},
            status=http.HTTPStatus.OK
        )
