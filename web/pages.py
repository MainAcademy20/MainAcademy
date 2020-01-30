from app import app


@app.route('/')
def main():
    return 'Hello world. <a href="/page1">Go to page 1</a>'


@app.route('/page1')
def page1():
    return "Page 1 Content. (TODO: create link back to main page)"



if __name__ == '__main__':
    app.run()
