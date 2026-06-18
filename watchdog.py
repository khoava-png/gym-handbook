import os
import sys
import time
import subprocess
from datetime import datetime

# Files to watch
WATCH_FILES = ["index.html", "Nghien_Cuu_Dinh_Duong_Gym.md"]
LOG_FILE = "watchdog.log"
CHECK_INTERVAL_SECONDS = 5
DEBOUNCE_DELAY_SECONDS = 2  # Wait after change detected to ensure file writing is complete

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] {message}"
    print(formatted_msg)
    sys.stdout.flush()
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted_msg + "\n")
    except Exception as e:
        print(f"Error writing to log: {e}")

def run_git_command(args):
    try:
        # Run command and capture output
        res = subprocess.run(args, capture_output=True, text=True, check=True)
        return True, res.stdout
    except subprocess.CalledProcessError as e:
        return False, f"Command '{' '.join(args)}' failed.\nstdout: {e.stdout}\nstderr: {e.stderr}"

def push_updates():
    log_message("Phát hiện thay đổi! Đang chuẩn bị tự động đẩy lên GitHub...")
    
    # Wait to make sure file write has finished completely
    time.sleep(DEBOUNCE_DELAY_SECONDS)
    
    # 1. git add
    success, out = run_git_command(["git", "add"] + WATCH_FILES)
    if not success:
        log_message(f"Lỗi git add: {out}")
        return
        
    # Check if there are actual changes staged
    success, out = run_git_command(["git", "status", "--porcelain"])
    if not success:
        log_message(f"Lỗi git status: {out}")
        return
    
    if not out.strip():
        log_message("Không có thay đổi thực tế nào để commit.")
        return

    # 2. git commit
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    commit_msg = f"Auto-update: Cập nhật cẩm nang dinh dưỡng ({timestamp})"
    success, out = run_git_command(["git", "commit", "-m", commit_msg])
    if not success:
        log_message(f"Lỗi git commit: {out}")
        return
    log_message(f"Commit thành công: {commit_msg}")

    # 3. git push
    log_message("Đang đẩy lên GitHub (git push origin main)...")
    success, out = run_git_command(["git", "push", "origin", "main"])
    if not success:
        log_message(f"Lỗi git push: {out}")
    else:
        log_message("Đẩy lên GitHub thành công! Giao diện online đã được cập nhật.")

def main():
    log_message("Khởi động Watchdog Auto-Push cho cẩm nang Dinh dưỡng...")
    log_message(f"Đang theo dõi các file: {', '.join(WATCH_FILES)}")
    
    # Initialize file modification timestamps
    last_modified = {}
    for filename in WATCH_FILES:
        if os.path.exists(filename):
            last_modified[filename] = os.path.getmtime(filename)
        else:
            last_modified[filename] = 0.0

    while True:
        try:
            change_detected = False
            for filename in WATCH_FILES:
                if not os.path.exists(filename):
                    continue
                    
                current_mtime = os.path.getmtime(filename)
                
                # If first time tracking or file has been modified
                if filename not in last_modified or current_mtime > last_modified[filename]:
                    # If this is the initial load, don't trigger push, just track it
                    if filename in last_modified and last_modified[filename] > 0:
                        change_detected = True
                    last_modified[filename] = current_mtime
            
            if change_detected:
                push_updates()
                # Update timestamps again after git operations to avoid double trigger
                for filename in WATCH_FILES:
                    if os.path.exists(filename):
                        last_modified[filename] = os.path.getmtime(filename)
                        
        except KeyboardInterrupt:
            log_message("Đang tắt Watchdog...")
            break
        except Exception as e:
            log_message(f"Có lỗi bất thường xảy ra trong vòng lặp: {e}")
            
        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
