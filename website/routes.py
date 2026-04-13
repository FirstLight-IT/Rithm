from flask import Blueprint, render_template, request, redirect, url_for, session

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    errors = []
    if request.method == 'POST':
        ATime_input = request.form.get('ATime').strip()
        ATime_input = ATime_input.split(" ")

        BTime_input = request.form.get('BTime').strip()
        BTime_input = BTime_input.split(" ")

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

        if not errors:
            
            session['ATime'] = ATime
            session['BTime'] = BTime
            return redirect(url_for('routes.main'))
    
    return render_template('home.html', errors=errors)


@bp.route('/solution')
def main():
    ATime = session.get('ATime',[])
    BTime = session.get('BTime',[])

    print(ATime)

    return render_template('main.html')