# GIT – GitHub – GitLab cho học phần ASPX (.NET Framework 4.8.1) — Nhóm 3 thành viên

Bài trình bày đi từ **cơ bản → nâng cao → siêu nâng cao**, mọi ví dụ gắn với **project ASP.NET Web Forms 4.8.1**.

## Cấu trúc nộp bài

```
TuHoc_ASPX/
├── PhanCong_Nhom3TV.md        ← chia việc, timeline, kịch bản, câu hỏi phản biện
├── KichBan_ThuyetTrinh.md     ← lời nói chi tiết từng slide + phân vai
├── README.md                  ← file này: hướng dẫn biên dịch + nộp bài
├── CauHoi_PhanBien_MoRong.md  ← 30 câu phản biện + gợi ý trả lời
├── BangThuatNgu_Glossary.md   ← 70 thuật ngữ Anh–Việt
├── Checklist_NopBai.md        ← checklist nộp bài theo người + deadline
├── HuongDan_BienDich_Overleaf.md ← biên dịch LaTeX + 10 lỗi thường gặp
├── TieuChi_ChamDiem_Rubric.md ← rubric tự chấm thang 10
├── NhatKy_Commit_Mau.md       ← mẫu log/PR/MR cho repo demo
├── HinhAnh/                   ← 15 hình SVG (vector)
│   ├── git-3-vung.svg, git-branch-merge.svg, gitflow.svg, pr-flow.svg
│   ├── cicd-tongquan.svg, cicd-github.svg, cicd-gitlab.svg
│   └── git-rebase-vs-merge.svg, git-internals-objects.svg, lichsu-git-timeline.svg,
│       protected-branch.svg, conventional-commits.svg, secrets-quanly.svg,
│       gitlab-mr-approvals.svg, trangthai-file-git.svg
├── Demo_ASPX/                 ← mẫu dựng repo demo ASPX 4.8.1
│   ├── README-DEMO.md, gitignore-ASPNET-NET481.txt, github-workflow-ci-yml.txt,
│   └── gitlab-ci-yml.txt, Web-Release-config-mau.txt
├── BaoCao_LaTeX/              ← báo cáo (article, tiếng Việt, biên dịch từ main.tex)
│   ├── main.tex               ← file gốc: bìa + mục lục + input + tài liệu tham khảo
│   ├── chuong1-gioithieu.tex … chuong8-ketluan.tex (16 file: 8 chương, module hóa)
│   ├── phulucA-banglenh.tex, phulucB-gitignore.tex, phulucC-yaml.tex,
│   │   phulucD-kichbandemo.tex
│   └── tailieu_thamkhao.bib   ← 10 mục tham khảo
└── Slide_LaTeX/               ← slide Beamer 16:9 (~50 slides, biên dịch từ slide.tex)
    ├── slide.tex              ← file gốc: tiêu đề + mục lục + 8 section
    └── phan1-modau.tex … phan8-ketluan-qa.tex (8 phần)
```

## Cách biên dịch LaTeX (cần TeX Live / MiKTeX + gói tiếng Việt)

Báo cáo:

```bash
cd BaoCao_LaTeX
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Slide:

```bash
cd Slide_LaTeX
pdflatex slide.tex
pdflatex slide.tex
```

> Ghi chú: file `.tex` dùng `pdflatex` + `fontenc T5` + `babel vietnamese` nên biên dịch
> được ngay trên Overleaf (chọn Compiler = pdfLaTeX) hoặc TeXstudio/VS Code + LaTeX Workshop.
> Hình SVG: khi biên dịch, xuất SVG ra PDF/PNG (Inkscape: `inkscape file.svg -o file.pdf`)
> rồi đặt cạnh `.tex`, hoặc chèn trực tiếp nếu dùng `LuaLaTeX + svg package`.
> Trong source, hình vẽ chính đã được dựng bằng **TikZ** nên vẫn biên dịch ra hình
> ngay cả khi chưa chuyển đổi SVG.

## Cách nộp bài (gợi ý)

1. Nén `BaoCao_LaTeX/` + `Slide_LaTeX/` + `HinhAnh/` + 2 file `.md` thành 1 ZIP.
2. Xuất thêm `main.pdf` + `slide.pdf` để thầy/cô chấm nhanh không cần biên dịch.
3. Đính kèm link repo GitHub + GitLab (public) có pipeline xanh trong báo cáo (Chương 7).
4. Điền tên + MSSV 3 thành viên vào: bìa báo cáo, slide đầu, file phân công.

## Quy ước viết chung (đọc trước khi sửa file)

- Tiếng Việt toàn bộ; thuật ngữ giữ tiếng Anh: commit, branch, merge, pull request, pipeline…
- Lệnh Git/VS trong khối `lstlisting`, có chú thích dòng lệnh quan trọng.
- Mọi chương: lý thuyết → ví dụ chạy được → hình → ví dụ ASPX 4.8.1 → chốt ý.
- Commit theo Conventional Commits: `docs: ...`, `feat: ...`, `fix: ...`.
