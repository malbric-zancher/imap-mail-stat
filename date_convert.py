import datetime
#from datetime import datetime, timedelta

x = raw_input('Start date eg. "10-Aug-2016":\t')
inc_by = int(raw_input('Increment by:\t'))
inc_until = int(raw_input('Increment for X days:\t'))
y = datetime
conversion = y.datetime.strptime(x, '%d-%b-%Y')

print 10 * '.'
print 'X: %r\ninc_by: %r\ninc_until: %r' % (x, inc_by, inc_until)
print 'After conversion: %r' % conversion
print 10 * '.'
# changing the date after conversion has been made
# let's increment by 1 day

for i in range(inc_until):
    conversion += datetime.timedelta(days=inc_by)
    print(conversion)

'''    
inc = conversion + y.timedelta(days=inc_by)
print 'Converted + incremented by 1: %r' % inc
'''
# now we have to change it back to previous string format after conversion and
# incrementation is successful
back = conversion.strftime('%d-%b-%Y')
print 'After conv+inc we get: %r' % back
