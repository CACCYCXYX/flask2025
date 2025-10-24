from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
def generate_phone_numbers():
    phone_numbers = set()
    while len(phone_numbers) < 1000:
        number = random.randint(9000000000, 9999999999)
        number_7 = f'7{number}'
        phone_numbers.add(number_7)
    return phone_numbers
phone_numbers_all = generate_phone_numbers()

@app.route('/')
def index():
    return render_template('index.html', numbers=phone_numbers_all)

@app.route('/phone')
def phone_detail():
    phone_number = request.args.get('number', '')
    return render_template('phone_detail.html', phone_number=phone_number)

@app.route('/search', methods=['POST'])
def search_phone():
    search_query = request.form.get('search_query', '').strip()
    return redirect(url_for('phone_detail', number=search_query))

if __name__ == '__main__':
    app.run(debug=True)