from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from .forms import CommentForm, SendMail
from django.db.models import Q
from taggit.models import Tag
from django.core.mail import send_mail
from personal.settings import EMAIL_HOST_USER
# Create your views here.


def home(request):
    latest = Post.objects.all()[:5]
    context = {'latest': latest}
    return render(request, 'blog/home.html', context)


def blog_list(request):
    qs = Post.objects.all().order_by('publish')
    r = random.choice(qs)

    paginator = Paginator(qs, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts, 'page': page, 'r': r}
    return render(request, 'blog/blog.html', context)


def post(request, id, post):
    post = get_object_or_404(Post, id=id, slug=post)

    comments = post.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()

    else:
        comment_form = CommentForm()
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(
        tags__in=post_tags_ids).exclude(id=post.id)[:2]
    context = {'post': post, 'similar_posts': similar_posts,
               'comments': comments, 'comment_form': comment_form}
    return render(request, 'blog/blog-single.html', context)


def about(request):
    context = {}
    return render(request, 'blog/about.html', context)


def contact(request):
    success = ''
    if request.method == 'POST':
        form = SendMail(data=request.POST)
        if form.is_valid():
            subject = 'Mail from' + \
                str(form['name']) + 'regarding yoursite.com'
            message = form['message']
            to_email = form['email']
            send_mail(subject, message, EMAIL_HOST_USER,
                      to_email, fail_silently=False)
            form = SendMail()
            success = 'Email Sent successfully'
    else:
        form = SendMail()

    context = {'form': form, 'success': success}
    return render(request, 'blog/contact.html', context)


def search(request):
    objls = Post.objects.all()
    if request.method == 'GET':
        q = request.GET.get('q')
        qs = objls.filter(Q(title__icontains=q) |
                          Q(content__icontains=q)).distinct()
    paginator = Paginator(qs, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {'q': q, 'qs': posts, 'page': page}
    return render(request, 'blog/blog-list-search.html', context)


def search_tag(request, tag_slug):
    objls = Post.objects.all()
    if tag_slug:
        q = tag_slug
        tag = get_object_or_404(Tag, slug=tag_slug)
        qs = objls.filter(tags__in=[tag])
    paginator = Paginator(qs, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    context = {'q': q, 'qs': posts, 'page': page}
    return render(request, 'blog/blog-list-search.html', context)
