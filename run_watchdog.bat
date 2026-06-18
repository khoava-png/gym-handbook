@echo off
title Gym Doc Watchdog Auto-Push
color 0A
echo ====================================================================
echo            NET DO GYM HANDBOOK - AUTO-PUSH WATCHDOG
echo ====================================================================
echo  [Trang thai] Dang khoi dong va theo doi file...
echo  [Luu y] De cua so nay hoat dong de tu dong dong bo khi luu file.
echo  [Tat dung] Nhan to hop phims Ctrl + C hoac dong cua so nay de tat.
echo ====================================================================
echo.

python watchdog.py

if %errorlevel% neq 0 (
    color 0C
    echo.
    echo [Loi] Khong the chay script Python. Vui long kiem tra xem Python da duoc cai dat chua.
    pause
)
