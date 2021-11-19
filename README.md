# CodeJ
A python project made to generate code using either OpenAI's codex or GPT-J (Although not as good as codex)

## Install requirements
```
pip install -r requirements.txt
```
## Gpt-J
first set everything up (Note: you can change the temperature to a higher value for more creative results)
```python
from CodeJ import GenerationJ

lang = "Python"
temperature = 0.6
top_p = 1.0
```python
J = GenerationJ("file_name")
```
Now call the method to generate text
```python
J.generate("Python", temperature, top_p, "Make a square", "Make a triangle using turtle")
```
For Both the gptj and codex version you can pass as many prompts as you want
## Codex

```python
from CodeJ import Generation3

temperature = 0.3
gpt3 = Generation3("Temp", "Replace with your API key")
gpt3.generation("Python", 0.416, "Make a square using the turtle module", "Add take the power of numbers in an array", "Print CodeJ is awesome")
```
Sign up for an api-key here https://beta.openai.com/signup
Use the free Gpt-J version if you want as well

