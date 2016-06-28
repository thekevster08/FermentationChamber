from ConfigParser import SafeConfigParser

config = SafeConfigParser()

def updateSampleTime(sampleTime):
    config.read('config.ini')
    config.set('main', 'sampleTime', sampleTime)
    with open('config.ini', 'w') as f:
        config.write(f)
        
def updateSetpoint(setpoint):
    config.read('config.ini')
    config.set('controller', 'setpoint', setpoint)
    with open('config.ini', 'w') as f:
        config.write(f)
        
def updateActiveDeadband(activeDeadband):
    config.read('config.ini')
    config.set('controller', 'activeDeadband', activeDeadband)
    with open('config.ini', 'w') as f:
        config.write(f)
        
def updateInactiveDeadband(inactiveDeadband):
    config.read('config.ini')
    config.set('controller', 'inactiveDeadband', inactiveDeadband)
    with open('config.ini', 'w') as f:
        config.write(f)
