from game import IllegalActionError
from ui import Bot, COMMANDS, Ui


with open("token.txt") as file:
    TOKEN = file.read().strip()


def bot():
    Bot(Ui()).run(TOKEN)


def cli():
    ui = Ui()
    ui.display_prompt()
    if ui.output:
        print(ui.output.get(), end="")
    while not ui.quit:
        prompt = input()
        if not prompt.startswith("."):
            continue
        if prompt.startswith(".."):
            continue
        try:
            for command in COMMANDS:
                if not command.recognises(prompt):
                    continue
                command.execute(ui, prompt)
                break
            else:
                print(f"unknown command {prompt}")
        except (IllegalActionError, ValueError) as error:
            print(str(error))
        ui.display_prompt()
        if ui.output:
            print(ui.output.get(), end="")


bot()
