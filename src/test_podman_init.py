import os
from click.testing import CliRunner
from main import podman_init


def test_podman_init_python_flask():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'python'], input='flask\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_python_fastapi():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'python'], input='fastapi\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_python_django():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'python'], input='django\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_java_spring():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'java'], input='spring\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_java_quarkus():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'java'], input='quarkus\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_java_micronaut():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'java'], input='micronaut\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_java_vertx():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'java'], input='vertx\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_go_gin():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'go'], input='gin\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_go_echo():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'go'], input='echo\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_go_chi():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'go'], input='chi\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_go_fiber():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'go'], input='fiber\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_node_express():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'node'], input='express\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_node_nest():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'node'], input='nest\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore') 

def test_podman_init_node_koa():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'node'], input='koa\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore') 

def test_podman_init_node_fastify():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'node'], input='fastify\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')  

def test_podman_init_chash_dotnet_core():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'c#'], input='.net core\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')  

def test_podman_init_chash_blazor():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'c#'], input='blazor\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore') 

def test_podman_init_invalid_language():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'invalid_language'])
    assert result.exit_code != 0
    expected_error_message = "Invalid language selected."
    assert expected_error_message in result.output