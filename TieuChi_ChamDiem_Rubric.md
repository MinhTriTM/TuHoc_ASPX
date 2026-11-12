# Rubric Tự Chấm — Đề Tài GIT – GitHub – GitLab (Thang 10)

> Học phần ASPX (.NET Framework 4.8.1), nhóm 3 thành viên: TV1 = Lê Quang An – 0024415453 · TV2 = Lê Tuấn Kiệt – 0024417193 · TV3 = Đoàn Minh Trí – 0024417136 (trưởng nhóm).
> Chấm sau buổi tổng duyệt, trước ngày nộp 1 ngày.

## 0. Tổng Quan 6 Tiêu Chí

| # | Tiêu chí | Điểm tối đa | TV phụ trách chính | Tự chấm |
|---|----------|------------:|--------------------|---------|
| 1 | Nội dung Git (căn bản → nâng cao) | 2.0 | TV1 | |
| 2 | GitHub + GitHub Actions cho ASPX 4.8.1 | 2.0 | TV2 | |
| 3 | GitLab + CI + Bảng so sánh | 2.0 | TV3 | |
| 4 | Slide thuyết trình (Beamer) | 1.5 | TV2 (cả nhóm góp nội dung) | |
| 5 | Báo cáo LaTeX (article + BibTeX) | 1.5 | TV3 (cả nhóm góp nội dung) | |
| 6 | Demo live + Trả lời phản biện | 1.0 | Cả nhóm | |
| | **Tổng** | **10.0** | | |

## 1. Nội Dung Git — 2.0 Điểm (TV1)

| Mức | Khoảng điểm | Mô tả yêu cầu | TV phụ trách | Tự chấm |
|-----|------------|---------------|--------------|---------|
| Xuất sắc | 1.75 – 2.0 | Đủ 20 lệnh chạy được (`init`, `clone`, `add`, `commit`, `branch`, `merge`, `rebase`, `stash`, `reset`, `revert`, `tag`, `cherry-pick`, `reflog`…); giải thích đúng blob/tree/commit và SHA; có rebase tương tác, hooks, `.gitignore` chuẩn ASP.NET; mọi ví dụ gắn project ASPX 4.8.1 | TV1 | |
| Tốt | 1.25 – 1.5 | Đủ 15 lệnh cơ bản + `branch`/`merge`/`stash`/`tag`; giải thích được 3 vùng (working tree, staging, repo); có rebase hoặc hooks; thiếu 1–2 ví dụ ASPX | TV1 | |
| Đạt | 0.75 – 1.0 | Chỉ lệnh cơ bản (`add`/`commit`/`log`/`diff`); nhánh/merge còn lý thuyết suông; chưa có internals, chưa ví dụ ASPX cụ thể | TV1 | |
| Chưa đạt | 0 – 0.5 | Lệnh sai hoặc không chạy được; nhầm `reset`/`revert`; không phân biệt được merge/rebase; không có demo local | TV1 | |

## 2. GitHub + Actions — 2.0 Điểm (TV2)

| Mức | Khoảng điểm | Mô tả yêu cầu | TV phụ trách | Tự chấm |
|-----|------------|---------------|--------------|---------|
| Xuất sắc | 1.75 – 2.0 | PR mẫu merge qua ≥ 1 approve; Actions `windows-latest` + `msbuild` build project 4.8.1 xanh; có Protected branch + Secret + cache NuGet; trình bày đủ 8 tính năng (Issues, PR, Actions, Packages, Pages, Security, Codespaces, Copilot) | TV2 | |
| Tốt | 1.25 – 1.5 | PR merge được nhưng thiếu review hoặc thiếu resolve conflict; Actions xanh nhưng chưa cache; trình bày được 5–6 tính năng GitHub | TV2 | |
| Đạt | 0.75 – 1.0 | Chỉ fork/clone + push; PR mở nhưng chưa merge qua review; Actions vàng/đỏ hoặc build bằng `dotnet build` sai runner cho 4.8.1 | TV2 | |
| Chưa đạt | 0 – 0.5 | Không có PR; không có file `.github/workflows/ci-aspx-481.yml`; hoặc toàn bộ lý thuyết không demo | TV2 | |

## 3. GitLab + So Sánh — 2.0 Điểm (TV3)

| Mức | Khoảng điểm | Mô tả yêu cầu | TV phụ trách | Tự chấm |
|-----|------------|---------------|--------------|---------|
| Xuất sắc | 1.75 – 2.0 | MR approve + merge; pipeline GitLab (Windows runner + `msbuild`) xanh; giải thích đúng `stages`/`jobs`/`artifacts`/`cache`; bảng so sánh GitHub↔GitLab ≥ 20 tiêu chí; có Environments hoặc Registry demo | TV3 | |
| Tốt | 1.25 – 1.5 | MR merge được nhưng thiếu Approval rule; pipeline xanh nhưng thiếu `artifacts`/`cache`; bảng so sánh 12–19 tiêu chí | TV3 | |
| Đạt | 0.75 – 1.0 | Chỉ mirror repo sang GitLab; MR mở chưa merge; pipeline đỏ hoặc chưa có; bảng so sánh dưới 12 tiêu chí, thiếu giá/CI/bảo mật | TV3 | |
| Chưa đạt | 0 – 0.5 | Không có project GitLab; không có `.gitlab-ci.yml`; không có bảng so sánh | TV3 | |

## 4. Slide Beamer — 1.5 Điểm (TV2 Tổng Hợp)

| Mức | Khoảng điểm | Mô tả yêu cầu | TV phụ trách | Tự chấm |
|-----|------------|---------------|--------------|---------|
| Xuất sắc | 1.25 – 1.5 | 55–65 slide, `pdflatex` sạch không lỗi; đủ tên + MSSV, số trang; ≥ 6 hình (TikZ/SVG); mỗi phần có 1 slide chốt ý; font chữ ≥ 18pt, đọc được từ hàng cuối | TV2 | |
| Tốt | 0.9 – 1.0 | Đủ 3 phần nội dung + mở đầu/kết luận; 4–5 hình; còn 1–2 warning LaTeX; vài slide chữ nhỏ hoặc quá nhiều chữ | TV2 | |
| Đạt | 0.5 – 0.75 | Thiếu 1 phần nội dung hoặc thiếu slide phân công/Q&A; dưới 4 hình; biên dịch được nhưng lỗi font tiếng Việt ở vài slide | TV2 | |
| Chưa đạt | 0 – 0.25 | Không biên dịch được; hoặc dưới 30 slide; không có hình; thiếu tên thành viên | TV2 | |

## 5. Báo Cáo LaTeX — 1.5 Điểm (TV3 Tổng Hợp)

| Mức | Khoảng điểm | Mô tả yêu cầu | TV phụ trách | Tự chấm |
|-----|------------|---------------|--------------|---------|
| Xuất sắc | 1.25 – 1.5 | Đủ 8 chương + 5 phụ lục (A–E) + `.bib` ≥ 10 nguồn trích dẫn đúng; `pdflatex` + `bibtex` sạch; mục lục, số hình/bảng, tài liệu tham khảo đầy đủ; chính tả tiếng Việt đã soát 1 lượt | TV3 | |
| Tốt | 0.9 – 1.0 | Đủ 6 chương chính + 3 phụ lục; `.bib` 6–9 nguồn; còn warning trích dẫn chưa resolve; vài lỗi chính tả nhỏ | TV3 | |
| Đạt | 0.5 – 0.75 | Thiếu ≥ 2 chương hoặc thiếu phụ lục C (YAML mẫu); dưới 6 nguồn tham khảo; mục lục hoặc số trang hình sai | TV3 | |
| Chưa đạt | 0 – 0.25 | Không biên dịch được; hoặc dưới 4 chương; không có `.bib`; copy nội dung không trích nguồn | TV3 | |

## 6. Demo Live + Trả Lời — 1.0 Điểm (Cả Nhóm)

| Mức | Khoảng điểm | Mô tả yêu cầu | TV phụ trách | Tự chấm |
|-----|------------|---------------|--------------|---------|
| Xuất sắc | 0.9 – 1.0 | Mỗi TV demo 5–7 phút đúng mảng (TV1: conflict `Web.config`; TV2: PR + Actions xanh; TV3: MR + pipeline + bảng so sánh); trả lời đúng ≥ 4/5 câu phản biện của mảng mình; tổng giờ 20–25 phút + Q&A | TV1 + TV2 + TV3 | |
| Tốt | 0.7 – 0.8 | Demo đủ 3 mảng nhưng 1 mảng quá giờ hoặc phải thử lại lệnh; trả lời đúng 3/5 câu mỗi mảng | TV1 + TV2 + TV3 | |
| Đạt | 0.5 – 0.6 | Chỉ 2/3 mảng demo live, mảng còn lại chiếu ảnh; trả lời đúng 2/5 câu; vượt quá 30 phút tổng | TV1 + TV2 + TV3 | |
| Chưa đạt | 0 – 0.4 | Không demo live (chỉ đọc slide); hoặc không trả lời được câu hỏi cơ bản (`pull` vs `fetch`, fork vs branch) | TV1 + TV2 + TV3 | |

## 7. Cách Tính Điểm

1. Mỗi người tự chấm phần mình phụ trách theo khoảng điểm của mức đạt được,
   ghi số cụ thể (1 chữ số thập phân) vào cột **Tự chấm**.
2. Hai thành viên còn lại review chéo: nếu chênh nhau quá 0.5 điểm ở một
   tiêu chí thì demo lại phần đó rồi chốt số chung.
3. Điểm nhóm = tổng 6 ô tự chấm (tối đa 10.0). Ghi tổng vào đây: ___ / 10.
4. Mọi ô **Tự chấm** phải kèm bằng chứng: link PR/MR, ảnh pipeline xanh,
   file PDF biên dịch được. Ô nào không có bằng chứng tính mức **Chưa đạt**.

## 8. Ngưỡng Mục Tiêu 9+

- [ ] Không có tiêu chí nào ở mức **Chưa đạt** (điều kiện cần).
- [ ] Tiêu chí 1, 2, 3 mỗi tiêu chí ≥ 1.75 (3 mảng nội dung đều Xuất sắc).
- [ ] Tiêu chí 4 + 5 mỗi tiêu chí ≥ 1.25 (slide và báo cáo đều Xuất sắc).
- [ ] Tiêu chí 6 ≥ 0.9 (demo khô 2 lần không lỗi lệnh, mỗi người thuộc 5 câu phản biện).
- [ ] Tổng ≥ 9.0 mới được nộp; 8.0–8.9 sửa 1 ngày rồi chấm lại; dưới 8.0 họp nhóm
      phân việc bổ sung theo timeline tuần 2 trong `PhanCong_Nhom3TV.md`.
