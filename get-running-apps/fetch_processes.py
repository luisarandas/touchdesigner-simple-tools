
# 20-04-2024 luisarandas

import re
import subprocess

def fetch_process_list():
    try:
        # Supress CMD with startupinfo object
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        output = subprocess.check_output('tasklist', encoding='utf-8', startupinfo=startupinfo).strip()
        lines = output.split('\n')
        return lines
    except subprocess.CalledProcessError as e:
        print(f"Failed to fetch processes: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def populate_process_table(process_lines, table_dat):
    # Fill specified Table DAT with process information sorted by memory usage
    if not process_lines:
        print("No process lines to process.")
        return
    table_dat.clear()
    headers = ['Image Name', 'PID', 'Session Name', 'Session#', 'Mem Usage']
    table_dat.appendRow(headers)
    process_details = []
    for line in process_lines[3:]:
        parts = re.split(r"\s+", line.strip(), maxsplit=4)
        if len(parts) == 5:
            mem_usage = parts[4].replace(' K', '').replace(',', '')
            mem_usage = int(mem_usage) if mem_usage.isdigit() else 0
            process_details.append(parts[:4] + [mem_usage])

    process_details.sort(key=lambda x: x[4], reverse=True)
    for details in process_details:
        details[4] = f"{details[4]} K"
        table_dat.appendRow(details)


_processes = fetch_process_list()
populate_process_table(_processes, op('process_table'))
