import os
import subprocess
import time

OUTPUT_DIR = "screenshot"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_test_case(answers, filename):
    process = subprocess.Popen(
        ["python", "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )

    input_data = "\n".join(answers) + "\n"
    stdout, stderr = process.communicate(input=input_data)

    print(f"[+] Kasus Uji Selesai: {filename}")
    return stdout

test_cases = [
    {
        "nama": "kasus1.png",
        "deskripsi": "Kasus 1: Ransomware (File terenkripsi + Server terhenti)",
        # 1:t, 2:y, 3:t, 4:y, 5:t, 6:t, 7:t, 8:t, 9:t, 10:t
        "jawaban": ["t", "y", "t", "y", "t", "t", "t", "t", "t", "t"]
    },
    {
        "nama": "kasus2.png",
        "deskripsi": "Kasus 2: Kasus Negatif (Hanya email mencurigakan)",
        # 1:t, 2:t, 3:t, 4:t, 5:t, 6:y, 7:t, 8:t, 9:t, 10:t
        "jawaban": ["t", "t", "t", "t", "t", "y", "t", "t", "t", "t"]
    },
    {
        "nama": "kasus3.png",
        "deskripsi": "Kasus 3: Multi Kesimpulan (DDoS + SQL Injection)",
        # 1:y (DB error), 2:t, 3:y (SQL syntax), 4:t, 5:y (Trafik abnormal), 6:t, 7:t, 8:t, 9:y (Server down), 10:t
        "jawaban": ["y", "t", "y", "t", "y", "t", "t", "t", "y", "t"]
    }
]

from playwright.sync_api import sync_playwright

def generate_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 900, "height": 700})

        for case in test_cases:
            output_text = run_test_case(case["jawaban"], case["nama"])

            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{
                        background-color: #0d1117;
                        color: #c9d1d9;
                        font-family: 'Courier New', Courier, monospace;
                        padding: 20px;
                        margin: 0;
                    }}
                    .terminal {{
                        background-color: #161b22;
                        border: 1px solid #30363d;
                        border-radius: 8px;
                        padding: 15px;
                        white-space: pre-wrap;
                        font-size: 13px;
                        line-height: 1.4;
                        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
                    }}
                    .title {{
                        color: #58a6ff;
                        font-weight: bold;
                        margin-bottom: 10px;
                    }}
                </style>
            </head>
            <body>
                <div class="title">// {case['deskripsi']}</div>
                <div class="terminal">{output_text}</div>
            </body>
            </html>
            """

            page.set_content(html_content)
            save_path = os.path.join(OUTPUT_DIR, case["nama"])
            page.screenshot(path=save_path, full_page=True)
            print(f"  [✓] Screenshot tersimpan di: {save_path}")

        browser.close()

if __name__ == "__main__":
    print("=== MEMULAI AUTOMATED TESTING & SCREENSHOT CAPTURE ===")
    generate_screenshots()
    print("\n[SELESAI] Semua screenshot telah tersimpan di dalam folder 'screenshot/'.")
