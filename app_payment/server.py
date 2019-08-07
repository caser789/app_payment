from dock.web import DockApp
from dock.common import config

app = DockApp("")

import app_payment
app.mount(app_payment)

@app.flaskapp.route('/')
def health():
    return 'OK'


if __name__ == '__main__':
    app.run()
