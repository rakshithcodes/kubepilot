import typer
from kubepilot.kubernetes.pods import list_pods
app = typer.Typer()


@app.command()
def hello():
    print("Hello from KubePilot v2")


@app.command()
def version():
    print("0.1.0")

@app.command()
def pods(
    namespace: str = typer.Option(None, "-namespace", "-n", help="Namespace to list pods from. If not provided, the current namespace will be used.")
    ):
    if namespace:
        list_pods(namespace)
    else:    
        list_pods()

if __name__ == "__main__":
    app()