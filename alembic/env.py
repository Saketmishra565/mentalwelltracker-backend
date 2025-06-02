from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
import os

# Add your app root directory to the sys.path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your SQLAlchemy Base and your engine from your app
from app.database import engine  # Your SQLAlchemy engine
from app.models.base import Base  # Your declarative base metadata
from app.database import SQLALCHEMY_DATABASE_URL
from app.models import user
from app.database import Base
from app.models import email_verification

# Alembic Config object, provides access to .ini config file values
config = context.config

# Optionally, you can set the database URL dynamically (if you have it in your app config)
# Uncomment and adjust if you have a database URL variable somewhere in your app
# from app.config import settings
# config.set_main_option('sqlalchemy.url', settings.SQLALCHEMY_DATABASE_URL)

# Setup logging from config file
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata for 'autogenerate' support
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    if not url:
        # Fallback to engine url if not set in config file
        url = str(engine.url)

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    # Use the existing engine connection
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
