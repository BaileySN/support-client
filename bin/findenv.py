import platform


def get_osname():
    env = 'linux'
    if platform.system():
        if platform.system().lower() in ['linux', 'linux2']:
            env = 'linux'
        elif platform.system().lower() in ['mac', 'darwin']:
            env = 'mac'
        elif platform.system().lower() in ['win32', 'win64', 'windows', 'win', 'nt']:
            env = 'nt'
    return env
