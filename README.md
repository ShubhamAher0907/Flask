# Code Explanation
The Flask application defines three routes, each returning a simple text message when accessed.

**1. Root Path (/)**
**Route: **/
**Function:** hello()
**Response:** "Hey this is my first Flask app!"
**Description:** This is the default route of the application. When you access the root URL (e.g., http://localhost:5000/), this route is triggered, and it returns a welcome message.

**2. Second Path (/route2)**
**Route:** /route2
**Function:** adder()
**Response:** "I am on the second page!"
**Description:** This route is triggered when you visit the URL http://localhost:5000/route2. It returns a message indicating you are on the second page.

**3. Third Path (/route2/page)**
**Route:** /route2/page
**Function:** page()
**Response:** "I am on the third page!"
**Description:** This route is a sub-path of the second route. 
It is triggered when you visit the URL **http://localhost:5000/route2/page**, and it returns a message indicating you are on the third page.
