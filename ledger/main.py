from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from ledger.api.api_v1.api import api_router
from ledger.db.session import Session

app = FastAPI()

origins = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
),
app.include_router(api_router)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response


"""
@app.post("/transactions/parse")
def parse_transactions_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    with open(file.filename, "wb") as uploaded_file:
        contents = file.file.read()
        uploaded_file.write(contents)

    with open(file.filename) as csv_file:
        tx_reader = csv.reader(csv_file)
        for line in tx_reader:
            print(f"{line}")

    os.remove(file.filename)
"""
