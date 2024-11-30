from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        name = request.form['name']
        car_model = request.form['car_model']
        rental_date = request.form['rental_date']
        # Aici poți adăuga logica pentru a salva rezervarea
        return f"Rezervare făcută pentru {name} cu modelul {car_model} pe data de {rental_date}."
    return render_template('reserve.html')

if __name__ == '__main__':
    app.run(debug=True)
