import typer

app = typer.Typer()


@app.command()
def hello():
    print("Hello from KubePilot v2")


@app.command()
def version():
    print("0.1.0")


if __name__ == "__main__":
    app()