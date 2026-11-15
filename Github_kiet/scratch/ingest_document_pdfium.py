import os
import sys

def validate_safe_path(pdf_path: str) -> str:
  resolved_path = os.path.realpath(os.path.abspath(pdf_path))
  brain_root = os.path.realpath(os.path.expanduser("~/.gemini/antigravity/brain"))
  under_brain = False
  try:
    if os.path.commonpath([brain_root, resolved_path]) == brain_root:
      under_brain = True
  except ValueError:
    pass
  under_tmp = False
  try:
    if os.path.commonpath(["/tmp", resolved_path]) == "/tmp":
      under_tmp = True
  except ValueError:
    pass
  under_cwd = False
  try:
    cwd_root = os.path.realpath(os.getcwd())
    if os.path.commonpath([cwd_root, resolved_path]) == cwd_root:
      under_cwd = True
  except ValueError:
    pass
  under_workspace = False
  try:
    ws_candidates = ["/workspace", os.path.realpath(os.path.join(os.getcwd(), "..")), os.environ.get("WORKSPACE", "")]
    for candidate in ws_candidates:
      if candidate and os.path.exists(candidate):
        ws_root = os.path.realpath(candidate)
        if os.path.commonpath([ws_root, resolved_path]) == ws_root:
          under_workspace = True
          break
  except ValueError:
    pass
  if not (under_brain or under_tmp or under_workspace or under_cwd):
    print(f"Error: Path '{pdf_path}' outside allowed directories.", file=sys.stderr)
    sys.exit(1)
  return resolved_path

def ingest(pdf_path: str) -> None:
  path = validate_safe_path(pdf_path)
  if not os.path.exists(path) or not path.lower().endswith(".pdf"):
    print(f"Error: Invalid PDF path '{path}'", file=sys.stderr)
    sys.exit(1)
  if os.path.getsize(path) > 50 * 1024 * 1024:
    print("Error: File exceeds 50MB limit", file=sys.stderr)
    sys.exit(1)
  with open(path, "rb") as f:
    if f.read(5) != b"%PDF-":
      print("Error: Invalid PDF magic header", file=sys.stderr)
      sys.exit(1)
  try:
    import pypdfium2 as pdfium
    import PIL  # reached implicitly by pdfium's .to_pil() below
  except ImportError as e:
    print(
        f"Error: PDF dependency {e.name!r} is not installed ({e}). "
        "Report this; do not install it here. Operator remedy: "
        "pip install --user pypdfium2 Pillow",
        file=sys.stderr,
    )
    sys.exit(1)

  doc = pdfium.PdfDocument(path)
  page_count = len(doc)
  if page_count == 0 or page_count > 150:
    print(f"Error: Invalid page count ({page_count})", file=sys.stderr)
    sys.exit(1)

  artifact_dir = os.path.dirname(path)
  scratch_dir = os.path.join(artifact_dir, "scratch", "document_pages")
  os.makedirs(scratch_dir, exist_ok=True)
  scale = 200.0 / 72.0
  pages_text = []
  total_len = 0
  for i in range(page_count):
    page = doc[i]
    try:
      t = page.get_textpage().get_text_range()
    except Exception:
      t = ""
    pages_text.append(t)
    total_len += len(t.strip())
    page.render(scale=scale).to_pil().save(os.path.join(scratch_dir, f"page-{i + 1}.png"))

  avg_len = total_len / max(page_count, 1)
  if avg_len < 50:
    print("Error: Scanned PDF detected. Digital PDF required.", file=sys.stderr)
    sys.exit(1)

  map_path = os.path.join(artifact_dir, "DOCUMENT_TEXT_MAP.md")
  with open(map_path, "w", encoding="utf-8") as out:
    out.write("# Document Text & Page Navigation Map\n\n")
    out.write("> [!IMPORTANT]\n> Text navigation index. For proofs and figures, inspect page images in `page_image_dir`.\n\n")
    for i, t in enumerate(pages_text):
      out.write(f"## [Page {i + 1}] (`page-{i + 1}.png`)\n\n{t.strip()}\n\n---\n\n")
  print(f"Artifact directory: {artifact_dir}")
  print(f"Text map: {map_path}")
  print(f"Page images: {scratch_dir}")
  print(f"Successfully mapped {page_count} pages to DOCUMENT_TEXT_MAP.md")

if __name__ == "__main__":
  if len(sys.argv) < 2:
    sys.exit(1)
  ingest(sys.argv[1])
