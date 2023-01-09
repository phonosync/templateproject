# Python Development Guide
Based on work by Filip Nowak. Thank you!

## The Zen of Python
```python
import this
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.  
Explicit is better than implicit.  
Simple is better than complex.  
Complex is better than complicated.  
Flat is better than nested.  
Sparse is better than dense.  
Readability counts.  
Special cases aren't special enough to break the rules.  
Although practicality beats purity.  
Errors should never pass silently.  
Unless explicitly silenced.  
In the face of ambiguity, refuse the temptation to guess.  
There should be one-- and preferably only one --obvious way to do it.  
Although that way may not be obvious at first unless you're Dutch.  
Now is better than never.  
Although never is often better than *right* now.  
If the implementation is hard to explain, it's a bad idea.  
If the implementation is easy to explain, it may be a good idea.  
Namespaces are one honking great idea -- let's do more of those!  

## Comply to [PEP8](https://www.python.org/dev/peps/pep-0008/)

Requirement: Application need to contain tests implementing PEP8 with the following exceptions allowed:

* E402 - in tests, module-level imports not being placed at the top of the source file are fine.
* E501 - maximum line length is set to `112` characters (more practical and still tidy / readable)
* E265 - it is OK to comment code without adding space after #

Rationale: [PEP8](https://www.python.org/dev/peps/pep-0008/) is quite neutral middleground between more radical coding standards or conventions, it's
often used, so it's less likely to cause friction between developers.

Can be checked with:
```python pycodestyle --max-line-length=112 2_LanguageFeatures\my_module.py```
configuration in `setup.cfg`
```
[pycodestyle]
count = False
ignore = E262,E265
max-line-length = 112
statistics = True
```


## Don't (ab)use lambdas

Requirement: Don't use lambdas if possible.

Rationale: In Python they have severe limitations, and rarely are really needed. They can make code harder to understand, without real benefit.

## Prefer idiomatic Python

Requirement: Prefer idiomatic Python, as [Python is not Java](https://dirtsimple.org/2004/12/python-is-not-java.html).

Example:

Don't:
```
url = 'https://' + fqdn + some_path + '/?' + query_string
```

Do:
```
url = ''.join(['https://', fqdn, some_path, '/?', query_string])
```

Don't:
```
f = open('test.txt', 'r')
f.write(data)
f.close()
```

Do:
```
with open('test.txt', 'r') as f:
    f.write()
```

Don't:
```
if animal == 'gato' or animal == 'bird' or animal == 'dragon':
    return True
```

Do:
```
if animal in ('gato', 'bird', 'dragon'):
    return True
```

Don't:
```
class X:

    @property
    def a(self):
        # do something clever
        return self._a

    @a.setter
    def a(self, value):
        # do something even cleverer
        self._a = value
```

Do:
```
>>> x = X()
>>> x.a
Traceback (most recent call last):
  # ... etc
AttributeError: 'X' object has no attribute 'a'
>>> x.a = 'foo'
>>> x.a
'foo'
```

Rationale: One of the strengths of Python is its elegant and sparse syntax. There is a learning curve to it, and
there is always a temptation to bring your experience from other programming languages directly to other languages,
but his is not preferred approach, as on the long run, it makes code harder to maintain, read and can cause issues
you didn't anticipated. Idiomatic Python is universal language of all of the Python programmers, let's use it!

## Don't (ab)use the exceptions

Requirement: When possible don't define your own exceptions, if you really must, throw existing maching your situation. Don't allow exceptions to leak between layers of your code. Handle it if you can, and emit value
meaningful for the caller, compliant with API of the method / function in which that happened; communicate with values. Try not to catch `Exception` or other runtime exceptions you won't be able to handle.

Example:

Don't:
```
def fun1(message):
    try:
        with open('test.txt', 'r') as f:
            f.write(message)
    except Exception as e:
        raise MyOwnException(e)

def fun2():
        fun1()
```

Do:
```
def fun1():
    try:
        with open('test.txt', 'r') as f:
            f.write(message)
    except IOError as e:
        return False, None, e

def fun2():
        fun1()
```

Rationale: Exceptions which are relevant to - for example - file system operations sometimes can be remediated, handled in I/O-related code. The higher in the code hierarchy you are, the less likely is that they could be handled (there will be no code specialized in taking care of file system I/O for example), or that they will be useful. Exceptions should be contained where they
were raised, but relevant messages or failure reasons, in case of need, can be emmiteded as return values from methods in which that happened.

## Don't (ab)use inheritance

Requirement: Prefer composition over inheritance. Don't succumb to the [inheritance diamond](https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem), don't rely too much on method resolution order.
The longer the inheritance chain, the [smellier the code](https://en.wikipedia.org/wiki/Code_smell) is.

Rationale: Code structre should be simple enough to understand it without exercising things like [C3 linearization](https://en.wikipedia.org/wiki/C3_linearization).

## Don't mutate mutable arguments

Requirement: Don't modify mutable arguments passed to your method or function. `copy.deepcopy` it first.

Don't:
```
def fun1(wet_cat_dict, cat):
    if is_dry(cat) and cat in _wet_cat_dict:
        del(wet_cat_dict[cat])
    return wet_cat_dict
```

Do:
```
def fun1(wet_cat_dict, cat):
    _wet_cat_dict = copy.deepcopy(wet_cat_dict)
    if is_dry(cat) and cat in _wet_cat_dict:
        del(_wet_cat_dict[cat])
    return _wet_cat_dict
```

Rationale: It can cause [side effects](https://en.wikipedia.org/wiki/Side_effect_(computer_science)), [race conditions](https://en.wikipedia.org/wiki/Race_condition) and other unwanted behaviors.

## [Embrace simplicity](https://www.python.org/dev/peps/pep-0020/)

Requirement: Prefer simplicity and readability over "clever" and smart code. Keep things simple, but not simpler than required.

Rationale: Simple is better than complex ;)

## Document code you are writing
Requirement: The Project should have a README.md file with the following sections:
* Description of the Project
* Dependencies and Setup/Installation Instructions
* Tests: When I have installed the application, how can I test it

Requirement: All of the classes and methods need to be documented in consistent way. Single project needs to have one
convention and syntax of the docstrings, for example [reStructuredText](https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html).

Rationale: It is good way to document your intent and functionality you are trying to implement. In case of more
complex code, such documentation can also serve as design papers. Other developers using your code will read
your notes, will learn - for example - about method's API, will know what to expect and how to use it, what
behavior should be considered a bug, and what not.

Example ([Google-like](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) docstring style - good compromise between readability and and expressiveness):

```
def _load_key_from_env(self, key):
    '''load configuration by its key from shell environment

       args:
           key : str
              env var name.

       notes:
          - `key` will be capitalized before deserialization attempt.
          - value of `key` is expected to by JSON-represented.

       returns:
           <succes: True>, <value> |
           <failure: False>, <reason> |
           <key not found: None>, <message>'''
```

## Testing Strategy

Requirement: All of the methods and functions need to come with tests, and / or unit tests.  There is no excuse for not doing it.
Remember that tests you won't write today, are the debt you and your teammates will need to pay later, with
extra-time spent on the code, every single time you will want to touch it.

Rationale: Writing code you know for which you will need to implement unit tests, will encourage you to make it modular,
with well defined APIs. You don't know when something will break, and you don't want to test it manually - one of the
purposes of the unit tests, is to double as regression tests.

See [Python testing strategy](https://git.swissre.com/users/s5yx2e/repos/varia/browse/p&c/PYTHON_TESTING_STRATEGY.md) for more on testing topic.

### Example
Python REST API, utilizing five classes (all by composition):

```
 [APP]
   |
  [D]
  / \
 /   \
[C] [B]
     |
    [A]
```

All of the components are coming with the tests:

* APP: integration / happy paths tests, load / resilience tests, mixed tests for all methods and functions.
* A, B, C, D: mixed tests for all functions and methods.

By mixed tests we mean:

* Tests which are testing both methods / functions APIs (unit / white box test aspect).
* Compatibility of the methods / functions APIs with their dependencies (for example tests for class `B`, will _not_ mock class `A`).
* Compatibility of the wrapper classes with their "providers" (for example `A` class is a wrapper around DB access module, and its tests need to answer
  questions like "does version X of `A` work with version Y of DB driver and Z of Python?").

## Use pull requests and code reviews
Requirement: Use version control system workflows and pull requests as a way to contribute to the code.
All of the pull requests, need to be reviewed.

Rationale: Check [wikipedia article](https://en.wikipedia.org/wiki/Code_review) on that.


## Project Organisation
```
root folder  
|-- src
    |-- utils
        |-- __init__.py
        |-- utils_module1.py
        |-- utils_module2.py
        |...
    |-- core
        |-- __init__.py
        |-- core_module1.py
        |-- core_module2.py
        |...
|-- notebooks
    | -- notebook1.ipynb
    | -- notebook2.ipynb
    |...
|-- ressources
    |-- ressource1.csv
    |-- ressource2.json
    |..
|-- app.py
|-- .env
|-- .env.template
|-- .gitignore
|-- setup.cfg
|-- requirements.txt
|-- README.md
|-- LICENSE.md
```

## Application configuration
### Minimize numbers of configuration variables
For small projects: Use code-level-defaults and runtime configuration

### Manifest `runtime configuration` as environmental variables
This is also where access credentials etc. are managed. Keep a template configuration file in the version control system.

Rationale: This is one of the canonical ways of configuring containerised applications. Great support for Python through `dotenv` package.
