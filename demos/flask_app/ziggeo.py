from flask import Flask, flash, request, render_template, redirect, url_for, _request_ctx_stack
from Ziggeo import Ziggeo
from pprint import pprint

# Please be sure to add provide with Application Token and Private Key
# provided by ziggeo application
api_token='29ddc63d7396ceaaa4ff27712bb68d35'
api_key='4b50678a63c35ea68bd2b96354de77b8'
ziggeo = Ziggeo(api_token, api_key)

# Navigation will show navigation menu and in home page
navigation = [('/', 'Home'), ('/videos', 'Videos'), ('/record', 'Record Video'), ('/upload', 'Upload Video')];

app = Flask(__name__)
# Random generated key, for cookies security
app.secret_key = 'hyXUVtGl4IPbDZdJsQWBZ937BUwx'

@app.before_request
def before_request():
    method = request.form.get('_method', '').upper()
    if method:
        request.environ['REQUEST_METHOD'] = method
        ctx = _request_ctx_stack.top
        ctx.url_adapter.default_method = method
        assert request.method == method
def check_api_and_token_avaibility():
    if (len(api_key) < 5 or len(api_token) < 5) and request.endpoint != 'error_page':
        return redirect(url_for('error_page', message='Api key and token are required. Please add it to ziggeo.py file in root directory.'))


@app.route('/')
def index():
    return render_template('index.html', title="Ziggeo Application Home page", navigation=navigation);


@app.route('/videos')
def show_videos():
    videos = ziggeo.videos().index({"limit":10, "skip":0})
    return render_template('videos.html', title="Ziggeo All Videos", videos=videos, api_token=api_token, navigation=navigation);


@app.route('/video/<video_id>', methods=['GET', 'DELETE', 'POST'])
def single_video(video_id):

    if request.method == 'DELETE':
        delete_video(video_id)
        return render_template('success.html', message="Video was successfully deleted", navigation=navigation)
        # return redirect(url_for('success'), code=307)
        # return make_response(render_template('success.html', message="Success", navigation=navigation), 404)

    if request.method == 'POST':

        update_video(video_id, data)
        return redirect(url_for('success'), code=302)


    video = ziggeo.videos().get(video_id)
    return render_template('video.html', title="Single video via Ziggeo version 2", video=video, api_token=api_token, navigation=navigation)

@app.route('/download-video/<video_id>')
def download_video(video_id):
    return ziggeo.videos().download_video(video_id)


@app.route('/download-image/<video_id>')
def download_image(video_id):
    return ziggeo.videos().download_image(video_id)


@app.route('/record')
def record_video():
    return render_template('record.html', title="Record video with Ziggeo version 2", api_token=api_token, navigation=navigation)


@app.route('/upload')
def upload_video():
    return render_template('upload.html', title="Upload video with Ziggeo version 2", api_token=api_token, navigation=navigation)


@app.route('/error/<message>')
def error_page(message):
    return render_error_message(message)

@app.route('/success', methods=['GET', 'DELETE', 'POST'])
def success():
    return render_template('success.html', navigation=navigation)

# Custom methods
def delete_video(video_id):
    if ziggeo.videos().delete(video_id):
        message = "Video was successfully deleted"
        flash(message, 'success')
        return render_template('success.html', message=message, navigation=navigation)
    else:
        message = "There was some error with deleting"
        flash(message, 'error')
        return render_error_message(message)

def render_error_message(message):
    return render_template('error.html', message=message)


if __name__ == "__main__":
    app.debug = True
    app.run(host="127.0.0.1", port=3030)
