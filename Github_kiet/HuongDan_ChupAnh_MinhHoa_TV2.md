# HƯỚNG DẪN CHỤP VÀ THAY THẾ ẢNH MINH HỌA THÀNH VIÊN 2 (TV2 — GITHUB & CI/CD)

> **Dành cho:** Thành viên 2 (Kiệt) — Phụ trách nội dung GitHub, GitHub Actions và Slide Beamer.  
> **Áp dụng cho:** Báo cáo LaTeX ([main.pdf](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/BaoCao_LaTeX/main.pdf)) và Slide thuyết trình ([slide.pdf](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Slide_LaTeX/slide.pdf)).  
> **Thư mục lưu trữ ảnh:** [HinhAnh/tv2_screenshots/](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/HinhAnh/tv2_screenshots/)

---

## I. CƠ CHẾ HOẠT ĐỘNG VÀ QUY TẮC THAY ẢNH

1. **Đã có sẵn 12 ảnh giữ chỗ (Placeholder):**
   - Hệ thống đã chèn sẵn 12 khung ảnh minh họa vào đúng vị trí các chương mục trong Báo cáo LaTeX (Chương 4) và các frame của Slide Beamer (Phần 4 & Phần 5).
   - Hiện tại tài liệu đã biên dịch sẵn và hiển thị khung viền kỹ thuật màu xanh chứa hướng dẫn.
2. **Quy trình thay ảnh thật cực kỳ đơn giản (3 bước):**
   - **Bước 1:** Chụp ảnh màn hình thật theo hướng dẫn chi tiết từng mục dưới đây.
   - **Bước 2:** Lưu ảnh với **đúng tên tệp** được quy định và chép đè vào thư mục:
     `T:\HK1_26_27\Lap_trinh_aspx\TuHoc_ASPX\HinhAnh\tv2_screenshots\`
   - **Bước 3:** Chạy lệnh cập nhật và biên dịch lại (xem mục IV cuối file) để PDF tự động nhận ảnh thật mà **không cần chỉnh sửa bất kỳ dòng mã LaTeX nào**.
3. **Tiêu chuẩn ảnh chụp đẹp:**
   - **Định dạng:** PNG (`.png`).
   - **Tỉ lệ khuyến nghị:** 16:9 (Độ phân giải $1920 \times 1080$ hoặc $1280 \times 720$).
   - **Gợi ý thao tác:** Nhấn `F11` trên trình duyệt để ẩn thanh dấu trang/tiêu đề thừa; dùng công cụ `Snipping Tool` (phím tắt `Windows + Shift + S`) để quét chọn vùng ảnh rõ nét.

---

## II. BẢNG TỔNG HỢP 12 ẢNH MINH HỌA TV2

| STT | Tên tệp ảnh (`.png`) | Tiêu đề hình minh họa | Xuất hiện trong Báo cáo | Xuất hiện trong Slide |
| :---: | :--- | :--- | :---: | :---: |
| **1** | `hinh4-1-kanban-project.png` | Bảng Kanban GitHub Projects quản lý đồ án ASPX | Hình 4.1 (Mục 4.2) | Slide Phần 4 |
| **2** | `hinh4-2-issues-chitiet.png` | Giao diện chi tiết GitHub Issues theo dõi lỗi | Hình 4.2 (Mục 4.2) | Báo cáo chi tiết |
| **3** | `hinh4-3-pull-request-diff.png` | Giao diện Pull Request và so sánh mã nguồn (diff) | Hình 4.4 (Mục 4.3) | Slide Phần 4 |
| **4** | `hinh4-4-inline-code-review.png` | Code Review dòng-từng-dòng & Inline Suggestion | Hình 4.5 (Mục 4.4) | Báo cáo chi tiết |
| **5** | `hinh4-5-repository-rulesets.png` | Cấu hình Repository Rulesets bảo vệ nhánh | Hình 4.6 (Mục 4.5) | Slide Phần 4 |
| **6** | `hinh4-6-actions-pipeline-green.png` | Pipeline GitHub Actions chạy xanh 100% | Hình 4.7 (Mục 4.7) | Slide Phần 5 |
| **7** | `hinh4-7-actions-build-artifact.png` | Gói Build Artifact sẵn sàng tải về triển khai | Hình 4.9 (Mục 4.7/4.9)| Slide Phần 5 |
| **8** | `hinh4-8-secrets-variables.png` | Cấu hình Secrets và biến môi trường bảo mật | Hình 4.8 (Mục 4.8) | Slide Phần 5 |
| **9** | `hinh4-9-actions-nuget-cache.png` | Tab Caches lưu trữ bộ nhớ đệm gói NuGet | Hình 4.10 (Mục 4.9) | Báo cáo chi tiết |
| **10**| `hinh4-10-copilot-suggestion.png` | Trợ lý AI GitHub Copilot gợi ý mã C# Web Forms | Hình 4.11 (Mục 4.13)| Báo cáo chi tiết |
| **11**| `hinh4-11-push-protection-block.png` | Secret Scanning Push Protection (GH009) chặn push | Hình 4.12 (Mục 4.14)| Slide Phần 5 |
| **12**| `hinh4-12-security-overview.png` | Bảng điều khiển an ninh GitHub Security Suite | Hình 4.13 (Mục 4.14)| Báo cáo chi tiết |

---

## III. HƯỚNG DẪN CHI TIẾT CÁCH THAO TÁC & CHỤP TỪNG ẢNH

### 1. `hinh4-1-kanban-project.png` — Bảng Kanban GitHub Projects
* **Mục đích:** Chứng minh nhóm có tổ chức quản lý dự án khoa học bằng công cụ chính thống của GitHub.
* **Cách thực hiện:**
  1. Truy cập vào GitHub, mở tab **Projects** của tài khoản hoặc tổ chức $\rightarrow$ Tạo hoặc mở Project dạng **Board**.
  2. Tạo 4 cột: `Todo`, `In Progress`, `Done` (hoặc `Under Review`).
  3. Tạo 4–5 thẻ mô phỏng công việc đồ án:
     - `feat(auth): Xây dựng giao diện Login.aspx` (cột Done).
     - `feat(home): Tạo trang Default.aspx và Master Page` (cột Done).
     - `ci(actions): Thiết lập workflow build MSBuild 4.8.1` (cột Done / In Progress).
     - `test(webconfig): Kiểm thử chuỗi kết nối SQL Server` (cột Todo).
* **Vùng chụp:** Toàn bộ bảng Kanban với các thẻ công việc rõ ràng.

---

### 2. `hinh4-2-issues-chitiet.png` — Giao diện chi tiết GitHub Issues
* **Mục đích:** Minh họa quy trình tiếp nhận và quản lý lỗi/tính năng gắn với đồ án ASPX.
* **Cách thực hiện:**
  1. Trong repo GitHub, vào tab **Issues** $\rightarrow$ Bấm mở một Issue cụ thể (ví dụ Issue `#12: fix(auth): Lỗi bỏ trống mật khẩu trên trang Login.aspx`).
  2. Trong nội dung Issue: Ghi mô tả lỗi ngắn gọn, các bước tái hiện lỗi (Steps to Reproduce) và hành vi mong muốn.
  3. Thanh bên phải (Sidebar): Gán **Assignees** (tài khoản TV2), **Labels** (gắn nhãn `bug`, `enhancement`), **Projects** và **Milestone** (ví dụ `Sprint 1 - Nộp bài`).
* **Vùng chụp:** Khu vực tiêu đề, nội dung thảo luận và thanh thông tin sidebar bên phải.

---

### 3. `hinh4-3-pull-request-diff.png` — Giao diện Pull Request và Diff mã nguồn
* **Mục đích:** Minh họa tính năng so sánh khác biệt mã nguồn (diff) trước khi hợp nhất.
* **Cách thực hiện:**
  1. Mở một Pull Request từ nhánh tính năng (ví dụ `feature/dang-nhap`) vào nhánh `main`.
  2. Nhấp vào tab **Files changed**.
  3. Cuộn đến phần code hiển thị sự khác biệt:
     - Dòng màu đỏ: Code cũ bị xóa.
     - Dòng màu xanh: Code mới được thêm vào (ví dụ kiểm tra `string.IsNullOrEmpty` trong `Login.aspx.cs`).
* **Vùng chụp:** Tiêu đề PR (`Pull Request #15`) kèm khung so sánh diff xanh/đỏ rõ ràng.

---

### 4. `hinh4-4-inline-code-review.png` — Code Review dòng-từng-dòng & Suggestion
* **Mục đích:** Thể hiện kỹ năng đánh giá code chuyên nghiệp theo chuẩn OWASP ASVS v4.0.
* **Cách thực hiện:**
  1. Trong tab **Files changed** của PR, rê chuột vào một dòng code $\rightarrow$ Nhấp biểu tượng dấu cộng `+` màu xanh để mở khung bình luận.
  2. Gõ bình luận góp ý và nhấp vào biểu tượng **Add a suggestion** (hoặc gõ khối ```` ```suggestion ````):
     - Gợi ý sửa thông báo lỗi thành: `lblMessage.Text = "Invalid username or password.";`
  3. Nhấn **Start a review** hoặc **Add review comment** để khối suggestion hiển thị nút *Commit suggestion*.
* **Vùng chụp:** Khung bình luận có chứa diff gợi ý thay đổi trực tiếp (Inline Suggestion).

---

### 5. `hinh4-5-repository-rulesets.png` — Cấu hình Repository Rulesets bảo vệ nhánh
* **Mục đích:** Minh họa cấu hình bảo vệ nhánh hiện đại nhất 2026 của GitHub (thay thế Classic Branch Protection).
* **Cách thực hiện:**
  1. Vào **Settings** của repository $\rightarrow$ Menu bên trái chọn **Rules** $\rightarrow$ **Rulesets**.
  2. Tạo hoặc mở một Ruleset bảo vệ nhánh `main` (ví dụ đặt tên: `Protect Production Main`).
  3. Đảm bảo hiển thị các tùy chọn đã bật:
     - [x] *Enforcement status: Active*
     - [x] *Restrict creations* & *Restrict updates*
     - [x] *Block force pushes* & *Block deletions*
     - [x] *Require a pull request before merging* (Required approvals: 1)
     - [x] *Require status checks to pass* (chọn check `CI ASPX 4.8.1`).
* **Vùng chụp:** Trang cấu hình Ruleset hiển thị rõ các quy tắc đã được tích chọn.

---

### 6. `hinh4-6-actions-pipeline-green.png` — Pipeline GitHub Actions chạy xanh 100%
* **Mục đích:** Minh chứng kỹ thuật quan trọng nhất của TV2 — pipeline build tự động ASP.NET 4.8.1 thành công.
* **Cách thực hiện:**
  1. Vào tab **Actions** của repo $\rightarrow$ Nhấp vào một lần chạy workflow gần nhất của `CI ASPX 4.8.1`.
  2. Mở chi tiết job `build` chạy trên `windows-latest`.
  3. Mở rộng các step để thấy dấu **tích xanh tròn (Success)** ở mọi bước:
     - `actions/checkout@v4`
     - `Setup MSBuild`
     - `Setup NuGet`
     - `Cache NuGet packages`
     - `Restore packages`
     - `Build solution (MSBuild Release)`
     - `Run tests (dotnet test)`
     - `Upload web package artifact`
* **Vùng chụp:** Cây danh sách các step đều có biểu tượng tích xanh và thời gian thực thi (dưới 1–2 phút).

---

### 7. `hinh4-7-actions-build-artifact.png` — Gói Build Artifact sẵn sàng tải về
* **Mục đích:** Chứng minh pipeline không chỉ biên dịch kiểm tra mà còn đóng gói thành phẩm web triển khai.
* **Cách thực hiện:**
  1. Trong trang tóm tắt (Summary) của lượt chạy GitHub Actions vừa thành công ở trên.
  2. Cuộn xuống mục **Artifacts** ở dưới cùng.
  3. Hiển thị tệp artifact: `aspx-site-package` (hoặc `aspx-deployable-package.zip`), kèm dung lượng (vài MB) và thời hạn lưu giữ (7 days).
* **Vùng chụp:** Khu vực bảng **Artifacts** với link tải tệp zip sản phẩm.

---

### 8. `hinh4-8-secrets-variables.png` — Cấu hình Secrets bảo mật
* **Mục đích:** Chứng minh nhóm không lưu mật khẩu trong code mà dùng biến môi trường bảo mật của GitHub.
* **Cách thực hiện:**
  1. Vào **Settings** của repo $\rightarrow$ Menu trái chọn **Secrets and variables** $\rightarrow$ **Actions**.
  2. Trong thẻ **Repository secrets**, hiển thị danh sách các khóa đã tạo:
     - `DB_CONNECTION_STRING` (cập nhật gần nhất, giá trị đã được mã hóa).
     - `STAGING_IIS_SERVER_IP` (nếu có).
  3. Lưu ý: GitHub tự động ẩn giá trị bí mật, chỉ hiện tên biến và ngày cập nhật.
* **Vùng chụp:** Bảng danh sách Repository Secrets hiển thị tên biến `DB_CONNECTION_STRING`.

---

### 9. `hinh4-9-actions-nuget-cache.png` — Tab Caches lưu trữ bộ nhớ đệm NuGet
* **Mục đích:** Thể hiện kỹ thuật tối ưu tốc độ và hạn ngạch (quota) máy ảo Windows runner.
* **Cách thực hiện:**
  1. Vào tab **Actions** $\rightarrow$ Thanh bên trái chọn **Management** $\rightarrow$ **Caches**.
  2. Hiển thị mục cache đã tạo có khóa bắt đầu bằng: `nuget-Windows-...` kèm dung lượng và thời gian truy xuất gần nhất (Last accessed).
* **Vùng chụp:** Bảng Caches hiển thị khóa cache NuGet và dung lượng lưu trữ.

---

### 10. `hinh4-10-copilot-suggestion.png` — Trợ lý GitHub Copilot hỗ trợ lập trình
* **Mục đích:** Minh họa ứng dụng AI hỗ trợ sinh mã C# an toàn chống Timing Attack (`FixedTimeEquals`).
* **Cách thực hiện:**
  1. Mở Visual Studio 2022 hoặc VS Code với tiện ích mở rộng GitHub Copilot đã đăng nhập.
  2. Gõ dòng chú thích:
     `// Check login for page Login.aspx (production-ready constant-time comparison)`
  3. Để Copilot hiển thị gợi ý code mờ (Ghost text) chứa phương thức `CryptographicOperations.FixedTimeEquals` hoặc các thẻ ASPX Web Forms.
* **Vùng chụp:** Cửa sổ code editor hiển thị dòng gợi ý mờ của Copilot.

---

### 11. `hinh4-11-push-protection-block.png` — Secret Scanning Push Protection (GH009)
* **Mục đích:** Minh họa tình huống thực tế khi một thành viên vô tình push connection string thật và bị GitHub chặn ngay từ cửa.
* **Cách thực hiện:**
  1. Trên máy cá nhân, tạo một commit có chứa chuỗi kết nối SQL Server thật (hoặc một token PAT mẫu).
  2. Chạy `git push origin feature/test-secret`.
  3. Màn hình Git Bash / PowerShell sẽ xuất hiện thông báo lỗi màu đỏ chính thức:
     ```text
     remote: error: GH009: Secrets detected in push:
     remote:  - Azure Storage Account Key detected in Web.config:15
     remote: To bypass, visit: https://github.com/.../unblock-secret/...
     To https://github.com/...
      ! [remote rejected] feature/test-secret -> feature/test-secret (push declined)
     ```
* **Vùng chụp:** Màn hình terminal hiển thị rõ thông báo lỗi `GH009: Secrets detected in push`.

---

### 12. `hinh4-12-security-overview.png` — Bảng điều khiển an ninh GitHub Security
* **Mục đích:** Thể hiện cái nhìn tổng quan về hệ thống phòng thủ 3 lớp (Secret Scanning, Dependabot, CodeQL).
* **Cách thực hiện:**
  1. Trong repository GitHub, chọn tab **Security** trên thanh điều hướng.
  2. Hiển thị bảng tổng quan Security overview:
     - **Vulnerability alerts** (Dependabot: 0 open alerts hoặc danh sách đã vá).
     - **Secret scanning** (Push protection: Enabled).
     - **Code scanning** (CodeQL: configured / passing).
* **Vùng chụp:** Bảng tổng quan Security Overview hiển thị trạng thái bảo mật của toàn bộ repo.

---

## IV. LỆNH ĐỒNG BỘ VÀ BIÊN DỊCH LẠI SAU KHI THAY ẢNH

Sau khi bạn đã chụp xong các ảnh và lưu vào thư mục `HinhAnh/tv2_screenshots/`, hãy mở PowerShell tại thư mục gốc `TuHoc_ASPX` và chạy lệnh sau để tự động đồng bộ ảnh và biên dịch lại Báo cáo + Slide:

```powershell
# 1. Đồng bộ ảnh sang các thư mục con phục vụ biên dịch
Copy-Item -Path "HinhAnh\tv2_screenshots\*" -Destination "BaoCao_LaTeX\HinhAnh\tv2_screenshots\" -Force
Copy-Item -Path "HinhAnh\tv2_screenshots\*" -Destination "Slide_LaTeX\HinhAnh\tv2_screenshots\" -Force

# 2. Biên dịch lại Báo cáo LaTeX (main.pdf)
cd BaoCao_LaTeX
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
cd ..

# 3. Biên dịch lại Slide Beamer (slide.pdf)
cd Slide_LaTeX
pdflatex -interaction=nonstopmode slide.tex
cd ..

Write-Host "Hoàn tất! main.pdf và slide.pdf đã được cập nhật với ảnh thật của bạn." -ForegroundColor Green
```

---

> [!TIP]
> Bạn không bắt buộc phải chụp đủ cả 12 ảnh cùng một lúc! Bạn có thể chụp trước 3–4 ảnh quan trọng nhất (như `hinh4-1`, `hinh4-5`, `hinh4-6`), chép đè vào thư mục rồi biên dịch thử. Các vị trí chưa có ảnh thật sẽ tiếp tục hiển thị khung giữ chỗ kỹ thuật rất ngay ngắn và chuyên nghiệp.
