import typer

app = typer.Typer()


@app.command()
def init_tictactoe():
    print("Initializing tic tac toe")


if __name__ == "__main__":
    app()
