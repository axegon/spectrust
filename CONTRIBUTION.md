# Contributions.

Few people get this far...
CONGRATULATIONS! You're a badass!

All contributers are welcome but several things should be kept in mind. The project is open source and you are free to
clone it, use it or modify it in whichever way you see fit. And providing feedback and contribution back is highly
appreciated. There are rules that need to be followed however:

1. Be respectful to others.
2. Do not take criticism personally - nobody actually creates perfect code the first time around (except Linus of course).
3. Do not expect immediate fixes and pushes - we all have lives outside github.

## Reporting bugs

Please provide as much information as possible. The bare minimum should be:

* Traceback/errors you are getting
* System information - operating system, CPU architecture.
* Steps to reproduce.

## Contributing code.

As most projects, this would follow somewhat similar methodology:

1. Fork the repository.
2. Make your changes.
3. Send a pull request, stating the purpose of your changes.
4. When you add a new feature or modifying the existing one, also provide documentation.

One thing to keep in mind - this repository does not provide a `.gitignore`. The reason being, people have different
preferences when it comes to IDE's, what they want to keep at arms length from their code for different purposes.
Or as Rick Sanchez put it - "we all go to weird places". And without any doubts in my mind - whatever floats your boat.
So you are left with the responsibility to create your own `.gitignore` and maintain it carefully - exclude any
arbitrary files created by your IDE, along with builds, shared objects, wheels, eggs, or any binary files that do
not explicitly contribute to the project. And with that in mind, put your `.gitignore` in your `.gitignore`.
Any pull requests containing arbitrary files will be rejected on those basis.

### Coding style.

The project uses a [PEP-8](https://pep8.org/) coding style and [numpy docstrings](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard).
All classes and methods must be documented. Exceptions are made for __repr__ methods and property methods.



