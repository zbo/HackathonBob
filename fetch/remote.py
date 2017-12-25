import paramiko

class remote:

    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        pkey = '/Users/zhu/PycharmProjects/HackathonBob/fetch/key'
        self.key = paramiko.RSAKey.from_private_key_file(pkey)

    def connect(self):
        self.ssh.connect("10.244.20.154", 22, "ec2-user", pkey=self.key)

    def run(self, command):
        self.run_command(command)

    def close(self):
        self.ssh.close()

    def run_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout, stderr

if __name__ == "__main__":
    ssh_one = remote()
    ssh_one.connect()
    stdout, stderr = ssh_one.run_command("pwd")
    print stdout.readlines()
    print stderr.readlines()
    ssh_one.close()


