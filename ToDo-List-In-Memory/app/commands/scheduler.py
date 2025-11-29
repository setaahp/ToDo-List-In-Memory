import schedule
import time
from app.db.session import SessionLocal
from app.services.task_service import TaskServiceDB

def run_autoclose():
    try:
        db = SessionLocal()
        task_service = TaskServiceDB(db)
        success, message = task_service.close_overdue_tasks()
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")
        db.close()
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error: {e}")

def run_scheduler():
    print("Starting task scheduler...")
    
    interval_minutes = 15  
    schedule.every(interval_minutes).minutes.do(run_autoclose)
    
    print(f"Auto-close scheduled to run every {interval_minutes} minutes")
    print("Press Ctrl+C to stop the scheduler")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped")

if __name__ == "__main__":
    run_scheduler()
