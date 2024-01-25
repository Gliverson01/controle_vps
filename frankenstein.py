from run_commands_on_vps import run_commands_on_vps
from flask import Flask, render_template, request
from executar_script import executar_comando_na_vps

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    error = None

    if request.method == 'POST':
        if 'num_vps' in request.form:
            vps_list = []
            num_vps = int(request.form['num_vps'])

            for i in range(num_vps):
                ip_key = f'ip_{i+1}'
                username_key = f'username_{i+1}'
                password_key = f'password_{i+1}'

                if ip_key in request.form and username_key in request.form and password_key in request.form:
                    ip = request.form[ip_key]
                    username = request.form[username_key]
                    password = request.form[password_key]

                    vps_list.append({
                        'ip': ip,
                        'username': username,
                        'password': password
                    })
                else:
                    break

            commands = ['fetch', 'reset --hard', 'pull']
            output = run_commands_on_vps(vps_list, commands)

        elif 'hostname' in request.form and 'password' in request.form:
            hostname = request.form['hostname']
            password = request.form['password']

            output = executar_comando_na_vps(hostname, password)

            if "Erro" in output:
                error = output
                output = None

    return render_template('index.html', num_vps=1, output=output, error=error)

if __name__ == '__main__':
    app.run(debug=True)
