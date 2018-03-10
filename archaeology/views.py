from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import  *
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from xhtml2pdf import pisa



#view for projects
def project(request):
    project_details = Projects.objects.all()
    if project_details:
        return render(request,'archaeology/project/project.html',{'project_details':project_details})
    else:
        return render(request,'archaeology/project/project.html',{'error_message':'There are no projects currently going on '})

def add_project(request):
    error_message = ""
    if not request.user.is_authenticated:
        context = {
            'error_pre_message': 'You must be logged in to publish paper', 'error_message': 'Please log in',
            'url': "/login_user/"
        }
        return render(request, 'archaeology/home/error.html', context)
    form = ProjectForm(request.POST or None, request.FILES)
    if request.method == "POST":
        print("Post")
        if form.is_valid():
            publication = form.save(commit=False)
            publication.save()
            return render(request,'archaeology/home/home.html')
    context = {
        'form': form,
        'error_message': error_message,
    }
    return render(request, 'archaeology/project/add_project.html', context)

def delete_project(request,publication_id):
    public = get_object_or_404(Projects,pk=publication_id)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    public.delete()
    return redirect('archaeology:user_details')

def ddelete_project(request):
    all_monument = get_list_or_404(Projects)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    context = {
        'all_monument': all_monument,
        'title':'project',
    }
    return render(request,'archaeology/delete.html',context)

#views for publication
def user_view(request):
    return render(request,'archaeology/publication/first.html')


def publications(request):
    all_publications = Publication.objects.all().order_by('date')
    context = {'all_publications':all_publications}
    return render(request,template_name='archaeology/publication/all_details.html',context=context)

def add_publication(request):
    error_message = ""
    if not request.user.is_authenticated:
        context = {
            'error_pre_message':'You must be logged in to publish paper','error_message':'Please log in','url':"/login_user/"
        }
        return render(request,'archaeology/home/error.html',context)
    user_det = User_profile.objects.get(user=request.user)
    if not user_det.is_premium():
        context = {
            'error_pre_message': 'You must be premium user to publish a paper', 'error_message': 'Please upgrade',
            'url': "/user/"
        }
        return render(request, 'archaeology/home/error.html', context)
    form = PublicationForm(request.POST or None, request.FILES  )
    if request.method == "POST":
        if form.is_valid():
            publication = form.save(commit=False)
            publication.user = request.user
            name = publication.paper.url.split('.')[-1]
            if name == "pdf":
                publication.date = datetime.now()
                publication.save()
                return redirect('archaeology:home')
            error_message = "Only pdf forms are supported"
    context = {
        'form':form,
        'error_message':error_message,
    }
    return render(request,'archaeology/publication/add_publication.html',context)

def view_publication(request,publication_id):
    publication = get_object_or_404(Publication,pk=publication_id)
    return render(request,'archaeology/publication/view_publication.html',{'publication':publication})

def view_detailed_publication(request,publication_id):
    user_det = get_object_or_404(User_profile,user=request.user)
    if user_det.is_premium():
        publication= get_object_or_404(Publication,pk=publication_id)
        return HttpResponse(publication.paper,content_type='application/pdf')
    context = {
        'error_pre_message': 'You should be a premium user to view this.',
        'error_message': 'Upgrade', 'url': '/user',
    }
    return render(request, 'archaeology/home/error.html', context)

def delete_publicaton(request,publication_id):
    public = get_object_or_404(Publication,pk=publication_id)
    if not request.user == public.user:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    public.delete()
    return redirect('archaeology:publication')

def search_publication(request):
    publication = Publication.objects.all()
    query = request.GET.get("q")
    if query:
        museum1 = publication.filter(
            Q(name__icontains=query)
        ).distinct()

        return render(request, 'archaeology/home/search.html', {
            'museum1':museum1,
        })
    return HttpResponse("There are no search results")

def user_publication(request):
    if not request.user.is_authenticated:
        return redirect('archaeology:login_user')
    public = Publication.objects.filter(user=request.user)
    return render(request,'archaeology/user/user_details.html',{'public':public})

#views for users
def user_details(request):
    if request.user.is_authenticated:
        user_det= get_object_or_404(User_profile,user=request.user)
        if request.user.is_superuser:
            msg = message.objects.all()
            if msg:
                return render(request,'archaeology/user/admin_details.html',{'user_det':user_det,'msg':msg})
            return render(request,'archaeology/user/admin_details.html',{'user_det':user_det})
        comments = feedback.objects.filter(user=request.user)
        comments2 = artifact_feedback.objects.filter(user=request.user)
        comments3 = museum_feedback.objects.filter(user=request.user)
        tick = Buy_ticket.objects.filter(user=request.user)
        tick1 = Buy_excavation_ticket.objects.filter(user=request.user)
        tick2 = Buy_museum_ticket.objects.filter(user=request.user)
        context = {'user_det':user_det}
        if comments:
            context.update( {'comments':comments})
        if comments2:
            context.update({'comments2':comments2})
        if comments3:
           context.update( {'comments3':comments3})
        if tick:
            context.update( {'tick':tick})
        if tick1:
            context.update({'tick1': tick1})
        if tick2:
            context.update({'tick2':tick2 })
        return render(request,'archaeology/user/details.html',context)
    return redirect('archaeology:login_user')

def logout_user(request):
    logout(request)
    return redirect('archaeology:login_user')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('archaeology:user_details')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('archaeology:home')
            else:
                return render(request, 'archaeology/user/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'archaeology/user/login.html', {'error_message': 'Invalid login'})
    return render(request, 'archaeology/user/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('archaeology:user_details')
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user_det = form.save(commit=False)
            username = form.cleaned_data['username']
            emailid = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=emailid, password=password)
            user.set_password(password)
            user.save()
            print("USer save")
            user = authenticate(username=username, password=password)
            user_det.user = user
            user_det.user_type = "visitor"
            print ("Hi")
            user_det.save()
            print ("SAVE")
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('archaeology:home')
    context = {
            "form": form,
        }
    return render(request, 'archaeology/user/register.html', context)

def upgrade (request):
    if request.user.is_authenticated:
        user_det = get_object_or_404(User_profile,user=request.user)
        user_det.user_type = "archaeologist"
        user_det.save()
        return redirect('archaeology:user_details')
    else:
        return redirect('archaeology:login_user')


# Create your views here.
def home(request):
	return render(request,'archaeology/home/home.html' )

def mission(request):
    return render(request,'archaeology/home/mission.html')

def search(request):
    museum = Museum.objects.all()
    artifact = Artifact.objects.all()
    monument = Monument.objects.all()
    query = request.GET.get("q")
    if query:
        museum1 = museum.filter(
            Q(name__icontains=query)
        ).distinct()
        artifact1 = artifact.filter(
            Q(name__icontains=query)
        ).distinct()
        monument1 = monument.filter(
            Q(name__icontains=query)
        ).distinct()

        return render(request, 'archaeology/home/search.html', {
            'museum1':museum1,'artifact1':artifact1,'monument1':monument1
        })

def contact(request):
    form = MessageForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            museum = form.save(commit=False)
            museum.save()
            return redirect('archaeology:home')
    context = {'form': form}
    return render(request, 'archaeology/home/details.html', context)

#views for library
def Library_all(request):
    all_library = Library.objects.all()
    return render(request, 'archaeology/library/library.html', {'all_library':all_library})

def Library_details(request,Library_id):
    library = get_object_or_404(Library,pk = Library_id)
    books = Books.objects.filter(library=library)
    return render(request,'archaeology/library/details.html',{'library':library,'books':books})

def add_library(request):
    if not request.user.is_superuser:
        return render(request, 'archaeology/home/error.html',
                          {'error_message': "Your are not allowed to add Museum"})
    form = LibraryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        museum = form.save(commit=False)
        museum.save()
        return redirect('archaeology:home')
    context = {'form': form}
    return render(request, 'archaeology/library/add_library.html', context)

def delete_library(request,publication_id):
    public = get_object_or_404(Library,pk=publication_id)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    public.delete()
    return redirect('archaeology:user_details')

def ddelete_library(request):
    all_monument = get_list_or_404(Library)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    context = {
        'all_monument': all_monument,
        'title':'library',
    }
    return render(request,'archaeology/delete.html',context)

def good_feedback(request):
    #feedback_user = feedback.objects.filter(rating=5)
    #feedback_user1= feedback.objects.filter(rating=4)
    feedback_user2 = feedback.objects.filter(Q(text__contains="good")).distinct()
    feedback_user = feedback.objects.filter(Q(text__contains="best")).distinct()
    feedback_user1 = feedback.objects.filter(Q(text__contains="nice")).distinct()
    return render(request,'archaeology/good_feedback.html',{'feedback_user':feedback_user,'feedback_user1':feedback_user1,'feedback_user2':feedback_user2})



#views for artifact
def artifact_all(request):
    all_artifact = Artifact.objects.all()
    return render(request, 'archaeology/artifact/artifact.html', {'all_artifact':all_artifact})

def artifact_details(request,artifact_id):
    monument = get_object_or_404(Artifact,pk = artifact_id);
    feedback_user = artifact_feedback.objects.filter(artifact=monument)
    return render(request,'archaeology/artifact/artifact_details.html',{'monument':monument, 'feedback_user':feedback_user})

def create_artifact_feedback(request,artifact_id):
    if not request.user.is_authenticated():
        return render(request, 'archaeology/user/login.html',{'error_message':"You must login to give feedback"})
    else:
        form = ArtifactFeedbackForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            artifact = get_object_or_404(Artifact,pk=artifact_id)
            feedback.artifact = artifact
            feedback.save()
            return render(request, 'archaeology/home/home.html')
    context = {'form': form}
    return render(request, 'archaeology/monument/give_feedback.html', context)

def add_artifact(request):
    if not request.user.is_superuser:
        return render(request, 'archaeology/home/error.html',
                          {'error_message': "Your are not allowed to add Museum"})
    form = ArtifactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        museum = form.save(commit=False)
        museum.save()
        return redirect('archaeology:home')
    context = {'form': form}
    return render(request, 'archaeology/artifact/forms.html', context)

def delete_artifact_feedback(request,feedback_id):
    feed = get_object_or_404(artifact_feedback,pk=feedback_id)
    feed.delete()
    return redirect('archaeology:user_details')


def delete_artifact(request,publication_id):
    public = get_object_or_404(Artifact,pk=publication_id)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    public.delete()
    return redirect('archaeology:user_details')

def ddelete_artifact(request):
    all_monument = get_list_or_404(Artifact)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    context = {
        'all_monument': all_monument,
        'title':'artifact',
    }
    return render(request,'archaeology/delete.html',context)

#details for monuments
def monument_all(request):
    all_monument = Monument.objects.all()
    return render(request, 'archaeology/monument/monument.html', {'all_monument':all_monument})

def monument_details(request,monument_id):
    monument = get_object_or_404(Monument,pk = monument_id);
    feedback_user = feedback.objects.filter(monument = monument);
    tick =Ticket.objects.filter( monument=monument)
    return render(request,'archaeology/monument/monument_detail.html',{'monument':monument, 'feedback_user':feedback_user,'tick':tick})

def create_feedback(request,monument_id):
    if not request.user.is_authenticated():
        return render(request, 'archaeology/user/login.html',{'error_message':"You must login to give feedback"})
    else:
        form = FeedbackForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            monument = get_object_or_404(Monument,pk=monument_id)
            feedback.monument =monument
            feedback.save()
            return render(request, 'archaeology/home/home.html')
    context = {'form': form}
    return render(request, 'archaeology/monument/give_feedback.html', context)

def delete_feedback(request,feedback_id):
    feed = get_object_or_404(feedback,pk=feedback_id)
    feed.delete()
    return redirect('archaeology:user_details')

def buy_ticket(request,monument_id):
    if request.user.is_authenticated:
        form = ticketform(request.POST or None)
        monument = get_object_or_404(Monument, pk=monument_id)
        tick = get_object_or_404(Ticket, monument=monument)
        if request.method == 'POST' and form.is_valid():
            tic_object = form.save(commit=False)
            tic_object.ticket = tick
            tic_object.user = request.user
            tic_object.calculate()

            tic_object.save()
            a = tic_object.pk
            print (a);
            adult_total = tic_object.ticket.adult_ticket_rate * tic_object.adult_no
            child_total = tic_object.ticket.child_ticket_rate * tic_object.child_no
            context = {'tic_object':tic_object ,'adult_total':adult_total,'child_total':child_total}
            return render(request,'archaeology/ticket/bought.html',context)
        else:
            context = {'form':form,'tick':tick,'monument_id':monument_id}
            return render(request,'archaeology/ticket/ticket.html',context)
    return redirect('archaeology:login_user')

def download_ticket(request,ticket_id):
    template = get_template('archaeology/ticket/invoice.html')
    tick_object = get_object_or_404(Buy_ticket,pk=ticket_id)
    primary = tick_object.pk
    user_name = tick_object.user.get_username
    monument_name = tick_object.ticket.monument.name
    adult_ticket_rate = tick_object.ticket.adult_ticket_rate
    child_ticket_rate = tick_object.ticket.child_ticket_rate
    adult_no = tick_object.adult_no
    child_no = tick_object.child_no
    total = tick_object.amount
    adult_total = tick_object.ticket.adult_ticket_rate * tick_object.adult_no
    child_total = tick_object.ticket.child_ticket_rate * tick_object.child_no
    context = {'tick_object':tick_object,'adult_total':adult_total,'child_total':child_total, 'user_name':user_name,
              'monument_name':monument_name,'adult_ticket_rate':adult_ticket_rate, 'child_ticket_rate':child_ticket_rate,
               'adult_no':adult_no,'child_no':child_no ,'total':total,'primary':primary
               }
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Not available")

def add_monument(request):
    if not request.user.is_superuser:
        return render(request, 'archaeology/home/error.html',
                          {'error_message': "Your are not allowed to add Museum"})
    form = MonumentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        museum = form.save(commit=False)
        museum.save()
        return redirect('archaeology:home')
    context = {'form': form}
    return render(request, 'archaeology/monument/forms.html', context)

def ddelete_monument(request):
    all_monument = get_list_or_404(Monument)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    context = {
        'all_monument': all_monument,
        'title':'monument',
    }
    return render(request,'archaeology/delete.html',context)


def delete_monument(request,monument_id):
    public = get_object_or_404(Monument,pk=monument_id)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    public.delete()
    return redirect('archaeology:user_details')

#functions for museums

def add_museum(request):
    if not request.user.is_superuser:
        return render(request, 'archaeology/home/error.html',{'error_pre_message':"Your are not allowed to add Museum",
                                                              'error_message':"Go back",'url':""})
    else:
        form = MusuemForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            museum = form.save(commit = False)
            museum.save()
            return redirect('archaeology:home')
        context = {'form': form}
        return render(request, 'archaeology/museum/add_museum.html', context)

def musuem_all(request):
    all_museum = Museum.objects.all()
    return render(request, 'archaeology/museum/musuem.html', {'all_museum': all_museum})

def musuem_details(request, musuem_id):
    monument = get_object_or_404(Museum, pk=musuem_id);
    feedback_user = museum_feedback.objects.filter(musuem=monument);
    return render(request, 'archaeology/museum/musuem_details.html',
                      {'monument': monument, 'feedback_user': feedback_user})

def create_museum_feedback(request,museum_id):
    form = MuseumFeedbackForm(request.POST or None)
    if not request.user.is_authenticated():
        return render(request, 'archaeology/user/login.html',{'error_message':"You must login to give feedback"})
    else:
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            museum = get_object_or_404(Museum,pk=museum_id)
            feedback.musuem = museum
            feedback.save()
            return render(request, 'archaeology/home/home.html')
    form = MuseumFeedbackForm(request.POST or None, request.FILES or None)
    context = {'form': form}
    return render(request, 'archaeology/monument/give_feedback.html', context)

def buy_museum_ticket(request, museum_id):
    if request.user.is_authenticated:
        form = MuseumTicketForm(request.POST or None)
        museum = get_object_or_404(Museum, pk=museum_id)
        tick = get_object_or_404(Museum_ticket, museum=museum)
        if request.method == 'POST' and form.is_valid():
            tic_object = form.save(commit=False)
            tic_object.ticket = tick
            tic_object.user = request.user
            tic_object.calculate()
            tic_object.save()
            adult_total = tic_object.ticket.adult_ticket_rate * tic_object.adult_no
            child_total = tic_object.ticket.child_ticket_rate * tic_object.child_no
            context = {'tic_object': tic_object, 'adult_total': adult_total, 'child_total': child_total}
            return render(request, 'archaeology/ticket/archaeology/bought.html', context)
        else:
             context = {'form': form, 'tick': tick, 'museum':museum}
             return render(request, 'archaeology/ticket/archaeology/ticket.html', context)
    return redirect('archaeology:login_user')

def download_museum_ticket(request, ticket_id):
    template = get_template('archaeology/ticket/archaeology/invoice.html')
    tick_object = get_object_or_404(Buy_museum_ticket , pk =ticket_id)
    primary = tick_object.pk
    user_name = tick_object.user.get_username
    monument_name = tick_object.ticket.museum.name
    adult_ticket_rate = tick_object.ticket.adult_ticket_rate
    child_ticket_rate = tick_object.ticket.child_ticket_rate
    adult_no = tick_object.adult_no
    child_no = tick_object.child_no
    total = tick_object.amount
    adult_total = tick_object.ticket.adult_ticket_rate * tick_object.adult_no
    child_total = tick_object.ticket.child_ticket_rate * tick_object.child_no
    context = {
               'adult_total': adult_total,
               'child_total': child_total,
               'user_name': user_name,
               'monument_name': monument_name,
               'adult_ticket_rate': adult_ticket_rate,
               'child_ticket_rate': child_ticket_rate,
               'adult_no': adult_no,
               'child_no': child_no,
               'total': total,
               'primary': primary,
               }
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Not available")

def delete_museum(request,publication_id):
    public = get_object_or_404(Museum,pk=publication_id)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    public.delete()
    return redirect('archaeology:user_details')

def delete_museum_feedback(request,feedback_id):
    feed = get_object_or_404(museum_feedback,pk=feedback_id)
    feed.delete()
    return redirect('archaeology:user_details')

def ddelete_museum(request):
    all_monument = get_list_or_404(Museum)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    context = {
        'all_monument': all_monument,
        'title':'museum',
    }
    return render(request,'archaeology/delete.html',context)


# functions for Excavations
def excavation_all(request):
    all_excavation = Excavations.objects.all()
    return render(request, 'archaeology/excavation/excavation.html', {'all_excavation':all_excavation})

def excavation_details(request,excavation_id):
    excavation = get_object_or_404(Excavations,pk = excavation_id)
    return render(request,'archaeology/excavation/excavation_details.html',{'excavation':excavation })

def buy_excavation_ticket(request, excavation_id):
    if request.user.is_authenticated:
        form = ExcavationTicketForm(request.POST or None)
        excavation = get_object_or_404(Excavations, pk=excavation_id)
        tick = get_object_or_404(Excavation_ticket,excavation=excavation)
        if request.method == 'POST' and form.is_valid():
            tic_object = form.save(commit=False)
            tic_object.ticket = tick
            tic_object.user = request.user
            tic_object.calculate()
            tic_object.save()
            adult_total = tic_object.ticket.adult_ticket_rate * tic_object.adult_no
            child_total = tic_object.ticket.child_ticket_rate * tic_object.child_no
            context = {'tic_object': tic_object, 'adult_total': adult_total, 'child_total': child_total}
            return render(request, 'archaeology/ticket/excavation/bought.html', context)
        else:
             context = {'form': form, 'tick': tick, 'excavation':excavation}
             return render(request, 'archaeology/ticket/excavation/ticket.html', context)
    return redirect('archaeology:login_user')

def download_excavation_ticket(request, excavation_id):
    template = get_template('archaeology/ticket/archaeology/invoice.html')
    tick_object = get_object_or_404(Buy_excavation_ticket , pk =excavation_id)
    primary = tick_object.pk
    user_name = tick_object.user.get_username
    monument_name = tick_object.ticket.excavation.name
    adult_ticket_rate = tick_object.ticket.adult_ticket_rate
    child_ticket_rate = tick_object.ticket.child_ticket_rate
    adult_no = tick_object.adult_no
    child_no = tick_object.child_no
    total = tick_object.amount
    adult_total = tick_object.ticket.adult_ticket_rate * tick_object.adult_no
    child_total = tick_object.ticket.child_ticket_rate * tick_object.child_no
    context = {
               'adult_total': adult_total,
               'child_total': child_total,
               'user_name': user_name,
               'monument_name': monument_name,
               'adult_ticket_rate': adult_ticket_rate,
               'child_ticket_rate': child_ticket_rate,
               'adult_no': adult_no,
               'child_no': child_no,
               'total': total,
               'primary': primary,
               }
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Not available")

def add_excavation(request):
    if not request.user.is_superuser:
        return render(request, 'archaeology/home/error.html',
                          {'error_message': "Your are not allowed to add Museum"})
    form = ExcavationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        museum = form.save(commit=False)
        museum.save()
        return redirect('archaeology:home')
    context = {'form': form}
    return render(request, 'archaeology/excavation/add_excavation.html', context)

def delete_excavation(request,publication_id):
    public = get_object_or_404(Excavations,pk=publication_id)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    public.delete()
    return redirect('archaeology:user_details')

def ddelete_excavation(request):
    all_monument = get_list_or_404(Excavations)
    if not request.user.is_superuser:
        context = {
            'error_pre_message':'Your are not authorized to delete the publication',
            'error_message':'Go back','url':'/publication',
        }
        return render(request,'archaeology/home/error.html',context)
    context = {
        'all_monument': all_monument,
        'title':'excavation',
    }
    return render(request,'archaeology/delete.html',context)
