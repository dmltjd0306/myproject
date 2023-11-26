# myproject
Yun We Seong
CPE-202
20936687


**I added a file for vscode just incase.

### 1. List View:
- **Description:** Display a list of all notes belonging to the logged-in user.
- **Implementation:**
  - Create a view that retrieves all notes associated with the current user.
  - Render a template that displays a paginated list of notes.
  - Each note in the list should show essential information like the title and a snippet of the content.

### 2. Detail View:
- **Description:** Show the details of a specific note.
- **Implementation:**
  - Create a view that retrieves a specific note based on its ID.
  - Render a template that displays the full content of the note along with other details.
  - Ensure that only the owner of the note has access to its details.

### 3. Create View:
- **Description:** Allow users to create new notes.
- **Implementation:**
  - Create a view that handles both GET and POST requests.
  - Render a form for users to input the title and content of the new note.
  - Validate and save the new note to the database.
  - Ensure the note is associated with the logged-in user.

### 4. Delete View:
- **Description:** Allow users to delete a specific note.
- **Implementation:**
  - Create a view that handles the deletion of a note based on its ID.
  - Display a confirmation page before allowing the actual deletion.
  - Ensure that only the owner of the note can initiate the deletion.

### 5. Update View:
- **Description:** Allow users to edit and update the content of a specific note.
- **Implementation:**
  - Create a view that handles both GET and POST requests.
  - Retrieve the note based on its ID, pre-fill the form with existing data.
  - Validate and save the updated content to the database.
  - Ensure that only the owner of the note can initiate the update.

### 6. Simple Admin Panel (not Django Admin):
- **Description:** Allow administrators to manage notes through a basic admin panel.
- **Implementation:**
  - Create a separate admin interface with basic CRUD operations.
  - Restrict access to this admin panel to users with administrative privileges.
  - Design a clean and intuitive interface for administrators to manage notes.

### 7. Proper Authorization and Authentication:
- **Description:** Ensure that only authorized users can perform actions on notes.
- **Implementation:**
  - Use Django's built-in authentication system for user login and logout.
  - Implement proper user authentication for all views, allowing only logged-in users to access certain functionalities.
  - Use Django's built-in authorization to check if the current user has the necessary permissions (ownership) for actions like updating or deleting a note.

