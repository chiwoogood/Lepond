#!/bin/bash
set -e

host="$1"
shift
cmd="$@"

until redis-cli -h "$host" ping > /dev/null 2>&1; do
  echo "Redis is unavailable - sleeping"
  sleep 1
done

echo "Redis is up - executing command"
exec $cmd
