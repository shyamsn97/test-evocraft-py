import click

from test_evocraft_py.test_evocraft_py import shutdown_server, start_server, start_server_interactive

@click.command()
@click.option('--start/--shutdown', default=True)
@click.option('--interactive', is_flag=True)
def main(start, interactive):
    """Simple program that greets NAME for a total of COUNT times."""
    if start:
        if interactive:
            print("Running in interactive mode!")
            start_server_interactive()
        else:
            print("Starting server!")
            start_server()
    else:
        print("Shutting down server!")
        shutdown_server()

if __name__ == '__main__':
    main()
