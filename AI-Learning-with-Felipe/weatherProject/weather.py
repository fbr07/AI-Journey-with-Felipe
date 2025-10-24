print("Hello Python World")
import sys

print("✅ Python is running from this interpreter:")
print(sys.executable)  # should point to ...\.venv\Scripts\python.exe

print("\n✅ Virtual environment site-packages path (first few entries):")
for p in sys.path[:3]:
    print(" -", p)

# Optional: confirm requests is importable (installed in your venv)
try:
    import requests

    print("\n✅ 'requests' is installed. Version:", requests.__version__)
except ImportError:
    print("\n❌ 'requests' is not installed in this environment.")
    print("   Run: pip install requests")
