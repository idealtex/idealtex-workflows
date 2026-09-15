import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import textwrap

workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/workflow-services-release.yml").read_text()
step = workflow.split("      - name: Update latest image\n", 1)[1].split("      - name:", 1)[0]
script = textwrap.dedent(step.split("        run: |\n", 1)[1])
bash = str(Path(os.environ["ProgramFiles"]) / "Git/bin/bash.exe") if os.name == "nt" else shutil.which("bash")
stub = r'''
git() {
  case "$*" in
    'fetch --no-tags origin main') return "$FETCH_STATUS" ;;
    'rev-parse FETCH_HEAD') printf '%s\n' "$MAIN_SHA" ;;
    *) return 99 ;;
  esac
}
docker() {
  printf '%s\n' "$@" >> "$DOCKER_CALLS"
  return "$PUSH_STATUS"
}
'''
with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    for main_sha, fetch_status, push_status in (("current", 0, 0), ("newer", 0, 0), ("current", 23, 0), ("current", 0, 42)):
        summary = root / "summary"
        calls = root / "docker-calls"
        summary.write_text("")
        calls.write_text("")
        env = os.environ | {
            "MAIN_SHA": main_sha, "GITHUB_SHA": "current",
            "FETCH_STATUS": str(fetch_status), "PUSH_STATUS": str(push_status),
            "IMAGE": "ghcr.io/example/app:v1.2.3", "LATEST_IMAGE": "ghcr.io/example/app:latest",
            "GITHUB_STEP_SUMMARY": summary.as_posix(), "DOCKER_CALLS": calls.as_posix(),
        }
        result = subprocess.run([bash, "-euo", "pipefail", "-c", stub + script], env=env, capture_output=True)
        assert result.returncode == (fetch_status or push_status), result.stderr.decode()
        expected = ["buildx", "imagetools", "create", "--prefer-index=false", "--tag", env["LATEST_IMAGE"], env["IMAGE"]]
        assert calls.read_text().splitlines() == (expected if main_sha == "current" and not fetch_status else [])
        assert ("DEV image:" in summary.read_text()) == (main_sha == "current" and not fetch_status and not push_status)
        if main_sha == "newer":
            assert "Skipped latest" in summary.read_text()
print("PASS: latest promotion, stale rerun, fetch failure and registry failure")
