template = Import('../template.py')


def intro():
    intro = '''
Donner les inforamtion du compte agriculteur'''
    return intro


def MyAcountAgri():
    result = template.head()
    result += template.nav()
    result += template.header()
    result += intro()
    result += template.footer()
    return result
