# Gunicorn server configuration for concurrent request handling

workers = 4                # Tune based on available CPU cores
bind = "0.0.0.0:8000"      # Bind to all interfaces
timeout = 120              # Time allowed for a request before timing out
loglevel = "info"          # Logging level for debugging and monitoring
