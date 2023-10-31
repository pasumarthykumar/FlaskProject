from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Wildcrafts%4012@localhost/FLASKDB'

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employee'  # Specify the table name

    emp_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    
# Define a route to query and display employee records
@app.route('/employees')
def display_employees():
    try:
        employees = Employee.query.all()
        if employees:
            employee_list = [f"Employee ID: {employee.emp_id}, Name: {employee.fname} {employee.lname}" for employee in employees]
            return '<br>'.join(employee_list)
        else:
            return "No employee records found."
    except Exception as e:
        return f"Database connection failed. Error: {str(e)}"






if __name__ == '__main__':
    app.run(debug=True)
