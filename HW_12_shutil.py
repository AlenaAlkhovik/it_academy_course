import shutil
import os

# task 1
shutil.copy('settings.ini', 'settings_backup.ini')

# task 2
os.makedirs('logs_backup', exist_ok=True)
shutil.copy('app.log', 'logs_backup/app.log')

# task 3
if os.path.exists('project_backup'):
    shutil.rmtree('project_backup')
shutil.copytree('project', 'project_backup')

# task 4
if os.path.exists('report.txt'):
    shutil.move('report.txt','report_old.txt')
else:
    print("File report.txt doesn't exist")

# task 5
os.makedirs(os.path.join('logs', 'archive'), exist_ok=True)
for item in os.listdir('logs'):
    path = os.path.join('logs', item)
    if os.path.isfile(path):
        path_2 = os.path.join('logs', 'archive', item)
        shutil.move(path, path_2)

# task 6
def clean_build():
    if os.path.exists('build'):
        shutil.rmtree('build')
        print('The "build" directory is deleted')
    else:
        print('The "build" directory does not exist. Nothing to delete')

clean_build()

# task 7
shutil.make_archive('project_backup', 'zip', 'project')

# task 8
if os.path.exists('restored_project'):
    shutil.rmtree('restored_project')

shutil.unpack_archive('project_backup.zip', 'restored_project')

# task 9
def learn_disk_usage():
    total, used, free = shutil.disk_usage('.')
    mb = 1024**2
    print(f'Total = {total/mb:.2f} MB')
    print(f'Used = {used/mb:.2f} MB')
    print(f'Free = {free/mb:.2f} MB')

learn_disk_usage()

# task 10
path = shutil.which('python') or shutil.which('python3')
if path:
    print(path)
else:
    print('Command not found.')