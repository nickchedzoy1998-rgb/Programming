# Write your solution here
# If you use the classes made in the previous exercise, copy them here

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
        programmers = []
        for order in self._orders:
            if order.programmer_name not in programmers:
                programmers.append(order.programmer_name)
        return programmers
    
    def mark_finished(self, id:int):
        for o in self._orders:
            if o.task_id == id:
                o.mark_finished()
                return
        raise ValueError('No such task')
            
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
        unfinished_hours = 0
        for order in self.unfinished_orders():
            if order.programmer_name == programmer:
                programmer_exists = True
                unfinished_count += 1
                unfinished_hours += order.est_hours
        
        if not programmer_exists:
            raise ValueError('No programmer found with this name.')

        return (finished_count, unfinished_count, finished_hours, unfinished_hours)
    

class OrderBookApplication:
    def __init__(self):
        self._orderbook = OrderBook()

    def help(self):
        print('commands:')
        print('0 exit')
        print('1 add order')
        print('2 list finished tasks')
        print('3 list unfinished tasks')
        print('4 mark task as finished')
        print('5 programmers')
        print('6 status of programmer')

    def add_order(self):
        description = input('description: ')
        programmer_input = input('programmer and workload estimate: ')
        parts = programmer_input.rsplit(' ', 1)
        if len(parts) != 2:
            raise ValueError('Invalid programmer input')

        programmer_name, hours_text = parts
        est_hours = int(hours_text)
        order = Task(description, est_hours, programmer_name)
        self._orderbook.add_order(order)
        print('added!')
    
    def list_finished(self):
        finished = self._orderbook.finished_orders()
        if not finished:
            print('no finished tasks')
            return
        for order in finished:
            print(order)

    def list_unfinished(self):
        unfinished = self._orderbook.unfinished_orders()
        if not unfinished:
            print('no unfinished tasks')
            return
        for order in unfinished:
            print(order)

    def mark_task_finished(self):
        task_id = int(input('id: '))
        self._orderbook.mark_finished(task_id)
        print('marked as finished')

    def get_programmers(self):
        for programmer in self._orderbook.programmers():
            print(programmer)

    def programmer_status(self):
        programmer = input('programmer: ')
        finished_count, unfinished_count, finished_hours, scheduled_hours = (
            self._orderbook.status_of_programmer(programmer)
        )
        print(f'programmer: {programmer}')
        print(
            f'tasks: finished {finished_count} not finished {unfinished_count}, '
            f'hours: done {finished_hours} scheduled {scheduled_hours}'
        )

    def execute(self):
        self.help()
        while True:
            print('')
            command = input('command: ')
            try:
                if command == '0':
                    break
                elif command == '1':
                    self.add_order()
                elif command == '2':
                    self.list_finished()
                elif command == '3':
                    self.list_unfinished()
                elif command == '4':
                    self.mark_task_finished()
                elif command == '5':
                    self.get_programmers()
                elif command == '6':
                    self.programmer_status()
                else:
                    raise ValueError('Invalid command')
            except Exception:
                print('erroneous input')


app = OrderBookApplication()
app.execute()