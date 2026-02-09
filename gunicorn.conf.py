import os
import multiprocessing

workers = max(1, multiprocessing.cpu_count() * 2 + 1)
worker_class = "sync"
bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"
timeout = 120
keepalive = 5
accesslog = "-"
errorlog = "-"
loglevel = "info"
proc_name = "survey_system"
