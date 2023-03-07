import http
import json

from django import views
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import BookForm, PaperForm, EventForm, ContractForm, PlanForm, PlanApplicationForm, DocumentForm, \
    CostTopicForm, CostSectionForm
from .models import Book, Paper, Event, Contract, Plan, PlanApplication, Document, CostTopic, CostSection
from django.shortcuts import render

from .serializers import Utils


class PlanView(views.View):
    def get(self, request, plan_id=None):
        if plan_id is None:
            search_query = request.GET.get('q', None)
            plan_list = Plan.get_plan_list(search_query)
            return render(
                request,
                "plan.html",
                context= {'data': Utils.serialize_array(plan_list)},
                status=http.HTTPStatus.OK,
            )
        else:
            try:
                plan = Plan.get_plan_by_id(id=plan_id)
            except Plan.DoesNotExist:
                return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
            return JsonResponse(
                data=plan.to_dict(),
                status=http.HTTPStatus.OK
            )

    def post(self, request):
        #data = json.loads(request.body.decode('utf-8'))
        data = request.POST

        form = PlanForm(data)
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

    def put(self, request, plan_id):
        try:
            plan = Plan.get_plan_by_id(id=plan_id)
            #data = json.loads(request.body.decode('utf-8'))
            data = request.POST
            form = PlanForm(data, instance=plan)
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

        except Plan.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)

    def delete(self, request, plan_id):
        try:
            plan = Plan.get_plan_by_id(id=plan_id)
        except Plan.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
        plan.delete()
        return JsonResponse(
            data={},
            status=http.HTTPStatus.OK
        )


class DocumentView(views.View):
    def get(self, request, plan_id, document_id=None):
        if document_id is None:
            try:
                plan = Plan.get_plan_by_id(plan_id)
                document_list = plan.get_document_set()
            except Plan.DoesNotExist:
                return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
            return JsonResponse(
                data=Utils.serialize_array(document_list),
                status=http.HTTPStatus.OK,
                safe=False
            )
        else:
            try:
                document = Document.get_document_by_id(id=document_id)
            except Document.DoesNotExist:
                return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
            return JsonResponse(
                data=document.to_dict(),
                status=http.HTTPStatus.OK
            )

    def post(self, request,plan_id):
        #data = json.loads(request.body.decode('utf-8'))
        data = request.POST
        form = DocumentForm(data , request.FILES)
        if form.is_valid():
            new_doc = form.save(commit = False)
            try:
                plan = Plan.get_plan_by_id(plan_id)
            except Plan.DoesNotExist:
                return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
            new_doc.plan = plan
            new_doc.save()
            return JsonResponse(
                data={},
                status=http.HTTPStatus.CREATED
            )
        else:
            return JsonResponse(
                data=form.errors,
                status=http.HTTPStatus.BAD_REQUEST
            )

    def put(self, request, document_id,plan_id):
        try:
            document = Document.get_document_by_id(id=document_id)
            #data = json.loads(request.body.decode('utf-8'))
            data = request.POST
            form = DocumentForm(data,request.FILES, instance=document)
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

        except Document.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)

    def delete(self, request, document_id,plan_id):
        try:
            document = Document.get_document_by_id(id=document_id)
        except Document.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
        document.delete()
        return JsonResponse(
            data={},
            status=http.HTTPStatus.OK
        )


class ApplicationView(views.View):
    def get(self, request, plan_id):
        plan = Plan.get_plan_by_id(plan_id)
        application = plan.application
        if application is None:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
        else:
            return JsonResponse(
                data=application.to_dict(),
                status=http.HTTPStatus.OK
            )

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        form = PlanApplicationForm(data)
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

    def put(self, request, plan_id):
        try:
            plan = Plan.get_plan_by_id(id=plan_id)
            data = json.loads(request.body.decode('utf-8'))
            form = PlanApplicationForm(data, instance=plan.application)
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

        except PlanApplication.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)





class CostSectionView(views.View):
    def get(self, request, topic_id, section_id=None):
        if section_id is None:
            topic = CostTopic.get_topic_by_id(topic_id)
            section_list = topic.get_topic_set()
            return JsonResponse(
                data=Utils.serialize_array(section_list),
                status=http.HTTPStatus.OK,
                safe=False
            )
        else:
            try:
                section = CostSection.get_section_by_id(id=section_id)
            except CostSection.DoesNotExist:
                return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
            return JsonResponse(
                data=section.to_dict(),
                status=http.HTTPStatus.OK
            )

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        form = CostSectionForm(data)
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

    def put(self, request, section_id):
        try:
            section = CostSection.get_section_by_id(id=section_id)
            data = json.loads(request.body.decode('utf-8'))
            form = CostSectionForm(data, instance=section)
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

        except CostSection.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)

    def delete(self, request, section_id):
        try:
            section = CostSection.get_section_by_id(id=section_id)
        except CostSection.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
        section.delete()
        return JsonResponse(
            data={},
            status=http.HTTPStatus.OK
        )


class TopicView(views.View):
    def get(self, request, plan_id, topic_id=None):
        if topic_id is None:
            plan = Plan.get_plan_by_id(plan_id)
            application = plan.application
            topic_list = application.get_topic_set()
            return JsonResponse(
                data=Utils.serialize_array(topic_list),
                status=http.HTTPStatus.OK,
                safe=False
            )
        else:
            try:
                topic = CostTopic.get_topic_by_id(id=topic_id)
            except CostTopic.DoesNotExist:
                return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
            return JsonResponse(
                data=topic.to_dict(),
                status=http.HTTPStatus.OK
            )

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        form = CostTopicForm(data)
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

    def put(self, request, topic_id):
        try:
            topic = CostTopic.get_topic_by_id(id=topic_id)
            data = json.loads(request.body.decode('utf-8'))
            form = CostTopicForm(data, instance=topic)
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

        except CostTopic.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)

    def delete(self, request, topic_id):
        try:
            topic = CostTopic.get_topic_by_id(id=topic_id)
        except CostTopic.DoesNotExist:
            return JsonResponse(data={}, status=http.HTTPStatus.NOT_FOUND)
        topic.delete()
        return JsonResponse(
            data={},
            status=http.HTTPStatus.OK
        )


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
        #data = json.loads(request.body.decode('utf-8'))
        data = request.POST
        form = BookForm(data , request.FILES)
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
            #data = json.loads(request.body.decode('utf-8'))
            data = request.POST
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
                    status=http.HTTPStatus.BAD_REQUEST,
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
        #data = json.loads(request.body.decode('utf-8'))
        data = request.POST
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
            #data = json.loads(request.body.decode('utf-8'))
            data = request.POST
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
        #data = json.loads(request.body.decode('utf-8'))
        data = request.POST
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
            #data = json.loads(request.body.decode('utf-8'))
            data = request.POST
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

class UploadDocumentView(views.View):
    pass