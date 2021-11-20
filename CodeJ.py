import openai as op
from Prompts import Programming_Languages
from Context import programming_language_contexts, programming_language_examples
from GPTJ.gptj_api import Completion as completion


class Generation3:

    def __init__(self, output_file, api_key):
        assert isinstance(output_file, str), "output_file most be string value"
        self.output_file = output_file
        self.api_key = str(api_key)
        op.api_key = self.api_key

    def generation(self, language, temperature, *args):
        period = "."
        programming_languages = str(language)
        for i in args:
            assert isinstance(i, str), "args most be string value"
        assert isinstance(temperature, float), "temperature most be float value"
        assert temperature < 1, "temperature must be less than 1"
        list_of_examples = []
        for arg in args:
            string_of_examples = str(arg)
            list_of_examples.append(string_of_examples)
        if programming_languages == "MATLAB":
            prompt = Programming_Languages[0]
            stop_token = "%Task: "
            split_token = "%Code:\n"
            comment_token = "% "
        elif programming_languages == "Julia":
            prompt = Programming_Languages[1]
            stop_token = "#Task: "
            split_token = "#Code:\n"
            comment_token = "# "
        elif programming_languages == "C#":
            prompt = Programming_Languages[2]
            stop_token = "//Task: "
            split_token = "//Code:\n"
            comment_token = "// "
        elif programming_languages in {"Python", "Python3"}:
            prompt = Programming_Languages[3]
            stop_token = "#Task: "
            split_token = "#Code:\n"
            comment_token = "# "
        elif programming_languages == "C++":
            prompt = Programming_Languages[4]
            stop_token = "//Task: "
            split_token = "//Code:\n"
            comment_token = "// "
        elif programming_languages == "Q#":
            prompt = Programming_Languages[5]
            stop_token = "//Task: "
            split_token = "//Code:\n"
            comment_token = "// "
        elif programming_languages == "F#":
            prompt = Programming_Languages[6]
            stop_token = "//Task: "
            split_token = "//Code:\n"
            comment_token = "// "
        elif programming_languages == "JavaScript":
            prompt = Programming_Languages[7]
            stop_token = "//Task: "
            split_token = "//Code:\n"
            comment_token = "// "
        elif programming_languages == "Kotlin":
            prompt = Programming_Languages[8]
            stop_token = "//Task: "
            split_token = "//Code:\n"
            comment_token = "// "
        elif programming_languages == "Dart":
            prompt = Programming_Languages[9]
            stop_token = "//Task: "
            split_token = "//Code:\n"
            comment_token = "// "
        elif programming_languages == "Java":
            prompt = Programming_Languages[10]
            stop_token = "//Task: "
            split_token = "//Code:\n"
            comment_token = "// "
        elif programming_languages == "C":
            prompt = Programming_Languages[11]
            stop_token = "//Task: "
            split_token = "//Code:\n"
            comment_token = "// "
        elif programming_languages == "CSS":
            prompt = Programming_Languages[12]
            stop_token = "/*Task: "
            split_token = "/*Code: */\n"
            comment_token = "/* "
            out_comment_token = "*/"
        elif programming_languages == "HTML":
            prompt = Programming_Languages[13]
            stop_token = "<!--Task: "
            split_token = "<!--Code: -->\n"
            comment_token = "<!-- "
            out_comment_token = " -->"
        else:
            print("Invalid language please choose from the following languages: MATLAB, Julia, C#, Python, Python3, C++, Q#, F#, JavaScript, Kotlin, Dart, Java, C, CSS, HTML")

        def gpt3_gen():
            inputs = []
            outputs = []
            for i in list_of_examples:
                Prompt = prompt + i + period
                res = op.Completion.create(prompt=Prompt, engine="davinci-codex", max_tokens=333, echo=False,
                                           temperature=temperature,
                                           top_p=1.0, frequency_penalty=0.38, presence_penalty=0.39,
                                           best_of=1, stop=stop_token, n=1)
                response = res["choices"][0]["text"]
                output = response.split(split_token)
                final_response = str(output[1])
                inputs.append(i)
                outputs.append(final_response)

            return [inputs, outputs]

        def save_to_file(file_name, lang):
            if lang == "MATLAB":
                with open(f"completions/MATLAB/Codex/{file_name}.m", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Julia":
                with open(f"completions/Julia/Codex/{file_name}.jl", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "C#":
                with open(f"completions/C#/Codex/{file_name}.cs", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Python" or lang == "Python3":
                with open(f"completions/Python/Codex/{file_name}.py", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "C++":
                with open(f"completions/C++/Codex/{file_name}.cpp", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Q#":
                with open(f"completions/Q#/Codex/{file_name}.qs", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "F#":
                with open(f"completions/F#/Codex/{file_name}.fs", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "JavaScript":
                with open(f"completions/JavaScript/Codex/{file_name}.js", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Kotlin":
                with open(f"completions/Kotlin/Codex/{file_name}.kt", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Dart":
                with open(f"completions/Dart/Codex/{file_name}.dart", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Java":
                with open(f"completions/Java/Codex/{file_name}.java", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "C":
                with open(f"completions/C/Codex/{file_name}.c", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "CSS":
                with open(f"completions/CSS/Codex/{file_name}.css", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + out_comment_token + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "HTML":
                with open(f"completions/HTML/Codex/{file_name}.html", "w", encoding="UTF-8") as f:
                    Ins = gpt3_gen()[0]
                    Outs = gpt3_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + out_comment_token + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")

        save_to_file(self.output_file, programming_languages)


class GenerationJ:
    def __init__(self, output_file):
        assert isinstance(output_file, str), "output_file most be string value"
        self.output_file = output_file

    def generate(self,  language, temperature, top_p, *args):
        period = "."
        programming_languages = str(language)
        for i in args:
            assert isinstance(i, str), "args most be string value"
        assert isinstance(temperature, float), "temperature most be float value"
        assert isinstance(top_p, float), "top most be int value"
        assert 0 <= top_p <= 10, "top_p most be float value"
        assert 0 <= temperature <= 10, "temperature most be float value"
        list_of_examples = []
        for arg in args:
            string_of_examples = str(arg)
            list_of_examples.append(string_of_examples)
        if programming_languages == "MATLAB":
            context = programming_language_contexts[0]
            prompt = programming_language_examples[0]
            comment_token = "% "
        elif programming_languages == "Julia":
            context = programming_language_contexts[1]
            prompt = programming_language_examples[1]
            comment_token = "# "
        elif programming_languages == "C#":
            context = programming_language_contexts[2]
            prompt = programming_language_examples[2]
            comment_token = "// "
        elif programming_languages in {"Python", "Python3"}:
            context = programming_language_contexts[3]
            prompt = programming_language_examples[3]
            comment_token = "# "
        elif programming_languages == "C++":
            context = programming_language_contexts[4]
            prompt = programming_language_examples[4]
            comment_token = "// "
        elif programming_languages == "Q#":
            context = programming_language_contexts[5]
            prompt = programming_language_examples[5]
            comment_token = "// "
        elif programming_languages == "F#":
            context = programming_language_contexts[6]
            prompt = programming_language_examples[6]
            comment_token = "// "
        elif programming_languages == "JavaScript":
            context = programming_language_contexts[7]
            prompt = programming_language_examples[7]
            comment_token = "// "
        elif programming_languages == "Kotlin":
            context = programming_language_contexts[8]
            prompt = programming_language_examples[8]
            comment_token = "// "
        elif programming_languages == "Dart":
            context = programming_language_contexts[9]
            prompt = programming_language_examples[9]
            comment_token = "// "
        elif programming_languages == "Java":
            context = programming_language_contexts[10]
            prompt = programming_language_examples[10]
            comment_token = "// "
        elif programming_languages == "C":
            context = programming_language_contexts[11]
            prompt = programming_language_examples[11]
            comment_token = "// "
        elif programming_languages == "CSS":
            context = programming_language_contexts[12]
            prompt = programming_language_examples[12]
            comment_token = "/*"
            out_comment_token = "*/"
        elif programming_languages == "HTML":
            context = programming_language_contexts[13]
            prompt = programming_language_examples[13]
            comment_token = "<!--"
            out_comment_token = "-->"
        else:
            print("Invalid language please choose from the following languages: MATLAB, Julia, C#, Python, Python3, C++, Q#, F#, JavaScript, Kotlin, Dart, Java, C, CSS, HTML")

        def gptj_gen():
            inputs = []
            outputs = []
            for i in (list_of_examples):
                Prompt = i + period
                context_settings = completion(context, prompt)
                response = context_settings.completion(prompt=Prompt, user="User", bot="Quantum Coder", max_tokens=333, temperature=temperature, top_p=top_p)
                inputs.append(i)
                outputs.append(response)
            return [inputs, outputs]

        def save_to_file(file_name, lang):
            if lang == "MATLAB":
                with open(f"completions/MATLAB/gptj/{file_name}.m", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Julia":
                with open(f"completions/Julia/gptj/{file_name}.jl", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "C#":
                with open(f"completions/C#/gptj/{file_name}.cs", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Python" or lang == "Python3":
                with open(f"completions/Python/gptj/{file_name}.py", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "C++":
                with open(f"completions/C++/gptj/{file_name}.cpp", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Q#":
                with open(f"completions/Q#/gptj/{file_name}.qs", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "F#":
                with open(f"completions/F#/gptj/{file_name}.fs", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "JavaScript":
                with open(f"completions/JavaScript/gptj/{file_name}.js", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Kotlin":
                with open(f"completions/Kotlin/gptj/{file_name}.kt", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Dart":
                with open(f"completions/Dart/gptj/{file_name}.dart", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "Java":
                with open(f"completions/Java/gptj/{file_name}.java", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "C":
                with open(f"completions/C/gptj/{file_name}.c", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + out_comment_token + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "CSS":
                with open(f"completions/CSS/gptj/{file_name}.css", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")
            elif lang == "HTML":
                with open(f"completions/HTML/gptj/{file_name}.html", "w", encoding="utf-8") as f:
                    Ins = gptj_gen()[0]
                    Outs = gptj_gen()[1]
                    for i in range(len(Ins)):
                        f.write(comment_token + Ins[i] + out_comment_token + "\n")
                        f.write(Outs[i])
                    f.write("\n\n")

        save_to_file(self.output_file, programming_languages)




