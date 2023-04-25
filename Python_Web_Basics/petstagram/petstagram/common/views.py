from django.shortcuts import render, redirect
from django.urls import reverse
from pyperclip import copy

from petstagram.common.forms import PhotoCommentForm, SearchPhotosForm
from petstagram.common.models import PhotoLike, PhotoComment
from petstagram.common.utils import get_photo_url, get_user_liked_photos
from petstagram.core.photo_utils import apply_likes_count, apply_user_like_photo
from petstagram.photos.models import Photo


# Create your views here.


def index(request):
    search_form = SearchPhotosForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    photos = Photo.objects.all()
    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)

    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_like_photo(photo) for photo in photos]
    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
        'search_form': SearchPhotosForm(),
    }
    return render(request, 'common/home-page.html', context)


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        PhotoLike.objects.create(photo_id=photo_id)
    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    photo_details_url = request.META['HTTP_HOST'] + reverse('details photo', kwargs={
        'pk': photo_id
    })
    copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))


def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()
    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.save()

    return redirect('index')