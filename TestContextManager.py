class TestContextManager:
    def __init__(self):
        pass
    def __enter__(self):
        print('Started')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Finished')
    def execute(self):
        print('Executing')

with TestContextManager() as tcm:
    #tcm is the return of the __enter__ method
    tcm.execute()
    
