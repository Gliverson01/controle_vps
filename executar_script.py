import paramiko

def executar_comando_na_vps(hostname, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, username='root', password=password)
        comando = './instala_resetV2.sh'
        stdin, stdout, stderr = ssh.exec_command(comando)
        output = stdout.read().decode()
        return output

    except Exception as e:
        return f"Erro na conexão: {e}"

    finally:
        ssh.close()
