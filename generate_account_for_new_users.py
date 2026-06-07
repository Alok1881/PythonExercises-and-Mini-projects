import csv
import secrets
from random import randint
from pathlib import Path

script_dir = Path(__file__).resolve().parent
candidates = [script_dir / "data" / "users_in.csv", script_dir / "data" / "user_in.csv"]
input_path = next((p for p in candidates if p.exists()), candidates[0])
output_path = script_dir / "data" / "users_out.csv"

def norm(s: str) -> str:
    return ''.join(ch for ch in (s or '').lower() if ch.isalnum()) or 'user'

def gen_username(real: str, existing: set) -> str:
    base = norm(real)
    for _ in range(100):
        candidate = f"{base}{randint(100,9999)}"
        if candidate not in existing:
            return candidate
    i = 1
    while True:
        candidate = f"{base}{i}"
        if candidate not in existing:
            return candidate
        i += 1

def process(file_in, file_out):
    sample = file_in.read(1024); file_in.seek(0)
    try:
        delim = csv.Sniffer().sniff(sample).delimiter
    except Exception:
        delim = '\t' if '\t' in sample else ','

    reader = csv.DictReader(file_in, delimiter=delim)
    writer = csv.DictWriter(file_out, fieldnames=reader.fieldnames, delimiter=',')
    writer.writeheader()
    existing = set()
    for row in reader:
        row['password'] = secrets.token_hex(8)
        real = (row.get('real_name') or '').strip()
        raw = (row.get('username') or '').strip()
        if not raw or norm(raw) == norm(real):
            row['username'] = gen_username(real, existing)
        else:
            row['username'] = norm(raw)
        existing.add(row['username'])
        print('Simulating useradd:', ['/sbin/useradd', '-c', real, '-m', '-G', 'users', '-p', row['password'], row['username']])
        writer.writerow(row)

try:
    with open(input_path, 'r', newline='') as fin, open(output_path, 'w', newline='') as fout:
        process(fin, fout)
except PermissionError:
    alt = output_path.with_name('users_out_new.csv')
    print(f'Could not write {output_path}; writing to {alt} instead')
    with open(input_path, 'r', newline='') as fin, open(alt, 'w', newline='') as fout:
        process(fin, fout)