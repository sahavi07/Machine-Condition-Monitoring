"""
Database Models for Machine Condition Monitoring System.
Defines SQLAlchemy schema for storing sensor telemetry.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class MachineReading(db.Model):
    __tablename__ = 'machine_readings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reading_id = db.Column(db.Integer, nullable=False, unique=True)
    machine_id = db.Column(db.String(20), nullable=False, index=True)
    vibration = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=True)  # Nullable to handle missing values
    alert_flag = db.Column(db.Integer, nullable=False, default=0)
    recorded_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        """Serializes DB model into JSON-friendly dictionary format."""
        return {
            "id": self.id,
            "reading_id": self.reading_id,
            "machine_id": self.machine_id,
            "vibration": self.vibration,
            "temperature": self.temperature,
            "alert_flag": self.alert_flag,
            "recorded_at": self.recorded_at.isoformat() if self.recorded_at else None
        }
