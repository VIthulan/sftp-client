import pysftp

sftp = None


def make_connection(host, username, password):
    try:
        global sftp
        sftp = pysftp.Connection(host=host, username=username, password=password)
    except Exception, e:
        print "Issue when making connection: %s" % str(e)


#
# Path : In which path to create folder if not exists and upload file
# file_name: local file path and name
#
def upload_to_directory(path, dir_name, file_name):
    try:
        with sftp.cd():
            sftp.chdir(path)
            sftp.makedirs(dir_name)
            sftp.chdir(dir_name)
            sftp.put(file_name, preserve_mtime=True)
    except Exception, e:
        print "Issue when uploading file %s to directory %s : %s" % (file_name, path, str(e))


#
# Path : exact folder path
#
def remove_directory(path):
    try:
        sftp.execute('rm -rf %s/' % path)
    except Exception, e:
        print "Issue when removing directory %s: %s" % (path, str(e))


#
# Path : in which location to run command
#
def execute_command(path, command):
    try:
        sftp.execute('cd %s && %s' % (path, command))
    except Exception, e:
        print "Issue when executing command %s: %s" % (command, str(e))


execute_command('/root/batman/', 'mkdir master')


sftp.close()
