from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
#from django.core.urlresolvers import reverse   #Django 2.0 removes the django.core.urlresolvers module, which was moved to 
# django.urls in version 1.10. https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

#@login_required is decorator used to restrict access to 'users' data
@login_required  
def topics(request):
    """Show all topics."""
    #topics = Topic.objects.order_by('date_added')
    #Restricting Topics Access to Appropriate Users. Above line doesn't restrict
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')

    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required  
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required  
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            #form.save()
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required  
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    #kp: When the following two lines were accidentally indented at the same level as the 'if form.is_valid():', the
    #    server reported errors and I couldn't open the http://127.0.0.1:8000/new_entry/3/ (also saw errors there).
    # The error was as follows:
    #     ValueError: The view learning_logs.views.new_entry didn't return an HttpResponse object. It returned None instead.
    # So, I googled and found this page https://stackoverflow.com/questions/26258905/the-view-didnt-return-an-httpresponse-object-it-returned-none-instead
    # which said Python is very sensitive to indentation and so on. So, fixing the indentation fixed the problem.
    #
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
    

@login_required  
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Following 2 lines for "Protecting the edit_entry Page"
    if topic.owner != request.user:
        raise Http404


    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
