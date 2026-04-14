from flask import Blueprint, render_template, request, redirect, url_for, session
from console import calculation

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    errors = []
    if request.method == 'POST':
        ATime_input = request.form.get('ATime').strip().split(" ")
        BTime_input = request.form.get('BTime').strip().split(" ")
        algorithm = request.form.get("algorithm")

        algorithm = True if algorithm == 'FCFS' else False

        try:
            ATime = [int(a) for a in ATime_input]
            BTime = [int(b) for b in BTime_input]
        except ValueError:
            errors.append("Please enter valid numbers.")
            return render_template('home.html', errors=errors)

        if len(ATime) != len(BTime):
            errors.append("Mismatched number of values.")
        if len(ATime) < 2:
            errors.append("Must have at least 2 values.")
        if any(b <= 0 for b in BTime):
            errors.append("Burst time should not be zero or negative.")

        if not errors:
            session['ATime'] = ATime
            session['BTime'] = BTime
            session['algorithm'] = algorithm
            return redirect(url_for('routes.main'))
    
    return render_template('home.html', errors=errors)

@bp.route('/solution')
def main():
    ATime = session.get('ATime', [])
    BTime = session.get('BTime', [])
    algorithm = session.get('algorithm')

    n = len(BTime)
    # This table is now in execution order from console.py
    executionTable = calculation(BTime, ATime, algorithm)

    # Sort by Process ID (P1, P2, P3...) for the bottom table
    sortedTable = sorted(executionTable, key=lambda row: row[0])
 
    sumTAT = sum(row[4] for row in executionTable)
    sumWT = sum(row[5] for row in executionTable)

    AveTAT = float(sumTAT)/n if n > 0 else 0
    AveWT = float(sumWT)/n if n > 0 else 0

    return render_template('main.html', executionTable=executionTable, sortedTable=sortedTable, AveTAT=AveTAT, AveWT=AveWT)