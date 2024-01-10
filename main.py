from flask import Flask, request

app = Flask(__name__, static_url_path='/static')

NAME = 'DessertBot 🍧😋'

DESSERTS = [
    'cake', 'ice cream', 'fruit salad', 'chocolates', 'macaroons', 'strawberries'
]


@app.route('/desserts', methods=['GET', 'POST'])
def index():
    list_html = ''

    for dessert in DESSERTS:
        image_filename = f'/static/{dessert.replace(" ", "-")}.jpg'

        list_html += f'''
            <figure>
                <img src="{image_filename}" alt="{dessert}" width="300" height="200">
                <button name="favourite" value="{dessert}" class="btn">I ❤ {dessert}</button>
            </figure>
        '''

    form_html = f'''
        <p>What is your favourite dessert?</p>

        <form method="post" action="/pick-favourite" class="desserts-form">
            {list_html}
        </form>
    '''

    return {
        'author': NAME,
        'text': form_html,
        'css': '/static/css/desserts.css'
    }


@app.post('/pick-favourite')
def pick_favourite_dessert():
    form_data = request.get_json().get('form_data', {})
    favourite = form_data.get('favourite')

    return {'author': NAME, 'text': f'Yum! I love {favourite} too!'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
