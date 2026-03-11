"""APScheduler instance for backup and analysis jobs."""

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from jobs.backup_job import run_backup
from jobs.analysis_job import run_analysis

_scheduler = AsyncIOScheduler()


def get_scheduler():
    _scheduler.add_job(run_backup, IntervalTrigger(hours=1), id="backup")
    _scheduler.add_job(run_analysis, IntervalTrigger(hours=6), id="analysis")
    return _scheduler
