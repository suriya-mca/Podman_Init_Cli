import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from click.testing import CliRunner
from main import podman_init

def test_podman_init_python_flask():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'python'], input='flask\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_python_fastapi():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'python'], input='fastapi\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_python_django():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'python'], input='django\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_java_spring():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'java'], input='spring\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_java_quarkus():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'java'], input='quarkus\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_java_micronaut():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'java'], input='micronaut\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_java_vertx():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'java'], input='vertx\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_java_javalin():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'java'], input='javalin\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_go_gin():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'go'], input='gin\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_go_echo():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'go'], input='echo\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_go_chi():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'go'], input='chi\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_go_fiber():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'go'], input='fiber\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_node_express():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'node'], input='express\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_node_nest():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'node'], input='nest\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore') 

def test_podman_init_node_koa():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'node'], input='koa\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore') 

def test_podman_init_node_fastify():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'node'], input='fastify\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')  

def test_podman_init_chash_dotnet_core():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'c#'], input='.net core\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')  

def test_podman_init_chash_blazor():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'c#'], input='blazor\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_rust_actix():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'rust'], input='actix\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_rust_axum():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'rust'], input='axum\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_rust_rocket():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'rust'], input='rocket\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_rust_warp():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'rust'], input='warp\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')

def test_podman_init_rust_tide():
    runner = CliRunner()
    result = runner.invoke(podman_init, ['--project-name', 'test_project', '--language', 'rust'], input='tide\n8000\n')
    assert result.exit_code == 0
    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('docker-compose.yml')
    assert os.path.isfile('.dockerignore')
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')
    os.remove('.dockerignore')