import os
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import  mail


def save_picture(form_picture):
    random_hex = os.urandom(16).hex()
    f_name, f_ext = os.path.splitext(form_picture.filename)
    # print(form_picture.filename,"extension: ", f_ext)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    print(picture_fn, picture_path)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    # form_picture.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = '''To reset your password, Visit the following link:
{}

if you did not make this request then simply ignore this email and no changes will be made!
'''.format(url_for('users.reset_token', token=token, _external=True))

    mail.send(msg)

