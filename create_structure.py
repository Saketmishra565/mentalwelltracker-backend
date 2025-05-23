import os

structure = [
    "app/alembic",
    "app/auth",
    "app/models",
    "app/routers",
    "app/schemas",
    "app/services",
    "app/utils",
]

files = {
    "app/auth": ["__init__.py", "dependencies.py", "jwt.py", "password.py"],
    "app/models": ["__init__.py", "base.py", "user.py", "reminder.py", "motivation.py", "notification.py", "tracking.py"],
    "app/routers": ["__init__.py", "auth.py", "users.py", "reminders.py", "motivation.py", "notifications.py", "tracking.py"],
    "app/schemas": ["__init__.py", "auth.py", "user.py", "reminder.py", "motivation.py", "notification.py", "tracking.py"],
    "app/services": ["__init__.py", "auth.py", "user.py", "reminder.py", "motivation.py", "notification.py", "tracking.py"],
    "app/utils": ["__init__.py", "config.py", "constants.py", "exceptions.py", "validators.py"],
}

base_files = [
    ".env.example",
    ".gitignore",
    "app/database.py",
    "app/main.py",
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    "README.md",
]

# Create folders
for folder in structure:
    os.makedirs(folder, exist_ok=True)

# Create files in subfolders
for folder, file_list in files.items():
    for file in file_list:
        open(os.path.join(folder, file), "w").close()

# Create base files
for file in base_files:
    open(file, "w").close()

print("✅ Project structure created successfully!")
