# Picture handler
import os
import secrets
from functools import wraps
from flask_login import current_user
from PIL import Image
from flask import current_app, abort


def add_profile_pic(form_picture):
    rand_token = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = rand_token + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/images/' + picture_fn)

    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function
