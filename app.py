from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)
# main-page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['sub'] == 'City':
            # Fetch form data
            return redirect('/city')
        if request.form['sub'] == 'Airport':
            # Fetch form data
            return redirect('/airp')
        if request.form['sub'] == 'Airport_consists_of':
            # Fetch form data
            return redirect('/airpco')
        if request.form['sub'] == 'Airline':
            # Fetch form data
            return redirect('/airl')
        if request.form['sub'] == 'Flight':
            # Fetch form data
            return redirect('/flight')
        if request.form['sub'] == 'Flight_info':
            # Fetch form data
            return redirect('/flighti')
        if request.form['sub'] == 'Notice_board':
            # Fetch form data
            return redirect('/nb')
        if request.form['sub'] == 'Flight_Passenger_transmits':
            # Fetch form data
            return redirect('/fpt')
        if request.form['sub'] == 'Employee':
            # Fetch form data
            return redirect('/emp')
        if request.form['sub'] == 'Employee_handles':
            # Fetch form data
            return redirect('/emph')
        if request.form['sub'] == 'Passenger':
            # Fetch form data
            return redirect('/pass')
        if request.form['sub'] == 'Ticket':
            # Fetch form data
            return redirect('/ticket')
        if request.form['sub'] == 'Admin_Support':
            # Fetch form data
            return redirect('/admin_sup')
        if request.form['sub'] == 'Engineer':
            # Fetch form data
            return redirect('/engineer')
        if request.form['sub'] == 'Luggage':
            # Fetch form data
            return redirect('/luggage')
        if request.form['sub'] == 'Connecting_Flight':
            # Fetch form data
            return redirect('/con_flight')
        if request.form['sub'] == 'Non_Stop_Flight':
            # Fetch form data
            return redirect('/ns_flight')

    return render_template('index.html')

# City-operations
@app.route('/city', methods=['GET', 'POST'])
def city():
    if request.method == 'POST':
        if request.form['sub'] == 'Show Table':
            # Fetch form data
            return redirect('/cityview')

        if request.form['sub'] == 'Insert':
            # Fetch form data
            cityDetails = request.form
            cname = cityDetails['cname']
            state = cityDetails['state']
            coun = cityDetails['coun']
            cur = mysql.connection.cursor()
            cur.execute("insert into city values(%s, %s, %s)",(cname, state, coun))
            mysql.connection.commit()
            cur.close()

        if request.form['sub'] == 'Update':
            cityDetails = request.form
            cname = cityDetails['cname']
            state = cityDetails['state']
            coun = cityDetails['coun']
            cur = mysql.connection.cursor()
            cur.execute("update city set state=%s, country=%s where city_name=%s", (state, coun, cname))
            mysql.connection.commit()
            cur.close()
            
        if request.form['sub'] == 'Delete':
            cityDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            cname = cityDetails['cname']
            # state = cityDetails['state']
            # coun = cityDetails['coun']
            cur = mysql.connection.cursor()
            cur.execute("delete from city where city_name = %s", (cname))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/cityview')
    return render_template('city.html')

# City view
@app.route('/cityview')
def cityview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM city")
    if resultValue > 0:
        cityDetails = cur.fetchall()
        return render_template('cityview.html',cityDetails=cityDetails)
    else:
        return render_template('cityview.html')

# Airport-operations
@app.route('/airp', methods=['GET', 'POST'])
def airport():
    if request.method == 'POST':
        if request.form['airp'] == 'Show Table':
            # Fetch form data
            return redirect('/airpview')

        if request.form['airp'] == 'Insert':
            # Fetch form data
            airpDetails = request.form
            aname = airpDetails['aname']
            astate = airpDetails['astate']
            acoun = airpDetails['acoun']
            cname = airpDetails['cname']
            cur = mysql.connection.cursor()
            cur.execute("insert into airport values(%s, %s, %s, %s)",(aname, astate, acoun, cname))
            mysql.connection.commit()
            cur.close()
        if request.form['airp'] == 'Update':
            airpDetails = request.form
            aname = airpDetails['aname']
            astate = airpDetails['astate']
            acoun = airpDetails['acoun']
            cname = airpDetails['cname']
            cur = mysql.connection.cursor()
            cur.execute("update airport set a_state=%s, a_country=%s, city_name=%s where a_name=%s", (astate, acoun, cname, aname))
            mysql.connection.commit()
            cur.close()
        # if request.form['airp'] == 'Delete':
            airpDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            aname = airpDetails['aname']
            # astate = airpDetails['astate']
            # acoun = airpDetails['acoun']
            # cname = airpDetails['cname']
            cur = mysql.connection.cursor()
            cur.execute("delete from airport where a_name = %s", (aname))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/airpview')
    return render_template('airport.html')

# Airport view
@app.route('/airpview', methods=['GET', 'POST'])
def airportview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM airport")
    if resultValue > 0:
        airpDetails = cur.fetchall()
        return render_template('airportview.html',airpDetails=airpDetails)
    else:
        return render_template('airportview.html')

# Airport_consists_of operations
@app.route('/airpco', methods=['GET', 'POST'])
def airport_consists_of():
    if request.method == 'POST':
        if request.form['airpco'] == 'Show Table':
            # Fetch form data
            return redirect('/airpcoview')

        if request.form['airpco'] == 'Insert':
            # Fetch form data
            airpcoDetails = request.form
            aname = airpcoDetails['aname']
            airid = airpcoDetails['airid']
            cur = mysql.connection.cursor()
            cur.execute("insert into airport_consists_of values(%s, %s)",(aname, airid))
            mysql.connection.commit()
            cur.close()
        if request.form['airpco'] == 'Update':
            airpcoDetails = request.form
            aname = airpcoDetails['aname']
            airid = airpcoDetails['airid']
            cur = mysql.connection.cursor()
            cur.execute("update airport_consists_of set a_name=%s where air_id=%s", (aname, airid))
            mysql.connection.commit()
            cur.close()
        if request.form['airpco'] == 'Delete':
            airpcoDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            aname = airpcoDetails['aname']
            airid = airpcoDetails['airid']
            cur = mysql.connection.cursor()
            cur.execute("delete from airport_consists_of where a_name = %s and air_id = %s", (aname, airid))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/airpcoview')
    return render_template('airport_consists_of.html')

# Airport_consists_of view
@app.route('/airpcoview')
def airportcoview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM airport_consists_of")
    airpcoDetails = cur.fetchall()
    if resultValue > 0:
        airpcoDetails = cur.fetchall()
        return render_template('airport_consists_ofview.html',airpcoDetails=airpcoDetails)
    else:
        return render_template('airport_consists_ofview.html')

# Airline operations
@app.route('/airl', methods=['GET', 'POST'])
def airline():
    if request.method == 'POST':
        if request.form['airl'] == 'Show Table':
            # Fetch form data
            return redirect('/airlview')

        if request.form['airl'] == 'Insert':
            # Fetch form data
            airlDetails = request.form
            airid = airlDetails['airid']
            airname = airlDetails['airname']
            cur = mysql.connection.cursor()
            cur.execute("insert into airline values(%s, %s)",(airid, airname))
            mysql.connection.commit()
            cur.close()
        if request.form['airl'] == 'Update':
            airlDetails = request.form
            airname = airlDetails['airname']
            airid = airlDetails['airid']
            cur = mysql.connection.cursor()
            cur.execute("update airline set air_name=%s where air_id=%s", (airname, airid))
            mysql.connection.commit()
            cur.close()
        if request.form['airl'] == 'Delete':
            airlDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            # airname = airlDetails['airname']
            airid = airlDetails['airid']
            cur = mysql.connection.cursor()
            cur.execute("delete from airline where air_id = %s", (airid))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/airlview')
    return render_template('airline.html')

# Airline view
@app.route('/airlview')
def airlineview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM airline")
    if resultValue > 0:
        airlDetails = cur.fetchall()
        return render_template('airlineview.html',airlDetails=airlDetails)
    else:
        return render_template('airlineview.html')

# Flight operations
@app.route('/flight', methods=['GET', 'POST'])
def flight():
    if request.method == 'POST':
        if request.form['flight'] == 'Show Table':
            # Fetch form data
            return redirect('/flightview')

        if request.form['flight'] == 'Insert':
            # Fetch form data
            flightDetails = request.form
            fno = flightDetails['fno']
            fsrc = flightDetails['fsrc']
            fdest = flightDetails['fdest']
            fdepttime = flightDetails['fdepttime']
            farrtime = flightDetails['farrtime']
            fdur = flightDetails['fdur']
            fstat = flightDetails['fstat']
            airid = flightDetails['airid']
            cur = mysql.connection.cursor()
            cur.execute("insert into flight values(%s, %s, %s, %s, %s, %s, %s, %s)",(fno, fsrc, fdest, fdepttime, farrtime, fdur, fstat, airid))
            mysql.connection.commit()
            cur.close()
        if request.form['flight'] == 'Update':
            flightDetails = request.form
            fno = flightDetails['fno']
            fsrc = flightDetails['fsrc']
            fdest = flightDetails['fdest']
            fdepttime = flightDetails['fdepttime']
            farrtime = flightDetails['farrtime']
            fdur = flightDetails['fdur']
            fstat = flightDetails['fstat']
            airid = flightDetails['airid']
            cur = mysql.connection.cursor()
            cur.execute("update flight set fsource=%s, fdest=%s, fdepart_time=%s, fduration=%s, fstatus=%s, air_name=%s where fno=%s", (fsrc, fdest, fdepttime, farrtime, fdur, fstat, airid, fno))
            mysql.connection.commit()
            cur.close()
        if request.form['flight'] == 'Delete':
            flightDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            fno = flightDetails['fno']
            # fsrc = flightDetails['fsrc']
            # fdest = flightDetails['fdest']
            # fdepttime = flightDetails['fdepttime']
            # farrtime = flightDetails['farrtime']
            # fdur = flightDetails['fdur']
            # fstat = flightDetails['fstat']
            # airid = flightDetails['airid']
            cur = mysql.connection.cursor()
            cur.execute("delete from flight where fno = %s", (fno))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/flightview')
    return render_template('flight.html')

# Flight view
@app.route('/flightview')
def flightview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM flight")
    if resultValue > 0:
        flightDetails = cur.fetchall()
        return render_template('flightview.html',flightDetails=flightDetails)
    else:
        return render_template('flightview.html')

# Flight_info operations
@app.route('/flighti', methods=['GET', 'POST'])
def flighti():
    if request.method == 'POST':
        if request.form['flighti'] == 'Show Table':
            # Fetch form data
            return redirect('/flightiview')

        if request.form['flighti'] == 'Insert':
            # Fetch form data
            flightiDetails = request.form
            fno = flightiDetails['fno']
            nbid = flightiDetails['nbid']
            cur = mysql.connection.cursor()
            cur.execute("insert into flight_info values(%s, %s)",(fno, nbid))
            mysql.connection.commit()
            cur.close()
        if request.form['flighti'] == 'Update':
            flightiDetails = request.form
            fno = flightiDetails['fno']
            nbid = flightiDetails['nbid']
            cur = mysql.connection.cursor()
            cur.execute("update flight_info set nbid=%s where fno=%s", (nbid, fno))
            mysql.connection.commit()
            cur.close()
        if request.form['flighti'] == 'Delete':
            flightiDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            fno = flightiDetails['fno']
            nbid = flightiDetails['nbid']
            cur = mysql.connection.cursor()
            cur.execute("delete from flighti where fno = %s and nb_id=%s", (fno, nbid))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/flightiview')
    return render_template('flight_info.html')

# Flight_info view
@app.route('/flightiview')
def flightiview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM flight_info")
    if resultValue > 0:
        flightiDetails = cur.fetchall()
        return render_template('flight_infoiview.html',flightiDetails=flightiDetails)
    else:
        return render_template('flight_infoview.html')

# Notice_board operations
@app.route('/nb', methods=['GET', 'POST'])
def nb():
    if request.method == 'POST':
        if request.form['nb'] == 'Show Table':
            # Fetch form data
            return redirect('/nbview')

        if request.form['nb'] == 'Insert':
            # Fetch form data
            nbDetails = request.form
            nbid = nbDetails['nbid']
            gno = nbDetails['gno']
            arr = nbDetails['arr']
            dept = nbDetails['dept']
            src = nbDetails['src']
            dest = nbDetails['dest']
            status = nbDetails['status']
            term = nbDetails['term']
            cur = mysql.connection.cursor()
            cur.execute("insert into notice_board values(%s, %s, %s, %s, %s, %s, %s, %s)",(nbid, gno, arr, dept, src, dest, status, term))
            mysql.connection.commit()
            cur.close()
        if request.form['nb'] == 'Update':
            nbDetails = request.form
            nbid = nbDetails['nbid']
            gno = nbDetails['gno']
            arr = nbDetails['arr']
            dept = nbDetails['dept']
            src = nbDetails['src']
            dest = nbDetails['dest']
            status = nbDetails['status']
            term = nbDetails['term']
            cur = mysql.connection.cursor()
            cur.execute("update notice_board set Gate_no=%s, nb_arr=%s, nb_depart=%s, nb_source=%s, nb_dest=%s, nb_status=%s, terminal=%s where fno=%s", (gno, arr, dept, src, dest, status, term, nbid))
            mysql.connection.commit()
            cur.close()
        if request.form['nb'] == 'Delete':
            nbDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            nbid = nbDetails['nbid']
            # gno = nbDetails['gno']
            # arr = nbDetails['arr']
            # dept = nbDetails['dept']
            # src = nbDetails['src']
            # dest = nbDetails['dest']
            # status = nbDetails['status']
            # term = nbDetails['term']
            cur = mysql.connection.cursor()
            cur.execute("delete from notice_board where nb_id = %s", (nbid))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/nbview')
    return render_template('notice_board.html')

# Notice_board view
@app.route('/nbview')
def nbview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM notice_board")
    if resultValue > 0:
        nbDetails = cur.fetchall()
        return render_template('notice_boardview.html',nbDetails=nbDetails)
    else:
        return render_template('notice_boardview.html')

# Flight_passenger_transmits operations
@app.route('/fpt', methods=['GET', 'POST'])
def fpt():
    if request.method == 'POST':
        if request.form['fpt'] == 'Show Table':
            # Fetch form data
            return redirect('/fptview')

        if request.form['fpt'] == 'Insert':
            # Fetch form data
            fptDetails = request.form
            fno = fptDetails['fno']
            pid = fptDetails['pid']
            nbid = fptDetails['nbid']
            cur = mysql.connection.cursor()
            cur.execute("insert into flight_passenger_transmits values(%s, %s, %s)",(fno, pid, nbid))
            mysql.connection.commit()
            cur.close()
        if request.form['fpt'] == 'Update':
            fptDetails = request.form
            fno = fptDetails['fno']
            pid = fptDetails['pid']
            nbid = fptDetails['nbid']
            cur = mysql.connection.cursor()
            cur.execute("update flight_passenger_transmits set nb_id=%s and P_id = %s where fno=%s", (nbid, pid, fno))
            mysql.connection.commit()
            cur.close()
        if request.form['fpt'] == 'Delete':
            fptDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            fno = fptDetails['fno']
            pid = fptDetails['pid']
            nbid = fptDetails['nbid']
            cur = mysql.connection.cursor()
            cur.execute("delete from flight_passenger_transmits where fno = %s and p_id = %s and nb_id = %s", (fno, pid, nbid))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/fptview')
    return render_template('flight_pass_trans.html')

# Flight_passenger_transmits view
@app.route('/fptview')
def fptview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM flight_passenger_transmits")
    if resultValue > 0:
        fptDetails = cur.fetchall()
        return render_template('flight_pass_transview.html',fptDetails=fptDetails)
    else:
        return render_template('flight_pass_transview.html')

# employee operations
@app.route('/emp', methods=['GET', 'POST'])
def emp():
    if request.method == 'POST':
        if request.form['emp'] == 'Show Table':
            # Fetch form data
            return redirect('/empview')

        if request.form['emp'] == 'Insert':
            # Fetch form data
            empDetails = request.form
            eid = empDetails['eid']
            efirst = empDetails['efirst']
            elast = empDetails['elast']
            estreet = empDetails['estreet']
            ecity = empDetails['ecity']
            estate = empDetails['estate']
            epin = empDetails['epin']
            emn = empDetails['emn']
            esex = empDetails['esex']
            edob = empDetails['edob']
            esal = empDetails['esal']
            edes = empDetails['edes']
            aname = empDetails['aname']
            cur = mysql.connection.cursor()
            cur.execute("insert into employee values(%s, %s, %s, %s, %s, %s, %d, %d, %s, %s, %d, %s, %s)",(eid, efirst, elast, estreet, ecity, estate, epin, emn, esex, edob, esal, edes, aname))
            mysql.connection.commit()
            cur.close()
        if request.form['emp'] == 'Update':
            empDetails = request.form
            eid = empDetails['eid']
            efirst = empDetails['efirst']
            elast = empDetails['elast']
            estreet = empDetails['estreet']
            ecity = empDetails['ecity']
            estate = empDetails['estate']
            epin = empDetails['epin']
            emn = empDetails['emn']
            esex = empDetails['esex']
            edob = empDetails['edob']
            esal = empDetails['esal']
            edes = empDetails['edes']
            aname = empDetails['aname']
            cur = mysql.connection.cursor()
            cur.execute("update employee set efirst_name=%s, elast_name=%s, e_street=%s, e_city=%s, E_state=%s, e_pincode=%d, emp_mno=%d, emp_sex=%s, emp_dob=%s, emp_salary=%s, Edesignation=%s, a_name=%s where emp_id=%s", (efirst, elast, estreet, ecity, estate, epin, emn, esex, edob, esal, edes, aname, eid))
            mysql.connection.commit()
            cur.close()
        if request.form['emp'] == 'Delete':
            empDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            eid = empDetails['eid']
            # efirst = empDetails['efirst']
            # elast = empDetails['elast']
            # estreet = empDetails['estreet']
            # ecity = empDetails['ecity']
            # estate = empDetails['estate']
            # epin = empDetails['epin']
            # emn = empDetails['emn']
            # esex = empDetails['esex']
            # edob = empDetails['edob']
            # esal = empDetails['esal']
            # edes = empDetails['edes']
            # aname = empDetails['aname']
            cur = mysql.connection.cursor()
            cur.execute("delete from employee where emp_id = %s", (eid))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/empview')
    return render_template('employee.html')

# employee view
@app.route('/empview')
def empview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM employee")
    if resultValue > 0:
        empDetails = cur.fetchall()
        return render_template('employeeview.html', empDetails=empDetails)
    else:
        return render_template('employeeview.html')

# Employee_handles operations
@app.route('/emph', methods=['GET', 'POST'])
def emphandles():
    if request.method == 'POST':
        if request.form['emph'] == 'Show Table':
            # Fetch form data
            return redirect('/emphview')

        if request.form['emph'] == 'Insert':
            # Fetch form data
            emphDetails = request.form
            eid = emphDetails['eid']
            pid = emphDetails['pid']
            cur = mysql.connection.cursor()
            cur.execute("insert into flight_info values(%s, %s)",(eid, pid))
            mysql.connection.commit()
            cur.close()
        if request.form['emph'] == 'Update':
            emphDetails = request.form
            eid = emphDetails['eid']
            pid = emphDetails['pid']
            cur = mysql.connection.cursor()
            cur.execute("update employee_handles set p_id=%s where emp_id=%s", (pid, eid))
            mysql.connection.commit()
            cur.close()
        if request.form['emph'] == 'Delete':
            emphDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            eid = emphDetails['eid']
            pid = emphDetails['pid']
            cur = mysql.connection.cursor()
            cur.execute("delete from emph where emp_id = %s and p_id = %s", (eid, pid))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/emphview')
    return render_template('employee_handles.html')

# Employee_handles view
@app.route('/emphview')
def emphview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM employee_handles")
    if resultValue > 0:
        emphDetails = cur.fetchall()
        return render_template('employee_handlesview.html',emphDetails=emphDetails)
    else:
        return render_template('employee_handlesview.html')

# Passenger operation
@app.route('/pass', methods=['GET', 'POST'])
def passenger():
    if request.method == 'POST':
        if request.form['pass'] == 'Show Table':
            # Fetch form data
            return redirect('/passview')

        if request.form['pass'] == 'Insert':
            # Fetch form data
            passDetails = request.form
            pid = passDetails['pid']
            pmno = passDetails['pmno']
            pfn = passDetails['pfn']
            pln = passDetails['pln']
            pdob = passDetails['pdob']
            psex = passDetails['psex']
            pidt = passDetails['pidt']
            pidn = passDetails['pidn']
            cur = mysql.connection.cursor()
            cur.execute("insert into passenger values(%s, %d, %s, %s, %s, %s, %d, %s)",(pid, pmno, pfn, pln, pdob, psex, pidn, pidt))
            mysql.connection.commit()
            cur.close()
        if request.form['pass'] == 'Update':
            passDetails = request.form
            pid = passDetails['pid']
            pmno = passDetails['pmno']
            pfn = passDetails['pfn']
            pln = passDetails['pln']
            pdob = passDetails['pdob']
            psex = passDetails['psex']
            pidt = passDetails['pidt']
            pidn = passDetails['pidn']
            cur = mysql.connection.cursor()
            cur.execute("update passenger set pfirst_name=%s, plast_name=%s, p_mno=%d, p_dob=%s, p_sex=%s, p_idno=%d, p_idtype=%s where p_id=%s", (pfn, pln, pmno, pdob, psex, pidn, pidt, pid))
            mysql.connection.commit()
            cur.close()
        if request.form['pass'] == 'Delete':
            passDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            pid = passDetails['pid']
            # pmno = passDetails['pmno']
            # pfn = passDetails['pfn']
            # pln = passDetails['pln']
            # pdob = passDetails['pdob']
            # psex = passDetails['psex']
            # pidt = passDetails['pidt']
            # pidn = passDetails['pidn']
            cur = mysql.connection.cursor()
            cur.execute("delete from passenger where p_id = %s", (pid))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/passview')
    return render_template('passenger.html')

# Passenger view
@app.route('/passview')
def passview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM passenger")
    if resultValue > 0:
        passDetails = cur.fetchall()
        return render_template('passengerview.html', passDetails=passDetails)
    else:
        return render_template('passengerview.html')

# ticket operations
@app.route('/ticket', methods=['GET', 'POST'])
def ticket():
    if request.method == 'POST':
        if request.form['tick'] == 'Show Table':
            # Fetch form data
            return redirect('/ticketview')

        if request.form['tick'] == 'Insert':
            # Fetch form data
            tickDetails = request.form
            tno = tickDetails['tno']
            airname = tickDetails['airname']
            tprice = tickDetails['tprice']
            seatno = tickDetails['seatno']
            classcategory = tickDetails['classcategory']
            arr = tickDetails['arr']
            dept = tickDetails['dept']
            dura = tickDetails['dura']
            dot = tickDetails['dot']
            psrc = tickDetails['psrc']
            pdest = tickDetails['pdest']
            term = tickDetails['term']
            pid = tickDetails['pid']
            dob = tickDetails['dob']
            doc = tickDetails['doc']
            charge = tickDetails['charge']
            cur = mysql.connection.cursor()
            cur.execute("insert into ticket values(%s, %s, %d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d)",(tno, airname, tprice, seatno, classcategory, arr, dept, dura, dot, psrc, pdest, term, pid, dob, doc, charge))
            mysql.connection.commit()
            cur.close()
        if request.form['tick'] == 'Update':
            tickDetails = request.form
            tno = tickDetails['tno']
            airname = tickDetails['airname']
            tprice = tickDetails['tprice']
            seatno = tickDetails['seatno']
            classcategory = tickDetails['classcategory']
            arr = tickDetails['arr']
            dept = tickDetails['dept']
            dura = tickDetails['dura']
            dot = tickDetails['dot']
            psrc = tickDetails['psrc']
            pdest = tickDetails['pdest']
            term = tickDetails['term']
            pid = tickDetails['pid']
            dob = tickDetails['dob']
            doc = tickDetails['doc']
            charge = tickDetails['charge']
            cur = mysql.connection.cursor()
            cur.execute("update ticket set air_name=%s, ticket_price=%d, seat_no=%s, class=%s, arr=%s, depart=%s, duration=%s, do_travel=%s, p_source=%s, p_dest=%s, terminal=%s, p_id=%s, do_book=%s, do_cancel=%s, charge=%d where ticket_no=%s", (airname, tprice, seatno, classcategory, arr, dept, dura, dot, psrc, pdest, term, pid, dob, doc, charge, tno))
            mysql.connection.commit()
            cur.close()
        if request.form['tick'] == 'Delete':
            tickDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            tno = tickDetails['tno']
            # airname = tickDetails['airname']
            # tprice = tickDetails['tprice']
            # seatno = tickDetails['seatno']
            # classcategory = tickDetails['classcategory']
            # arr = tickDetails['arr']
            # dept = tickDetails['dept']
            # dura = tickDetails['dura']
            # dot = tickDetails['dot']
            # psrc = tickDetails['psrc']
            # pdest = tickDetails['pdest']
            # term = tickDetails['term']
            # pid = tickDetails['pid']
            # dob = tickDetails['dob']
            # doc = tickDetails['doc']
            # charge = tickDetails['charge']
            cur = mysql.connection.cursor()
            cur.execute("delete from ticket where ticket_no = %s", (tno))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/tickview')
    return render_template('ticket.html')

# ticket view
@app.route('/ticketview')
def ticketview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM ticket")
    if resultValue > 0:
        tickDetails = cur.fetchall()
        return render_template('ticketview.html', tickDetails=tickDetails)
    else:
        return render_template('ticketview.html')

# admin_support operations
@app.route('/admin_sup', methods=['GET', 'POST'])
def admin_sup():
    if request.method == 'POST':
        if request.form['adminsup'] == 'Show Table':
            # Fetch form data
            return redirect('/admin_supview')

        if request.form['adminsup'] == 'Insert':
            # Fetch form data
            adminsupDetails = request.form
            eid = adminsupDetails['eid']
            astype = adminsupDetails['astype']
            cur = mysql.connection.cursor()
            cur.execute("insert into admin_support values(%s, %s)",(eid, astype))
            mysql.connection.commit()
            cur.close()
        if request.form['adminsup'] == 'Update':
            adminsupDetails = request.form
            eid = adminsupDetails['eid']
            astype = adminsupDetails['astype']
            cur = mysql.connection.cursor()
            cur.execute("update admin_support set astype=%s where emp_id=%s", (astype, eid))
            mysql.connection.commit()
            cur.close()
        if request.form['adminsup'] == 'Delete':
            adminsupDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            eid = adminsupDetails['eid']
            # astype = adminsupDetails['astype']
            cur = mysql.connection.cursor()
            cur.execute("delete from adminsup where emp_id = %s", (eid))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/admin_supview')
    return render_template('admin_sup.html')

# Admin_support view
@app.route('/admin_supview')
def admin_supview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM admin_support")
    if resultValue > 0:
        adminsupDetails = cur.fetchall()
        return render_template('admin_supview.html', adminsupDetails=adminsupDetails)
    else:
        return render_template('admin_supview.html')

# engineer operations
@app.route('/engineer', methods=['GET', 'POST'])
def engineer():
    if request.method == 'POST':
        if request.form['engi'] == 'Show Table':
            # Fetch form data
            return redirect('/engineerview')

        if request.form['engi'] == 'Insert':
            # Fetch form data
            engineerDetails = request.form
            eid = engineerDetails['eid']
            etype = engineerDetails['etype']
            cur = mysql.connection.cursor()
            cur.execute("insert into engineer values(%s, %s)",(eid, etype))
            mysql.connection.commit()
            cur.close()
        if request.form['engi'] == 'Update':
            engineerDetails = request.form
            eid = engineerDetails['eid']
            etype = engineerDetails['etype']
            cur = mysql.connection.cursor()
            cur.execute("update engineer set etype=%s where emp_id=%s", (etype, eid))
            mysql.connection.commit()
            cur.close()
        if request.form['engi'] == 'Delete':
            engineerDetails = request.form
            eid = engineerDetails['eid']
            # etype = engineerDetails['etype']
            cur = mysql.connection.cursor()
            cur.execute("delete from engineer where emp_id = %s", (eid))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/engineerview')
    return render_template('engineer.html')

# engineer view
@app.route('/engineerview')
def engineerview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM engineer")
    if resultValue > 0:
        engineerDetails = cur.fetchall()
        return render_template('engineerview.html', engineerDetails=engineerDetails)
    else:
        return render_template('engineerview.html')

# luggage operations
@app.route('/luggage', methods=['GET', 'POST'])
def luggage():
    if request.method == 'POST':
        if request.form['luggage'] == 'Show Table':
            # Fetch form data
            return redirect('/luggageview')

        if request.form['lugg'] == 'Insert':
            # Fetch form data
            luggageDetails = request.form
            pid = luggageDetails['pid']
            lid = luggageDetails['lid']
            nob = luggageDetails['nob']
            cur = mysql.connection.cursor()
            cur.execute("insert into luggage values(%s, %s, %d)",(pid, lid, nob))
            mysql.connection.commit()
            cur.close()
        if request.form['lugg'] == 'Update':
            luggageDetails = request.form
            pid = luggageDetails['pid']
            lid = luggageDetails['lid']
            nob = luggageDetails['nob']
            cur = mysql.connection.cursor()
            cur.execute("update luggage set p_id=%s, no_of_bags=%d where luggage_id=%s", (pid, nob, lid))
            mysql.connection.commit()
            cur.close()
        if request.form['lugg'] == 'Delete':
            luggageDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            pid = luggageDetails['pid']
            lid = luggageDetails['lid']
            nob = luggageDetails['nob']
            cur = mysql.connection.cursor()
            cur.execute("delete from luggage where luggage_id = %s and p_id = %s", (lid, pid))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/luggageview')
    return render_template('luggage.html')

# luggage view
@app.route('/luggageview')
def luggageview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM luggage")
    if resultValue > 0:
        luggageDetails = cur.fetchall()
        return render_template('luggageview.html', luggageDetails=luggageDetails)
    else:
        return render_template('luggageview.html')

# con_flight operations
@app.route('/con_flight', methods=['GET', 'POST'])
def con_flight():
    if request.method == 'POST':
        if request.form['conf'] == 'Show Table':
            # Fetch form data
            return redirect('/con_flightview')

        if request.form['conf'] == 'Insert':
            # Fetch form data
            confDetails = request.form
            fno = confDetails['fno']
            layt = confDetails['layt']
            nos = confDetails['nos']
            cur = mysql.connection.cursor()
            cur.execute("insert into connecting_flight values(%s, %s, %d)",(fno, layt, nos))
            mysql.connection.commit()
            cur.close()
        if request.form['conf'] == 'Update':
            confDetails = request.form
            fno = confDetails['fno']
            layt = confDetails['layt']
            nos = confDetails['nos']
            cur = mysql.connection.cursor()
            cur.execute("update connecting_flight set no_of_stops=%d, layover_time=%s where fno=%s", (nos, layt, fno))
            mysql.connection.commit()
            cur.close()
        if request.form['conf'] == 'Delete':
            confDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            fno = confDetails['fno']
            # layt = confDetails['layt']
            # nos = confDetails['nos']
            cur = mysql.connection.cursor()
            cur.execute("delete from connecting_flight where fno = %s", (fno))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/con_flightview')
    return render_template('con_flight.html')

# con_flight view
@app.route('/con_flightview')
def con_flightview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM connecting_flight")
    if resultValue > 0:
        confDetails = cur.fetchall()
        return render_template('con_flightview.html', confDetails=confDetails)
    else:
        return render_template('con_flightview.html')

# ns_flight operations
@app.route('/ns_flight', methods=['GET', 'POST'])
def ns_flight():
    if request.method == 'POST':
        if request.form['ns'] == 'Show Table':
            # Fetch form data
            return redirect('/ns_flightview')

        if request.form['ns'] == 'Insert':
            # Fetch form data
            nsDetails = request.form
            fno = nsDetails['fno']
            cur = mysql.connection.cursor()
            cur.execute("insert into non_stop_flight values(%s)",(fno))
            mysql.connection.commit()
            cur.close()
        if request.form['ns'] == 'Update':
            nsDetails = request.form
            fno = nsDetails['fno']
            cur = mysql.connection.cursor()
            cur.execute("update non_stop_flight set fno=%s where fno=%s", (fno, fno))
            mysql.connection.commit()
            cur.close()
        if request.form['ns'] == 'Delete':
            nsDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            fno = nsDetails['fno']
            cur = mysql.connection.cursor()
            cur.execute("delete from non_stop_flight where fno = %s", (fno))
            mysql.connection.commit()
            cur.close()
        
        return redirect('/ns_flightview')
    return render_template('ns_flight.html')

# ns_flight view
@app.route('/ns_flightview')
def ns_flightview():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM non_stop_flight")
    if resultValue > 0:
        nsDetails = cur.fetchall()
        return render_template('ns_flightview.html', nsDetails=nsDetails)
    else:
        return render_template('ns_flightview.html')


if __name__ == '__main__':
    app.run(debug=True)
