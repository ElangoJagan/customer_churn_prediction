import sys

def get_error_details(error:Exception, sys_module)->str:
    
    """
    Extracts detailed error information including file name,
    line number and error message.

    Args:
        error: The exception that was raised
        sys_module: The sys module for traceback extraction

    Returns:
        Formatted error message string
    """
    _,_, exc_tb= sys_module.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number= exc_tb.tb_lineno
    error_message = str(error)
    
    return(
        f"\n{'='*60}\n"
        f"ERROR DETAILS:\n"
        f"  File    : {file_name}\n"
        f"  Line    : {line_number}\n"
        f"  Message : {error_message}\n"
        f"{'='*60}"
    )
    

class CustomException(Exception):
    
    """
    Custom exception class that provides detailed error information.

    New OOP Concept Learned: __str__ + __repr__
    __str__  → what humans see when exception is printed
    __repr__ → what developers see when debugging
    """
    
    def __init__(self, error:Exception, sys_module):
        
        """
        Initialize CustomException with detailed error info.

        Args:
            error: The exception that was raised
            sys_module: The sys module for traceback extraction
        """
        self.error_message = get_error_details(error, sys_module)
        super().__init__(self.error_message)
    
    def __str__(self):
        '''Human friendly error message'''
        return self.error_message
    def __repr__(self):
        'developer friendly error representation'
        return f'CustomException({self.error_message})'