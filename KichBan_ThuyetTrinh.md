# KỊCH BẢN THUYẾT TRÌNH CHI TIẾT (20–25 phút)

> Phân vai: TV1 = Lê Quang An (0024415453) · TV2 = Lê Tuấn Kiệt (0024417193) · TV3 = Đoàn Minh Trí (0024417136, trưởng nhóm + MC).

> Người nói chính ghi ở đầu mỗi đoạn. Câu chữ là lời nói gợi ý — thuộc ý, không cần thuộc lòng.
> Bấm giờ tổng duyệt 2 lần. Chuẩn bị sẵn: repo demo, tab Actions xanh, tab pipeline GitLab xanh,
> 1 terminal Git, 1 trình duyệt mở sẵn conflict `Web.config`.

## MỞ ĐẦU (TV3, 2 phút, slide 1–3)

- "Nhóm em có 3 thành viên, đề tài GIT – GitHub – GitLab gắn với học phần ASPX .NET 4.8.1.
  Vì sao cần Git cho môn này? Vì đồ án Web Forms có 3 người cùng sửa `*.aspx`, `*.aspx.cs`,
  `Web.config` — không có Git là đè code, mất bài, không biết ai sửa gì."
- Roadmap: "TV1 trình bày Git từ cơ bản đến internals. TV2 trình bày GitHub + CI build ASPX.
  Em trình bày GitLab + so sánh + quy trình nhóm. Cuối cùng là demo pipeline xanh và kết luận."

## PHẦN 1 — GIT (TV1, 7 phút, slide 4–25)

1. **Kiến trúc 3 vùng (1 phút):** chỉ hình Working → Staging → Repository.
   "Mọi lệnh Git chỉ xoay quanh 3 vùng này. `add` đưa vào Staging, `commit` chụp ảnh vào Repo."
2. **Luồng cơ bản (1 phút):** `config → init/clone → add/commit → log/diff`.
   Nhấn mạnh `.gitignore` cho ASP.NET: `bin/`, `obj/`, `packages/`, `.vs/` — "không commit rác build".
3. **Nhánh + merge (1 phút):** chỉ hình branch/merge. "Mỗi người 1 nhánh `feature/...`, xong merge
   về `develop`. Nhánh rẻ vì chỉ là con trỏ tới commit."
4. **DEMO LIVE (3 phút):**
   - `git status → add → commit → log --oneline --graph`
   - Tạo nhánh, sửa `Default.aspx`, merge, **cố tình gây conflict `Web.config` → giải quyết**,
     `git stash` + `git tag v1.0`.
5. **Nâng cao 30 giây:** "Muốn hiểu sâu: blob/tree/commit + SHA; `rebase -i`, `bisect`, hooks,
   LFS cho file lớn, ký commit GPG. Chi tiết ở Chương 3 báo cáo."

Câu chốt: "Nắm chắc Git local thì GitHub/GitLab chỉ là thêm server + quy trình review."

## PHẦN 2 — GITHUB (TV2, 7 phút, slide 26–45)

1. **Từ Git lên GitHub (1 phút):** "Git là công cụ, GitHub là nơi đặt repo + cộng tác:
   Issues, Pull Request, Actions, Security."
2. **PR + Review (2 phút):** mở PR mẫu trên màn hình.
   "Luồng chuẩn: push nhánh → mở PR → 1 người review → CI phải xanh → merge.
   Protected branch chặn push thẳng và chặn merge khi chưa review."
3. **DEMO Actions (3 phút):** mở tab Actions pipeline xanh.
   "Workflow `ci-aspx-481.yml` chạy trên `windows-latest`: restore NuGet → `msbuild` solution
   4.8.1 → chạy test → publish artifact. Vì .NET Framework 4.8.1 cần MSBuild + .NET Framework
   nên **không** build bằng `ubuntu + dotnet build`."
4. **Bảo mật 1 phút:** "Secret scanning chặn lộ connection string; Dependabot báo thư viện cũ;
   secret để trong Settings → Secrets, **không** hardcode `Web.config`." (TV3 sẽ demo ca lộ secret ở Q&A nếu bị hỏi.)

Câu chốt: "GitHub chuẩn hoá cộng tác bằng PR + review + CI bắt buộc xanh."

## PHẦN 3 — GITLAB + SO SÁNH + QUY TRÌNH NHÓM (TV3, 7 phút, slide 46–63)

1. **GitLab (2 phút):** "GitLab tích hợp sẵn DevOps: Groups/Projects, Issues/Boards,
   Merge Request + Approval rules, CI/CD, Registry, Environments."
2. **DEMO pipeline (2 phút):** mở pipeline GitLab xanh.
   "File `.gitlab-ci.yml`: stages `build → test → deploy`, job build chạy Windows runner
   gọi `msbuild`. Artifacts lưu gói publish; Environments trỏ về server IIS demo."
3. **So sánh (1.5 phút):** chỉ bảng 5 dòng quan trọng nhất:
   CI/CD (GitLab tích hợp sâu / GitHub Actions linh hoạt), self-host (GitLab mạnh),
   review (cả hai đều tốt), giá sinh viên (đều miễn phí đủ dùng), phù hợp ASPX (cả hai đều cần Windows runner).
4. **Quy trình nhóm (1.5 phút):** chỉ hình GitFlow rút gọn.
   "`main` (nộp bài, khoá) ← `develop` ← `feature/tvX-...`. Mọi merge qua PR/MR + 1 approve + CI xanh.
   Conflict `Web.config`: người merge pull `develop` mới nhất, giữ connection string mẫu,
   secret thật nằm trong Secret/CI variables."

## KẾT LUẬN (cả nhóm, 2 phút, slide 64–65)

- TV1: "Takeaway của em: hiểu 3 vùng + nhánh thì 90% lỗi Git tự xử được."
- TV2: "Takeaway của em: PR + CI xanh là lưới an toàn trước khi code vào nhánh chung."
- TV3: "Takeaway của nhóm: GitHub hay GitLab đều tốt — quan trọng là kỷ luật nhánh + review +
  không commit secret. Nhóm em đã áp dụng đúng quy trình này để làm chính bài báo cáo này:
  3 nhánh, review chéo, CI biên dịch LaTeX. Em xin hết và mời thầy/cô đặt câu hỏi."

## DỰ PHÒNG SỰ CỐ DEMO

- Mất mạng: dùng ảnh chụp pipeline xanh trong slide + repo local vẫn demo được Git.
- Actions/GitLab queue lâu: mở sẵn 1 lần chạy xanh cũ (permalink), không chạy mới trên sân khấu.
- Conflict demo fail: chuẩn bị sẵn 2 commit gây conflict cố định + lệnh `git merge --abort` để làm lại.
- Ai quên lời: người kế tiếp nói luôn phần mình, MC (TV3) lấp 1 câu nối.
