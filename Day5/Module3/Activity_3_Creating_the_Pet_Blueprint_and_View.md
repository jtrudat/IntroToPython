# Activity: Creating the Pet Blueprint and View

In the last activity, we reorganized our PetFax Flask app to allow for modularizing logic. In this activity, we'll break our routes into a separate blueprint and serve a proper index view.

## Getting Started

1. Open your terminal.
2. Navigate to [PetFax](../PetFax).
3. Open it in your code editor of choice.
4. Activate the virtual environment by running `. venv/bin/activate` in the root of the repository.
5. Run the app with `flask run --reload`.

## Creating the Blueprint

Before we can even decide what our blueprint will be, let's remind ourselves what we're building. A local animal shelter has asked us to create an application that displays the pets up for adoption along with a fun fact about the species. If we look at the given data, we can see that the main focus is the pet.

As such, it would make sense for our blueprint to be a 'pet' blueprint. Let's get started on that.

### In terminal

1. Create a `pet.py` file on the same level as the `__init__.py` file.
2. Open that file in your code editor.
3. At the top of the file, import `Blueprint` from `flask`.
4. Create a new instance of Blueprint and save it to a variable called bp.
   - Remember, creating a new blueprint instance requires three arguments:
     - The name of the blueprint. Let's name ours `pet`.
     - The location of the blueprint. We can just use the handy `__name__`.
     - The URL prefix that should be used for all routes attached to this blueprint. Let's go with `/pets`.

**Our app is small, so it's fine to just have our blueprint on the same level as our `__init__` file. When apps get larger, it can be a good idea to create separate folders for blueprints.**

### What your code should look like

```python
from flask import Blueprint 

bp = Blueprint('pet', __name__, url_prefix="/pets")
```

We can't quite test this blueprint yet. We need to add some routes before we can do that. So, let's add an index.

### pet.py

1. Define a route on the blueprint instance that goes to `/`.
2. Define a method for the route named `index`.
3. In the index method, return a string (for example: 'This is the pets index'). This is just for testing purposes.

### What your code should look like

```python
@bp.route('/')
def index():
    return 'This is the pets index'
```

#### If we tried to test this out by going to http://127.0.0.1:5000/pets, it would not work yet. Why not?

<details>
    <summary>1. We made some typos.</summary>

    Incorrect - While it's possible there's a typo somewhere, that is not the primary reason.
</details>
<details>
    <summary>2. We should have created the route on the app instance, not on the blueprint..</summary>

    Incorrect - This would technically make the route work, but it would make the blueprint useless. Why isn't the blueprint itself working yet?
</details>
<details>
    <summary>3. We need to import the app into the blueprint file.</summary>

    Incorrect - We don't have a global app instance since we created an application factory to avoid having to do this.
</details>
<details>
    <summary>4. We have not registered the blueprint in the application factory.</summary>

    Correct! - The application has no idea the blueprint exists yet, so we must import and register it.
</details>

## Registering the Blueprint

To let the application know of the blueprint's existence, we need to register it in the factory.

### `__init__.py`

1. Above where we return the `app` in `create_app`, import the `pet` file.
2. Underneath that, call the `register_blueprint` method on the `app` instance.
3. Pass the pet blueprint into the method.

#### What your code should look like

```python
# factory
def create_app():
    # [ ... ]

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

    # return the app 
    return app
```

Now we should be able to successfully test the `/pets` route in the browser. Try it out at [http://127.0.0.1:5000/pets](http://127.0.0.1:5000/pets).

## Rendering Views

We've finally completed the basic setup of our app. With that out of the way, we can start focusing on rendering templates.

**In terminal**

1. Jinja is built into Flask by default, so we do not need to do any installations or configuration to use its templating. All we have to do is create a `templates` folder that Jinja will use when looking for files to render.
2. In that folder, create an `index.html` file. We don't need to use any custom Jinja file extensions, we can simply use HTML.
3. In the `index.html` file, autocomplete the HTML boilerplate using your code editor's shortcut.
4. In the body, create an `h1` tag that says `Welcome to PetFax`.

#### What your code should look like

```html
<body>
    <h1>Welcome to PetFax</h1>
</body>
```

If we go to `/pets` again, nothing will have changed. This template we just created won't be used yet because we have not actually told the route to render it.

### petfax/pet.py

1. At the top of the file where we imported `Blueprint` from `flask`, add `render_template` to the import list.
2. In the index method for the index route, instead of returning a string, return `render_template` and pass it the `index.html` template.

#### What your code should look like

```python
from flask import ( Blueprint, render_template ) 

# [ ... ]

@bp.route('/')
def index():
    return render_template('index.html')
```

Now if we go to [http://127.0.0.1:5000/pets](http://127.0.0.1:5000/pets), we should see our template being rendered!

## Displaying Data

With our template successfully rendered, we can now focus on displaying the given data. The data was given to us in JSON file format, as opposed to a database. To use this data, we will have to utilize a few functions that Python has available:

1. [open()](https://docs.python.org/3/library/functions.html#open) to open files. This is a built-in function.
2. [json.load()](https://docs.python.org/3/library/json.html) to decode JSON. The base json package will have to be imported.

### petfax/pet.py

1. At the top of the file with our other imports, import json.
2. Underneath that, we can `open()` the `pets.json` file by passing it as an argument.
3. Once that file is opened, however, it still isn't readable for Python. This is where json comes in. Pass the entire open function as an argument to `json.load()`.
4. Save that decoded JSON file to a variable. Let's name it `pets`.
5. To ensure we loaded it in correctly, print the pets variable. Once you save the file, you should see the data in terminal.

#### What your code should look like

```python
import json

pets = json.load(open('pets.json'))
print(pets)
```

Now that we have access to our data, we can pass it to the template as a variable. In our template, we can then loop through it using embedded Python.

### petfax/pet.py

1. In the `index` route method, pass the `render_template` a second argument. Let's name it `pets` as well and pass it the `pets` variable that we just loaded with data.
2. Now in `templates/index.html`, we can loop through the data using the `pets` variable.
3. Loop through it using embedded Python and display:
   - `pet_name` as an `h2`
   - `pet_photo` as an `img`
4. Remember, for embedded Python, we use:
   - `{{ }}` for inserting variable values.
   - `{% %}` for evaluating Python logic.
   - `end<statement>` to end the evaluation. For example, `endif` to end an IF statement, or `endfor` to end a for loop.

#### What your code should look like

```python
# pet.py
@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)
```

```html
<!-- index.html -->
<body>
    <h1>Welcome to PetFax</h1>
    {% for pet in pets %}
        <h2>{{ pet.pet_name }}</h2>
        <img src="{{ pet.pet_photo }}" alt="Photo of pet"/>
    {% endfor %}
</body>
```

Check out the new pets index page! We should now see images of the actual pets.

![Gif of the index view](lessons-ppp-5-blueprints-and-views-Activity.1.png)

## Conclusion

With just blueprints and views, our app is looking much better. It would be nice to style the index though, wouldn't it? You'll learn how to add styling and static files in the next activity.
