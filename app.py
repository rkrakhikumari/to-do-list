from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append({"text": task, "completed": False})
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    del tasks[task_id]
    return redirect(url_for('index'))

@app.route('/mark_completed/<int:task_id>', methods=['POST'])
def mark_completed(task_id):
    tasks[task_id]["completed"] = True
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)

