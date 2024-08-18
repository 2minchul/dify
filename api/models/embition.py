from sqlalchemy import BigInteger

from extensions.ext_database import db
from .types import StringUUID


class DocumentDirectory(db.Model):
    __tablename__ = 'embition_document_directories'

    # initial fields
    id = db.Column(BigInteger, primary_key=True, autoincrement=True)
    dataset_id = db.Column(StringUUID, nullable=False)
    document_id = db.Column(StringUUID, nullable=False)
    dir_path = db.Column(db.String(512), nullable=False, default='/')
