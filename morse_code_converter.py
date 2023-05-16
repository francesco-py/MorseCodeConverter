class MorseCodeConverter:
    def __init__(self):
        self.morse_dict = {
        "a":"•-",
        "b":"-•••",
        "c":"-•-•",
        "d":"-••",
        "e":"•",
        "f":"••-•",
        "g":"--•",
        "h":"••••",
        "i":"••",
        "j":"•---",
        "k":"-•-",
        "l":"•-••",
        "m":"--",
        "n":"-•",
        "o":"---",
        "p":"•--•",
        "q":"--•-",
        "r":"•-•",
        "s":"•••",
        "t":"-",
        "u":"••-",
        "v":"•••-",
        "w":"•--",
        "x":"-••-",
        "y":"-•--",
        "z":"--••",
        "1":"•----",
        "2":"••---",
        "3":"•••--",
        "4":"••••-",
        "5":"•••••",
        "6":"-••••",
        "7":"--•••",
        "8":"---••",
        "9":"----•",
        "0":"-----",
        ".":"•-•-•-",
        ",":"--••--",
        "?":"••--••",
        "!":"-•-•--",
        "/":"-••-•",
        "(":"-•--•",
        ")":"-•--•-",
        ":":"---•••",
        ";":"-•-•-•",
        "=":"-•••-",
        "+":"•-•-•",
        "-":"-••••-",
        "_":"••--•-",
        '"':"•-••-•",
        "@":"•--•-• ",
        "$":"•••-••-",
        " ":"|"
        }




    def convert_to_morse(self, message):
        converted_message = [*str(message).lower()]
        converted_message = "".join([f"{self.morse_dict[char]}/" for char in converted_message])
        return converted_message




    def convert_to_text(self, message):
        message = message.split("/")
        converted_message = []
        for char in message:
            for values in self.morse_dict.items():
                if values[1] == char:
                    converted_message.append(values[0])
        return "".join(converted_message)



