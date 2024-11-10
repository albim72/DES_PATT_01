from flask import Flask, render_template, request, redirect, url_for

# Flask application initialization
app = Flask(__name__)

# Model
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True


class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()


# Initialize model
task_model = TaskModel()

# View (using Flask's template system)
@app.route('/')
def index():
    tasks = task_model.get_tasks()
    return render_template('index.html', tasks=tasks)


# Controller routes
@app.route('/add', methods=['POST'])
def add_task():
    description = request.form.get('description')
    if description:
        task_model.add_task(description)
    return redirect(url_for('index'))


@app.route('/remove/<int:task_index>')
def remove_task(task_index):
    task_model.remove_task(task_index)
    return redirect(url_for('index'))


@app.route('/complete/<int:task_index>')
def complete_task(task_index):
    task_model.complete_task(task_index)
    return redirect(url_for('index'))


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
