import http
import json

from django import views
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import BookForm, PaperForm, EventForm, ContractForm
from .models import Book, Paper, Event, Contract
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

class PaperView(views.View):
    def get(self, request, paper_id=None):
        if paper_id is None:
            search_query = request.GET.get('q', None)
            paper_list = Paper.get_paper_list(search_query)
            return JsonResponse(
                data=Utils.serialize_array(paper_list),
                status=http.HTTPStatus.OK,
                safe=False
            )
        else:
            try:
                paper = Paper.get_paper_by_id(id=paper_id)
            except Paper.DoesNotExist:
                return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
            return JsonResponse(
                data=paper.to_dict(),
                status=http.HTTPStatus.OK
            )

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        form = PaperForm(data)
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

    def put(self, request, paper_id):
        try:
            paper = Paper.get_paper_by_id(id=paper_id)
            data = json.loads(request.body.decode('utf-8'))
            form = PaperForm(data, instance=paper)
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

        except Paper.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)

    def delete(self, request, paper_id):
        try:
            paper = Paper.get_paper_by_id(id=paper_id)
        except Paper.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
        paper.delete()
        return JsonResponse(
            data={},
            status=http.HTTPStatus.OK
        )


class EventView(views.View):
    def get(self, request, event_id=None):
        if event_id is None:
            search_query = request.GET.get('q', None)
            event_list = Event.get_event_list(search_query)
            return JsonResponse(
                data=Utils.serialize_array(event_list),
                status=http.HTTPStatus.OK,
                safe=False
            )
        else:
            try:
                event = Event.get_event_by_id(id=event_id)
            except Event.DoesNotExist:
                return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
            return JsonResponse(
                data=event.to_dict(),
                status=http.HTTPStatus.OK
            )

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        form = EventForm(data)
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

    def put(self, request, event_id):
        try:
            event = Event.get_event_by_id(id=event_id)
            data = json.loads(request.body.decode('utf-8'))
            form = EventForm(data, instance=event)
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

        except Event.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)

    def delete(self, request, event_id):
        try:
            event = Event.get_event_by_id(id=event_id)
        except Event.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
        event.delete()
        return JsonResponse(
            data={},
            status=http.HTTPStatus.OK
        )
