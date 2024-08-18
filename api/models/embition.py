import base64
import hashlib
import hmac
import json
import logging
import os
import pickle
import re
import time
from json import JSONDecodeError

from sqlalchemy import func, BigInteger
from sqlalchemy.dialects.postgresql import JSONB

from configs import dify_config
from core.rag.retrieval.retrival_methods import RetrievalMethod
from extensions.ext_database import db
from extensions.ext_storage import storage

from .account import Account
from .model import App, Tag, TagBinding, UploadFile
from .types import StringUUID


class DocumentDirectory(db.Model):
    __tablename__ = 'embition_document_directories'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='document_directories_pkey'),
        db.Index('document_directories_dataset_id_idx', 'dataset_id'),
        db.Index('document_directories_document_id_idx', 'document_id'),
        db.Index('document_directories_dir_path_idx', 'dir_path'),
    )

    # initial fields
    id = db.Column(BigInteger, primary_key=True, autoincrement=True)
    dataset_id = db.Column(StringUUID, nullable=False)
    document_id = db.Column(StringUUID, nullable=False)
    dir_path = db.Column(db.String(512), nullable=False, default='/')
