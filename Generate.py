from CodeGen import GenerationJ, Generation3

lang = "Python"
temperature = 0.9
top_p = 1.0


J = GenerationJ("Temp")
J.generate("Python", temperature, top_p, "Make a square", "Make a triangle using turtle")
