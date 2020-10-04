#!/usr/bin/env bash
gunicorn -w 16 -b 0:8000 -t 360 sea_nation.wsgi
