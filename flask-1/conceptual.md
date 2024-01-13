### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is a server-side language often used for backend development, while JavaScript is primarily a client-side language used for frontend development.
Python is known for readability and ease of use, while JavaScript is more flexible and dynamic.
Python uses indentation for code structure, while JavaScript uses curly braces.
Python is often used for data analysis, artificial intelligence, and scientific computing, while JavaScript is essential for web development.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
You can use the 'get' method or a try-except block.

- What is a unit test?
A unit test is a type of software testing where individual units or components of a program are tested in isolation. It ensures that each part of a program functions as expected.

- What is an integration test?
An integration test checks that different components of a system work together. It verifies that integrated components can communicate and produce the correct output.

- What is the role of web application framework, like Flask?
Flask is a web application framework for Python. It provides tools, libraries, and patterns to build web applications. Flask handles routing, request handling, and templating, making it easier to build web applications.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
Use route URL parameter when the data is essential to the resource (e.g., /foods/pretzel for a specific food).
Use query param when the data is optional or used for filtering (e.g., /foods?type=pretzel for filtering foods by type).

- How do you collect data from a URL placeholder parameter using Flask?
Use the @app.route decorator with a route that includes <variable> in the URL. Define a function with the corresponding parameter.

- How do you collect data from the query string using Flask?
Access the query parameters using request.args.get("param_name") in your route function.

- How do you collect data from the body of the request using Flask?
Use request.get_json() or request.form.get("key") to access data from the request body.

- What is a cookie and what kinds of things are they commonly used for?
A cookie is a small piece of data stored on the client's browser. It's commonly used for session management, user authentication, and tracking user behavior.

- What is the session object in Flask?
The session object in Flask is used to store user-specific information between requests. It uses cookies to maintain session data.

- What does Flask's `jsonify()` do?
jsonify() is a Flask function that converts a Python dictionary into a JSON response. It sets the appropriate content type and returns a JSON-formatted response.