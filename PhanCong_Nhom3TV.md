# PHÂN CÔNG NHÓM 3 THÀNH VIÊN — Đề tài: GIT – GitHub – GitLab (Học phần ASPX, .NET Framework 4.8.1)

> File này là nguồn chân lý duy nhất (Single Source of Truth) cho kế hoạch nhóm.
> Đổi tên `TV1/TV2/TV3` thành tên thật + MSSV trước khi nộp.

## 0. Mục tiêu nộp bài (Definition of Done)

| # | Hạng mục nộp | File/Thư mục | Người chịu trách nhiệm chính |
|---|--------------|--------------|-------------------------------|
| 1 | Slide thuyết trình (PDF + source) | `Slide_LaTeX/slide.tex` → `slide.pdf` | TV2 (tổng hợp), cả nhóm viết nội dung phần mình |
| 2 | Báo cáo LaTeX (PDF + source + .bib) | `BaoCao_LaTeX/main.tex` → `main.pdf` | TV3 (tổng hợp), cả nhóm viết nội dung phần mình |
| 3 | Bộ hình minh họa | `HinhAnh/*.svg` (+ TikZ trong .tex) | TV1 |
| 4 | Repo demo ASPX .NET 4.8.1 có lịch sử Git mẫu | Link GitHub + link GitLab trong báo cáo | TV1 + TV2 + TV3 (mỗi người 1 nhánh feature) |
| 5 | Kịch bản nói + câu hỏi phản biện | `KichBan_ThuyetTrinh.md` | Cả nhóm, TV3 tổng hợp |

**Quy tắc nhóm:**
- Mọi nội dung viết bằng **tiếng Việt** (thuật ngữ kỹ thuật giữ tiếng Anh).
- Mọi commit tuân thủ **Conventional Commits**: `docs: ...`, `feat: ...`, `fix: ...`.
- Không push thẳng `main` — luôn qua **Pull Request / Merge Request** + 1 người review.
- Mỗi phần phải có: lý thuyết + **lệnh/ví dụ chạy được** + **hình minh họa** + **ví dụ gắn với project ASPX 4.8.1**.

---

## 1. Phân công theo thành viên (mỗi người 1 mảng + 1 đầu việc chung)

### TV1 — GIT CĂN BẢN → SIÊU NÂNG CAO (Local Git + Internals)
- **Báo cáo:** Chương 1 (Giới thiệu) + Chương 2 (Git căn bản) + Chương 3 (Git nâng cao).
- **Slide:** Phần 1 + Phần 2 (khoảng slide 1–25).
- **Demo live (5–7 phút):** `init/clone → add/commit → branch/merge → rebase → stash → reset/revert → tag`, giải quyết **conflict file `Web.config`**.
- **Hình phụ trách:** `git-3-vung.svg`, `git-branch-merge.svg`, `gitflow.svg`.
- **Repo demo:** tạo repo mẫu `AspxDemo_NET481` (.NET Framework 4.8.1, Web Forms), viết `.gitignore` chuẩn, tạo lịch sử commit mẫu.
- **Tiêu chí đạt:** người chưa biết Git xem xong làm được 20 lệnh cơ bản; giải thích được blob/tree/commit.

### TV2 — GITHUB + CI/CD CHO ASPX (GitHub + Actions)
- **Báo cáo:** Chương 4 (GitHub) + Phụ lục C.1 (mẫu GitHub Actions YAML).
- **Slide:** Phần 3 (khoảng slide 26–45).
- **Demo live (5–7 phút):** Fork → PR → Review → Resolve conflict → Merge; chạy **GitHub Actions build `msbuild` + test** cho project ASPX 4.8.1; demo Protected Branch + Secret.
- **Hình phụ trách:** `pr-flow.svg`, `cicd-github.svg`.
- **Repo demo:** nhánh `feature/github-actions`, file `.github/workflows/ci-aspx-481.yml` chạy thật (xanh).
- **Tiêu chí đạt:** PR mẫu được merge qua review; Actions build pass; trình bày được 8 tính năng GitHub (Issues, PR, Actions, Packages, Pages, Security, Codespaces, Copilot).

### TV3 — GITLAB + SO SÁNH + ỨNG DỤNG NHÓM (GitLab + Tổng hợp)
- **Báo cáo:** Chương 5 (GitLab) + Chương 6 (So sánh) + Chương 7 (Áp dụng nhóm ASPX) + Chương 8 (Kết luận) + Phụ lục + `.bib`.
- **Slide:** Phần 4 + Phần 5 + Kết luận (khoảng slide 46–65) + slide Phân công + Q&A.
- **Demo live (5–7 phút):** Mirror repo sang GitLab → Merge Request → Approval → **GitLab CI (Windows runner, `msbuild`)** → Environments; demo bảng so sánh.
- **Hình phụ trách:** `cicd-gitlab.svg`, `cicd-tongquan.svg`.
- **Repo demo:** nhánh `feature/gitlab-ci`, file `.gitlab-ci.yml` chạy thật; trang so sánh GitHub↔GitLab.
- **Tiêu chí đạt:** MR được approve + merge; pipeline pass; bảng so sánh ≥ 20 tiêu chí; báo cáo biên dịch không lỗi, đầy đủ mục lục + tài liệu tham khảo.

---

## 2. Đề cương chi tiết (map với file LaTeX)

| Chương báo cáo | Nội dung từ cơ bản → siêu nâng cao | Người viết |
|---|---|---|
| C1. Giới thiệu | Lý do chọn đề tài, mục tiêu, phạm vi, liên hệ học phần ASPX .NET 4.8.1, phương pháp thực hiện | TV1 |
| C2. Git căn bản | Lịch sử; kiến trúc 3 vùng + `.git`; cài đặt/cấu hình; `add/commit/status/log/diff`; nhánh/merge; hoàn tác (`reset/revert/restore`); `stash/tag`; `.gitignore` cho ASP.NET; demo ASPX | TV1 |
| C3. Git nâng cao | Internals (blob/tree/commit, SHA, packfile); rebase tương tác; `cherry-pick/reflog/bisect`; hooks; LFS; submodule/subtree; worktree; ký commit (GPG/SSH); `sparse-checkout`/partial clone; `filter-repo`; `rerere`; GitFlow/GitHub Flow/Trunk-Based; Conventional Commits | TV1 |
| C4. GitHub | Tổng quan; Issues/Projects/Wiki; Fork/PR/Review; Protected branch + CODEOWNERS + Rulesets; **Actions CI/CD cho ASPX 4.8.1**; Packages/Pages; Advanced Security (Dependabot, CodeQL, secret scanning); Copilot | TV2 |
| C5. GitLab | Tổng quan; Groups/Projects/Issues/Boards; MR + Approval rules; **CI/CD `.gitlab-ci.yml` cho ASPX 4.8.1 (Windows runner)**; Environments/Review Apps; Registry; Self-hosted vs SaaS; Auto DevOps | TV3 |
| C6. So sánh | Bảng ≥ 20 tiêu chí: Git vs GitHub vs GitLab; GitHub vs GitLab (giá, CI/CD, review, bảo mật, self-host, phù hợp ASPX) | TV3 |
| C7. Áp dụng nhóm | Quy trình 3 người: `main/develop/feature` + PR/MR; checklist review Web Forms; xử lý conflict `Web.config`; quản lý connection string/secret; lịch sử commit mẫu; bài tập + rubric | TV3 (TV1+TV2 góp ví dụ) |
| C8. Kết luận | Tổng kết, hạn chế, hướng phát triển | TV3 |
| Phụ lục | A. Bảng lệnh Git; B. `.gitignore` mẫu; C. YAML mẫu; D. Kịch bản demo; E. Phân công | TV1 (A,B) + TV2 (C.1) + TV3 (C.2,D,E) |

---

## 3. Timeline đề xuất (2 tuần)

| Tuần | Việc | Output |
|------|------|--------|
| Tuần 1 – Ngày 1–2 | TV1 dựng repo demo + `.gitignore`; TV2 tạo repo GitHub; TV3 tạo project GitLab (mirror) | 2 repo + 3 nhánh feature |
| Tuần 1 – Ngày 3–5 | Mỗi người viết nháp chương báo cáo của mình + vẽ hình được giao | Nháp `.tex` theo nhánh |
| Tuần 1 – Ngày 6–7 | Review chéo qua PR/MR (mỗi PR ≥ 1 approve); TV2 làm Actions xanh; TV3 làm pipeline GitLab xanh | PR/MR đã merge + CI xanh |
| Tuần 2 – Ngày 1–3 | TV3 tổng hợp báo cáo; TV2 tổng hợp slide; TV1 kiểm tra lệnh + hình | `main.pdf` + `slide.pdf` bản beta |
| Tuần 2 – Ngày 4–5 | Tổng duyệt: demo khô, bấm giờ, chuẩn bị câu hỏi phản biện | Kịch bản final |
| Tuần 2 – Ngày 6 | Nộp: slide PDF + báo cáo PDF + source LaTeX + link repo | Checklist nộp bài tick đủ |

---

## 4. Kịch bản thuyết trình (20–25 phút + 5–10 phút hỏi đáp)

| Phút | Người | Nội dung |
|------|-------|----------|
| 0–2 | TV3 | Mở đầu: vì sao nhóm ASPX cần Git; roadmap bài nói |
| 2–9 | TV1 | Git từ cơ bản → nâng cao + demo local (kèm 1 conflict `Web.config`) |
| 9–16 | TV2 | GitHub + PR + Actions build ASPX 4.8.1 (show pipeline xanh) |
| 16–22 | TV3 | GitLab + MR + pipeline + bảng so sánh + quy trình nhóm 3 người |
| 22–25 | Cả nhóm | Kết luận + bài học; mỗi người nói 1 câu takeaway |
| Hỏi đáp | Cả nhóm | Chia câu theo mảng: Git→TV1, GitHub→TV2, GitLab/so sánh→TV3 |

---

## 5. Ngân hàng câu hỏi phản biện (chuẩn bị trước)

**Dành cho TV1 (Git):**
1. `git pull` khác gì `git fetch + git merge`? Khi nào `pull --rebase` tốt hơn?
2. `reset --soft/mixed/hard` khác nhau thế nào? Trường hợp nào được phép dùng `--hard`?
3. `merge` vs `rebase` vs `cherry-pick` — chọn cái nào khi nào? Vì sao cấm rebase nhánh public?
4. Giải thích blob/tree/commit và vì sao Git phát hiện đổi 1 byte?
5. `.gitignore` không có tác dụng với file đã commit — xử lý thế nào (`git rm --cached`)?

**Dành cho TV2 (GitHub):**
6. Fork khác branch khi nào? Vì sao bài tập nhóm dùng branch + PR thay vì fork?
7. Protected branch + required review + status check chặn được lỗi gì? Demo 1 lần bị chặn.
8. GitHub Actions build project .NET Framework 4.8.1 cần image/runner gì? Vì sao không dùng `ubuntu-latest` + `dotnet build`?
9. Secret trong Actions khác biến môi trường thường thế nào? Lưu connection string ở đâu?
10. Giải thích chiến lược cache NuGet packages để pipeline chạy nhanh.

**Dành cho TV3 (GitLab + tổng hợp):**
11. Merge Request khác Pull Request ở điểm nào (tên gọi, Approval rules, Merge trains)?
12. `.gitlab-ci.yml` gồm những khối chính nào? `stages/jobs/artifacts/cache` dùng ra sao?
13. Vì sao build ASPX 4.8.1 trên GitLab cần Windows runner + `msbuild`? Vẽ pipeline stages.
14. So sánh GitHub vs GitLab theo 5 tiêu chí quan trọng nhất với đồ án môn học.
15. Nhóm 3 người, 1 người push `Web.config` chứa connection string thật lên public repo — xử trí từng bước?

---

## 6. Checklist nộp bài (tick trước khi nộp)

- [ ] `Slide_LaTeX/slide.pdf` biên dịch sạch, đủ tên + MSSV 3 thành viên, số trang, ≥ 6 hình.
- [ ] `BaoCao_LaTeX/main.pdf` đủ bìa + mục lục + ≥ 6 chương + phụ lục + tài liệu tham khảo.
- [ ] Source `.tex` + `.bib` + `HinhAnh/` nộp kèm, biên dịch lại được từ đầu.
- [ ] Link repo GitHub + GitLab public, có lịch sử PR/MR + pipeline xanh (chụp ảnh bỏ vào báo cáo).
- [ ] Mỗi thành viên thuộc phần demo + 5 câu phản biện của mình.
- [ ] Chạy kiểm tra chính tả tiếng Việt 1 lượt; thuật ngữ tiếng Anh viết nhất quán.
