from colorama import Fore
import openai
from CodeJ import Generation3, GenerationJ


def generate_response():
    Model = str(input("Choose a model codex or gptj (to exit ,type quit anytime to exit): "))
    if Model == "quit":
        exit()
    if Model == "codex":
        try:
            list_of_prompts = []
            number_of_prompts = int(input("Enter the number of prompts you want to generate: "))
            if number_of_prompts == "quit":
                exit()
            if number_of_prompts < 0:
                print("You can only generate a positive number of prompts")
            for prompt in range(number_of_prompts):
                prompts = str(input(f'Enter prompt {prompt + 1}: '))
                if prompts == "quit":
                    exit()
                list_of_prompts.append(prompts)
            lang = str(input("Choose a programing language: "))
            if lang not in {
                "MATLAB",
                "Julia",
                "C#",
                "Python", "Python3",
                "C++",
                "Q#", "F#",
                "JavaScript",
                "Kotlin",
                "Dart",
                "Java",
                "C", "CSS", "HTML"}:
                print("Please enter a valid language")
                generate_response()
            if lang == "quit":
                exit()
            file_name = str(input("Choose a file name to store your code: "))
            if file_name == "quit":
                exit()
            try:
                temperature = float(
                    input("Enter a temperature from 0.0 to 1.0 (Max 10.0 if you are using gpt-j) to choose how "
                          "creative "
                          "or on topic you want the response to be\nNote lower values produce more accurate results: "))
                if temperature == "quit":
                    exit()
                try:
                    key = str(input("Enter your api key: "))
                    if key == "quit":
                        exit()
                    gpt3 = Generation3(file_name, key)
                    print(f"{Fore.BLUE}generation for {len(list_of_prompts)} prompts beginning{Fore.WHITE}")
                    gpt3.generation(lang, temperature, *list_of_prompts)
                except openai.error.AuthenticationError:
                    print("Your API key is invalid please try again")
            except ValueError:
                print("Please enter a valid number for temperature")
        except ValueError:
            print("Please enter a number for number of prompts")
    elif Model == "gptj":
        try:
            list_of_prompts = []
            number_of_prompts = int(input("Enter the number of prompts you want to generate: "))
            if number_of_prompts == "quit":
                exit()
            if number_of_prompts < 0:
                print("You can only generate a positive number of prompts")
            for prompt in range(number_of_prompts):
                prompts = str(input(f'Enter prompt {prompt + 1}: '))
                if prompts == "quit":
                    exit()
                list_of_prompts.append(prompts)
            lang = str(input("Choose a programing language: "))
            if lang not in {
                "MATLAB",
                "Julia",
                "C#",
                "Python", "Python3",
                "C++",
                "Q#", "F#",
                "JavaScript",
                "Kotlin",
                "Dart",
                "Java",
                "C", "CSS", "HTML"}:
                print("Please enter a valid language")
                generate_response()
            if lang == "quit":
                exit()
            file_name = str(input("Choose a file name to store your code: "))
            if file_name == "quit":
                exit()
            try:
                temperature = float(
                    input("Enter a temperature from 0.0 to 1.0 Max 10.0 if you are using gpt-j (NOT recommended) to choose how "
                          "creative "
                          "or on topic you want the response to be\nNote lower values produce more accurate results: "))
                if temperature == "quit":
                    exit()
                top_p = 5 / 12
                J = GenerationJ(file_name)
                print(f"{Fore.BLUE}generation for {len(list_of_prompts)} prompts beginning{Fore.WHITE}")
                J.generate(lang, temperature, top_p, *list_of_prompts)
            except ValueError:
                print("Please enter a valid number of the temperature")
        except ValueError:
            print("Please enter a valid number for the number of prompts")
    else:
        print("Invalid model")