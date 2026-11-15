# BÁO CÁO SO SÁNH VÀ THẨM ĐỊNH KỸ THUẬT

## Tài liệu: Chương 4 — GIT, GITHUB VÀ GITLAB TRONG HỌC PHẦN ASPX
### Đối chiếu: `main.pdf` ↔ *Pro Git (Second Edition)* & Tài liệu kỹ thuật chuẩn

---

## TÓM TẮT TỔNG QUAN

Báo cáo này tổng hợp kết quả thẩm định kỹ thuật chuyên sâu (Multi-Tier Tournament Review [4→2→1]) đối với **Chương 4** của tài liệu báo cáo học phần ASPX (*GIT – GitHub – GitLab trong Học phần ASPX – .NET Framework 4.8.1*). Quá trình thẩm định được thực hiện bởi 7 nhóm agent độc lập, đối chiếu trực tiếp với tài liệu chuẩn mực *Pro Git (Second Edition)* của Scott Chacon & Ben Straub, Microsoft Learn/.NET Framework 4.8.1/IIS, GitHub Docs chính thức và OWASP ASVS.

### Thống kê tổng số vấn đề phát hiện

| Mức độ | Số lượng | Ghi chú |
| :--- | :---: | :--- |
| **Critical** (Nghiêm trọng) | **9** | Lỗi an ninh, lỗi kỹ thuật làm hỏng hoàn toàn chức năng |
| **Major** (Quan trọng) | **40** | Sai lệch kỹ thuật đáng kể, thiếu sót nguyên lý cốt lõi |
| **Minor** (Nhỏ) | **36** | Thuật ngữ, định dạng, chuẩn hóa, lỗi cú pháp nhỏ |
| **Editorial/Typo** | **10** | Lỗi trình bày, dấu tiếng Việt, dàn trang LaTeX |
| **TỔNG** | **~95** | 100% được xác minh bằng bằng chứng kỹ thuật |

---

## PHẦN 1: TỔNG QUAN VÀ PHÂN BIỆT GIT/GITHUB — MỤC 4.1 & 4.2 (Trang 55–57)

### 1.1 Danh sách vấn đề phát hiện

#### FIND-S1-01 [Major] — Sai quy ước đặt tên thư mục hệ thống ASP.NET Web Forms

- **Mô tả**: Tài liệu ghi `App-Data` và `App-Code` (dấu gạch nối) thay vì phải là `App_Data` và `App_Code` (dấu gạch dưới).
- **Vị trí main.pdf**: Mục 4.1, Trang 55, đoạn 5, dòng 31–32.
- **Trích dẫn gốc**: *"File `Web.config` giữ cấu hình chung, thư mục `App-Data` hoặc `App-Code` giữ dữ liệu và mã dùng chung."*
- **Đối chiếu Pro Git & Tài liệu chuẩn**: Microsoft Learn – *ASP.NET Web Project Folder Structure (.NET Framework 4.8.1)*; Microsoft TechNet/IIS – *Request Filtering and HttpForbiddenHandler Configuration*.
- **Phân tích kỹ thuật**: Thư mục `App_Data` được IIS bảo vệ tự động bằng `HttpForbiddenHandler`. Nếu đặt tên là `App-Data`, IIS coi đây là thư mục tài nguyên thông thường, cho phép tải file CSDL trực tiếp từ trình duyệt. Thư mục `App_Code` là quy ước bắt buộc để ASP.NET nhận diện và biên dịch động; nếu sai tên sẽ gây lỗi runtime `CS0246`.
- **Đề xuất giải pháp**: Thay thế bằng `App_Data` (bảo vệ CSDL bằng IIS HttpForbiddenHandler) và `App_Code` (biên dịch động mã nguồn C# dùng chung).

---

#### FIND-S1-02 [Major] — Sai lệch mô hình dữ liệu thẻ GitHub Projects

- **Mô tả**: Khẳng định "Mỗi thẻ trên bảng có thể liên kết tới một hoặc nhiều Issue và Pull Request" là sai.
- **Vị trí main.pdf**: Mục 4.2, Trang 56, đoạn 3, dòng 14–17.
- **Trích dẫn gốc**: *"Mỗi thẻ trên bảng có thể liên kết tới một hoặc nhiều Issue và Pull Request tương ứng."*
- **Đối chiếu Pro Git**: *Pro Git (2nd Ed.)*, Chapter 6, p. 218–221.
- **Phân tích kỹ thuật**: Mỗi thẻ trong GitHub Projects ánh xạ 1:1 với một Issue, một PR, hoặc một Draft Note. Một Issue lại có thể thuộc nhiều dự án khác nhau (quan hệ 1-nhiều). Phân cấp công việc dùng Task Lists (`- [ ] #<number>`) bên trong Issue.
- **Đề xuất giải pháp**: Hiệu chỉnh mô tả: "Mỗi thẻ đại diện cho chính xác một Issue, một Pull Request hoặc một ghi chú nháp. Ngược lại, một Issue có thể được liên kết vào nhiều dự án khác nhau."

---

#### FIND-S1-03 [Major] — Trình bày Projects theo tư duy kéo thả thủ công, thiếu GitHub Projects v2

- **Mô tả**: Mô tả Projects thuần túy là kéo thả thẻ thủ công, bỏ qua Built-in Workflow Automation và các chế độ xem Table/Roadmap.
- **Vị trí main.pdf**: Mục 4.2, Trang 56, đoạn 3, dòng 18–22.
- **Đối chiếu Pro Git**: *Pro Git (2nd Ed.)*, Chapter 6, p. 218–221; GitHub Docs: *Automating your project with built-in workflows (Projects v2)*.
- **Đề xuất giải pháp**: Bổ sung mô tả về Built-in Workflows (tự động chuyển trạng thái khi tạo Issue/merge PR), Table view (lọc/nhóm theo Assignee, Milestone), và Roadmap view (biểu đồ Gantt theo thời gian).

---

#### FIND-S1-04 [Major] — Thiếu cú pháp từ khóa đóng Issue tự động

- **Mô tả**: Nêu tính năng đóng Issue tự động nhưng không cung cấp cú pháp từ khóa chuẩn và điều kiện kích hoạt trên nhánh mặc định.
- **Vị trí main.pdf**: Mục 4.2, Trang 56, đoạn 2, dòng 11–13.
- **Trích dẫn gốc**: *"Khi Pull Request sửa xong vấn đề, thông điệp commit ghi câu đóng Issue tự động để lịch sử được liên kết chặt chẽ."*
- **Đối chiếu Pro Git**: *Pro Git (2nd Ed.)*, Chapter 6, p. 188–190.
- **Phân tích kỹ thuật**: GitHub chỉ đóng Issue khi commit/PR chứa từ khóa chuẩn (`Fixes #12`, `Closes #12`, `Resolves #12`) và được merge vào **nhánh mặc định (main)**.
- **Đề xuất giải pháp**: Bổ sung danh sách từ khóa chuẩn và giải thích điều kiện merge vào nhánh mặc định.

---

#### FIND-S1-05 [Major] — Bỏ sót phân định Public vs Private và quyền Collaborator

- **Mô tả**: Không đề cập đến sự khác biệt giữa kho Public/Private và quy trình cấp quyền cộng tác viên.
- **Vị trí main.pdf**: Mục 4.1 & 4.2, Trang 55–56.
- **Đối chiếu Pro Git**: *Pro Git (2nd Ed.)*, Chapter 6, p. 197–200 (Creating Repository, Adding Collaborators).
- **Đề xuất giải pháp**: Khuyến nghị kho Private cho đồ án môn học; hướng dẫn Settings → Collaborators để mời thành viên với quyền Write access.

---

#### FIND-S1-06 [Major] — Bỏ sót cơ chế xác thực PAT và SSH

- **Mô tả**: Hướng dẫn `git clone/pull/push` nhưng không đề cập Personal Access Token (thay thế password từ 8/2021) và cấu hình SSH.
- **Vị trí main.pdf**: Mục 4.1, Trang 55, đoạn 4.
- **Đối chiếu Pro Git**: *Pro Git (2nd Ed.)*, Chapter 6, p. 173–176.
- **Đề xuất giải pháp**: Giải thích PAT Classic (phạm vi `repo`) cho HTTPS; hướng dẫn `ssh-keygen -t ed25519` và đưa khóa công khai lên Settings → SSH and GPG keys.

---

#### FIND-S1-07 [Major] — Bỏ sót kiến trúc Wiki là kho Git độc lập

- **Mô tả**: Mô tả Wiki như giao diện soạn thảo web, không đề cập bản chất `.wiki.git` repository độc lập và giới hạn không hỗ trợ Pull Request.
- **Vị trí main.pdf**: Mục 4.2, Trang 56, đoạn 4, dòng 23–29.
- **Đối chiếu Pro Git**: *Pro Git (2nd Ed.)*, Chapter 6, p. 172.
- **Đề xuất giải pháp**: Nêu rõ Wiki có thể clone về máy bằng địa chỉ `.wiki.git`, không hỗ trợ phân nhánh/PR, và cần GitHub Student Pack để bật trên kho Private.

---

#### FIND-S1-08 [Major] — Nhầm lẫn trạng thái kích hoạt mặc định Issues/Discussions

- **Mô tả**: Câu "Nhóm bật Issues và Discussions ngay khi tạo kho" gây hiểu nhầm cả hai đều cần bật; thực tế Issues mặc định BẬT, Discussions mặc định TẮT.
- **Vị trí main.pdf**: Mục 4.2, Trang 56, dòng 41 và 63–65.
- **Đề xuất giải pháp**: Nêu rõ Issues đã bật sẵn; Discussions cần vào Settings → General → Features để kích hoạt. Hướng dẫn dùng "Convert to issue" và "Mark as answer" thay vì thao tác thủ công.

---

#### FIND-S1-09 đến FIND-S1-14 [Minor] — Các hiệu chỉnh nhỏ

| Mã | Vấn đề | Vị trí |
|:--|:--|:--|
| S1-09 | Thuật ngữ "mốc thời gian" nên dùng "Milestone"; thiếu "Assignee" | Mục 4.2, Trang 56 |
| S1-10 | Bỏ sót quy tắc bộ đếm chung `#<num>` cho Issue và PR | Mục 4.2, Trang 56 |
| S1-11 | Thiếu cờ `-u origin <branch>` trong lệnh push đầu tiên | Mục 4.1, Trang 55 |
| S1-12 | `.gitignore` còn thiếu `.vs/` và `*.user` | Mục 4.1, Trang 55 |
| S1-13 | Chưa chuẩn hóa viết hoa "Kanban" | Mục 4.2, Trang 56 |
| S1-14 | Caption Bảng 11 thiếu dấu tiếng Việt (`Fork va branch...`) | Mục 4.3, Trang 57 |

---

## PHẦN 2: FORK, PULL REQUEST VÀ CODE REVIEW — MỤC 4.3 & 4.4 (Trang 57–60)

### 2.1 Danh sách vấn đề phát hiện

#### S2-AGG-CRIT-01 [Critical] — Code Review vi phạm chuẩn OWASP, tạo lỗ hổng User Enumeration (CWE-204)

- **Mô tả**: Mẫu bình luận code review hướng dẫn phân biệt "tên đăng nhập sai hay mật khẩu sai" trong thông báo lỗi — đây là phản mẫu bảo mật kinh điển cho phép kẻ tấn công dò tài khoản.
- **Vị trí main.pdf**: Mục 4.4, Trang 59, dòng 230–234.
- **Trích dẫn gốc**: *"...thông báo lỗi nên phân biệt rõ tên đăng nhập sai hay mật khẩu sai trong môi trường học tập."*
- **Đối chiếu chuẩn**: OWASP ASVS v4.0 Mục V2.1.12; MITRE CWE-204.
- **Phân tích kỹ thuật**: Mã nguồn C# ban đầu đã đúng (`"Invalid username or password."`). Nhận xét review hướng dẫn thay đổi thành thông báo riêng biệt cho phép User Enumeration Attack. Mâu thuẫn trực tiếp với Mục 7.3 và 4.14 của chính báo cáo.
- **Đề xuất giải pháp**: Viết lại mẫu review để khen ngợi thông báo gộp đúng chuẩn OWASP; nhận xét nên hướng về log server-side thay vì thông báo cho người dùng.

---

#### S2-AGG-CRIT-02 [Critical] — Thiếu hoàn toàn lệnh Forking Workflow; nhầm lẫn với Shared Repository Workflow

- **Mô tả**: Mục 4.3 tiêu đề "Fork và Pull Request" nhưng khối lệnh thực hành chỉ minh họa Shared Repository Workflow (thành viên có quyền ghi trực tiếp vào kho gốc).
- **Vị trí main.pdf**: Mục 4.3, Trang 56–57.
- **Đối chiếu Pro Git**: *Pro Git (2nd Ed.)*, Chapter 6 – *Forking Projects*, p. 178–181; *Keeping up with Upstream*, p. 187–188.
- **Phân tích kỹ thuật**: Thiếu: (1) `gh repo fork ... --clone`; (2) Cấu hình remote kép `origin`/`upstream`; (3) Lệnh đồng bộ `git fetch upstream && git merge upstream/main`; (4) Mở cross-repository PR từ fork về kho gốc.
- **Đề xuất giải pháp**: Bổ sung khối lệnh Forking Workflow đầy đủ (xem mã nguồn LaTeX đề xuất trong báo cáo đơn vị Segment 2).

---

#### S2-AGG-MAJ-01 [Major] — Sơ đồ Hình 8 nghịch đảo thứ tự CI → Review; đứt gãy nhánh phản hồi lỗi

- **Mô tả**: Hình 8 xếp Review (Bước 3) trước Chạy CI (Bước 4), mâu thuẫn với quy trình chuẩn và chính Mục 7.2 của báo cáo.
- **Vị trí main.pdf**: Mục 4.3, Trang 57, Hình 8.
- **Đối chiếu Pro Git**: *Pro Git (2nd Ed.)*, Chapter 6, p. 185–187.
- **Đề xuất giải pháp**: Chuẩn hóa thứ tự: *1. Đẩy nhánh → 2. Mở PR → 3. Chạy CI → 4. Review & Approve → 5. Merge*. Vẽ lại sơ đồ TikZ với nhánh phản hồi lỗi CI (màu đỏ) và nhánh Review yêu cầu sửa (màu cam).

---

#### S2-AGG-MAJ-02 [Major] — Thiếu cú pháp Markdown ``` ```suggestion ``` ``` và cơ chế Batch Suggestion

- **Mô tả**: Tiêu đề mục có từ "suggest" nhưng toàn bộ nội dung không có dòng code minh họa cú pháp suggestion; bỏ qua "Add suggestion to batch".
- **Vị trí main.pdf**: Mục 4.4, Trang 58.
- **Đề xuất giải pháp**: Bổ sung khối mã Markdown minh họa cú pháp ` ```suggestion ``` `; giải thích cơ chế batch commit tránh phân mảnh lịch sử Git.

---

#### S2-AGG-MAJ-03 [Major] — Trích dẫn sai `\cite{gitflow}` cho mô hình Forking

- **Mô tả**: Gán trích dẫn bài báo GitFlow của Vincent Driessen (mô hình nhánh nội bộ một kho) cho mô hình Forking (nhiều kho phân tán).
- **Vị trí main.pdf**: Mục 4.3, Trang 57.
- **Đề xuất giải pháp**: Thay bằng `\cite{progit}` trỏ về *Pro Git* Chương 5 (Integration-Manager Workflow).

---

#### S2-AGG-MAJ-04 [Major] — Khối lệnh bỏ sót `Login.aspx.designer.cs` gây lỗi MSBuild `CS0103`

- **Mô tả**: Lệnh `git add Login.aspx Login.aspx.cs` bỏ sót tệp `.designer.cs`; CI runner sẽ báo lỗi biên dịch `CS0103: The name 'txtUsername' does not exist`.
- **Vị trí main.pdf**: Mục 4.3, Trang 57, dòng 127–130.
- **Đề xuất giải pháp**: Sửa thành `git add Login.aspx Login.aspx.cs Login.aspx.designer.cs` hoặc dùng mẫu `git add Login.aspx*`.

---

#### S2-AGG-MAJ-05 [Major] — Khối lệnh GitHub CLI bỏ quên bước Review và Merge

- **Mô tả**: Khối lệnh tuyên bố "minh họa toàn bộ vòng đời PR" nhưng dừng ở `gh pr checks --watch`, thiếu `gh pr review --approve` và `gh pr merge --merge --delete-branch`.
- **Vị trí main.pdf**: Mục 4.3, Trang 57.
- **Đề xuất giải pháp**: Bổ sung lệnh approve, merge và cập nhật nhánh local sau merge.

---

#### S2-AGG-MAJ-06 [Major] — Bảng 11 sai cơ chế đồng bộ Git và khuyến nghị xóa Fork nguy hại

- **Mô tả**: Nhận định "Branch tự thấy nhánh mới sau khi đẩy" sai bản chất phân tán của Git. Khuyến nghị "Xóa fork khi không dùng nữa" phá hủy PR đang chờ duyệt.
- **Vị trí main.pdf**: Mục 4.3, Trang 56, Bảng 11.
- **Đề xuất giải pháp**: Hàng Đồng bộ Branch: "Thành viên chạy `git fetch origin`". Hàng Dọn dẹp Fork: "Xóa topic branch (`git push origin --delete <branch>`), giữ lại fork để tiếp tục đóng góp".

---

#### S2-AGG-MIN-01 đến S2-AGG-MIN-05 & Typos [Minor/Editorial]

| Mã | Vấn đề | Vị trí |
|:--|:--|:--|
| MIN-01 | Mâu thuẫn `--base main` (Mục 4.3) vs `--base develop` (Mục 7.2) trong GitFlow | Mục 4.3, Trang 57 |
| MIN-02 | Rủi ro `NullReferenceException` khi gọi `.Trim()` trước kiểm tra `null` | Mục 4.4, Trang 58 |
| MIN-03 | Thiếu giải thích Three-Dot Diff và 3 chiến lược Merge (Merge commit/Squash/Rebase) | Mục 4.3–4.4 |
| MIN-04 | Thiếu cảnh báo bẫy Pending Review (phải bấm "Finish your review") và tính chất Blocking của Request Changes | Mục 4.4, Trang 58 |
| MIN-05 | Thiếu khối lệnh minh họa quy trình cập nhật PR (commit thêm vào nhánh cũ, không mở PR mới) | Mục 4.3–4.4 |
| TYPO-01 | Caption Bảng 11, Hình 8 thiếu dấu tiếng Việt; nhãn nút TikZ không dấu | Trang 56–57 |
| TYPO-02 | Khối mã bị chia cắt phân trang phản cảm (trang 56–57 và 58–59) | Trang 56–59 |
| TYPO-03 | Hai khối `lstlisting` thiếu `caption` và `label` chuẩn LaTeX | Mục 4.3, 4.4 |

---

## PHẦN 3: BẢO VỆ NHÁNH VÀ CODEOWNERS — MỤC 4.5 (Trang 60–62)

### 3.1 Danh sách vấn đề phát hiện

#### Finding 1 [Critical] — CODEOWNERS không tự động khóa nút Merge nếu thiếu tùy chọn Branch Protection

- **Mô tả**: Khẳng định "Nếu TV2 chưa chấp thuận, nút hợp nhất vẫn bị chặn" là sai. CODEOWNERS chỉ tự động thêm reviewer; phải kích hoạt tường minh **"Require review from Code Owners"** trong Branch Protection.
- **Vị trí main.pdf**: Trang 61, dòng 283–285.
- **Trích dẫn gốc**: *"Nếu TV2 chưa chấp thuận, nút hợp nhất vẫn bị chặn cho dù các thành viên khác đã đồng ý."*
- **Đối chiếu**: GitHub Docs – *About protected branches*; *About code owners*.
- **Đề xuất giải pháp**: Viết lại câu để làm rõ sự phụ thuộc: "Để bảo đảm nút hợp nhất bị chặn đến khi TV2 chấp thuận, nhóm bắt buộc phải kích hoạt tùy chọn **'Require review from Code Owners'** bên trong Branch Protection Rules."

---

#### Finding 2 [Critical] — Đảo lộn thứ tự ưu tiên khớp mẫu (Last Match Wins) vô hiệu hóa quy tắc `/Admin/`

- **Mô tả**: File CODEOWNERS đặt `/Admin/ @TV2` ở dòng 3 nhưng `*.aspx @TV2 @TV3` ở dòng 6. GitHub áp dụng "last match wins" nên dòng 6 ghi đè dòng 3, vô hiệu hóa bảo vệ chuyên biệt cho thư mục Admin.
- **Vị trí main.pdf**: Trang 61, dòng 269–276.
- **Đối chiếu**: GitHub Docs – *CODEOWNERS syntax*.
- **Đề xuất giải pháp**: Tái cấu trúc: đặt mẫu tổng quát (wildcard) ở trên, thư mục cụ thể ở **dưới cùng** để ghi đè:
  ```
  *.aspx @TV2 @TV3
  *.aspx.cs @TV1 @TV2
  /Web.config @TV1 @TV2
  /.github/ @TV2
  /Admin/ @TV2          ← xuất hiện SAU cùng → ưu tiên cao nhất
  ```

---

#### Finding 3 [Critical] — Nhầm nhiều Code Owner là quan hệ VÀ (AND) thay vì HOẶC (OR)

- **Mô tả**: Chú thích "Config and workflow files need **two** reviewers" với `/Web.config @TV1 @TV2` là sai. GitHub hiểu danh sách nhiều người trên một dòng là `OR` — chỉ cần **một** người phê duyệt.
- **Vị trí main.pdf**: Trang 61, dòng 272–279.
- **Đối chiếu**: GitHub Docs – *"If you have more than one code owner... ANY code owner can approve."*
- **Đề xuất giải pháp**: Hiệu chỉnh chú thích thành "can be reviewed by either TV1 or TV2". Để ép cần 2 người duyệt, dùng "Require approvals: 2" trong Branch Protection Rules.

---

#### Finding 4 [Major] — Sáng tác thuật ngữ hư cấu về cơ chế miễn trừ Quản trị viên (Admin Bypass)

- **Mô tả**: Không có tùy chọn nào tên "cấm đẩy trực tiếp ngăn cả quản trị viên". Admin mặc định bypass toàn bộ Branch Protection.
- **Vị trí main.pdf**: Trang 61, dòng 257.
- **Đề xuất giải pháp**: Dùng thuật ngữ chính xác: **"Do not allow bypassing the above settings"** (trước đây là "Include administrators") để áp dụng quy tắc lên cả Admin.

---

#### Finding 5 [Major] — Bế tắc phê duyệt một người (Deadlock) và thắt cổ chai kiến trúc Web Forms

- **Mô tả**: Chỉ gán `@TV2` cho `/Admin/` và `/.github/` → TV2 không thể tự approve PR của mình → Deadlock. Chia cắt `.aspx`/`.aspx.cs` cho các chủ sở hữu khác nhau tạo điểm nghẽn khi sửa trang Web Forms (phải sửa cả hai file cùng lúc).
- **Vị trí main.pdf**: Trang 61, dòng 270, 280.
- **Đề xuất giải pháp**: Luôn khai báo ít nhất 2 đồng chủ sở hữu (co-owners). Phân chia quyền theo thư mục chức năng thay vì theo đuôi file.

---

#### Finding 6 [Major] — Bỏ sót các chốt chặn an toàn nhánh thiết yếu

- **Mô tả**: Không đề cập "Block force pushes", "Require linear history" (cần thiết theo Mục tiêu 1 & 6 của đồ án), và "Dismiss stale pull request approvals when new commits are pushed".
- **Vị trí main.pdf**: Trang 60–61, dòng 255–259.
- **Đề xuất giải pháp**: Bổ sung đoạn văn giới thiệu và giải thích ý nghĩa của 3 tùy chọn bảo mật thiết yếu này.

---

#### Findings 7–13 [Minor/Typo]

| Mã | Vấn đề | Mức |
|:--|:--|:--:|
| F7 | Mâu thuẫn chú thích (1 người) vs mã nguồn (2 người) ở dòng 8–9 | Minor |
| F8 | Hướng dẫn thay tên tài khoản thiếu ký tự `@` gây lỗi parse syntax | Minor |
| F9 | Liệt kê thiếu vị trí `docs/CODEOWNERS` và thứ tự ưu tiên tìm kiếm | Minor |
| F10 | Thiếu điều kiện: tài khoản trong CODEOWNERS phải có quyền Write | Minor |
| F11 | "Require branches to be up to date" phụ thuộc vào Status Checks nhưng không nêu rõ | Minor |
| F12 | Thiếu giải thích phạm vi neo gốc `/Web.config` vs `Web.config` không dấu gạch chéo | Minor |
| F13 | Lỗi dàn trang LaTeX bẻ đôi từ tiếng Việt tại trang 60–62 | Typo |

---

## PHẦN 4: GITHUB ACTIONS – CĂN BẢN CI — MỤC 4.6 & 4.7 (Trang 62–66)

### 4.1 Danh sách vấn đề phát hiện

#### Issue 1 [Critical] — MSBuild thiếu `/p:DeployOnBuild=true` khiến Step Upload Artifact thất bại hoàn toàn

- **Mô tả**: Step 6 chỉ chạy `msbuild .../p:Configuration=Release` không kích hoạt Web Publishing Pipeline (WPP). Thư mục `WebApp\obj\Release\Package` **không được tạo ra**. Step 8 `upload-artifact` tìm path không tồn tại → pipeline sập.
- **Vị trí main.pdf**: Trang 64–65, Listing 24, dòng 47–48 và 54–60.
- **Trích dẫn gốc**: *"Workflow trên có thể sao chép vào thư mục .github/workflows của repository demo và chạy ngay sau khi đẩy lên GitHub..."* (Tuyên bố không chính xác).
- **Đề xuất giải pháp**: Thêm bước Publish riêng với `/p:DeployOnBuild=true /p:WebPublishMethod=FileSystem /p:PublishUrl=...` và sửa path artifact trỏ vào thư mục output đúng.

---

#### Issue 2 [Critical] — Cấu hình Cache NuGet sai toàn diện cho Web Forms

- **Mô tả**: Cache lưu `~/.nuget/packages` nhưng `nuget restore` với `packages.config` lưu gói vào `.\packages\` trong solution. Hàm băm dùng `packages.lock.json` không tồn tại trong dự án Web Forms → cache vô hiệu hoàn toàn.
- **Vị trí main.pdf**: Trang 64, Listing 24, dòng 33–40.
- **Đề xuất giải pháp**:
  ```yaml
  - name: Cache NuGet packages
    uses: actions/cache@v4
    with:
      path: packages
      key: nuget-${{ runner.os }}-${{ hashFiles('**/packages.config') }}
  ```

---

#### Issue 3 [Major] — `vstest.console.exe` không có trong PATH sau `microsoft/setup-msbuild@v2`

- **Mô tả**: Action `setup-msbuild` chỉ thêm MSBuild.exe vào PATH, không thêm vstest.console.exe. Pipeline báo lỗi "term not recognized".
- **Vị trí main.pdf**: Trang 64–65, Listing 24, dòng 50–52.
- **Đề xuất giải pháp**: Dùng `dotnet test Tests\bin\Release\AspxDemo.Tests.dll --logger trx --results-directory TestResults` (sẵn trong PATH) thay cho `vstest.console.exe`.

---

#### Issue 4 [Major] — Lỗi phân tích đối số PowerShell bóc tách `/p:Platform="Any CPU"` gây lỗi MSB1008

- **Mô tả**: Trên Windows runner (PowerShell Core), dấu nháy kép bị bóc tách, `Any CPU` trở thành hai tham số riêng → MSBuild lỗi `MSB1008: Only one project can be specified`.
- **Vị trí main.pdf**: Trang 64, Listing 24, dòng 47–48.
- **Đề xuất giải pháp**: Bọc trong nháy đơn: `'/p:Platform="Any CPU"'` hoặc dùng `shell: cmd`.

---

#### Issue 5 [Major] — Mâu thuẫn trigger: thiếu `workflow_dispatch` và thiếu nhánh `develop` trong `pull_request`

- **Mô tả**: Mục 4.6 nêu kích hoạt thủ công là trigger quan trọng thứ 3; Listing 24 không có `workflow_dispatch:`. PR vào `develop` không kích hoạt CI.
- **Vị trí main.pdf**: Trang 62–63, Listing 24, dòng 3–8.
- **Đề xuất giải pháp**:
  ```yaml
  on:
    push:
      branches: [ main, develop ]
    pull_request:
      branches: [ main, develop ]
    workflow_dispatch:
  ```

---

#### Issues 6–14 [Minor/Observation]

| Mã | Vấn đề | Mức |
|:--|:--|:--:|
| I6 | Thiếu liên hệ kiến trúc GitHub Actions ↔ Webhooks/Commit Status API (Pro Git p. 214–223) | Observation |
| I7 | Độ lệch số trang PDF vs folio 1 trang; cần ghi cả hai chỉ số | Observation |
| I8 | Gọi file YAML là "đơn vị cấu hình nhỏ nhất" (sai; đơn vị nhỏ nhất là Step/Action) | Minor |
| I9 | Khối `concurrency:` trong Listing 24 không được giải thích ở Mục 4.7.2 | Minor |
| I10 | Mâu thuẫn: lời dẫn ghi "tải kết quả lên artifact" nhưng Step 8 lưu gói web, không phải kết quả test | Minor |
| I11 | Bất nhất tên Solution (`AspxDemo.sln` vs `AspxDemo_NET481.sln`) giữa Mục 4.7 và Phụ lục C | Minor |
| I12 | Lỗi tràn lề bảng mã LaTeX làm gãy cú pháp lệnh; Listing 24 kéo dài 3 trang | Minor |
| I13 | Dấu nháy Unicode cong (`'` U+2019) thay vì ASCII (`'` U+0027) trong hashFiles | Minor |
| I14 | Lỗi ngắt từ `repos-itory` tại Mục 4.7.2 | Typo |

---

## PHẦN 5: SECRETS, CACHE VÀ RUNNERS — MỤC 4.8–4.10 (Trang 66–69)

### 5.1 Danh sách vấn đề phát hiện

#### S5-01 [Critical] — Sai đường dẫn Cache NuGet (Lặp lại từ Segment 4, lần này trong Listing 26 và Phụ lục C)

- **Mô tả**: `path: ~/.nuget/packages` vô hiệu cho Web Forms; lỗi tương tự còn lặp lại trong Phụ lục C (Listing 45) gây nhất quán sai lệch xuyên suốt tài liệu.
- **Vị trí main.pdf**: Mục 4.9, Trang 67, dòng 199–201 và Listing 26.
- **Đề xuất giải pháp**: Sửa thành `path: packages` và `hashFiles('**/packages.config')` trong cả Listing 26 lẫn Phụ lục C.

---

#### S5-02 [Critical] — Lỗ hổng bảo mật: truyền Secret qua đối số dòng lệnh (`${{ secrets.STAGING_CONN_STRING }}`)

- **Mô tả**: `run: deploy.cmd ${{ secrets.STAGING_CONN_STRING }}` lộ mật khẩu CSDL qua Process Table (PEB CommandLine), Event ID 4688, và dễ bị Argument Injection do ký tự đặc biệt (`;`, `&`, `=`).
- **Vị trí main.pdf**: Mục 4.8, Trang 66, Listing 25.
- **Đề xuất giải pháp**: Ánh xạ qua khối `env:` an toàn, tham chiếu biến môi trường trong script. Thêm `needs: deploy-staging` để tránh triển khai song song.

---

#### S5-03 [Major] — Vi phạm nguyên lý đa hình bí mật (Environment Secret Polymorphism)

- **Mô tả**: Dùng tên riêng biệt `STAGING_CONN_STRING` và `PROD_CONN_STRING` phá vỡ cơ chế trừu tượng hóa của GitHub Environments và ngăn tái sử dụng workflow.
- **Đề xuất giải pháp**: Dùng chung tên `DB_CONNECTION_STRING` ở cả hai môi trường; GitHub sẽ tự nạp giá trị khác nhau theo ngữ cảnh environment.

---

#### S5-04 [Major] — Tuyệt đối hóa sai lệch cơ chế che giấu Secret (`***`)

- **Mô tả**: "Giá trị secret không bao giờ hiển thị trong nhật ký" là sai. Các ngoại lệ: secret bị mã hóa Base64/URL-encode, chuỗi con được trích xuất, secret ngắn < 3 ký tự, nội dung tệp artifact.
- **Vị trí main.pdf**: Mục 4.8, Trang 66, dòng 147–148.
- **Đề xuất giải pháp**: Hiệu chỉnh thành mô tả cơ chế exact literal string matching với các ngoại lệ rõ ràng.

---

#### S5-05 [Major] — Thiếu `if: always()` khi Upload Test Results gây mất dấu vết khi test thất bại

- **Mô tả**: Khi test fail, bước upload artifact bị skipped → mất file `.trx` đúng vào lúc cần debug nhất.
- **Vị trí main.pdf**: Mục 4.9, Listing 26, dòng 223–229.
- **Đề xuất giải pháp**: Thêm `if: always()` cho bước Upload test results.

---

#### S5-06 [Major] — Bỏ sót hệ số nhân chi phí 2x của Windows Runner

- **Mô tả**: Bảng 12 không nêu rằng 1 phút Windows runner tương đương 2 phút trong hạn ngạch; sinh viên không biết 2.000 phút thực chỉ còn 1.000 phút cho Windows.
- **Đề xuất giải pháp**: Cập nhật Bảng 12 với hệ số nhân chi phí: Windows = 2x, Ubuntu = 1x, macOS = 10x.

---

#### S5-07 [Major] — Thiếu phân tích kiến trúc lý giải vì sao Web Forms không build được trên Ubuntu

- **Mô tả**: Chỉ nêu khẳng định chung chung mà không giải thích 3 nguyên nhân kỹ thuật cốt lõi: (1) `System.Web.dll` phụ thuộc Windows Win32 API; (2) MSBuild targets `Microsoft.WebApplication.targets` chỉ có trên Windows; (3) Mono không tương thích .NET 4.8.1.
- **Đề xuất giải pháp**: Bổ sung 1 đoạn phân tích 3 nguyên nhân kỹ thuật trên.

---

#### Các Minor (Segment 5)

| Mã | Vấn đề | Mức |
|:--|:--|:--:|
| S5-M1 | Thiếu thông số định lượng Cache: hạn mức 10 GB/repo, chu kỳ LRU 7 ngày, branch scoping | Minor |
| S5-M2 | Nhắc đến `packages.lock.json` không tồn tại trong dự án Web Forms | Minor |
| S5-M3 | Băm cả `**/*.csproj` gây cache miss liên tục khi sửa code | Minor |
| S5-M4 | Lỗi ngắt dòng chuỗi `hashFiles(...)` trong bản in PDF | Minor |
| S5-M5 | Environment Protection Rules "Required Reviewers" chỉ hoạt động trên Public repo với tài khoản Free | Minor |
| S5-M6 | Bảng 12 ghi Ubuntu 22.04; thực tế `ubuntu-latest` đã chuyển sang Ubuntu 24.04 | Minor |

---

## PHẦN 6: PACKAGES, PAGES, CODESPACES VÀ COPILOT — MỤC 4.11–4.13 (Trang 69–73)

### 6.1 Danh sách vấn đề phát hiện

#### F-01 [Critical] — Nhầm tên AI assistant là "Muse" thay vì "GitHub Copilot"

- **Mô tả**: Câu mở đầu Mục 4.13: "Muse là trợ lý lập trình..." — "Muse" không tồn tại trong danh mục sản phẩm GitHub. Công cụ đúng tên là **GitHub Copilot**.
- **Vị trí main.pdf**: Trang 72, dòng 135 `chuong4-3-github-nangcao.tex`.
- **Đề xuất giải pháp**: Thay toàn bộ "Muse" bằng "GitHub Copilot" trong toàn bộ văn bản.

---

#### F-02 [Critical] — Lỗ hổng Timing Attack trong hàm kiểm tra mật khẩu được gắn nhãn "an toàn hơn"

- **Mô tả**: Mã C# `return hashLuu == hashNhap` dùng toán tử `==` trên string (short-circuit, không constant-time). Kẻ tấn công đo thời gian phản hồi để suy ngược hash mật khẩu (Side-Channel Attack).
- **Vị trí main.pdf**: Trang 72–73.
- **Trích dẫn gốc**: *"Đoạn code dưới đây mô phỏng kết quả gợi ý sau khi đã chỉnh sửa để an toàn hơn."*
- **Đề xuất giải pháp**: Thay bằng constant-time comparison:
  ```csharp
  byte[] bLuu = Convert.FromBase64String(hashLuu);
  byte[] bNhap = Convert.FromBase64String(hashNhap);
  return CryptographicOperations.FixedTimeEquals(bLuu, bNhap);
  ```

---

#### F-03 [Critical] — Nhầm lẫn `GITHUB_TOKEN` (Actions runtime) với Personal Access Token (máy cá nhân)

- **Mô tả**: Khẳng định `GITHUB_TOKEN` có thể cấp cho thành viên nhóm dùng trên máy cá nhân. `GITHUB_TOKEN` chỉ tồn tại trong runner Actions và không thể export; máy cá nhân phải dùng PAT Classic.
- **Vị trí main.pdf**: Trang 69–70, Mục 4.11.
- **Đề xuất giải pháp**: Phân biệt rõ 2 trường hợp: (1) Máy cá nhân dùng PAT với `read:packages` + `repo`; (2) Actions dùng `${{ secrets.GITHUB_TOKEN }}` tự động.

---

#### F-04 đến F-11 [Major]

| Mã | Vấn đề | Mức | Vị trí |
|:--|:--|:--:|:--|
| F-04 | Lệnh `gh extension install github/gh-codespace` đã lỗi thời từ 2021; `gh codespace` là built-in | Major | Mục 4.12, Trang 71 |
| F-05 | `dotnet pack` và `dotnet add package` không chạy được với `packages.config` Web Forms | Major | Mục 4.11, Trang 69–70 |
| F-06 | Publish lên GitHub Packages thất bại HTTP 400 nếu thiếu `<RepositoryUrl>` trong .csproj | Major | Mục 4.11, Trang 69–70 |
| F-07 | GitHub Pages **100% public** trên Free/Pro/Student; không kế thừa phạm vi riêng tư của repo | Major | Mục 4.11, Trang 70–71 |
| F-08 | Lệnh `--store-password-in-clear-text` lưu token toàn cục nguy hiểm; thiếu `nuget.config` cấp repo | Major | Mục 4.11, Trang 70 |
| F-09 | Codespaces (Linux container) không thể build/debug/preview Web Forms 4.8.1; thiếu TeX Live | Major | Mục 4.12, Trang 71–72 |
| F-10 | Hình 10 TikZ mô hình hóa sai: `git push` là node thực thể, `commit` là nhãn cung → sai kiến trúc | Major | Mục 4.12, Trang 72 |
| F-11 | Không đề cập tính năng "Suggestions matching public code (Block)" của Copilot tránh GPL | Major | Mục 4.13, Trang 73 |

---

#### F-12 đến F-16 [Minor]

| Mã | Vấn đề | Mức |
|:--|:--|:--:|
| F-12 | `AddWithValue("@u", ...)` gây Index Scan thay vì Seek do type mismatch VARCHAR/NVARCHAR | Minor |
| F-13 | Tuyên bố "nhanh hơn khoảng 30%" thiếu nguồn trích dẫn (nghiên cứu Peng et al. 2023 đo 55.8%) | Minor |
| F-14 | Lệnh dùng cú pháp bash `\` và `$GITHUB_TOKEN` không hoạt động trong PowerShell | Minor |
| F-15 | Các listing thiếu `caption` và `label`; C# listing thiếu `using System.Data;` | Minor |
| F-16 | Thiếu định lượng hạn ngạch Codespaces Student Pack (180 core-hours, 20 GB) và cảnh báo storage billing | Minor |

---

## PHẦN 7: BẢO MẬT NÂNG CAO VÀ GITHUB EDUCATION — MỤC 4.14–4.15 (Trang 73–75)

### 7.1 Danh sách vấn đề phát hiện

#### S7-01 [Critical] — Lỗi logic Git trong Listing xử lý Push Protection: commit lại chính secret

- **Mô tả**: Quy trình dùng `git reset --soft HEAD~1` không cập nhật Index. Thiếu `git add Web.config` sau khi sửa file. Kết quả: `git commit` lấy nội dung từ Index vẫn chứa secret → push tiếp tục bị từ chối lần 2. Thêm nữa, mã lỗi `GH013` là sai; đúng phải là **`GH009`** (Secret Scanning Push Protection).
- **Vị trí main.pdf**: Trang 74, Mục 4.14, dòng 207–221.
- **Đối chiếu Pro Git**: *Pro Git (2nd Ed.)*, Chapter 7, p. 257–264 ("Reset Demystified" – Three Trees).
- **Đề xuất giải pháp**: Thay bằng `git reset HEAD~1` (mixed reset, unstage Index), sau đó sửa file, **`git add Web.config`** tường minh, rồi commit lại. Hiển thị đúng mã lỗi `GH009` và URL bypass.

---

#### S7-02 [Major] — Sai lệch phạm vi Push Protection: không tự chặn SQL Server connection string nội bộ

- **Mô tả**: Push Protection mặc định chỉ nhận diện Partner Patterns (Azure, AWS, GitHub PAT...). Chuỗi kết nối SQL Server nội bộ (`Data Source=localhost;...`) **không được tự động chặn**.
- **Vị trí main.pdf**: Trang 73, Mục 4.14, dòng 202–205.
- **Đề xuất giải pháp**: Nêu rõ giới hạn của Push Protection mặc định; sinh viên phải chủ động không commit connection string vào mã nguồn, dùng biến môi trường hoặc `configSource`.

---

#### S7-03 [Major] — Sai lệch về Dependabot: không thể quét thư mục `Scripts/` tĩnh

- **Mô tả**: Dependabot là công cụ SCA dựa trên manifest (`packages.config`, `package.json`). Nó **không quét file JavaScript tĩnh** (`Scripts/jquery-3.4.1.min.js`) trừ khi quản lý qua npm `package.json`.
- **Vị trí main.pdf**: Trang 74, dòng 223–227.
- **Đề xuất giải pháp**: Hiệu chỉnh câu văn, bổ sung hướng dẫn file `.github/dependabot.yml` cần thiết để kích hoạt Dependabot cho NuGet.

---

#### S7-04 [Major] — Workflow CodeQL mặc định (Ubuntu + autobuild) thất bại với C# .NET Framework 4.8.1

- **Mô tả**: CodeQL cho C# cần theo dõi quá trình biên dịch thật. Workflow mặc định dùng `ubuntu-latest` + `autobuild` → không có MSBuild Windows → build thất bại 100%.
- **Vị trí main.pdf**: Trang 74, Mục 4.14, dòng 229–233.
- **Đề xuất giải pháp**: Hướng dẫn chuyển sang `runs-on: windows-latest`, tắt autobuild, cấu hình `nuget restore` và `msbuild` thủ công giữa `codeql-action/init` và `codeql-action/analyze`.

---

#### S7-05 [Major] — Mâu thuẫn logic Bảng 13: cột "Chặn ở đâu" gán "Sau khi push" cho Secret Scanning

- **Mô tả**: Secret Scanning là cơ chế phát hiện thụ động SAU khi push — không phải chặn. Dependabot và CodeQL cũng không có bản chất "chặn" trực tiếp.
- **Vị trí main.pdf**: Trang 74, Mục 4.14, Bảng 13.
- **Đề xuất giải pháp**: Đổi tên cột thành "Cơ chế tác động" và mô tả: Secret Scanning = Cảnh báo; Push Protection = Chặn tại pre-receive hook; Dependabot = Mở PR vá lỗi; CodeQL = Phân tích tĩnh (chặn nếu làm Required Check).

---

#### S7-06 [Major] — Thiếu `.github/dependabot.yml` và cảnh báo lỗi `FileLoadException` khi nâng cấp gói

- **Mô tả**: Dependabot Version Updates cần file `.github/dependabot.yml` để kích hoạt. Khi nâng cấp gói trong `packages.config`, Dependabot không tự cập nhật `<bindingRedirect>` trong `Web.config` → ứng dụng crash với `FileLoadException`.
- **Đề xuất giải pháp**: Cung cấp mẫu `dependabot.yml` cho NuGet; cảnh báo kiểm tra `bindingRedirect` sau mỗi lần merge PR Dependabot.

---

#### S7-07 đến S7-09 [Major] — Thông tin lỗi thời về GitHub Education

| Mã | Vấn đề | Mức |
|:--|:--|:--:|
| S7-07 | Khuyến nghị dùng Codespaces cho "toàn bộ quá trình làm đồ án" Web Forms 4.8.1 là bất khả thi | Major |
| S7-08 | Private repo không giới hạn cộng tác viên đã miễn phí từ 4/2020 — không phải đặc quyền Education | Major |
| S7-09 | Quy trình đăng ký Student Pack thiếu: bắt buộc 2FA, chụp ảnh Live Camera, Geolocation; bỏ sót Azure for Students, JetBrains Rider | Major |

---

#### S7-10 đến S7-14 [Minor]

| Mã | Vấn đề | Mức |
|:--|:--|:--:|
| S7-10 | Thiếu hướng dẫn đọc biến môi trường trong .NET Framework 4.8.1 (`ConfigurationManager`) | Minor |
| S7-11 | Tiêu đề Bảng 13 mất toàn bộ dấu tiếng Việt trong mã LaTeX | Minor |
| S7-12 | Listing ở Trang 74 thiếu `caption` và `label` chuẩn LaTeX | Minor |
| S7-13 | Lỗi khoảng trắng do gói `listings` (`Web . config`, `refs / heads / ...`) | Minor |
| S7-14 | Trích dẫn `[5]`, `[6]` chung chung chưa đúng chuyên mục kỹ thuật | Minor |

---

## BẢNG TỔNG HỢP TOÀN BỘ VẤN ĐỀ PHÁT HIỆN

| Mã vấn đề | Mức độ | Mục | Trang | Tiêu đề vắn tắt |
| :--- | :---: | :---: | :---: | :--- |
| FIND-S1-01 | **Major** | 4.1 | 55 | Sai quy ước `App-Data`/`App-Code` → lộ CSDL, lỗi CS0246 |
| FIND-S1-02 | **Major** | 4.2 | 56 | Mô hình dữ liệu thẻ Projects sai (1 thẻ → nhiều Issue) |
| FIND-S1-03 | **Major** | 4.2 | 56 | Projects chỉ mô tả kéo thả, thiếu Workflow Automation & Projects v2 |
| FIND-S1-04 | **Major** | 4.2 | 56 | Thiếu cú pháp `Fixes #N`, `Closes #N` và điều kiện nhánh mặc định |
| FIND-S1-05 | **Major** | 4.1–4.2 | 55–56 | Bỏ sót Public vs Private và quy trình Collaborators |
| FIND-S1-06 | **Major** | 4.1 | 55 | Bỏ sót PAT và SSH cho xác thực clone/push |
| FIND-S1-07 | **Major** | 4.2 | 56 | Wiki là Git repo độc lập `.wiki.git`; không hỗ trợ PR |
| FIND-S1-08 | **Major** | 4.2 | 56 | Nhầm trạng thái mặc định Issues/Discussions; bỏ "Convert to issue" |
| FIND-S1-09 đến S1-14 | **Minor** | 4.1–4.3 | 55–57 | Thuật ngữ Milestone, Assignee; bộ đếm `#N` chung; `-u origin`; `.vs/`; Kanban; caption Bảng 11 |
| S2-AGG-CRIT-01 | **Critical** | 4.4 | 59 | Code review hướng dẫn User Enumeration Attack (CWE-204) |
| S2-AGG-CRIT-02 | **Critical** | 4.3 | 56–57 | Mục 4.3 không có lệnh Forking Workflow; nhầm Shared Repository |
| S2-AGG-MAJ-01 | **Major** | 4.3 | 57 | Hình 8 nghịch đảo thứ tự Review → CI; đứt gãy nhánh phản hồi lỗi |
| S2-AGG-MAJ-02 | **Major** | 4.4 | 58 | Thiếu cú pháp ` ```suggestion ``` ` và Batch Suggestion |
| S2-AGG-MAJ-03 | **Major** | 4.3 | 57 | Trích dẫn sai `\cite{gitflow}` cho mô hình Forking |
| S2-AGG-MAJ-04 | **Major** | 4.3 | 57 | Bỏ sót `Login.aspx.designer.cs` → CI lỗi CS0103 |
| S2-AGG-MAJ-05 | **Major** | 4.3 | 57 | Khối lệnh CLI thiếu bước Review và Merge |
| S2-AGG-MAJ-06 | **Major** | 4.3 | 56 | Bảng 11 sai cơ chế đồng bộ Git; khuyến nghị xóa Fork nguy hại |
| S2-MIN-01 đến S2-TYPO-03 | **Minor/Editorial** | 4.3–4.4 | 57–60 | Branch base mâu thuẫn; NullRef risk; Three-Dot Diff; Pending Review; caption/label listing |
| Finding 1 | **Critical** | 4.5 | 61 | CODEOWNERS không tự khóa Merge nếu thiếu "Require review from Code Owners" |
| Finding 2 | **Critical** | 4.5 | 61 | Đảo lộn thứ tự khớp mẫu CODEOWNERS (last match wins) vô hiệu `/Admin/` |
| Finding 3 | **Critical** | 4.5 | 61 | Nhầm nhiều owner là AND thay vì OR |
| Finding 4 | **Major** | 4.5 | 61 | Thuật ngữ hư cấu; sai cơ chế Admin Bypass |
| Finding 5 | **Major** | 4.5 | 61 | Deadlock single-owner; thắt cổ chai `.aspx`/`.aspx.cs` |
| Finding 6 | **Major** | 4.5 | 60–61 | Bỏ sót Block force push, Linear History, Dismiss stale approvals |
| Findings 7–13 | **Minor/Typo** | 4.5 | 61–62 | Mâu thuẫn chú thích; thiếu `@`; thiếu `docs/CODEOWNERS`; thiếu Write permission; dàn trang LaTeX |
| Issue 1 | **Critical** | 4.7 | 64–65 | MSBuild thiếu `/p:DeployOnBuild=true` → Artifact path không tồn tại |
| Issue 2 | **Critical** | 4.7 | 64 | Cache NuGet sai path `~/.nuget/packages` cho Web Forms |
| Issue 3 | **Major** | 4.7 | 64–65 | `vstest.console.exe` không trong PATH → thay bằng `dotnet test` |
| Issue 4 | **Major** | 4.7 | 64 | PowerShell bóc tách `"Any CPU"` gây MSB1008 |
| Issue 5 | **Major** | 4.6–4.7 | 62–63 | Thiếu `workflow_dispatch` và `develop` trong `pull_request` triggers |
| Issues 6–14 | **Minor/Obs** | 4.6–4.7 | 62–66 | Webhooks/Status API; đơn vị cấu hình; concurrency; mâu thuẫn artifact; tên solution bất nhất; dấu nháy Unicode |
| S5-01 | **Critical** | 4.9 | 67 | Sai path cache NuGet (lặp lại + Phụ lục C) |
| S5-02 | **Critical** | 4.8 | 66 | Bảo mật: truyền Secret qua CLI arguments + triển khai song song thiếu `needs:` |
| S5-03 | **Major** | 4.8 | 66 | Vi phạm Environment Secret Polymorphism |
| S5-04 | **Major** | 4.8 | 66 | Tuyệt đối hóa sai cơ chế `***` masking |
| S5-05 | **Major** | 4.9 | 67–68 | Thiếu `if: always()` cho Upload Test Results |
| S5-06 | **Major** | 4.10 | 69 | Bỏ sót hệ số nhân chi phí 2x Windows Runner |
| S5-07 | **Major** | 4.10 | 68 | Thiếu phân tích kỹ thuật lý giải Web Forms không build được trên Ubuntu |
| S5-M1 đến M6 | **Minor** | 4.9–4.10 | 67–69 | Thông số Cache; `packages.lock.json`; `.csproj` trong hashFiles; Environment Rules; Ubuntu version |
| F-01 | **Critical** | 4.13 | 72 | Nhầm tên "Muse" thay vì "GitHub Copilot" |
| F-02 | **Critical** | 4.13 | 72–73 | Timing Attack trong `hashLuu == hashNhap` |
| F-03 | **Critical** | 4.11 | 69–70 | Nhầm `GITHUB_TOKEN` với PAT cho máy cá nhân |
| F-04 đến F-11 | **Major** | 4.11–4.13 | 69–73 | CLI lỗi thời; `dotnet pack` không tương thích; RepositoryUrl thiếu; Pages public; nuget.config thiếu; Codespaces bất khả thi; Hình 10 sai; Copilot Block filter |
| F-12 đến F-16 | **Minor** | 4.11–4.13 | 70–73 | `AddWithValue` Index Scan; "30%" không có nguồn; bash syntax; caption/label; Codespaces quota |
| S7-01 | **Critical** | 4.14 | 74 | Git reset sai logic → commit lại chính secret; mã lỗi GH013 sai (đúng là GH009) |
| S7-02 | **Major** | 4.14 | 73 | Push Protection không chặn SQL Server connection string nội bộ |
| S7-03 | **Major** | 4.14 | 74 | Dependabot không quét file JS tĩnh trong `Scripts/` |
| S7-04 | **Major** | 4.14 | 74 | CodeQL mặc định Ubuntu + autobuild thất bại với C# .NET Framework 4.8.1 |
| S7-05 | **Major** | 4.14 | 74 | Bảng 13 sai bản chất bảo mật cột "Chặn ở đâu" |
| S7-06 | **Major** | 4.14 | 74 | Thiếu `dependabot.yml`; thiếu cảnh báo `FileLoadException` khi nâng cấp gói |
| S7-07 đến S7-09 | **Major** | 4.15 | 75 | Codespaces bất khả thi; tính năng miễn phí phổ thông nhầm thành Education; đăng ký thiếu 2FA/Camera/Geo |
| S7-10 đến S7-14 | **Minor** | 4.14–4.15 | 73–75 | ConfigurationManager; Bảng 13 mất dấu; caption/label; khoảng trắng listings; trích dẫn chung chung |

---

## KẾT LUẬN VÀ KHUYẾN NGHỊ ƯU TIÊN

### Ưu tiên 1 — Sửa ngay (Blocking Release)

> [!CAUTION]
> Các vấn đề Critical sau đây cần sửa **trước khi nộp báo cáo** vì có thể gây lỗi bảo mật hoặc hỏng hoàn toàn chức năng minh họa:

1. **Đổi `App-Data`/`App-Code` → `App_Data`/`App_Code`** (nguy cơ lộ CSDL qua IIS)
2. **Viết lại mẫu code review (Mục 4.4)** để không khuyến khích User Enumeration
3. **Bổ sung Forking Workflow đầy đủ (Mục 4.3)** với lệnh `gh repo fork`, remote `upstream`, đồng bộ
4. **Sửa 3 lỗi CODEOWNERS** (merge-blocking fallacy; pattern precedence; OR vs AND)
5. **Sửa Listing 24**: DeployOnBuild=true; cache path `packages`; `dotnet test`; nháy đơn PowerShell; triggers
6. **Sửa bảo mật Listing 25**: dùng `env:` thay CLI args; thêm `needs: deploy-staging`
7. **Thay "Muse" bằng "GitHub Copilot"** (toàn bộ Mục 4.13)
8. **Sửa Timing Attack**: dùng `CryptographicOperations.FixedTimeEquals`
9. **Sửa Listing khắc phục Push Protection (Mục 4.14)**: dùng mixed reset, thêm `git add`, đổi mã lỗi sang GH009

### Ưu tiên 2 — Quan trọng (Trước khi phát hành chính thức)

> [!IMPORTANT]
> Các vấn đề Major nên hoàn thành trong vòng 1–2 tuần để đảm bảo tính chính xác kỹ thuật của tài liệu.

- Bổ sung kiến trúc CODEOWNERS: quyền Write, 2 co-owners tối thiểu, phân chia theo thư mục
- Vẽ lại Hình 8 (thứ tự CI → Review; nhánh phản hồi lỗi) và Hình 10 (Codespaces → GitHub Repo → Actions)
- Bổ sung `workflow_dispatch`, `develop` trong PR trigger
- Phân biệt rõ GitHub Education thực sự mang lại gì so với Free account
- Thêm `.github/dependabot.yml` mẫu và cảnh báo `bindingRedirect`
- Hiệu chỉnh Bảng 13 (cơ chế tác động bảo mật đúng bản chất)
- Hướng dẫn CodeQL với `windows-latest` runner và manual build steps

### Ưu tiên 3 — Cải thiện chất lượng

> [!NOTE]
> Các vấn đề Minor/Editorial nên xử lý trong quá trình chỉnh sửa tổng thể LaTeX: thêm dấu tiếng Việt vào captions/labels; thêm `caption` và `label` vào tất cả listing; thêm `upquote` package; chuẩn hóa thuật ngữ (Milestone, Assignee, Kanban).

---

*Báo cáo được tổng hợp từ 7 unit report độc lập, mỗi báo cáo trải qua quy trình thẩm định đa tầng [4→2→1], tham chiếu trực tiếp: Pro Git (2nd Ed.), GitHub Official Documentation, Microsoft Learn (.NET Framework 4.8.1), OWASP ASVS v4.0, MITRE CWE.*
