class Task:

    def __init__(self, id, title, priority="Media",
                 status="A Fazer", deadline=None):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = status
        self.deadline = deadline

    def __repr__(self):
        return (f"Task(id={self.id}, title='{self.title}', "
                f"priority='{self.priority}', "
                f"status='{self.status}', "
                f"deadline='{self.deadline}')")
