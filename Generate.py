from CodeJ import GenerationJ, Generation3

lang = "Python"
temperature = 0.6
top_p = 1.0


J = GenerationJ("file_name")
J.generate("Python", temperature, top_p, "Make a square", "Make a triangle using turtle")
