import os
import psutil
import json
from datetime import datetime

def get_system_usage():
    """Получает загрузку CPU, RAM и свободное место на дисках"""
    usage = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "CPU_Load (%)": psutil.cpu_percent(interval=1),
        "RAM_Usage (%)": psutil.virtual_memory().percent
    }
    return usage

def save_report():
    """Сохраняет отчёт в JSON"""

    # Используем абсолютный путь внутри контейнера
    report_dir = "/app/reports"
    os.makedirs(report_dir, exist_ok=True)

    report_path = os.path.join(report_dir, "cpu_ram_report.json")
    usage = get_system_usage()

    with open(report_path, "w") as f:
        json.dump(usage, f, indent=4)

    print(f"✅ Отчёт сохранён: {report_path}")

if __name__ == "__main__":
    print(get_system_usage())
    save_report()
