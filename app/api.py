import os
from flask import Blueprint , jsonify , request , send_from_directory
from flask_jwt import jwt_required , current_identity
from werkzeug import secure_filename

from .models import Post , User
from .utils import create_new_folder
from flask import current_app as app

api = Blueprint('api' , __name__ , url_prefix="/api")

@api.route('/posts')
@jwt_required()
def root(): 
    post_list = Post.query.all()
    posts  = [post.to_dict() for post in post_list]
    
    response ={'count':len(posts) , 'posts':posts}
    return jsonify(response)

@api.route('/post/<int:id>')
def view_post(id):
    post=  Post.query.get_or_404(id)
    return jsonify(post.to_dict())

@api.route('/user/<int:id>')
def user(id):
    user = User.query.filter(User.id==id).first()

    return jsonify(user.to_dict()) 

@api.route('/posts', methods=['POST'])
@jwt_required()
def post_post():
    data = request.get_json()
    # TODO validate
    title = data['title']
    content = data['content']
    user_id = current_identity.id

    post = Post(title=title , content=content, user_id=user_id)
    
    post.save()

    post = Post.query.filter(Post.title == title).first()
    return jsonify(post.to_dict()), 201

@api.route('/users')
@jwt_required()
def users():
    users =  [user.to_dict() for user in  User.query.all()]
    return jsonify(users)

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # TODO add validation
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])

    new_user.save()

    response = {'status_code':201, "message":"user created"}
    return jsonify(response) , 201

@api.route('/uploads', methods=['POST'])
def upload():
    if  request.files['upload']:
        file = request.files['upload']
        file_name = secure_filename(file.filename)
        create_new_folder(app.config['UPLOAD_FOLDER'])
        save_path = os.path.join(app.config['UPLOAD_FOLDER'],file_name)
        file.save(save_path)
        response = {
            'url':request.host+'/api/uploads/'+file_name

        }
        return jsonify(response)

@api.route('/uploads/<id>')
def serve_upload(id):
    return send_from_directory(app.config['UPLOAD_FOLDER'],id,as_attachment=False)