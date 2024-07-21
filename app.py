from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

attendance_records = [{'1': 'EMP001', 'timestamp': '2024-07-21 09:00:00'},
    {'2': 'EMP002', 'timestamp': '2024-07-21 09:05:00'},
    {'3': 'EMP003', 'timestamp': '2024-07-21 09:10:00'},
    {'4': 'EMP004', 'timestamp': '2024-07-21 13:00:00'},
    {'5': 'EMP005', 'timestamp': '2024-07-21 13:05:00'},
    {'6': 'EMP006', 'timestamp': '2024-07-21 13:10:00'},]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        
        attendance_records.append({'employee_id': employee_id, 'timestamp': timestamp})

        return jsonify({'message': 'Attendance recorded successfully.'})

@app.route('/get_attendance', methods=['GET'])
def get_attendance():
    return jsonify({'attendance_records': attendance_records})

if __name__ == '__main__':
    app.run(debug=True)
