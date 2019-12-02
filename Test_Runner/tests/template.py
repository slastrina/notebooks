# Template Test Harness

#import <the spatialnet tool>
class snetTest(object):
    tool_name = 'Pole Utilisation Report'
    test_case = 'TC01' # if needed making per test case test runners
    jira_address = None
    author = 'User'
    output_path = None
    result = None

    def __init__(self, output_path):
        self.output_path = output_path
    
    def sayHello(self):
        return "hello"
    
    def get_tool_name(self):
        return self.tool_name
    
    def get_test_case(self):
        return self.test_case
    
    def get_jira_address(self):
        return self.jira_address
    
    def get_author(self):
        return self.author
        
    def get_output_path(self):
        return self.output_path
        
    def startTest(self):
        # This is your test entry point. Implement your testing here
        pass
    
    def get_result(self):
        return self.result