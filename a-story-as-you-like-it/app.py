from bottle import Bottle, run, static_file
from narrative_data import read_text_from_file
from templates import base_template, display_story_node

app = Bottle()
texts = read_text_from_file("un-conte.json")

@app.route('/')
def home():
    origin = texts[1]
    return base_template(display_story_node(origin))


@app.route('/api/story/<id:int>', method="post")
def api(id):
    storynode = texts[id]
    return display_story_node(storynode)


@app.route('/css/<filename:path>')
def send_static(filename):
    return static_file(filename, root='css')

if __name__ == "__main__":
    run(app, host="localhost", port=8000, reloader=True)
