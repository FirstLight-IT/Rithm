from flask import Blueprint, render_template, request, redirect, url_for, session
from console import calculation

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    errors = []
    if request.method == 'POST':
        ATime_input = request.form.get('ATime').strip()
        ATime_input = ATime_input.split(" ")

        BTime_input = request.form.get('BTime').strip()
        BTime_input = BTime_input.split(" ")

        algorithm = request.form.get("algorithm")

        if algorithm =='FCFS':
            algorithm = True
        else:
            algorithm = False

        ATime = []
        BTime = []

        for a in ATime_input:
            a = int(a)
            ATime.append(a)

        for b in BTime_input:
            b = int(b)
            BTime.append(b)

        if len(ATime) != len(BTime):
            errors.append("Mismatched number of values.")

        if len(ATime) < 2 or len(BTime) < 2:
            errors.append("Must have at least 2 values.")

        if not errors:
            
            session['ATime'] = ATime
            session['BTime'] = BTime
            session['algorithm'] = algorithm
            return redirect(url_for('routes.main'))
    
    return render_template('home.html', errors=errors)


@bp.route('/solution')
def main():
    ATime = session.get('ATime',[])
    BTime= session.get('BTime',[])
    algorithm = session.get('algorithm')

    n = len(BTime)
    table = calculation(BTime, ATime, algorithm)

    sortedTable = sorted(table, key=lambda row: row[0])
 
    sumTAT = 0
    sumWT = 0

    for i in table:
        sumTAT += i[4]
        sumWT += i[5]

    AveTAT = float(sumTAT)/n
    AveWT = float(sumWT)/n

    return render_template('main.html', table=table, sortedTable=sortedTable, AveTAT=AveTAT, AveWT=AveWT)