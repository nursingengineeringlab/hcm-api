import os, time, copy, json
import threading, queue
from data_api.models import Senior
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

DEVICE_TIMEOUT = 60 * 5
MAX_DATA_ARRAY_LEN = 10

