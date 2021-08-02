class Testpaper():
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
        
class Student():
    def __init__(self):
        self.tests_taken = 'No tests taken'
        
    def take_test(self, testpaper, answers):
        correct_answers = 100 * sum(
            ans == corr_ans 
            for ans, corr_ans in zip(answers, testpaper.markscheme)
        ) / len(testpaper.markscheme)
        pass_mark = float(testpaper.pass_mark[:-1])
        is_passed = (
            'Passed!'
            if correct_answers >= pass_mark
            else 'Failed!'           
        )
        if not isinstance(self.tests_taken, dict):
            self.tests_taken = {}
        self.tests_taken.update(
            {testpaper.subject: f'{is_passed} ({correct_answers:.0f}%)'}
        )
