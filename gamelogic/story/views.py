import datetime
import time
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse, resolve
from django.views.generic.list_detail import object_detail, object_list
from story.forms import StoryEditForm
from story.models import Story

@login_required
def story_edit(request, slug):
    """ Edit a Story """
    messages.success(request, "Your Story was edited!")

    story = get_object_or_404(Story, slug=slug)
    if request.method == 'POST':
        form = StoryEditForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('story_detail', kwargs={'slug': slug}))
    else:
        form = StoryEditForm()

    return render_to_response('stories/story_edit.html', {
        'form':form,
        'object':story
    }, context_instance=RequestContext(request))
    
@login_required
def story_detail(request, slug):
    """ A Story """
    return object_detail(
        request,
        Story.objects.all(),
        slug=slug,
        template_object_name="story",
        template_name='stories/story_detail.html',
    )
    
@login_required
def story_list(request):
    """ A list of Stories """
    return object_list(
        request,
        Story.objects.all(),
        paginate_by=25,
        template_name='stories/stories_list.html',
        allow_empty=True,
    )