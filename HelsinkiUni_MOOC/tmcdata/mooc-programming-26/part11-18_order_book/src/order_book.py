class Task:
    _id_counter = 1
    def __init__(self, description: str, est_hours: int, programmer_name: str):
        self.description = description
        self.est_hours = est_hours
        self.programmer_name = programmer_name
        self._finished = False
        self.task_id = Task._id_counter
        Task._id_counter += 1

    @property
    def is_finished(self):
        if self._finished == True:
            return 'FINISHED'
        else:
            return 'NOT FINISHED'
    
    def mark_finished(self):
        self._finished = True

    def __str__(self):
        return f'{self.task_id}: {self.description} ({self.est_hours} hours), programmer {self.programmer_name} {self.is_finished}'


class OrderBook:
    def __init__(self):
        self._orders = []

    def add_order(self, order: Task):
        self._orders.append(order)

    def all_orders(self):
        return self._orders
    
    def programmers(self):
        return list(set([o.programmer_name for o in self._orders]))
    
    def mark_finished(self, id:int):
        for o in self._orders:
            if o.task_id == id:
                o.mark_finished()
                return
            
    def finished_orders(self):
        return [order for order in self._orders if order.is_finished == 'FINISHED']

    def unfinished_orders(self):
        return [order for order in self._orders if order.is_finished == 'NOT FINISHED']
    
    def status_of_programmer(self, programmer: str):
        programmer_exists = False

        finished_count = 0
        finished_hours = 0
        for order in self.finished_orders():
            if order.programmer_name == programmer:
                programmer_exists = True
                finished_count += 1
                finished_hours += order.est_hours

        unfinished_count = 0
        unifinished_hours = 0
        for order in self.unfinished_orders():
            if order.programmer_name == programmer:
                programmer_exists = True
                unfinished_count += 1
                unifinished_hours += order.est_hours
        
        if programmer_exists == False:
            raise ValueError('No programmer found with this name.')

        return (finished_count, unfinished_count, finished_hours, unifinished_hours)