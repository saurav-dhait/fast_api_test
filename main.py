from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Record(BaseModel):
    id: int
    latitude: float
    longitude: float
    sensor_values: List[float]


app = FastAPI()

records = []


@app.get("/")
async def root():
    return {"message": "Hello "}


@app.get("/records")
async def get_records():
    return {"records": records}


@app.get("/records/{record_id}")
async def get_record(record_id: int):
    for record in records:
        if record.id == record_id:
            return {"record": record}
    return {"message": f"no records with id : {record_id}"}


@app.post("/records")
async def create_records(record: Record):
    records.append(record)
    return {"records": records}


@app.delete("/records/{record_id}")
async def delete_record(record_id: int):
    for record in records:
        if record.id == record_id:
            records.remove(record)
            return {"message": f"record with id : {record_id} was deleted"}
    return {"message": f"no records with id : {record_id}"}
