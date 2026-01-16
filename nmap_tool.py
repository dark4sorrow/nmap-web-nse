import nmap
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# CORS is crucial here because your HTML is on port 80, but this API is on port 8000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

nm = nmap.PortScanner()

class ScanRequest(BaseModel):
    target: str
    script: str

ALLOWED_SCRIPTS = [
    "http-title",
    "ssl-enum-ciphers",
    "vuln",
    "smb-os-discovery",
    "dns-brute"
]

@app.get("/")
def read_root():
    return {"status": "NSE API Online", "scripts": ALLOWED_SCRIPTS}

@app.post("/scan")
def run_scan(request: ScanRequest):
    if request.script not in ALLOWED_SCRIPTS:
        raise HTTPException(status_code=400, detail="Script not allowed")

    print(f"[*] Scanning {request.target} with {request.script}...")
    
    try:
        # running with -sV for version detection
        scan_data = nm.scan(hosts=request.target, arguments=f'-sV --script {request.script}')
        return {"status": "success", "data": scan_data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # We specify the filename 'nmap_tool' in the run command if reloading is needed
    uvicorn.run(app, host="0.0.0.0", port=8000)
