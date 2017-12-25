import paramiko

def run_command(command):
    stdin, stdout, stderr = ssh.exec_command(command)
    print stdout.readlines()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

pkey = '/Users/zhu/PycharmProjects/HackathonBob/fetch/key'
key = paramiko.RSAKey.from_private_key_file(pkey)
ssh.connect("10.244.20.154", 22, "ec2-user", pkey=key)
run_command("pwd")
ssh.close()
