from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded data for locations, canteens, and meal timings
locations = {
    'Jamshedpur': ['Blast Furnace Canteen', 'Coke Plant Canteen', 'Sinter Plant Canteen'],
    'Kallinganagar': ['Steel Plant Canteen', 'Refinery Canteen', 'Smelting Plant Canteen'],
    'Kharagpur': ['Foundry Canteen', 'Assembly Plant Canteen', 'Research Center Canteen']
}

meal_timings = {
    'Breakfast': '8:30 AM - 9:30 AM',
    'Lunch': '12:30 PM - 1:30 PM',
    'Snacks': 'Afternoon',
    'Dinner': '7:30 PM - 8:30 PM'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/punchin', methods=['GET', 'POST'])
def punchin():
    if request.method == 'POST':
        location = request.form.get('location')
        canteen = request.form.get('canteen')

        # Here you would capture the punch-in data and process it as needed

        return redirect(url_for('punchout'))

    return render_template('punchin.html', locations=locations)

@app.route('/punchout', methods=['GET', 'POST'])
def punchout():
    if request.method == 'POST':
        location = request.form.get('location')
        canteen = request.form.get('canteen')

        # Here you would capture the punch-out data and process it as needed

        return redirect(url_for('index'))

    return render_template('punchout.html', locations=locations)

if __name__ == '__main__':
    app.run(debug=True)
