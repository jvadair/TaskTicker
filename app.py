from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from PyQt5.uic import loadUi
from pyntree import Node
from datetime import datetime, timedelta
import sys
import os
from uuid import uuid4

# Load pyuic-compiled files for type hints only
from ui.main import Ui_MainWindow
from ui.newtask import Ui_NewTask
from ui.wip import Ui_WIP
from ui.done import Ui_Done

"""
TODO (additional):
_-_-_-_-_-_-_-_-_-

- Timer/Stopwatch & pause button
- work chunks & well done on {x} chunk message (today, tommorow, future)
- Task completion & skip heatmap/stats
- Skip button for overdue tasks
- Info screen
"""

# Init
db = Node("db.pyn", autosave=True)
mem = Node()

# First time setup
if not db():
    db.tasks = []
    db.tags = ["Schoolwork", "Development"]


def sort_tasks():
    db.tasks = sorted(db.tasks(), key=lambda d: d.due())  # Sort by due date

def build_queue():
    todo_today = []
    todo_later = []

    sort_tasks()
    for task in db.tasks():
        if task.created().date() == datetime.now().date():
            todo_today.append(task)

    if todo_today:
        mem.queue = todo_today
    else:
        mem.queue = todo_later


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/main.ui', self)
        self.connect()

    def connect(self):
        self.btnNewTask.clicked.connect(self.new_task_dialog)
        self.btnExit.clicked.connect(app.exit)
        self.btnEngage.clicked.connect(self.wip_dialog)
        self.act_engage.triggered.connect(self.wip_dialog)

    def new_task_dialog(self):
        self.ntd_window = NewTask()
        self.ntd_window.show()

    def wip_dialog(self):
        build_queue()
        if len(mem.queue()) < 1:
            QMessageBox.warning(self, "Error", "Please add some tasks first.")
        else:
            self.wip = WIP()
            self.wip.show()


class NewTask(QWidget, Ui_NewTask):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/newtask.ui', self)
        self.setup()
        self.connect()

    def setup(self):
        self.cbxTags.addItems(db.tags())
        self.dteDate.setDate(datetime.now().date() + timedelta(days=1))

    def connect(self):
        self.btnCancel.clicked.connect(self.close)
        self.btnCreate.clicked.connect(self.create_new_task)

    def create_new_task(self):
        task = Node()
        task.uuid = str(uuid4())
        task.title = self.txtTitle.text()
        task.description = self.txtDescription.toPlainText()
        task.created = datetime.now()
        task.due = self.dteDate.dateTime().toPyDateTime()
        task.tags = self.cbxTags.currentText()
        db.tasks().append(task)
        print(db.tasks())
        self.close()


class WIP(QWidget, Ui_WIP):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/wip.ui", self)
        self.connect()
        self.refresh()

    def connect(self):
        self.clbDone.clicked.connect(self.next_task)
        self.tolExtra.clicked.connect(self.show_description)

    def next_task(self):
        if len(mem.queue()) > 0:
            task = mem.queue().pop(0)  # Remove the current task from the queue
            for i in range(0, len(db.tasks())):  # Scan db for task
                if db.tasks()[i].uuid() == task.uuid():  # Check for matching uuid
                    db.tasks().pop(i)  # Delete by inde
                    break
            if len(mem.queue()) > 0:
                self.refresh()
            else:
                self.window_done = Done()
                self.window_done.show()
                self.close()

    def refresh(self):
        self.lblTask.setText(mem.queue()[0].title())

    def show_description(self):
        task = mem.queue()[0]
        QMessageBox.information(self, task.title(), task.description())


class Done(QWidget, Ui_Done):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/done.ui", self)
        self.connect()

    def connect(self):
        self.clbReturn.clicked.connect(self.close)


if __name__ == "__main__":
    mem.queue = []
    os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = "1"
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
