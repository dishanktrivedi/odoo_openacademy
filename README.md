# odoo_openacademy
Openacademy app build in odoo.

Exercise:
Define a model
Define a new data model Course in the openacademy module. 
A course has a title and a description. 
Courses must have a title.

Exercise:
Define demonstration data
Create demonstration data filling the Courses model with a few demonstration courses.

Exercise:
Define new menu entries
Define new menu entries to access courses under the OpenAcademy menu entry. A user should be able to:
- display a list of all the courses
- create/modify courses

Exercise:
Customise form view using XML
Create your own form view for the Course object. Data displayed should be: the name and the description of the course.

Exercise:
Notebooks
In the Course form view, put the description field under a tab, such that it will be easier to add other tabs later, containing additional information.

Exercise:
Search courses
Allow searching for courses based on their title or their description.

Exercise:
Create a session model
For the module Open Academy, we consider a model for sessions: a session is an occurrence of a course taught at a given time for a given audience.
Create a model for sessions. A session has a name, a start date, a duration and a number of seats. Add an action and a menu item to display them. Make the new model visible via a menu item.

Exercise:
Many2one relations
Using a many2one, modify the Course and Session models to reflect their relation with other models:
- A course has a responsible user; the value of that field is a record of the built-in model res.users.
- A session has an instructor; the value of that field is a record of the built-in model res.partner.
- A session is related to a course; the value of that field is a record of the model openacademy.course and is required.
- Adapt the views.

Exercise:
Inverse one2many relations
Using the inverse relational field one2many, modify the models to reflect the relation between courses and sessions.

Exercise:
Multiple many2many relations
Using the relational field many2many, modify the Session model to relate every session to a set of attendees. Attendees will be represented by partner records, so we will relate to the built-in model res.partner. Adapt the views accordingly.

Exercise:
Alter existing content
Using model inheritance, modify the existing Partner model to add an instructor boolean field, and a many2many field that corresponds to the session-partner relation
Using view inheritance, display this fields in the partner form view

Exercise:
Domains on relational fields
When selecting the instructor for a Session, only instructors (partners with instructor set to True) should be visible.

Exercise:
More complex domains
Create new partner categories Teacher / Level 1 and Teacher / Level 2. The instructor for a session can be either an instructor or a teacher (of any level).

Exercise:
Computed fields
Add the percentage of taken seats to the Session model
Display that field in the list and form views
Display the field as a progress bar

Exercise:
Active objects – Default values
Define the start_date default value as today (see Date).
Add a field active in the class Session, and set sessions as active by default.

Exercise:
Warning
Add an explicit onchange to warn about invalid values, like a negative number of seats, or more participants than seats.

Exercise:
Add Python constraints
Add a constraint that checks that the instructor is not present in the attendees of his/her own session.

Exercise:
Add SQL constraints
With the help of PostgreSQL’s documentation , add the following constraints:
- CHECK that the course description and the course title are different
- Make the Course’s name UNIQUE

Exercise:
Exercise 6 - Add a duplicate option
Since we added a constraint for the Course name uniqueness, it is not possible to use the “duplicate” function anymore (Form ‣ Duplicate).
Re-implement your own “copy” method which allows to duplicate the Course object, changing the original name into “Copy of [original name]”.

Exercise:
List coloring
Modify the Session list view in such a way that sessions lasting less than 5 days are colored blue, and the ones lasting more than 15 days are colored red.

Exercise:
Calendar view
Add a Calendar view to the Session model enabling the user to view the events associated to the Open Academy.

Exercise:
Search views
- Add a button to filter the courses for which the current user is the responsible in the course search view. Make it selected by default.
- Add a button to group courses by responsible user.

Exercise:
Gantt charts
Add a Gantt Chart enabling the user to view the sessions scheduling linked to the Open Academy module. The sessions should be grouped by instructor.

Exercise:
Graph view
Add a Graph view in the Session object that displays, for each course, the number of attendees under the form of a bar chart.

Exercise:
Kanban view
Add a Kanban view that displays sessions grouped by course (columns are thus courses).

Exercise:
Add access control through the Odoo interface
Create a new user “John Smith”. Then create a group “OpenAcademy / Session Read” with read access to the Session model.

Exercise:
Add access control through data files in your module
Using data files,
- Create a group OpenAcademy / Manager with full access to all OpenAcademy models
- Make Session and Course readable by all users

Exercise:
Record rule
Add a record rule for the model Course and the group “OpenAcademy / Manager”, that restricts write and unlink accesses to the responsible of a course. If a course has no responsible, all users of the group must be able to modify it.

Exercise:
Define the wizard
Create a wizard model with a many2one relationship with the Session model and a many2many relationship with the Partner model.

Exercise:
Launch the wizard
- Define a form view for the wizard.
- Add the action to launch it in the context of the Session model.
- Define a default value for the session field in the wizard; use the context parameter self._context to retrieve the current session.

Exercise:
Register attendees
Add buttons to the wizard, and implement the corresponding method for adding the attendees to the given session.

Exercise:
Register attendees to multiple sessions
Modify the wizard model so that attendees can be registered to multiple sessions.

