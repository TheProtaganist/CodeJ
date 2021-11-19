MATLAB = """
%Task: Plot a circle with a given radius and center.
%Code: 
function h = circle(x,y,r)
hold on
th = 0:pi/50:2*pi;
xunit = r * cos(th) + x;
yunit = r * sin(th) + y;
h = plot(xunit, yunit);
hold off

%Task: Converting Fahrenheit to Celsius.
%Code: 
function Celsius = f_to_c(Fahrenheit)
Celsius = (5/9)*(Fahrenheit-32);
end

%Task: Ask a user to enter two numbers x and y store the product in a variable z.
%Code: 
promptX = 'Enter a number: ';
promptY = 'Enter a secound number: ';
x = input(promptX);
y = input(promptY);
z = x*Y

%Task: Multiply the elements of two 3-by-3 array matrices A and B.
%Code:
A = [1 0 3; 5 3 8; 2 4 6];
B = [2 3 7; 9 1 5; 8 8 3];
C = A.*B

%Task: Make an octagon and plot it and find the area.
%Code: 
p = % Make the octagon
linspace(0,2.*pi,9);
x = 1.2*cos(p)';
y = 1.2*sin(p)'; 

% Plot the polygon
plot(x,y);
axis equal

a = polyarea(x,y)';
disp(a) 

%Task: make a function to reload a gui app by closing it and automatically repopening it.
%Code: 
function reload(hObject, eventdata, handles)
close all;
clear all; 
clc; 
load gui.mat; 
load gui_workspace.mat; 
guidata(hObject, handles);
end

%Task: return the cube of a number.
%Code:
function cube = cube(x)
cube = x^3;
disp(cube)
end

%Task: """

Julia = """
#Task: Write a program that returns the root of the number.
#Code: 
x = int(input("Enter an integer: "))
while x > 0:
  n = int(input("Enter another one: "))
  if n > 0:
    break
  else:
    print("You entered a negative number. Please try again.")
if (x**2 == n) and (n > 0):
  println(n, "is the square root of", x)
else:
    println(x, "is not a perfect square root")
    
#Task: prompt the user to guess a word. If they guess successfully print "Congratulations" otherwise print "Try again".
#Code:
num_guesses = 0
correct_guess = "Julia"
while (True):
  guess = input("Enter a guess: ")
  num_guesses += 1
  if (guess == correct_guess):
    print("Congratulations")
    break
  elif (num_guesses == 3):
    print("Try again")
    break

#Task: Basic hello world in Julia.
#Code:
println("Hello World")

#Task: return the 9th power of a decimal type number.
#Code:
a = float(input("Enter an float number: "))
answer = a^9
println(answer)

#Task: Converting Fahrenheit to Celsius.
#Code:
f = float(input("Enter Fahrenheit scale: "))
c = (f - 32)*5/9
println("Celsius scale", c)

#Task: Ask a user to enter two numbers x and y store the product in a variable z.
#Code:
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = x*y
println("Product: ", z)

#Task: Ask user to enter a number and check if it is divisible by 2 or not. 
#Code:
n = int(input("Enter a number"))
if n%2 == 0:
  print("yes")
else:
 print("no")

#Task: """

C_Sharp = """
//Task: Make a basic hello world in Unity.
//Code:
using System;
using System.Collections:
using System.Collections.Generic;
using System.Linq;
using System.Text;
using UnityEngine;


public class HelloWorld : MonoBehaviour
{
    void Start()
    {
        Debug.Log("Hello World");
    }

}

//Task: Make a basic hello world in C#.
//Code:
using System;
using System.Collections;
using System.Collections.Generic;

namespace HelloWorld
{
    class HelloWorld
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World");
            Console.Readkey();
        }
    }
}


//Task: Write a function that takes in a string and returns the number of vowels in the string.
//Code:
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _02_VowelsInAString
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("Enter a string: ");

            string input = Console.ReadLine();

            int vowels = 0;

            for (int i = 0; i < input.Length; i++)
            {

                if (input[i] == 'a' || input[i] == 'e' || input[i] == 'i' || input[i] == 'o' || input[i] == 'u')  //if the character is a vowel, add 1 to the counter variable vowels
                {

                    vowels++;

                }

            }

            Console.WriteLine("The number of vowels in the string is: " + vowels); //print out the number of vowels in the string

        }

    }
}

//Task: Using Unity make a cube move up and set it to a random color.
//Code:

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Cube : MonoBehaviour {

    public float speed = 1f;

    // Use this for initialization
    void Start () {

    }

    // Update is called once per frame
    void Update () {

        transform.Translate(Vector3.up * Time.deltaTime * speed);

        if (transform.position.y >= 10) {
            Destroy(gameObject);
        }

        int r = Random.Range(0, 256);
        int g = Random.Range(0, 256);
        int b = Random.Range(0, 256);

        GetComponent<Renderer>().material.color = new Color32((byte)r, (byte)g, (byte)b, 255);

    }
}

//Task: Make a player move in any direction UpArrow, DownArrow, LeftArrow or RightArrow using Unity.
//Code:

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour {

    public float speed = 10f;

    private Rigidbody2D rb2d;

	// Use this for initialization
	void Start () {
        rb2d = GetComponent<Rigidbody2D>();
	}

	// Update is called once per frame
	void Update () {

        if (Input.GetKey(KeyCode.UpArrow)){
            rb2d.velocity = new Vector2(0, speed);

        } else if (Input.GetKey(KeyCode.DownArrow)){
            rb2d.velocity = new Vector2(0, -speed);
        } else if (Input.GetKey(KeyCode.LeftArrow)){
            rb2d.velocity = new Vector2(-speed, 0);

        } else if (Input.GetKey(KeyCode.RightArrow)){
            rb2d.velocity = new Vector2(speed, 0);

        } else {

            rb2d.velocity = new Vector2(0, 0);
        }

    }
}

//Task: return the 5th power of a decimal type number.
//Code:

using System;

class FifthPower
{
    static void Main()
    {
        Console.Write("Enter a decimal number: ");
        decimal number = decimal.Parse(Console.ReadLine());

        Console.WriteLine("The 5th power of the number is: {0}", Math.Pow(number, 5));
    }
}

//Task: Render text using unity.
//Code: 
using System;
using UnityEngine;
using UnityEngine.UI;

public class TextRendering : MonoBehaviour {

    public Font font;

    public float fontSize = 1f;

    public int textLength = 10;

    private Text textComponent;

    void Start() {
        textComponent = GetComponent<Text>();
        textComponent.font = font;
        textComponent.fontSize = fontSize;

        string text = "";

        for (int i = 0; i < textLength; i++) {
            char c = (char)('A' + i);
            text += c.ToString();
        }

        textComponent.text = text;

        Debug.Log(text);
    }

    void Update() { }
}

//Task: """

Python3 = """#Task: Write a program that draw an oval using the turtle module (NOT A CIRCLE).
#Code:
import turtle


def draw_oval(radius):
    turtle.setheading(45)
    for _ in range(2):
        # Draw Oval
        turtle.color("purple")
        turtle.circle(radius, 90)
        turtle.circle(radius // 2, 90)


# calling draw method
draw_oval(200)

#Task: Write a program that draws a square using the turtle module.
#Code:
import turtle


def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)


# calling draw method
draw_square(100)

#Task: Using numpy make a function that returns the sin, cos, tan, and cot of an angle in degrees.
#Code:
import numpy as np


def sin_cos_tan_cot(angle):
    return np.sin(angle), np.cos(angle), np.tan(angle), np.cot(angle)

sin_cos_tan_cot(45)

#Task: Make a class that represents a movie. The movie should have a title, storyline, rating, and opinion. With SEVERAL methods including a setter for the rating.
#Code:
class Movie:
    def __init__(self, title, storyline, rating, trailer):
        self.title = title
        self.storyline = storyline
        self.__rating = rating
        self.trailer = trailer

    def MovieInfo(self):
        return f"{self.title} is a {self.rating} movie with the storyline {self.storyline} and the trailer {self.trailer}"

    def set_rating(self, rating):
        self.rating = rating if rating in ["G", "PG", "PG-13", "R"] else "NR"


MovieInformation = Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                         "R", "Very True and informative")

MovieInformation.set_rating("R")
print(MovieInformation.MovieInfo())

#Task: There is a song named Georgie by Powers, write a program describing the song.
#Code:
artist = "Powers"
song_title = "Georgie"
song_genre = "Pop"
song_length = "3:25"
song_rating_of_100 = "100"

print(f"The song {song_title} by {artist} is a {song_genre} song with a length of {song_length} and a rating of {song_rating_of_100}")


#Task: Make an array of dictionaries that represents a list of songs. Each song should have a title, artist, genre, length, and rating.
#Code:
songs = {
    "Georgie": {
        "artist": "Powers",
        "genre": "Pop",
        "length": "3:25",
        "rating": "100"
    },
    "Never Gonna Give you up": {
        "artist": "Rick Astley",
        "genre": "Pop",
        "length": "3:32",
        "rating": "63"
    },
    "Sweetheart by Mariah Carey":
    {"artist": "Mariah Carey",
        "genre": "Pop",
        "length": "4:25",
        "rating": "100"},

}

for song in songs:
    print(f"The song {song} by {songs[song]['artist']} is a {songs[song]['genre']} song with a length of {songs[song]['length']} and a rating of {songs[song]['rating']}")

#Task: Write a program that returns the square root of the number.
#Code:
import math

def square_root(number):
    return math.sqrt(number)

#Task: """

C_plus_plus = """
//Task: Write a function that takes in a string and returns the number of vowels in the string.
//Code:
#include<iostream>
using namespace std;

// Function to check the Vowel
bool isVowel(char ch)
{
    ch = toupper(ch);
    return (ch=='A' || ch=='E' || ch=='I' ||
                       ch=='O' || ch=='U');
}

// Returns count of vowels in str
int countVowels(string str)
{
    int count = 0;
    for (int i=0; i<str.length(); i++)
        if (isVowel(str[i])) // Check for vowel
            ++count;
    return count;
}

// Main Calling Function
int main()
{
    //string object
    string str = "abc de";
    // Total numbers of Vowel
    cout << countVowels(str) << endl;
    return 0;
}

//Task: Create a class business that has a name, address, and phone number.
//Code:
#include<iostream>
using namespace std;
class business {
    private:
        string name;
        string address;
        string phone;
    public:
        business(string name, string address, string phone) {
            this->name = name;
            this->address = address;
            this->phone = phone;
        }
        void print() {
            cout << "Name: " << name << endl;
            cout << "Address: " << address << endl;
            cout << "Phone: " << phone << endl;
        }
};

int main() {
    business b("ABC", "123 Main St", "555-555-5555");
    b.print();
    return 0;
}

//Task: make a scientific calculator.
//Code:
#include<iostream>
using namespace std;
class calculator {
    private:
        double num1;
        double num2;
    public:
        calculator(double num1, double num2) {
            this->num1 = num1;
            this->num2 = num2;
        }

        // Addition function for calculator class.

        void add() { cout << "Addition of two numbers is " << (num1 + num2) << endl;}

        // Subtraction function for calculator class.

        void sub() { cout << "Subtraction of two numbers is " << (num1 - num2) << endl;}

        // Multiplication function for calculator class.

        void mul() { cout << "Multiplication of two numbers is " << (num1 * num2) << endl;}

        // Division function for calculator class.

        void div() { if(num2 != 0){cout << "Division of two numbers is " << (num1 / num2) << endl;} else{cout<<"Cannot divide by zero"<<endl;}}

    };
int main() {
    double a, b;
    cout<<"Enter the first number:"; cin>>a; cout<<endl;  cout<<"Entercal(a,b); cal.add(); cal.sub(); cal.mul(); cal.div(); return 0;} the second number:"; cin>>b; cout<<endl;  calculator

    return 0;
    }


//Task: retrun a number of days in a month.
//Code:
#include<iostream>
using namespace std;


int main() {
    int month, year;
    cout<<"Enter the month:"; cin>>month; cout<<endl;
    cout<<"Enter the year:"; cin>>year; cout<<endl;
    switch(month) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            cout<<"31 days"<<endl;
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            cout<<"30 days"<<endl;
            break;
        case 2:
            if(year%4==0) {
                cout<<"29 days"<<endl;
            }
            else {
                cout<<"28 days"<<endl;
            }
            break;
        default:
            cout<<"Invalid month"<<endl;
            break;
    }
    return 0;
}

//Task: return the 4th power of a number.
//Code:
#include<iostream>
using namespace std;


int main() {
    int num;
    cout<<"Enter the number:"; cin>>num; cout<<endl;
    cout<<"The 4th power of the number is "<<num*num*num*num<<endl;
    return 0;
}

//Task: return the sum of the first n natural numbers.
//Code:
#include<iostream>
using namespace std;


int main() {
    int num;
    cout<<"Enter the number:"; cin>>num; cout<<endl;
    int sum=0;
    for(int i=1;i<=num;i++) {
        sum+=i;
    }
    cout<<"The sum of the first "<<num<<" natural numbers is "<<sum<<endl;
    return 0;
}


//Task: prompt the user to guess a word. If they guess successfully print "Congratulations" otherwise print "Try again".
//Code:
#include<iostream>
using namespace std;


int main() {
    string word;
    cout<<"Enter the word:"; cin>>word; cout<<endl;
    if(word=="hello") {
        cout<<"Congratulations"<<endl;
    }
    else {
        cout<<"Try again"<<endl;
    }
    return 0;
}

//Task: """

Q_Sharp = """
//Task: Basic Hello world.
//Code:
namespace HelloQuantum {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    

    @EntryPoint()
    operation SayHello() : Unit {
        Message("Hello quantum world!");
    }
}

//Task: Initialize a simple qubit.
//Code:
namespace InitQubit {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    

    @EntryPoint()
    operation SetQubitState(desired : Result, q1 : Qubit) : Unit {
        using (qubit = Qubit()) {  // allocate a qubit
            H(qubit);              // put the qubit to superposition 
            Message("Qubit in state |1⟩");  // print the complex vector representation of the qubit state
            Reset(qubit);          // release the qubit resources (back to |0⟩)  
        }        
    }
}


//Task: Put the qubit to superposition.
//Code:
namespace sp {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    operation SetQubitState(desired : Result, q1 : Qubit) : Unit {
        using (qubit = Qubit()) {  // allocate a qubit
            H(qubit);              // put the qubit to superposition 
            Message("Qubit in state |1⟩");  // print the complex vector representation of the qubit state
            Reset(qubit);          // release the qubit resources (back to |0⟩)  
        }        
    }
}


//Task: Measure a qubit in the computational basis.
//Code:
namespace comBasis {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    operation SetQubitState(desired : Result, q1 : Qubit) : Unit {
        using (qubit = Qubit()) {  // allocate a qubit
            H(qubit);              // put the qubit to superposition 
            Message("Qubit in state |1⟩");  // print the complex vector representation of the qubit state
            let res = M(qubit);    // measure the qubit and store the result in res 
            Message($"Measured result was {res}");     // print the measurement result of the qubit  
            Reset(qubit);          // release the qubit resources (back to |0⟩)  
        }        
    }
}


//Task: Measure a qubit in the Bell basis states [-1/√2, -1/√2] and [1/√2, -1/√2].
//Code:
namespace Bell {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    operation SetQubitState(desired : Result, q1 : Qubit) : Unit {
        using (qubit = Qubit()) {  // allocate a qubit
            H(qubit);              // put the qubit to superposition 
            Message("Qubit in state |1⟩");  // print the complex vector representation of the qubit state
            
            let res1 = M(qubit);   // measure the qubit and store the result in res1
            Message($"Measured result was {res1}");     // print the measurement result of the qubit  

            let res2 = M(qubit);   // measure the qubit and store the result in res2
            Message($"Measured result was {res2}");     // print the measurement result of the qubit  

            Reset(qubit);          // release the qubit resources (back to |0⟩)  
        }        
    }
}


//Task: Put a qubit to superposition on |0>+|1> state and measure the result using H gate.
//Code:
namespace H_gate {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    operation SetQubitState(desired : Result, q1 : Qubit) : Unit {
        using (qubit = Qubit()) {  // allocate a qubit
            H(qubit);              // put the qubit to superposition 
            Message("Qubit in state |1⟩");  // print the complex vector representation of the qubit state
            
            let res = M(qubit);    // measure the qubit and store the result in res  

            Reset(qubit);          // release the qubit resources (back to |0⟩)  
        }        
    }
}


//Task: Put a qubit to superposition on |0>-|1> state and measure the result using X gate.
//Code:
namespace sp0 {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    operation SetQubitState(desired : Result, q1 : Qubit) : Unit {
        using (qubit = Qubit()) {  // allocate a qubit
            X(qubit);              // put the qubit to superposition with negative phase 
            Message("Qubit in state -|1⟩");  // print the complex vector representation of the qubit state            

            let res = M(qubit);    // measure the qubit and store the result in res  

            Reset(qubit);          // release the qubit resources (back to |0⟩)  
        }        
    }
}

//Task: """

F_Sharp = """
//Task: print a Basic Hello World.
//Code:
open System

let Hello_world_program() =
    printfn "Hello World!"
    
Hello_world_program()

//Task: add two numbers a and b.
//Code:
open System
open System.IO
let a = 1 
let b = 2 
let c = a + b 
printfn "sum of %d and %d is %d" a b c

//Task: Log of an exponential function.
//Code:
open System
open System.IO
let f_of_x = fun x -> Math.Log(1.0 + x * x)
printfn "the log of %f is %f" 1.0 f_of_x 1.0

//Task: Evaluate a trigonometric function at x.
//Code:
open System
open System.IO
let sinusoid = fun x -> Math.Sin(x) 
printfn "The sinusoid of %f is %f" 1.0 sinusoid 1.0


//Task: Print a Matrix.
//Code:
open System
open System.IO
let matrix = [| 1.0; 2.0; 3.0 |]
printfn "The matrix is %A" matrix


//Task: Print a list of numbers.
//Code:
open System
open System.IO
let numbers_list = [1; 2; 3; 4] 
printfn "The list is %A" numbers_list

//Task: Make the user guess the right sentence which is "Trees are fun".
//Code:
open System
open System.IO
let guess_sentence() = 
    printfn "Guess a sentence"
    let sentence = Console.ReadLine()
    if sentence = "Trees are fun" then
        printfn "You have guessed right!"
    else 
        printfn "Try Again!"

//Task: """

JavaScript = """
//Task: make a function that returns the sin, cos, tan, and cot of an angle in degrees.
//Code:
var degrees = 45;
var sin = Math.sin(degrees * Math.PI / 180);
var cos = Math.cos(degrees * Math.PI / 180);
var tan = Math.tan(degrees * Math.PI / 180);
var cot = 1 / tan;
console.log(sin, cos, tan, cot);


//Task: There is a song named Cyber Cities by Virtual singers a band, write the lyrics of the song.
//Code: 
console.log("Singing");
console.log("Cyber Cities By Virtual singers");
console.log("I'm in the future, I'm in a cyber world");
console.log("I'm in the future, I'm in a cyber world");
console.log("Can you feel it? Can you see it? Can you feel it now?");

//Task: Make an array of dictionaries that represents a list of books. Each song should have a title, artist, genre, pages, and rating.
//Code:

let book1 = ["Title": "The Da Vinci Code", "Author": "Dan Brown", "Genre": "Renery Thriller", "Pages": 599, "Rating": 3]
let book2 = ["Title": "The Ritual", "Author": "Phillip Pullman", "Genre": "Fantasy", "Pages": 526, "Rating": 4]
let book3 = ["Title": "The Great Gatsby", "Author":" F. Scott Fitzgerald", "Genre":"Classic Novels" ,  "Pages":244,"Rating":5]
let book4 = ["Title": "The Lion, the Witch and the Wardrobe", "Author":" C.S. Lewis", "Genre":"Children Fiction" ,  "Pages": 350,"Rating":3]
let book5 = ["Title": "The Secret Garden: A Novel of Suspense", "Author": "Frances Hodgson Burnett", "Genre":"Children Fiction" ,  "Pages": 245, "Rating":4]
let book6 = ["Title": "The Fault in our Stars","Author":" John Green",  "Genre":"Literary Fiction" ,  "Pages":328,"Rating":5 ]
let book7 = ["Title": "Gone Girl",  "Author":"Gillian Flynn",  "Genre":"Mystery Thriller" ,  "Pages":399,"Rating":5]

let listOfBooks = [book1,book2,book3,book4,book5,book6,book7]

func getRating(books:[Dictionary<String,Any>])->Int{
    var sum = 0
    for i in 0...books.count - 1{
        let rating = (books[i]["Rating"] as! Int)
        sum += rating
    }
    return sum / books.count
}

//Task: Write a program that returns the square root of the number.
//Code: 
var number = 9;
var sqrt = Math.sqrt(number);
console.log("The square root of: " + number + " is " + sqrt);


//Task: Write a program that returns the value of the following equation when x is given. (x > 0).
//Code: 
function findValueOfEquation(x) {
    return -1 / (Math.log(x));
}

 //Task: Build a function that will tell you if a triangle is equilateral, scalene or an isosceles triangle based on its measurements. The program should ask for the three lengths of the triangle and display a message telling you whether it's equilateral or not, etc.
//Code: 
function identifyTriangle(a, b, c) {

    if ((a == b && b == c) || (a != b && b != c && c != a)) {
        console.log("This is an Equilateral Triangle."); //
    } else if ((a == b && b != c) || (a != b && b == c)) {
        console.log("This is an Isosceles Triangle.");     

    } else if ((a != b && a != c && c != a) || (a == c && a != b)) {
        console.log("This is an Scalene Triangle.");      

    } else { console.log("Invalid Input."); };  
    return [a, b, c];      
    var s = (a + b + c) / 2;       
    var areaOfTriangle = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    return String(areaOfTriangle);            
};

//Task: prompt the user to guess a word. If they guess successfully print "Congratulations" otherwise print "Try again".
//Code: 
var word = "JavaScript";
var letter;
var count = 0;
var guessCount;
while (count < word.length) {
    guessCount = 0;
    letter = prompt("Guess a letter in the word.");

    if (word.indexOf(letter) > -1) {
        alert("Correct!"); 

        for (i = 0; i < word.length; i++) {
            if (word[i] == letter) {  count++; }  
            else if (word[i] != letter) { guessCount++ }; 
            guessCount++;                                            
        }     

    if (guessCount == word.length && count >= word.length) { alert ("Congratulations!"); break};  

    } else { alert("Try again"); };    

     console.log(count);

}

//Task: """

Kotlin = """
//Task: Add two numbers in a method called calculator.
//Code:
fun calculator(a: Int, b: Int) {
    print("The sum of given numbers is " + (a + b))
}

fun main(args: Array<String>) {
    val a = 5
    val b = 4

    calculator(a, b) //calling the method with arguments passed as a and b.
}

//Task: Make a simple story with some primitves "Name", "age", and "Favorite hobby".
//Code:
fun main(args: Array<String>) {
    val name = "Tim" //string
    val age = 25 //int
    val hobby = "Sports" //string

    print("My name is ${name} and my age is ${age} years old. My favorite hobby is ${hobby}.")
}

//Task: Use the following words in a method "Hello", "my", "name", and "is".
//Code:
fun main(args: Array<String>) {
    print("Hello my name is " + "Juan") //concatenation
}

//Task: Take a base num "base" and write a 2 methods that give you both the exponent and the log to a provided power.
//Code:
fun log(base: Double, power: Double) {
    val result = Math.log(power) / Math.log(base)
    print("The log of ${power} to the base ${base} is " + result)
}

fun exponent(base: Double, power: Double) {
    val result = Math.pow(base, power)
    print("The exponent of ${base} to the power ${power} is " + result)
}

//Task: Create a method called addOneToNum that takes one parameter and returns that number plus one. Assign this to a variable and print it out using the variable you get it with in your main method. Then print out the result of addOneToNum alone without assigning it to a variable. 
//Code:
fun main(args: Array<String>) {
    val result = addOneToNum(2)

    print(result)
}
fun addOneToNum(num: Int): Int {
    return num + 1 //returning the number plus one.
}

//Task: Suppose we are using android studio, write a method that shows a text that says "The product of num1 and num2 is (answer)" where num1 and num2 are the values of the variables. Make sure do display the text in the app and not the console.
//Code:
fun main(args: Array<String>) {
    val num1 = 5
    val num2 = 10

    printProduct(num1, num2) //calling the method with arguments passed as a and b.
}

fun printProduct(a: Int, b: Int){
    val text = "The product of ${a} and ${b} is ${a * b}" //text to be displayed in the app.

    print(text) //printing the text in the app not console.
}

//Task: Create a method called multiplyTwoNumbers that takes two parameters and returns the product of them. Then call this method in your main method and print out the result.
//Code:
fun main(args: Array<String>) {
    val result = multiplyTwoNumbers(2, 10)

    print(result)
}

fun multiplyTwoNumbers(a: Int, b: Int): Int {
    return a * b //returning the product of the two numbers.
}

//Task: """

Dart = """
//Task: give the radius and center.
//Code:
void main() {
  var radius = 10;
  var center = new Point(10, 10);
  var circle = new Circle(radius, center);
  print(circle.area);
}

//Task: Converting Fahrenheit to Celsius.
//Code:
void main() {
  var fahrenheit = 100;
  var celsius = (fahrenheit - 32) * 5 / 9;
  print(celsius);
}

//Task: Ask a user to enter two numbers x and y store the product in a variable z.
//Code:
void main() {
  var x = 10;
  var y = 20;
  var z = x * y;
  print(z);
}

//Task: Multiply the elements of two 3-by-3 array matrices A and B.
//Code:
void main() {
  var a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ];
  var b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ];
  var c = [];
  for (var i = 0; i < 3; i++) {
    c.add([]);
    for (var j = 0; j < 3; j++) {
      c[i].add(0);
      for (var k = 0; k < 3; k++) {
        c[i][j] += a[i][k] * b[k][j];
      }
    }
  }
  print(c);
}

//Task: Write a program to find the sum of all the elements of a matrix.
//Code:
void main() {
  var a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ];
  var sum = 0;
  for (var i = 0; i < 3; i++) {
    for (var j = 0; j < 3; j++) {
      sum += a[i][j];
    }
  }
  print(sum);
}

//Task: return the cube of a number.
//Code:
void main() {
  var x = 10;
  var y = x * x * x;
  print(y);
}

//Task: make a method that predicts the next number in the Fibonacci sequence.
//Code:
void main() {
  var x = 10;
  var y = fibonacci(x);
  print(y);
}

//Task: """

Java = """
//Task: Add two numbers in a method called calculator.
//Code:
public class Calculator {

    public static void main(String[] args) {
        calculator(2, 3);
    }

    public static void calculator(int a, int b) {
        System.out.println("Addition of two numbers is: " + (a + b));
    }
}

//Task: Make a simple story with some primitves "Name", "age", and "Favorite hobby".
//Code:
public class Story {
    public static void main(String[] args) {
        String name = "Sebastain";
        int age = 24;
        String hobby = "traveling";

        System.out.println("There was once a man named " + name);
        System.out.println("He is " + age + " years old and his favorite hobby is " + hobby);

    }
}

//Task: Use the following words in a "static" method "Hello", "my", "name", and "is".
//Code:
public class Static {

    public static void main(String[] args) {
        String hello = "Hello";
        String my = "my";
        String name = "name";
        String is = "is";

        staticSentence(hello, my, name, is);
    }

    public static void staticSentence(String a, String b, String c, String d) {
        System.out.println(a +" "+b+" "+c+" "+d);
    }
}


//Task: Take a base num "base" and write a 2 methods that give you both the exponent and the log to a provided power.
//Code:
public class Exponent {

    public static void main(String[] args) {
        System.out.println("The log to 10 of 1000 is: " + exponent(1000, 10) + " and the exponent of 10 of 3 is: " + log(3, 10));
    }

    public static double exponent(double number, double power) {
        return Math.pow(number, power);
    }

    public static int log(double base, double num) {
        return (int) Math.log(num) / Math.log(base);
    }
}


//Task: Create a method called addOneToNum that takes one parameter and returns that number plus one. Assign this to a variable and print it out using the variable you get it with in your main method. Then print out the result of addOneToNum alone without assigning it to a variable. 
//Code:
public class AddOne {

    public static void main(String[] args) { 
        int myInt = addOneToNum(2);

        System.out.println("My integer plus one is " + myInt);

        System.out.println("Adding one to 2 is " + addOneToNum(2));

    }

    public static int addOneToNum(int num) { 
        return num + 1; 
    } 
}

//Task: Suppose we are using android studio, write a method that shows a text that says "The product of num1 and num2 is (answer)" where num1 and num2 are the values of the variables. Make sure do display the text in the app and not the console.
//Code:
public class Android {

    public static void main(String[] args) { 
        int num1 = 10;
        int num2 = 100;

        displayText("The product of " + num1 + " and " + num2 + " is: " + (num1 * num2));

    }

    public static void displayText(String text) { 
        System.out.println(text); 
    } 
}


//Task: Create a method called multiplyTwoNumbers that takes two parameters and returns the product of them. Then call this method in your main method and print out the result.
//Code:
public class MultiplyTwoNumbers {

    public static void main(String[] args) { 
        System.out.println("The product of 2 and 3 is: " + multiplyTwoNumbers(5, 7));

    }

    public static int multiplyTwoNumbers(int x, int y) { 
        return x * y; 
    }  
}

//Task: """

C = """
//Task: prompt the user to guess a word. If they guess successfully print "Congratulations" otherwise print "Try again".
//Code:
#include<stdio.h>

int main(){
	int index, guess;
	char word[3] = "Tim";//enter the word that you want to guess

	printf("Guess a word\n");
	scanf("%d", &index);
	guess = word[index];

	if (guess == 'T'){ //enter the right character of the word that you want to guess
	printf("Congratulations!");
	}else{
	printf("Try again");
	}

	return 0;
}

//Task: print a short story keep it PG.
//Code:
#include<stdio.h>

int main(){

	printf("We are all caught up in our ordinary lives and we never know when fate will intervene.\n");
	printf("It's a Sunday morning and you walk down to the river bank,\n");
	printf("The water is flowing, the birds are singing and you feel happy as ever.\n");
	printf("Then you see something moving in the water, it is a small golden fish, it swims toward you.\n");
	printf("So happy that you jump into the water, with one hand on your hat and the other holding your pants.\n");
	printf("You catch the fish with one hand and somehow manage to put it into your coat pocket.\n");
	printf("You take out your book from your pocket and flip to a page that tells about how a man was carried away by a magical fish.\n");

	return 0;
}

//Task: return the sum of the first n natural numbers.
//Code:
#include<stdio.h>

int main(){

	int n, sum = 0;

	printf("Enter a number\n");
	scanf("%d", &n);

	while (n >= 1){//enter the n'th number that you want to calculate

	sum += n; //add to sum from the first value until it reaches the entered number
	n--; //decrement by one because of the while statement
	}

	printf("The sum of the first %d natural numbers is %d", n, sum); //printing out the result

	return 0;
}

//Task: Write a program that prints out all numbers between 1 and 100 with no duplicates.
//Code: 
#include<stdio.h>

int main(){

	int i = 0; //initialize a counter variable 
    int j = 1;//initialize another counter variable for use in nested loop.  

    for(i=1; i <=100 ; i++){ //outer loop from 1 to 100 incrementing by 1 each time.  

     for(j=1; j < 100/*lowest value*/; j++){ //inner loop from 1 to 99 incrementing by 1 each time  .  

         if(i != j) {  /*if outer loop count does not equal inner loop count, print out*/ 

             printf("%d ", i);  /*outer loop's count */ 
         }  
     }  

     printf("\n");   /*new line after every outer loop completes.*/ 
    }  

    return 0;  /*successful completion of program*/  
}


//Task: return the square power of a number.
//Code:
#include<stdio.h>

int main(){

	int a, b;

	printf("Enter a number\n");
	scanf("%d", &a);

	b = a * a;

	printf("The square power of %d is %d", a, b);

	return 0;
}

//Task: make a calculator.
//Code:
#include<stdio.h>

int main(){

	int num1, num2, add, sub, mul, div;

	printf("Enter the first number\n");
	scanf("%d", &num1);

	printf("Enter the second number\n");
	scanf("%d", &num2);

	add = num1 + num2; //addition
	sub = num1 - num2; //subtraction
	mul = num1 * num2; //multiplication 
	div = num1 / num2; //division 

	printf("The addition of %d and %d is %d\n", num1, num2, add);
	printf("The subtraction of %d and %d is %d\n", num1, num2, sub);
	printf("The multiplication of %d and %d is %d\n", num1, num2, mul);
	printf("The division of %d and %d is %.0lf\n", num1, num2, div);

    return 0;  /*successful completion of program*/  
}

//Task: make an array of 10 numbers and print out the sum of the numbers.
//Code:
#include<stdio.h>


int main(){

    int i, sum = 0;
    int array[10];
    
    for(i = 0; i < 10; i++){
        printf("Enter a number\n");
        scanf("%d", &array[i]);
        sum += array[i];}
        
    printf("The sum of the numbers is %d", sum);
    
    return 0;
    }

//Task: """

CSS = """
/*Task: Make rows to be 200px high and each column 50px wide. */
/*Code: */
div{
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    grid-template-rows: repeat(5, 200px);
    grid-row-gap: 1rem;   /* to give 1rem gap between the rows */
}

/*Task: Make a black grid with 10 columns, each with a width of 100 pixels. Make rows to be 200px high and each column 50px wide. */
/*Code: */
div{
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    grid-template-rows: repeat(5, 200px);
    grid-row-gap: 1rem;   /* to give 1rem gap between the rows */

     body {  /* for inner divs */ 
        background-color:#000;  /* black color */ 
        width:50px;   /* width of the inner divs */ 
        height:200px; /* height of the inner divs */ 

     } 

 }

/*Task: Align content in a grid.*/
/*Code: */
div{
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    grid-template-rows: repeat(5, 200px);
    grid-row-gap: 1rem;   /* to give 1rem gap between the rows */

     body {  /* for inner divs */ 
        background-color:#ffff00;  /* yellow color */ 
        width:50px;   /* width of the inner divs */ 
        height:200px; /* height of the inner divs */ 

     } 

     body {  /* for inner divs */ 
        background-color:#ffffff;  /* white color */ 
        width:50px;   /* width of the inner divs */ 
        height:200px; /* height of the inner divs */ 

     } 

     body {  /* for inner divs */ 
        background-color:#0000ff;   /* blue color */  
        width:50px;   /* width of the inner divs */ 
        height:200px; /* height of the inner divs */     

     }

     .align_center{   /* class for aligning center content in a row*/
         justify-self: center;   /* to align center content in a row*/     

     }
 }

/*Task: Use background-color to make an alternating color grid. */
/*Code: */
div{
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    grid-template-rows: repeat(5, 200px);
    grid-row-gap: 1rem;   /* to give 1rem gap between the rows */

     body {  /* for inner divs */ 
        background-color:#000000;  /* black color */ 
        width:50px;   /* width of the inner divs */ 
        height:200px; /* height of the inner divs */ 

     } 

     body {  /* for inner divs */ 
        background-color:#ffffff;  /* white color */  
        width:50px;   /* width of the inner divs */ 
        height:200px; /* height of the inner divs */     

     }

     .bg_black{   /* class for alternating colors in a row*/
         background-color:#000000;     

     }

     .bg_white{   /* class for alternating colors in a row*/
         background-color:#ffffff;     

     }
 }

/*Task: Use row-gap to space the rows out. */
/*Code: */
div{
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    grid-template-rows: repeat(5, 200px);
    grid-row-gap: 1rem;   /* to give 1rem gap between the rows */

     body {  /* for inner divs */ 
        background-color:#000000;  /* black color */ 
        width:50px;   /* width of the inner divs */ 
        height:200px; /* height of the inner divs */ 

     } 

     body {  /* for inner divs */ 
        background-color:#ffffff;  /* white color */  
        width:50px;   /* width of the inner divs */ 
        height:200px; /* height of the inner divs */     

     }
     .align_center{   /* class for aligning center content in a row*/
         justify-self: center;   /* to align center content in a row*/     

     }
 }


/*Task: Make rows to be 800px high and each column 600px wide.  */
/*Code: */
div{
    display: grid;
    grid-template-rows: repeat(8, 1fr);
    grid-template-columns: repeat(6, 1fr);
    background-color: cyan;
}


/*Task: Set all of the grid's gutter widths to be 45px.*/
/*Code: */
div{
    display: grid;
    grid-template-rows: repeat(8, 1fr);
    grid-template-columns: repeat(6, 1fr);
    background-color: cyan;
    grid-gap: 45px;   /* to give 45px gap between the rows and columns */
}

/*Task: """

HTML = """
<!--Task: Make a simple page to ask the user for a name and display "hello" plus the name with the text being 300 by 300 and in blue. Use <script> and </script> in the code Since we are using Java Scirpt-->
<!--Code: -->
<html>
<head>
	<title>Hello World</title>
	<script type="text/javascript">
	function askName(){
	var name = prompt("Please enter your name:");

	document.write("Hello " + name);

	}
</script>
</head>
<body onload="askName()">

            <button onclick="myFunction()">Click me!</button><br/>

        </body>
</html>

<!--Task: Make a yellow square in the center using css with the dimesions 200 by 200 -->
<!--Code: -->
<html>
<head>
	<title>Yello Square</title>
</head>
<style type="text/css">

        body { background-color: black; }

        .myRectangle {

            width: 200px;

            height: 200px;

            background-color: yellow;

            position:relative; /*You may leave this out*/

            left:50%; /*Set the left margin of the element to 50% of its parent element's width*/

            top:50%; /*Set the top margin of the element to 50% of its parent element's height*/ 

        }
</style>
<body>
	 <div class="myRectangle"></div>  
</body>
</html>
<!--Task: Make a red circle in a cyan background-->
<!--Code: -->
<html>
<head>
	<title>Red circle</title>
</head>
<style type="text/css">

        body { background-color: cyan; }

        .myCircle {

            width: 100%; /*Set the width of the element to 100% of its parent element's width*/

            height: 100%; /*Set the height of the element to 100% of its parent element's height*/ 

            border-radius: 50%; /*Set a border radius so it looks like a circle*/ 

            background-color: red;  /*Set the background color to red*/ 

            position:relative; 

        }
</style>
<body>
	 <div class="myCircle"></div> 
</body>
</html>
<!--Task: Make a red square in the center using css with the dimesions 100 by 100-->
<!--Code: -->
<html>
<head>
	<title>square 100 by 100</title>
</head>
<style type="text/css">

        body { background-color: black; }

        .mySquare {

            width: 100px;  /*Set the width of the element to 100% of its parent element's width*/ 

            height: 100px; /*Set the height of the element to 100% of its parent element's height*/ 

            background-color: red; /*Set the background color to red*/ 

            position:relative; 

        }
</style>
<body>
	 <div class="mySquare"></div>  
</body>
</html>

<!--Task: Using Java script make a simple page to ask the user for 2 numbers to add and update when the user enters 2 new numbers-->
<!--Code: -->
<html>
<head>
	<title>adding</title>
	<script type="text/javascript">
	function askNumber() {
	var firstnumber = prompt("Please enter the first number:");

	document.write(firstnumber + " added to the second number is :" + parseInt(firstnumber) + parseInt(secondnumber));

	}
</script>
</head>
<body onload="askNumber()">

            <button onclick="myFunction()">Click me!</button><br/>

        </body>
</html>
<!--Task: In a #5633a9 hex color background ask the user to divide 2 numbers in a white text field with #ffa500 text. Update the user when they enter a new number by dividing the two numbers and show the result in a white text field.-->
<!--Code: -->
<html>
<head>
	<title>division</title>
	<script type="text/javascript">
	function askNumber() {

    var firstnumber = prompt("Please enter the first number:");

     var secondnumber = prompt("Please enter the second number:");

     document.write("The answer is: " + parseInt(firstnumber) / parseInt(secondnumber)); 

    }
</script>
</head>
<style type="text/css">

        body { background-color: #5633a9; }

        .answer { color: white; font-size: 15px; font-family: sans-serif; }  /*Set these properties to style a div*/  

        .numbers { color:#ffa500 ; font-size: 17px; /*Set these properties to style an input box*/  } 
</style>   <body onload="askNumber()">    <div class="answer"></div><input type="text" name="" id="" class="numbers" /> </body></html>

<!--Task: Show a this image http://i.imgur.com/qz2XB.png in a #0000ff hex color background using css-->
<!--Code: -->
<html>
<head>
	<title>showing images</title>
</head>
<style type="text/css">

        body { background-color: #ff0000; }

        img { width: 300px; height: 300px; }  /*Set these properties to style an image*/  
</style>   <body><img src="http://i.imgur.com/qz2XB.png" alt="red square" /> </body></html>

<!--Task: """

Programming_Languages = [MATLAB, Julia, C_Sharp, Python3, C_plus_plus, Q_Sharp, F_Sharp, JavaScript, Kotlin, Dart, Java, C, CSS, HTML]