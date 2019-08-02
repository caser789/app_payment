from dock.web import DockApp

app = DockApp("")

from dock.common import config

@app.flaskapp.route('/')
def health():
    return 'OK'


if __name__ == '__main__':
    app.run()
