# HTML API Reference

Programmatic HTML generation.

## Import

```python
from stamp.main import HTML
```

## Overview

The HTML class provides a fluent API for building HTML documents programmatically.

## HTML Class

### HTML.__init__()

Initialize HTML builder.

```python
from stamp.main import HTML

html = HTML()
```

### HTML.__reset__()

Reset HTML builder state.

```python
html = HTML()
# ... add elements ...
html.__reset__()  # Clear and start fresh
```

### HTML.__run__()

Run/execute HTML generation.

**Returns:** str - Generated HTML

```python
html = HTML()
html.addhead("My Page")
html.addbody("Content")
result = html.__run__()
print(result)
```

### HTML.__crthtml__()

Create HTML document structure.

**Returns:** str - HTML document

```python
html = HTML()
html.__crthtml__()
# Creates basic HTML structure
```

## Element Methods

### HTML.addpar(text)

Add paragraph element.

**Parameters:**
- `text` (str): Paragraph text

```python
html = HTML()
html.addpar("This is a paragraph")
```

### HTML.addhead(text)

Add heading element.

**Parameters:**
- `text` (str): Heading text

```python
html = HTML()
html.addhead("Main Heading")
```

### HTML.addtxa(text, rows=None, cols=None, name=None)

Add textarea element.

**Parameters:**
- `text` (str): Textarea content
- `rows` (int): Number of rows (optional)
- `cols` (int): Number of columns (optional)
- `name` (str): Element name (optional)

```python
html = HTML()
html.addtxa("Enter text here", rows=5, cols=40, name="message")
```

### HTML.adddelm(text)

Add delete marker element.

**Parameters:**
- `text` (str): Marker text

```python
html = HTML()
html.adddelm("Delete this")
```

### HTML.addbtn(text, onclick=None)

Add button element.

**Parameters:**
- `text` (str): Button text
- `onclick` (str): JavaScript onclick handler (optional)

```python
html = HTML()
html.addbtn("Click Me", onclick="alert('Hello!')")
```

### HTML.addlbl(text, for_elem=None)

Add label element.

**Parameters:**
- `text` (str): Label text
- `for_elem` (str): Element to label (optional)

```python
html = HTML()
html.addlbl("Username", for_elem="username")
```

### HTML.addipt(type="text", name=None, value=None, placeholder=None)

Add input element.

**Parameters:**
- `type` (str): Input type (default: "text")
- `name` (str): Input name (optional)
- `value` (str): Input value (optional)
- `placeholder` (str): Placeholder text (optional)

```python
html = HTML()
html.addipt(type="text", name="username", placeholder="Enter username")
html.addipt(type="password", name="password", placeholder="Enter password")
```

### HTML.addlink(url, text)

Add link/anchor element.

**Parameters:**
- `url` (str): Link URL
- `text` (str): Link text

```python
html = HTML()
html.addlink("https://example.com", "Visit Example")
```

### HTML.addimg(src, alt=None)

Add image element.

**Parameters:**
- `src` (str): Image source URL
- `alt` (str): Alt text (optional)

```python
html = HTML()
html.addimg("image.jpg", alt="Description")
```

### HTML.addlist(items, ordered=False)

Add list element.

**Parameters:**
- `items` (list): List items
- `ordered` (bool): Ordered list (True) or unordered (False)

```python
html = HTML()

# Unordered list
html.addlist(["Item 1", "Item 2", "Item 3"], ordered=False)

# Ordered list
html.addlist(["First", "Second", "Third"], ordered=True)
```

### HTML.adddiv(content, id=None, class_=None)

Add div element.

**Parameters:**
- `content` (str): Div content
- `id` (str): Element ID (optional)
- `class_` (str): CSS class (optional)

```python
html = HTML()
html.adddiv("Content here", id="main", class_="container")
```

### HTML.addspan(content, class_=None)

Add span element.

**Parameters:**
- `content` (str): Span content
- `class_` (str): CSS class (optional)

```python
html = HTML()
html.addspan("Highlighted text", class_="highlight")
```

### HTML.addtable(headers, rows)

Add table element.

**Parameters:**
- `headers` (list): Table headers
- `rows` (list): Table rows (list of lists)

```python
html = HTML()

html.addtable(
    headers=["Name", "Age", "City"],
    rows=[
        ["Alice", 25, "NYC"],
        ["Bob", 30, "LA"],
        ["Charlie", 35, "Chicago"]
    ]
)
```

### HTML.addstyle(css)

Add CSS style.

**Parameters:**
- `css` (str): CSS code

```python
html = HTML()
html.addstyle("body { background-color: #f0f0f0; }")
```

### HTML.addscript(js_code)

Add JavaScript script.

**Parameters:**
- `js_code` (str): JavaScript code

```python
html = HTML()
html.addscript("console.log('Hello!');")
```

### HTML.addmetacset(charset)

Add meta charset element.

**Parameters:**
- `charset` (str): Character set (e.g., "UTF-8")

```python
html = HTML()
html.addmetacset("UTF-8")
```

### HTML.addlinkcss(url)

Add CSS link.

**Parameters:**
- `url` (str): CSS file URL

```python
html = HTML()
html.addlinkcss("styles.css")
```

### HTML.addtitle(title)

Add document title.

**Parameters:**
- `title` (str): Page title

```python
html = HTML()
html.addtitle("My Page")
```

### HTML.addbody(content)

Add body content.

**Parameters:**
- `content` (str): Body content

```python
html = HTML()
html.addbody("<h1>Hello World</h1>")
```

### HTML.adddphtml(html_content)

Add raw HTML content.

**Parameters:**
- `html_content` (str): Raw HTML

```python
html = HTML()
html.adddphtml("<div>Custom HTML</div>")
```

### HTML.addhtml(html_content)

Add HTML to document.

**Parameters:**
- `html_content` (str): HTML content

```python
html = HTML()
html.addhtml("<p>More content</p>")
```

## Usage Examples

### Simple Page

```python
from stamp.main import HTML

html = HTML()
html.addtitle("My Page")
html.addhead("Welcome")
html.addpar("This is a simple HTML page")

result = html.__run__()
print(result)
```

### Form with Inputs

```python
from stamp.main import HTML

html = HTML()
html.addtitle("Contact Form")
html.addhead("Contact Us")

html.addlbl("Name", for_elem="name")
html.addipt(type="text", name="name", placeholder="Your name")

html.addlbl("Email", for_elem="email")
html.addipt(type="email", name="email", placeholder="your@email.com")

html.addbtn("Submit")

result = html.__run__()
```

### Styled Page

```python
from stamp.main import HTML

html = HTML()
html.addtitle("Styled Page")
html.addmetacset("UTF-8")
html.addlinkcss("styles.css")

html.addstyle("""
    .container { padding: 20px; }
    .header { color: blue; }
""")

html.adddiv("Content", class_="container")
html.addhead("Header", class_="header")

result = html.__run__()
```

### Table

```python
from stamp.main import HTML

html = HTML()
html.addtitle("Data Table")

html.addtable(
    headers=["Name", "Age", "Score"],
    rows=[
        ["Alice", 25, 95],
        ["Bob", 30, 87],
        ["Charlie", 28, 92]
    ]
)

result = html.__run__()
```

### Interactive Page

```python
from stamp.main import HTML

html = HTML()
html.addtitle("Interactive Page")

html.addbtn("Click Me", onclick="alert('Button clicked!')")

html.addscript("""
    function showMessage() {
        console.log('Page loaded');
    }
    window.onload = showMessage;
""")

result = html.__run__()
```

### Complete Page

```python
from stamp.main import HTML

html = HTML()

# Meta and title
html.addmetacset("UTF-8")
html.addtitle("My Website")

# Styles
html.addstyle("""
    body { font-family: Arial, sans-serif; margin: 20px; }
    .container { max-width: 800px; margin: 0 auto; }
""")

# Content
html.addhead("Welcome to My Website")
html.addpar("This is the home page.")

html.addhead("Features")
html.addlist(["Feature 1", "Feature 2", "Feature 3"], ordered=False)

html.addhead("Links")
html.addlink("https://example.com", "Visit Example")

# Button with JavaScript
html.addbtn("Click Here", onclick="alert('Hello!')")

html.addscript("console.log('Page loaded');")

result = html.__run__()
```

## Notes

- Methods can be chained
- HTML is built incrementally
- Use `__run__()` to get final HTML
- Use `__reset__()` to start over
- CSS and JavaScript can be added inline
- All elements are properly escaped for safety

---

See [HTML Generation Examples](../examples/html-gen.md) for more examples.
See [HTML Guide](../guides/html-guide.md) for detailed guide.
