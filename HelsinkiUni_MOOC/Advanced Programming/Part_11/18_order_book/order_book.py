class Task:
    _id_counter = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self._finished = False
        self.id = Task._id_counter
        Task._id_counter += 1

    def is_finished(self):
        return self._finished

    def mark_finished(self):
        self._finished = True

    def __str__(self):
        status = "FINISHED" if self._finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self._orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        task = description if isinstance(description, Task) else Task(description, programmer, workload)
        self._orders.append(task)

    def all_orders(self):
        return self._orders

    def programmers(self):
        return [programmer for programmer in dict.fromkeys(order.programmer for order in self._orders)]

    def mark_finished(self, id: int):
        for order in self._orders:
            if order.id == id:
                order.mark_finished()
                return

        raise ValueError("No task found with this id.")

    def finished_orders(self):
        return [order for order in self._orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self._orders if not order.is_finished()]

    def status_of_programmer(self, programmer: str):
        finished_count = 0
        unfinished_count = 0
        finished_hours = 0
        unfinished_hours = 0

        for order in self._orders:
            if order.programmer != programmer:
                continue

            if order.is_finished():
                finished_count += 1
                finished_hours += order.workload
            else:
                unfinished_count += 1
                unfinished_hours += order.workload

        if finished_count == 0 and unfinished_count == 0:
            raise ValueError("No programmer found with this name.")

        return (finished_count, unfinished_count, finished_hours, unfinished_hours)