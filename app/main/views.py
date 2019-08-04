from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm,UpdateProfile,PitchForm
from ..models import Review,User,Pitch
from flask_login import login_required,current_user
from .. import db,photos
import markdown2  

@main.route('/')
def index():
    '''
    view root page function that returns index page
    '''
    # category = Category.get_categories()

    title = 'Home'
    return render_template('index.html', title = title)


@main.route('/pitches',methods = ['GET','POST'])
@login_required
def new_pitch():
    name = "Pitch"
    title = 'Welcome,Pitch your one-minute pitch!'
    form = PitchForm()
    
    if form.validate_on_submit():
        
        title=form.title.data
        post=form.pitch.data
        # upvote=0
        # downvote=0
        new_pitch = Pitch(title=title, post=post)
        
        db.session.add(new_pitch)
        db.session.commit()

         
    # new_pitch.save_pitch()
        return redirect(url_for('main.post_pitch'))


    return render_template('post.html',title = title, name=name, pitch_form =form)


@main.route('/posts')
@login_required
def post_pitch():

    pitches = Pitch.query.all()
    return render_template('new_pitch.html',pitches = pitches)


@main.route('/reviews/<id>',methods = ['GET', 'POST'])
def post_review(id):
    pitch = Pitch.query.filter_by(id=id).first()
    
    form = ReviewForm()
    
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        
        new_review = Review(review_title = title, review = review, pitch_id=id, posted_by=current_user.username)
        new_review.save_review()
        return redirect(url_for('.post_review',id=pitch.id))
    return render_template('reviews.html',form=form, pitch=pitch)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        print(path)
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))