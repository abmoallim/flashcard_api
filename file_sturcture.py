import os

# Define the new project structure
structure = {
    "": {
        "alembic": {
            "versions": [],
            "env.py": "",
            "script.py.mako": "",
            "alembic.ini": ""
        },
        "app": {
            "api": {
                "endpoints": [
                    "users.py",
                    "flashcards.py",
                    "decks.py",
                    "subscriptions.py",
                    "auth.py",
                    "__init__.py"
                ],
                "__init__.py": ""
            },
            "core": [
                "config.py",
                "security.py",
                "__init__.py"
            ],
            "crud": [
                "user.py",
                "flashcard.py",
                "deck.py",
                "subscription.py",
                "__init__.py"
            ],
            "db": {
                "models": [
                    "user.py",
                    "flashcard.py",
                    "deck.py",
                    "subscription.py",
                    "__init__.py"
                ],
                "base.py": "",
                "session.py": "",
                "init_db.py": "",
                "__init__.py": ""
            },
            "schemas": [
                "user.py",
                "flashcard.py",
                "deck.py",
                "subscription.py",
                "__init__.py"
            ],
            "main.py": "",
            "dependencies.py": "",
            "__init__.py": ""
        },
        ".env": "",
        "requirements.txt": "",
        "README.md": ""
    }
}

# Function to create directories and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for file in content:
                open(os.path.join(path, file), 'w').close()
        else:
            open(path, 'w').close()

# Create the structure
create_structure(".", structure)

print("Project structure created successfully.")
