import core as client

client.make_connection_with_key('10.3.11.164', 'root', '/home/vithulan/ssh-keys/tmp_id_rsa', '')
client.make_dir('/root/', 'sherlock')
client.upload_to_directory('sherlock', 'SF-00004', '../files/testsftp2')
client.close_connection()

