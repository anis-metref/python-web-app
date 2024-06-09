from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Employee

@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    first_name = request.form['first_name']
    phone = request.form['phone']
    address = request.form['address']
    city = request.form['city']
    position = request.form['position']
    new_employee = Employee(name=name, first_name=first_name, phone=phone, address=address, city=city, position=position)
    db.session.add(new_employee)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_employee/<int:id>', methods=['POST'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_employee/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employee.query.get(id)
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.first_name = request.form['first_name']
        employee.phone = request.form['phone']
        employee.address = request.form['address']
        employee.city = request.form['city']
        employee.position = request.form['position']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_employee.html', employee=employee)


if __name__ == '__main__':
    app.run(debug=True, host='192.168.56.20', port='5000')
