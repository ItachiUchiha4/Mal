def run(**args):

    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.44', username='pi', password='raspberry')
    stdin, stdout, stderr = ssh.exec_command("uptime")
    type(stdin)
    return stdout.readlines()
