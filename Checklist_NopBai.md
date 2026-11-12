# CHECKLIST NỘP BÀI — Đề tài GIT, GitHub, GitLab (ASPX, .NET Framework 4.8.1)

> Nhóm 3 thành viên: TV1 = Lê Quang An – 0024415453 (Git) — TV2 = Lê Tuấn Kiệt – 0024417193 (GitHub + CI/CD) — TV3 = Đoàn Minh Trí – 0024417136, trưởng nhóm (GitLab + tổng hợp).
> Nguyên tắc: mục nào tick xong phải có người kiểm tra ký nháy; không tick hộ khi chưa xem tận mắt.
> Deadline chung: ngày nộp ghi ở dòng cuối mỗi nhóm, chậm nhất 1 ngày trước giờ nộp chính thức.

---

## Nhóm 1 — Slide thuyết trình (`Slide_LaTeX/slide.tex` → `slide.pdf`)

| # | Mục kiểm tra | Người kiểm tra | Deadline | Hoàn thành |
|---|--------------|----------------|----------|------------|
| 1.1 | `slide.pdf` biên dịch sạch bằng `pdflatex` (chạy 2 lần), không còn lỗi `undefined reference`, không trang trắng thừa | TV2 | Tuần 2 – Ngày 3 | [ ] |
| 1.2 | Slide đầu có đủ: tên đề tài, tên + MSSV 3 thành viên, lớp, tên giảng viên, ngày báo cáo | TV3 | Tuần 2 – Ngày 3 | [ ] |
| 1.3 | Slide có đánh số trang, mục lục/agenda đầu phần, slide phân công và slide Q&A cuối | TV2 | Tuần 2 – Ngày 3 | [ ] |
| 1.4 | Đủ 3 phần theo phân công (TV1: slide 1–25, TV2: 26–45, TV3: 46–65), mỗi phần có ví dụ lệnh chạy được | TV1 | Tuần 2 – Ngày 3 | [ ] |
| 1.5 | Nhúng ít nhất 6 hình (3 vùng Git, branch/merge, PR flow, CI/CD GitHub, CI/CD GitLab, so sánh), hình rõ nét khi chiếu | TV1 | Tuần 2 – Ngày 4 | [ ] |
| 1.6 | Font chữ, cỡ chữ, màu sắc thống nhất; thuật ngữ tiếng Anh (commit, branch, merge, pull request, pipeline) viết nhất quán | TV3 | Tuần 2 – Ngày 4 | [ ] |
| 1.7 | Chạy kiểm tra chính tả tiếng Việt 1 lượt toàn bộ slide, sửa hết lỗi gõ dấu và từ viết hoa | TV3 | Tuần 2 – Ngày 5 | [ ] |

---

## Nhóm 2 — Báo cáo (`BaoCao_LaTeX/main.tex` → `main.pdf` + `.bib`)

| # | Mục kiểm tra | Người kiểm tra | Deadline | Hoàn thành |
|---|--------------|----------------|----------|------------|
| 2.1 | `main.pdf` biên dịch sạch theo đủ 4 bước (`pdflatex` → `bibtex` → `pdflatex` → `pdflatex`), không lỗi, không cảnh báo `citation undefined` | TV3 | Tuần 2 – Ngày 3 | [ ] |
| 2.2 | Đủ bìa, mục lục tự động, danh mục hình/bảng, đủ 8 chương (C1–C8) đúng đề cương `PhanCong_Nhom3TV.md` | TV3 | Tuần 2 – Ngày 3 | [ ] |
| 2.3 | Đủ phụ lục A–E (bảng lệnh Git, `.gitignore` mẫu, YAML mẫu, kịch bản demo, phân công) và tài liệu tham khảo từ file `.bib` | TV1 | Tuần 2 – Ngày 4 | [ ] |
| 2.4 | Mọi lệnh Git/YAML/config trong báo cáo đã chạy thử thật (không chép lý thuyết suông), output mẫu khớp thực tế | TV1 | Tuần 2 – Ngày 4 | [ ] |
| 2.5 | Bảng so sánh GitHub với GitLab đạt ít nhất 20 tiêu chí (giá, CI/CD, review, bảo mật, self-host, hỗ trợ ASPX 4.8.1) | TV3 | Tuần 2 – Ngày 4 | [ ] |
| 2.6 | Báo cáo ghi đúng link repo GitHub + GitLab (public) kèm ảnh chụp lịch sử commit và pipeline xanh | TV2 | Tuần 2 – Ngày 5 | [ ] |
| 2.7 | Kiểm tra chính tả tiếng Việt, đánh số hình/bảng/chương thống nhất, không còn TODO hay đoạn nháp | TV3 | Tuần 2 – Ngày 5 | [ ] |

---

## Nhóm 3 — Source LaTeX + hình (`BaoCao_LaTeX/`, `Slide_LaTeX/`, `HinhAnh/`)

| # | Mục kiểm tra | Người kiểm tra | Deadline | Hoàn thành |
|---|--------------|----------------|----------|------------|
| 3.1 | Nộp đủ source: `main.tex`, `tailieu_thamkhao.bib`, `slide.tex`, không thiếu file con (`\input`, style, logo nếu có) | TV3 | Tuần 2 – Ngày 5 | [ ] |
| 3.2 | Xóa file rác trước khi nén (`.aux`, `.log`, `.toc`, `.out`, `.synctex.gz`); chỉ giữ `.tex`, `.bib`, hình và PDF final | TV2 | Tuần 2 – Ngày 5 | [ ] |
| 3.3 | Đủ 15 hình SVG trong `HinhAnh/`: 7 hình lõi (`git-3-vung`, `git-branch-merge`, `gitflow`, `pr-flow`, `cicd-tongquan`, `cicd-github`, `cicd-gitlab`) + 8 hình bổ sung (`rebase-vs-merge`, `internals-objects`, `timeline`, `protected-branch`, `conventional-commits`, `secrets-quanly`, `mr-approvals`, `trangthai-file`) | TV1 | Tuần 2 – Ngày 4 | [ ] |
| 3.4 | Mỗi hình SVG mở được, chữ tiếng Việt không lỗi font; có bản TikZ hoặc bản PDF/PNG dự phòng để biên dịch ngay | TV1 | Tuần 2 – Ngày 4 | [ ] |
| 3.5 | Biên dịch lại từ đầu trên máy sạch (hoặc Overleaf với compiler `pdfLaTeX`) ra đúng `main.pdf` + `slide.pdf`, chụp ảnh làm bằng chứng | TV2 | Tuần 2 – Ngày 5 | [ ] |
| 3.6 | File ZIP nộp bài đặt tên đúng quy định lớp (ví dụ `Nhom_Git_GitHub_GitLab_0024415453_0024417193_0024417136.zip`), giải nén thử 1 lần | TV3 | Tuần 2 – Ngày 6 | [ ] |

---

## Nhóm 4 — Repo demo + pipeline (GitHub + GitLab, ASP.NET Web Forms 4.8.1)

| # | Mục kiểm tra | Người kiểm tra | Deadline | Hoàn thành |
|---|--------------|----------------|----------|------------|
| 4.1 | Repo GitHub và project GitLab để chế độ public, link truy cập được khi đăng xuất; README ghi rõ cách build bằng `msbuild` trên Windows | TV2 | Tuần 1 – Ngày 7 | [ ] |
| 4.2 | Lịch sử commit thật theo Conventional Commits (`feat:`, `fix:`, `docs:`), không commit gộp 1 cục vào phút cuối | TV1 | Tuần 2 – Ngày 2 | [ ] |
| 4.3 | Đủ 3 nhánh feature (mỗi TV 1 nhánh) và ít nhất 2 Pull Request + 1 Merge Request đã review (≥ 1 approve) rồi merge, không push thẳng `main` | TV2 | Tuần 2 – Ngày 2 | [ ] |
| 4.4 | GitHub Actions (`.github/workflows/ci-aspx-481.yml`, runner `windows-latest`, lệnh `msbuild`) chạy xanh lần cuối; có cache NuGet packages | TV2 | Tuần 1 – Ngày 7 | [ ] |
| 4.5 | GitLab CI (`.gitlab-ci.yml`, Windows runner, các stage `restore → build → test → package`) chạy xanh; artifacts lưu được gói build | TV3 | Tuần 1 – Ngày 7 | [ ] |
| 4.6 | Bật Protected Branch / Approval (GitHub) và Approval rules (GitLab) cho `main`; demo được 1 lần push bị chặn vì thiếu review | TV2 | Tuần 2 – Ngày 2 | [ ] |
| 4.7 | Không còn secret thật trong repo: connection string chuyển vào GitHub Secrets / GitLab CI variables, `Web.config` mẫu dùng giá trị giả | TV1 | Tuần 2 – Ngày 5 | [ ] |
| 4.8 | Chụp ảnh pipeline xanh + biểu đồ commit/branch đưa vào báo cáo (Chương 7) và slide demo, ảnh chụp trong 48 giờ trước nộp | TV3 | Tuần 2 – Ngày 5 | [ ] |

---

## Nhóm 5 — Chuẩn bị thuyết trình (20–25 phút + hỏi đáp)

| # | Mục kiểm tra | Người kiểm tra | Deadline | Hoàn thành |
|---|--------------|----------------|----------|------------|
| 5.1 | File `KichBan_ThuyetTrinh.md` chốt lời nói từng slide, phân vai theo phút (TV1: 2–9, TV2: 9–16, TV3: mở đầu + 16–22 + kết luận) | TV3 | Tuần 2 – Ngày 4 | [ ] |
| 5.2 | Tổng duyệt ít nhất 1 lần có bấm giờ: đủ 20–25 phút, chuyển mic mượt, không ai nói lố quá 1 phút | TV3 | Tuần 2 – Ngày 5 | [ ] |
| 5.3 | Demo khô cả 3 phần (TV1: conflict `Web.config`, TV2: PR + Actions, TV3: MR + pipeline GitLab), có video quay màn hình dự phòng khi mất mạng | TV1 | Tuần 2 – Ngày 5 | [ ] |
| 5.4 | Mỗi thành viên thuộc 5 câu phản biện mảng mình + trả lời trôi chảy 2 câu khó nhất (TV1: rebase, TV2: runner 4.8.1, TV3: xử lý lộ secret) | TV1 | Tuần 2 – Ngày 5 | [ ] |
| 5.5 | Chuẩn bị máy chiếu: sạc đầy pin, mang adapter HDMI, tắt thông báo, mở sẵn slide PDF + repo + tab pipeline, test mạng phòng học | TV2 | Tuần 2 – Ngày 6 | [ ] |
| 5.6 | In hoặc lưu offline 1 bản slide + báo cáo PDF trong USB dự phòng, đặt tên file rõ ràng theo họ tên nhóm | TV3 | Tuần 2 – Ngày 6 | [ ] |

---

## Ký xác nhận (ký sau khi tick đủ 5 nhóm)

| Thành viên | Họ tên | MSSV | Chữ ký | Ngày ký |
|------------|--------|------|--------|---------|
| TV1 — Git căn bản → nâng cao | Lê Quang An | 0024415453 | | |
| TV2 — GitHub + CI/CD | Lê Tuấn Kiệt | 0024417193 | | |
| TV3 — GitLab + so sánh + tổng hợp (trưởng nhóm) | Đoàn Minh Trí | 0024417136 | | |

> Cam kết: cả 3 thành viên đã cùng kiểm tra checklist này, mọi mục tick [x] đều đã xem tận mắt. File nộp cuối cùng là bản cả nhóm thống nhất.
