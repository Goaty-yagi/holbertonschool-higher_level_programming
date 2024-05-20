# Learning Objectives

- [How to select HTML elements in JavaScript](#How-to-select-HTML-elements-in-JavaScript)
- [What are differences between ID, class and tag name selectors](#What-are-differences-between-ID,-class-and-tag-name-selectors)
- [How to modify an HTML element style](#How-to-modify-an-HTML-element-style)
- [How to get and update an HTML element content](#How-to-get-and-update-an-HTML-element-content)
- [How to modify the DOM](#How-to-modify-the-DOM)
- [How to make a request with XmlHTTPRequest](#How-to-make-a-request-with-XmlHTTPRequest)
- [How to make a request with Fetch API](#How-to-make-a-request-with-Fetch-API)
- [How to listen/bind to DOM events](#How-to-listen/bind-to-DOM-events)
- [How to listen/bind to user events](#How-to-listen/bind-to-user-events)


## How to select HTML elements in JavaScript

### 1. Using getElementById
```javascript
const element = document.getElementById('myId');

```
### 2. Using getElementsByClassName
```javascript
const elements = document.getElementsByClassName('myClass');

```

### 3. Using getElementsByTagName
```javascript
const elements = document.getElementsByTagName('div');

```

### 4. Using querySelector
```javascript
const element = document.querySelector('.myClass');

```

### 5. Using querySelectorAll
```javascript
const elements = document.querySelectorAll('.myClass');

```
## What are differences between ID, class and tag name selectors
### ID Selectors
- Characteristics:
Uniqueness: An ID must be unique within an HTML document. Only one element can have a particular ID.

- Specificity: ID selectors have the highest specificity among the three types, meaning they will override class and tag name selectors if there are conflicts in styling rules.

### Class Selectors
- Characteristics:
Reusability: A class can be applied to multiple elements within an HTML document.

- Specificity: Class selectors have medium specificity, higher than tag name selectors but lower than ID selectors.

### Tag Name Selectors
- Characteristics:
Breadth: Tag name selectors target all elements of a specific tag within the document.
- Specificity: Tag name selectors have the lowest specificity.


## How to modify an HTML element style
### Using the style Property
```javascript
const element = document.getElementById('myDiv');
element.style.color = 'blue'; // Set text color to blue
element.style.backgroundColor = 'yellow'; // Set background color to yellow
element.style.fontSize = '20px'; // Set font size to 20px

```
## How to get and update an HTML element content
### 1. Using innerHTML
The innerHTML property allows you to get or set the HTML content of an element.
```javascript
const element = document.getElementById('myDiv');

// Get the content
const content = element.innerHTML;
console.log(content); // Output: This is the original content.

// Update the content
element.innerHTML = 'This is the updated content.';

```

### 2. Using innerText or textContent
```javascript
const paragraph = document.getElementById('myParagraph');

// Get the content
const text = paragraph.innerText; // or paragraph.textContent
console.log(text); // Output: This is some text.

// Update the content
paragraph.innerText = 'This is the updated text.'; // or paragraph.textContent = 'This is the updated text.';

```

### 3. Using nodeValue for Text Nodes
```javascript
const span = document.getElementById('mySpan');
const textNode = span.firstChild;

// Get the content
const nodeValue = textNode.nodeValue;
console.log(nodeValue); // Output: Hello, world!

// Update the content
textNode.nodeValue = 'Hello, universe!';

```
## How to modify the DOM
### 1. Changing the Content of Elements
```javascript
const contentDiv = document.getElementById('content');

// Using innerHTML
contentDiv.innerHTML = 'New <strong>HTML</strong> content';

// Using textContent
contentDiv.textContent = 'New text content';

```

### 2. Changing the Attributes of Elements
```javascript
const image = document.getElementById('myImage');

// Using setAttribute
image.setAttribute('src', 'newImage.jpg');
image.setAttribute('alt', 'New Image');

// Directly modifying properties
image.src = 'newImage.jpg';
image.alt = 'New Image';

```

### 3. Changing the Style of Elements
```javascript
const paragraph = document.getElementById('myParagraph');
paragraph.style.color = 'blue';
paragraph.style.fontSize = '20px';
paragraph.style.backgroundColor = 'yellow';

```

### 4. Adding and Removing Classes
```javascript
const div = document.getElementById('myDiv');

// Adding a class
div.classList.add('highlight');

// Removing a class
div.classList.remove('box');

// Toggling a class
div.classList.toggle('active');

// Checking if a class exists
const hasClass = div.classList.contains('highlight');
console.log(hasClass);  // true

```

### 5. Creating and Appending New Elements
```javascript
const list = document.getElementById('myList');
const newItem = document.createElement('li');
newItem.textContent = 'Item 3';

// Using appendChild
list.appendChild(newItem);

// Using append (allows multiple nodes and strings)
list.append('Item 4');

```

### 6. Removing Elements
```javascript
const list = document.getElementById('myList');
const item1 = document.getElementById('item1');

// Using removeChild
list.removeChild(item1);

// Using remove
const item2 = document.getElementById('item2');
item2.remove();

```

### 7. Replacing Elements
```javascript
const oldDiv = document.getElementById('oldDiv');
const newDiv = document.createElement('div');
newDiv.textContent = 'This is the new div.';

oldDiv.parentNode.replaceChild(newDiv, oldDiv);

```

### 8. Cloning Elements
```javascript
const original = document.getElementById('original');
const clone = original.cloneNode(true); // true for deep clone
original.parentNode.appendChild(clone);

```

## How to make a request with XmlHTTPRequest
### 1. Create an XMLHttpRequest Object
```javascript
const xhr = new XMLHttpRequest();

```
### 2. Configure the Request
```javascript
xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts', true);

```
- The first parameter is the HTTP method (e.g., 'GET', 'POST', 'PUT', 'DELETE').
- The second parameter is the URL to which the request is sent.
- The third parameter is a boolean indicating whether the request is asynchronous (true) or synchronous (false).

### 3. Set Up a Callback to Handle the Response
```javascript
xhr.onload = function() {
  if (xhr.status >= 200 && xhr.status < 300) {
    // Request was successful
    console.log(JSON.parse(xhr.responseText));
  } else {
    // Handle errors
    console.error('Request failed. Status:', xhr.status, 'Status Text:', xhr.statusText);
  }
};

```

### 4. Send the Request
```javascript
xhr.send();

```

## How to make a request with Fetch API
```javascript
fetch('https://jsonplaceholder.typicode.com/posts')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });

```
## How to listen/bind to DOM events
### Using addEventListener
```javascript
element.addEventListener(event, handler, options);

```
- element: The DOM element you want to bind the event to.
- event: A string representing the event type (e.g., 'click', 'mouseover', 'keydown').
- handler: The function to execute when the event occurs.
- options (optional): An object with properties that specify characteristics about the event listener.

### Common Events
- Mouse Events: click, dblclick, mouseover, mouseout, mousemove, mousedown, mouseup
- Keyboard Events: keydown, keypress, keyup
- Form Events: submit, focus, blur, change, input
- Window Events: load, resize, scroll
## How to listen/bind to user events
See above