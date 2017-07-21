import core as client

client.make_connection('', '', '')
client.make_dir('/root/', 'sherlock')
client.upload_to_directory('sherlock', 'SF-00001', '../files/testsftp2')
client.close_connection()

