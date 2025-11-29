import click
from app.db.session import SessionLocal
from app.services.task_service import TaskServiceDB

@click.command()
def autoclose_overdue():
    click.echo("Starting auto-close of overdue tasks...")

    try:
        db = SessionLocal()
        task_service = TaskServiceDB(db)
        success, message = task_service.close_overdue_tasks()
        click.echo(message)
        db.close()
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == "__main__":
    autoclose_overdue()
