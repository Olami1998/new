from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse
from .models import Post
from .forms import CommentForm, PostForm
from django.core.paginator import Paginator

# Create your views here.

#class PostList(generic.ListView):
 #   queryset = Post.objects.filter(status=1).order_by('-created_on')
  #  template_name = 'home/index.html'
   # paginate_by = 3
    
def home(request):
    topics = Post.objects.filter(status=1).order_by('-updated_on')
    paginator = Paginator(topics, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'topics': topics, 'page_obj': page_obj}
    
    return render(request, 'home/index.html', context)




def new_post(request):
    """Add a new post"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # Post data submitted; process data.
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('home:home')
            
    context = {'form': form}
    return render(request, 'home/new_post.html', context)

def edit_post(request, post_id):
    """Edit an existing entry."""
    topic = Post.objects.get(id=post_id)
    if topic.author != request.user:
        raise Http404
    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = PostForm(instance=topic)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:detail',args=[topic.id]))
        
    
    context = {'topic': topic, 'form': form, 'edit_post': edit_post}
    return render(request, 'home/edit_post.html', context)



#def detail(request, ID):
 #   post = Post.objects.get(id=ID)
  #  context = {
   #     "post":post
    #}
    #return render(request, 'home/single.html', context)

def detail(request, slug):
    template_name = 'home/single.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
