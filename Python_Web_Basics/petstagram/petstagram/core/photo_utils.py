def apply_user_like_photo(photo):
    # TODO fix this for user when authentication is created
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo
