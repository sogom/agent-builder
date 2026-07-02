#!/usr/bin/env bash
set -euo pipefail

PLATFORM="both"
TARGET=""
FORCE="false"

usage() {
  cat <<'EOF'
Usage:
  ./scripts/install.sh --target /path/to/project [--platform claude|factory|both] [--force]
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      TARGET="${2:-}"
      shift 2
      ;;
    --platform)
      PLATFORM="${2:-}"
      shift 2
      ;;
    --force)
      FORCE="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ -z "$TARGET" ]]; then
  echo "--target is required." >&2
  usage
  exit 1
fi

if [[ "$PLATFORM" != "claude" && "$PLATFORM" != "factory" && "$PLATFORM" != "both" ]]; then
  echo "--platform must be claude, factory, or both." >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
TARGET="$(cd "$TARGET" && pwd)"

copy_skill() {
  local destination="$1"

  if [[ -e "$destination" ]]; then
    if [[ "$FORCE" != "true" ]]; then
      echo "Destination already exists: $destination" >&2
      echo "Use --force to replace it." >&2
      exit 1
    fi
    rm -rf "$destination"
  fi

  mkdir -p "$destination"
  tar \
    --exclude=".git" \
    --exclude="*.zip" \
    -C "$SOURCE_DIR" -cf - . | tar -C "$destination" -xf -
  echo "Installed: $destination"
}

if [[ "$PLATFORM" == "claude" || "$PLATFORM" == "both" ]]; then
  mkdir -p "$TARGET/.claude/skills"
  copy_skill "$TARGET/.claude/skills/agent-builder"
fi

if [[ "$PLATFORM" == "factory" || "$PLATFORM" == "both" ]]; then
  mkdir -p "$TARGET/.factory/skills"
  copy_skill "$TARGET/.factory/skills/agent-builder"
fi

echo "Installation complete."
