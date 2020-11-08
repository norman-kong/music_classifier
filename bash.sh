#!/bin/sh

APP= '/Applications/MuseScore 3.5.app'
if [ ! -d "$APP" ]; then
  echo >&2 "$0: $APP not found."
  exit 1
fi
exec open -a "$APP" "$@"
