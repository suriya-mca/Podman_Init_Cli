import os
import sys
import click
from click import style
from jinja2 import Environment, FileSystemLoader

@click.command()
@click.option('--project-name', 
                 prompt='Enter project name', 
                 help='Name of the project')
@click.option('--language', 
                 prompt='Choose language', 
                 type=click.Choice(['python', 'java', 'go', 'node', 'c#', 'rust'], case_sensitive=False), 
                 help='Choose project language')
def podman_init(project_name, language):

    match language:
        case "python":       
            framework = click.prompt('Choose framework', 
                                      type=click.Choice(['django', 'fastapi', 'flask', 'pyramid', 'flacon', 'exit'], case_sensitive=False), 
                                      show_choices=True)

            port = click.prompt('Choose port', 
                                 type=int)

            if framework == 'exit':
                click.echo(style("Exiting...", fg='red'))
                sys.exit()

            template_dir = os.path.join(os.path.dirname(__file__), 'templates', language)

        case "java":        
            framework = click.prompt('Choose framework', 
                                      type=click.Choice(['spring', 'quarkus', 'micronaut', 'vertx', 'javalin', 'exit'], case_sensitive=False), 
                                      show_choices=True)

            port = click.prompt('Choose port', 
                                 type=int)

            if framework == 'exit':
                click.echo(style("Exiting...", fg='red'))
                sys.exit()

            template_dir = os.path.join(os.path.dirname(__file__), 'templates', language)

        case "go" :
            framework = click.prompt('Choose framework', 
                                      type=click.Choice(['gin', 'echo', 'chi', 'fiber', 'exit'], case_sensitive=False), 
                                      show_choices=True)

            port = click.prompt('Choose port', 
                                 type=int)

            if framework == 'exit':
                click.echo(style("Exiting...", fg='red'))
                sys.exit()

            template_dir = os.path.join(os.path.dirname(__file__), 'templates', language)

        case "node" :
            framework = click.prompt('Choose framework', 
                                      type=click.Choice(['express', 'nest', 'koa', 'fastify', 'exit'], case_sensitive=False), 
                                      show_choices=True)

            port = click.prompt('Choose port', 
                                 type=int)

            if framework == 'exit':
                click.echo(style("Exiting...", fg='red'))
                sys.exit()

            template_dir = os.path.join(os.path.dirname(__file__), 'templates', language)

        case "c#" :
            framework = click.prompt('Choose framework', 
                                      type=click.Choice(['.net core', 'blazor'], case_sensitive=False), 
                                      show_choices=True)

            port = click.prompt('Choose port', 
                                 type=int)

            if framework == 'exit':
                click.echo(style("Exiting...", fg='red'))
                sys.exit()

            template_dir = os.path.join(os.path.dirname(__file__), 'templates', language)

        case "rust" :
            framework = click.prompt('Choose framework', 
                                      type=click.Choice(['actix', 'axum', 'rocket', 'warp', 'tide', 'exit'], case_sensitive=False), 
                                      show_choices=True)

            port = click.prompt('Choose port', 
                                 type=int)

            if framework == 'exit':
                click.echo(style("Exiting...", fg='red'))
                sys.exit()

            template_dir = os.path.join(os.path.dirname(__file__), 'templates', language)

        case _:
            click.echo("Invalid language selected.")
            return

    load_jinja_env = Environment(loader=FileSystemLoader(template_dir))

    dockerfile_template = load_jinja_env.get_template('Dockerfile.j2')
    dockerfile_content = dockerfile_template.render(project_name=project_name, framework=framework, port=port)

    with open('Dockerfile', 'w') as f:
        f.write(dockerfile_content)

    compose_template = load_jinja_env.get_template('docker-compose.yml.j2')
    compose_content = compose_template.render(project_name=project_name, framework=framework, port=port)

    with open('docker-compose.yml', 'w') as f:
        f.write(compose_content)

    with open('.dockerignore', 'w') as f:
        f.write("*.pyc\n__pycache__/\n.git\n.gitignore\n*.env\n.vscode/\n.idea/\n")

    click.echo(style('✔ Podman initialized!', fg='green'))
    click.echo(style('RUN -> "podman-compose up"', fg='green'))

if __name__ == '__main__':
    podman_init()