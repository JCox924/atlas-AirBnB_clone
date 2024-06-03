#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """Base class for all models"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""
        from models import storage  # imported here to avoid circular import issues on test, I'm very sorry

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    
    def save(self):
        """Updates the `updated_at` attribute with current time and saves to storage"""
        from models import storage  # again imported here to avoid circular import issues, please forgive me
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
    
    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

