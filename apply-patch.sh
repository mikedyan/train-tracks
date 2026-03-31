#!/bin/bash
# Day 14 patch applier - uses python3 to apply the patch
cd "$(dirname "$0")"
python3 patch-day14.py
if [ $? -eq 0 ]; then
  echo "Patch applied successfully"
  rm -f patch-day14.py apply-patch.sh
  git add -A
  git commit -m "Day 14: Keyboard Shortcuts + Undo/Redo Polish"
  git push origin main
else
  echo "Patch failed!"
  exit 1
fi
