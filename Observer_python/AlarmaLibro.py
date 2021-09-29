from Subject import Subject

class AlarmaLibro(Subject):
    observers = []

    @classmethod
    def attach(cls, observer):
        cls.observers.append(observer)
    
    @classmethod
    def multi_attach(cls, attach_array):
        for i in attach_array:
            cls.observers.append(i)
    
    @classmethod
    def detach(cls, observer):
        try:
            cls.observers.remove(observer)
        except ValueError:
            print("No such observer to detach")

    @classmethod
    def clear_observers(cls):
        cls.observers.clear()

    @classmethod
    def notify_observers(cls, libro):
        for observer in cls.observers:
            observer.update(libro)
        cls.clear_observers()