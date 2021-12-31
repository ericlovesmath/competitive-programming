#!/usr/bin/env bash
cd "$(dirname ${BASH_SOURCE[0]})"
find . -type f -name '*.out' -print
read -p "Remove all *.out files (y/n)? " choice
case "$choice" in 
  y|Y ) find . -type f -name '*.out' -delete;;
  * ) ;;
esac

