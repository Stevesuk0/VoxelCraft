import minecraft.client.main.Main

class Start:
    def __init__(self) -> None:
        minecraft.client.main.Main.main(
            {
                'accessToken': '0',
                'version': '1.8'
            }
        )


Start()