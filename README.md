<h1 align="center">Fibonacci sequence</h1>
<p align="center"><a href="https://en.wikipedia.org/wiki/Fibonacci_sequence"><img src="images/readme/fibonacci.jpg" alt="Image of Fibonacci" width="500"></a></p>
<div align="center">
<a href="https://github.com/IsNotTheReal/prueba-readme/stargazers"><img src="https://img.shields.io/github/stars/IsNotTheReal/practice_01" alt="Stars Badge"/></a>
<a href="https://github.com/IsNotTheReal/prueba-readme/pulls"><img src="https://img.shields.io/github/issues-pr/IsNotTheReal/prueba-readme" alt="Pull Requests Badge"/></a>
<a href="https://github.com/IsNotTheReal/prueba-readme/issues"><img src="https://img.shields.io/github/issues/IsNotTheReal/prueba-readme" alt="Issues Badge"/></a>
</div>

## Contents:
  - [What's this about](#work)
      - [Software used](#software)
      - [Code](#code)
  - [Content](#content)
  - [More information](#more)

### What's this about

<div>The exercise is quite easily: you're asked to create, using the Python language, two scripts. One that generates the Fibonacci sequence 'n' times, and another that will call that script and, based on the given number 'n', will verify that the serialization has been done correctly and print it to the terminal.</div>

#### Software used

In the development of this program, four software applications have been utilized:

- Visual Studio Code (VSC) IDE.
- Python (v3.12.0), essential.
- Python extension installed in VSC.
- GitHub Desktop.
<table border="0"; align="center">
  <tr>
    <td><a href="https://code.visualstudio.com"><img src="images/readme/visual.png" alt="Image of Visual Studio Code's logo" width="150"></a></td>
    <td><a href="https://www.python.org"><img src="images/readme/python.png" alt="Image of Python's logo" width="150"></a></td>
    <td><a href="https://desktop.github.com"><img src="images/readme/github.png" alt="Image of GitHub's desktop app logo" width="150"></a></td>
  </tr>
</table>

#### Code

The key to this exercise is the use of the `unittest` library, which will be imported within the main script. This is because the exercise places its importance on the utilization of the `.assertEqual` subclass to verify that the string is generated correctly using for example the number 4 (the 5th position) for this purpose:
```
self.assertEqual(list_result[4], 3)
```

### Content

The repository contains two folders, the `README.md📄`, and the two scripts (the actual program). Inside the `files📁` folder, there is documentation in Galician that explains everything related to the production and execution of the project. However, in the `images📁` folder, all the images are stored, both those used for the documentation and for the readme itself.

### More information

The aim of the exercise is to learn how to use Python libraries and how to connect scripts together. If you don't understand their functionality, it's recommended to refer to the official Python documentation <a href="https://docs.python.org/3/">here</a>. Conversely, if you only have doubts about the use of the 'unittest' library, the solution can be found <a href="https://docs.python.org/3/library/unittest.html">here</a>.
