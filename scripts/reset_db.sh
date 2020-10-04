#!/usr/bin/env bash
echo "drop database $POSTGRES_DB; create database $POSTGRES_DB;" | psql
