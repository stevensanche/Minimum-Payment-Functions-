'''
CIS 122 Spring 2022 Project 2-2
Author(s): Steven Sanchez-Jimenez, C. Science
Description: Python functions; minimum payment function
'''

def payment(balance):
    '''
    calculting the 2.1% of the balance, then comparing it to $10 and the balance.
    If the minimum payment is greater than the balance, then the minimum payment
    becomes the balance.
    
    >>>payment(1000);
    21.0
    '''
    percent = balance*0.021
    minpay = max(10, percent)
    minpay = min(balance, minpay)
    print('Minimum payment for balance $%d is $%s.'%(balance,round(minpay, 1)))

payment(1000)
payment(600)
payment(25)
payment(8)

    
        
        
    
    
    
    
