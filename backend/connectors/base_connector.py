class BaseConnector:
    def get_schema(self):
        raise NotImplementedError
    
    def execute_query(self, query):
        raise NotImplementedError