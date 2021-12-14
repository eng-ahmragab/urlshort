from os import path
from datetime import datetime
#Flask imports
from flask import request, render_template, flash, redirect, url_for, abort, send_from_directory, session
from werkzeug.utils import secure_filename
#import the app, db objects
from app import app, db
#import the URL model
from app.models import URL







#============================================================================
#routes


@app.route('/')
def index():
    """
    renders the home page with shorten url form and upload image form
    """
    return render_template('index.html')
    #return "Hello, World!"








#Handle Shorten URL Form
@app.route('/shorten-url', methods=["POST"])
def shorten_url():
    """
    handles the shorten url form
    """
    #load the POST arguments
    short_name = request.form.get("shortName")
    url = request.form.get("url")
    #form validation
    if not short_name:
        flash("The short name field is required.", category="danger")
        return redirect(url_for("index"))
    if not url:
        flash("The url field is required.", category="danger")
        return redirect(url_for("index"))
    
    #we work with short_name in lower case
    short_name = short_name.lower()
    #check if short_name already exists in db
    short_name_exists = db.session.query(URL).filter(URL.short_name == short_name).first()
    if short_name_exists:
        flash("This short name is already taken, please choose another one.", category="danger")
        return redirect(url_for("index"))
    
    # write the short_name and url to DB
    new_url = URL(short_name=short_name, url=url, url_type="url")
    db.session.add(new_url)
    db.session.commit()
    print("[*] New URL insterted\n", new_url)
    
    #save the new short_name to cookie
    set_short_names_cookie(short_name)
    
    return render_template("short_url.html", short_name=short_name, url=url)









@app.route('/upload-image', methods=["POST"])
def upload_image():
    """
    handles the upload image form
    """
    #load the POST arguments
    short_name = request.form.get("shortName")
    file_input = request.files.get("fileInput")
    #form validation
    if not short_name:
        flash("The short name field is required.", category="danger")
        return redirect(url_for("index"))
    if not file_input:
        flash("The file input field is required.", category="danger")
        return redirect(url_for("index"))

    #we work with short_name in lower case
    short_name = short_name.lower()
    #check if short_name already exists in db
    short_name_exists = db.session.query(URL).filter(URL.short_name == short_name).first()
    if short_name_exists:
        flash("This short name is already taken, please choose another one.", category="danger")
        return redirect(url_for("index"))
    
    #read the file name securely
    file_name = secure_filename(file_input.filename)
    #check if extension is allowed
    file_ext = path.splitext(file_name)[1].lower()
    if file_ext not in app.config['UPLOAD_EXTENSIONS']:
        flash("The file extension is not allowed.", category="danger")
        return redirect(url_for("index"))
    
    #File upload
    #mix file name with timestamp to avoid duplicate files names
    dt_now = datetime.now()
    ts_now = int(dt_now.timestamp())
    file_name = str(ts_now) + "_" + file_name
    #save the file
    file_path = path.join(app.config['UPLOAD_FOLDER'], file_name)
    file_input.save(file_path)
    
    # write the short_name and url to DB
    new_url = URL(short_name=short_name, url=file_name, url_type="file")
    db.session.add(new_url)
    db.session.commit()
    print("[*] New URL insterted\n", new_url)
    
    #save the new short_name to cookie
    set_short_names_cookie(short_name)
    
    return render_template("short_url.html", short_name=short_name, url=None)









#redirect to the short_name to the original url
@app.route("/<short_name>")
def redirect_to_url(short_name):
    """
    renders the home page with shorten url form and upload image form
    Args:
        short_name (string): short_name read from the database
    """
    #check if the short_name doesn't exist in db
    short_name_exists = db.session.query(URL).filter(URL.short_name == short_name).first()
    if not short_name_exists:
        print("[*] Short name not found in DB")
        return abort(404)
    #read the url and url_type from short_name_exists record
    url = short_name_exists.url
    url_type = short_name_exists.url_type
    #redirect based on the url_type
    if url_type == "url":
        return redirect(url)
    elif url_type == "file":
        return redirect(url_for("serve_image", file_name=url))





#serve uploaded images
@app.route('/images/<file_name>')
def serve_image(file_name):
    """
    serves an image to a web browser
    Args:
        file_name (string): the file_name read from the database
    Returns:
        string: image url
    """
    try:
        return send_from_directory(app.config["UPLOAD_FOLDER"], file_name)
    except FileNotFoundError:
        return abort(404)














#custom 404 error page
@app.errorhandler(404)
def page_not_found(error):
    return render_template("not_found.html"), 404








#==========================================================================
def set_short_names_cookie(short_name):
    """
    handles saving short_name in the session cookies, with max size of 10 entries
    Args:
        short_name (string): short_name read from the form
    """
    short_names = []
    #check if short_names cookie already exist
    if session.get("short_names"):
        short_names = session["short_names"]
        #keep track of only the last n short_names
        short_names_cookie_size = 10
        if len(short_names) >= short_names_cookie_size:
            #pop out the last item of the short_names list
            short_names.pop()
    #insert short_name at the beginning of the list
    short_names.insert(0, short_name)
    #write short_names cookie
    session["short_names"] = short_names
    print("[*] Session set to:", "\n", session["short_names"])