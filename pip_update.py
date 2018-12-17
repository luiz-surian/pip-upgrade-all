import pkg_resources

packages = [dist.project_name for dist in pkg_resources.working_set]

with open('pip_upgrade.bat', 'w') as bat_file:
    bat_file.write('@echo off')
    bat_file.write('\n')
    bat_file.write('pip install --upgrade ' + ' '.join(packages))
    bat_file.write('\n')
    bat_file.write('pause')
