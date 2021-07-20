#!/usr/bin/env python3
import os
import shutil
import sys
import socket
import emails
import psutil

def check_cpu_usage(max_percent):
    """Returns True if the cpu usage is too high."""
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > max_percent:
        return True
    return False

def check_disk_full(disk, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percentage_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    if percentage_free < min_percent:
        return True
    return False

def check_memory_usage():
    """Returns True if there isn't enough memory, False otherwise."""
    mem = psutil.virtual_memory()
    THRESHOLD = 500 * 1024 * 1024
    if mem.available < THRESHOLD:
        return True
    return False

def check_hostname(localhost):
    """Returns True if the localhost cannot be resolved to 127.0.0.1."""
    hostname = socket.gethostbyname('localhost')
    if hostname != localhost:
        return True
    return False

def main():
    # Generate and send email
    sender = "automation@example.com"
    receiver = "something@example.com"
    body = "Please check your system and resolve the issue as soon as possible."

    if check_cpu_usage(max_percent=80):
        subject = "Error - CPU usage is over 80%."
        message = emails.generate_no_attachment(sender, receiver, subject, body)
        emails.send(message)
    if check_disk_full(disk="/", min_percent=20):
        subject = "Error - Available disk space is less than 20%"
        message = emails.generate_no_attachment(sender, receiver, subject, body)
        emails.send(message)
    if check_memory_usage():
        subject = "Error - Available memory is less than 500MB"
        message = emails.generate_no_attachment(sender, receiver, subject, body)
        emails.send(message)
    if check_hostname(localhost="127.0.0.1"):
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        message = emails.generate_no_attachment(sender, receiver, subject, body)
        emails.send(message)

main()
