# BÁO CÁO THẨM ĐỊNH VÀ SO SÁNH KỸ THUẬT LẦN 2 (ROUND 2 TECHNICAL AUDIT)
## CẬP NHẬT KIẾN THỨC CHUẨN MỚI NHẤT (2024–2026) CHO CHƯƠNG 4 BÁO CÁO HỌC PHẦN ASPX

- **Đối tượng thẩm định**: Chương 4 — *GitHub trong Quản trị Dự án và CI/CD cho Ứng dụng ASPX* trong [main.pdf](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/BaoCao_LaTeX/main.pdf) (Trang 55–75).
- **Cơ sở đối chiếu**:
  1. Nguyên tác kinh điển: [progit.pdf](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/progit.pdf) (*Pro Git, 2nd Edition* — Scott Chacon & Ben Straub).
  2. Hệ thống tài liệu kỹ thuật chuẩn mới nhất (2024–2026) được tải về cục bộ tại: [tai_lieu_chuan_2026/](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/tai_lieu_chuan_2026/).
     - **GitHub Official Docs (2024–2026)**: Workflow Syntax, Dependency Caching v4, Environments & Deployments, Repository Rulesets, CODEOWNERS Syntax, Push Protection on Command Line.
     - **Microsoft Learn**: ASP.NET Web Forms Folder Architecture (`App_Data`/`App_Code`), MSBuild Web Publishing Pipeline (WPP), NuGet `packages.config` vs `PackageReference`.
     - **OWASP ASVS v4.0**: Chuẩn an ninh xác thực người dùng (CWE-204) và so sánh mã băm mật khẩu thời gian không đổi (CWE-208).
- **Thời gian hoàn thành**: 15/11/2026.

---

## I. TỔNG HỢP NGUỒN TÀI LIỆU CHUẨN ĐÃ TẢI VỀ CỤC BỘ

Toàn bộ 18 tệp tài liệu kỹ thuật mới nhất đã được tải về và lưu trữ độc lập tại thư mục `Github_kiet/tai_lieu_chuan_2026/`:

| Tên tệp tài liệu | Dung lượng | Cơ quan / Nguồn xuất bản | Phạm vi áp dụng đối chiếu |
| :--- | :---: | :--- | :--- |
| `progit-ch06-1-setting-up-account.asc` | 5.3 KB | Pro Git Official Repo | Thiết lập tài khoản, khóa SSH, xác thực cá nhân |
| `progit-ch06-2-contributing.asc` | 28.3 KB | Pro Git Official Repo | Forking Projects, GitHub Flow, Pull Requests, Markdown |
| `progit-ch06-3-maintaining.asc` | 21.8 KB | Pro Git Official Repo | Quản lý repo, Collaborators, Mentions, Labels |
| `progit-ch06-4-managing-organization.asc` | 4.4 KB | Pro Git Official Repo | Quản lý tổ chức và phân quyền nhóm |
| `progit-ch06-5-scripting.asc` | 14.1 KB | Pro Git Official Repo | Webhooks và Statuses API (tiền thân Checks/Actions) |
| `progit-ch05-distributed-workflows.asc` | 6.8 KB | Pro Git Official Repo | Mô hình phân tán: Integration-Manager Workflow |
| `progit-ch07-reset.asc` | 17.2 KB | Pro Git Official Repo | Cơ chế Reset Demystified (Three Trees: HEAD, Index, WorkDir) |
| `github-about-code-owners.md` | 12.7 KB | GitHub Docs (Official) | Cú pháp CODEOWNERS: Last-match-wins, quan hệ OR |
| `github-about-rulesets.md` | 6.2 KB | GitHub Docs (Official) | Repository Rulesets hiện đại thay thế Classic Branch Protection |
| `github-actions-workflow-syntax.md` | 79.5 KB | GitHub Docs (Official) | Cú pháp YAML Actions, triggers, concurrency, permissions |
| `github-actions-dependency-caching.md` | 29.5 KB | GitHub Docs (Official) | Chiến lược Cache v4, path scoping, cache miss keys |
| `github-actions-deployments-environments.md` | 9.0 KB | GitHub Docs (Official) | Quản lý Secrets, Environments, Deployment Protection Rules |
| `github-actions-events-triggers.md` | 68.0 KB | GitHub Docs (Official) | Sự kiện kích hoạt workflow: push, pull_request, workflow_dispatch |
| `github-push-protection-on-the-command-line.md` | 5.9 KB | GitHub Docs (Official) | Cơ chế Push Protection, mã lỗi GH009, lệnh commit amend/rebase |
| `github-push-protection-in-the-github-ui.md` | 5.3 KB | GitHub Docs (Official) | Quy trình bypass hợp lệ trên giao diện web |
| `microsoft-learn-webforms-msbuild-nuget.md` | 6.6 KB | Microsoft Learn | Kiến trúc `App_Data`, MSBuild WPP cờ DeployOnBuild, NuGet cache |
| `owasp-asvs-v4-authentication.md` | 30.5 KB | OWASP Foundation | Chuẩn bảo mật thông báo đăng nhập chống User Enumeration |
| `owasp-asvs-v4-cryptography.md` | 6.0 KB | OWASP Foundation | So sánh mật khẩu thời gian không đổi FixedTimeEquals |

---

## II. CÁC NÂNG CẤP VÀ PHÁT HIỆN KỸ THUẬT MỚI TRONG SO SÁNH LẦN 2

Qua việc đối chiếu sâu với bộ tài liệu chuẩn mới nhất 2024–2026, các vấn đề kỹ thuật trong Chương 4 của `main.pdf` được làm rõ với bằng chứng xác thực và giải pháp chuẩn xác nhất:

### 1. Phân định Branch Protection cổ điển và Repository Rulesets hiện đại (Mục 4.5)
- **Tài liệu đối chiếu**: [github-about-rulesets.md](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/tai_lieu_chuan_2026/github-about-rulesets.md) & [github-about-code-owners.md](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/tai_lieu_chuan_2026/github-about-code-owners.md).
- **Phân tích chuẩn mới nhất**:
  - `main.pdf` mô tả Branch Protection thuần túy theo giao diện cũ (Classic Branch Protection).
  - GitHub hiện đại đã nâng cấp lên **Repository Rulesets**:
    + Cho phép áp dụng một bộ quy tắc cho **nhiều nhánh cùng lúc** bằng fnmatch pattern (ví dụ: `refs/heads/main`, `refs/heads/release/*`).
    + Quản trị quyền bỏ qua quy tắc (Bypass list) theo **Role (Repository Admin), Team hoặc Deploy Key**, thay vì phụ thuộc vào một nút checkbox "Include administrators" dễ gây hiểu lầm.
    + Hỗ trợ chế độ **Evaluate Mode**: Cho phép chạy thử nghiệm quy tắc để kiểm tra tác động mà không chặn đứng công việc của nhóm.
- **Xác thực 2 lỗi CODEOWNERS**:
  1. *Quy tắc thứ tự khớp mẫu (Precedence)*: Trích dẫn nguyên văn chuẩn GitHub Docs: `"Order is important; the last matching pattern takes the most precedence"`. File CODEOWNERS trong `main.pdf` đặt wildcard `*.aspx` sau `/Admin/` khiến quy tắc `/Admin/` bị ghi đè và vô hiệu hóa hoàn toàn.
  2. *Cơ chế nhiều chủ sở hữu*: Trích dẫn nguyên văn chuẩn GitHub Docs: `"...changes to JavaScript files could be approved by either @global-owner1 OR @global-owner2"`. Khẳng định rằng danh sách nhiều người trên 1 dòng là quan hệ **HOẶC (OR)**; không bao giờ là quan hệ VÀ (AND).

---

### 2. Chuẩn mực khắc phục Secret Scanning Push Protection (Mục 4.14)
- **Tài liệu đối chiếu**: [github-push-protection-on-the-command-line.md](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/tai_lieu_chuan_2026/github-push-protection-on-the-command-line.md) & [progit-ch07-reset.asc](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/tai_lieu_chuan_2026/progit-ch07-reset.asc).
- **Sai phạm trong main.pdf**:
  - `main.pdf` ghi: Gặp lỗi `GH013`, chạy `git reset --soft HEAD~1`, sửa file `Web.config`, rồi chạy `git commit -m "..."`.
  - Đây là sai lầm logic nghiêm trọng: `--soft` giữ nguyên Index. Sửa file trong Working Directory mà không `git add` thì Index vẫn giữ nguyên file cũ có chứa secret. Khi `git commit`, Git tạo commit từ Index, tức là **commit lại chính secret đó**.
  - Mã lỗi `GH013` là lỗi từ chối push chung (thường do nhánh bị bảo vệ hoặc thiếu quyền), không phải mã lỗi của Push Protection.
- **Quy trình chuẩn mực chính thức của GitHub (2024–2026)**:
  - Khi Push Protection chặn một secret (chuỗi kết nối SQL Server đối tác, Azure secret, PAT), Git in ra thông báo với mã lỗi **`GH009: Secret scanning detected secrets`** kèm URL để mở giao diện cấp phép bypass nếu cần thiết.
  - Hướng dẫn chuẩn từ GitHub Docs:
    ```bash
    # Bước 1: Loại bỏ chuỗi bí mật khỏi tệp cấu hình
    # Sửa Web.config (thay chuỗi nhạy cảm bằng biến môi trường hoặc chuỗi rỗng)

    # Bước 2: Cập nhật lại commit gần nhất thay vì tạo commit mới
    git commit --amend --all

    # Hoặc thực hiện tuần tự:
    # git add Web.config
    # git commit --amend -m "fix(config): loai bo chuoi ket noi nhay cam"

    # Bước 3: Đẩy lại lên remote an toàn
    git push origin feature/dang-nhap
    ```

---

### 3. Pipeline CI/CD cho ASP.NET Web Forms 4.8.1 (Mục 4.7 & Phụ lục C)
- **Tài liệu đối chiếu**: [microsoft-learn-webforms-msbuild-nuget.md](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/tai_lieu_chuan_2026/microsoft-learn-webforms-msbuild-nuget.md) & [github-actions-workflow-syntax.md](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/tai_lieu_chuan_2026/github-actions-workflow-syntax.md).
- **Các điểm cốt tử được hiệu chỉnh**:
  1. **DeployOnBuild**: Bắt buộc thêm các cờ Web Publishing Pipeline vào lệnh MSBuild:
     ```yaml
     - name: Build and Package Web Application
       run: |
         msbuild AspxDemo_NET481.sln /p:Configuration=Release `
           '/p:Platform="Any CPU"' `
           /p:DeployOnBuild=true `
           /p:WebPublishMethod=FileSystem `
           /p:PublishUrl="${{ github.workspace }}\PublishOutput" `
           /p:DeleteExistingFiles=True
     ```
  2. **Cache NuGet**: Thay thế hoàn toàn cấu hình sai `~/.nuget/packages` bằng:
     ```yaml
     - name: Cache NuGet packages
       uses: actions/cache@v4
       with:
         path: packages
         key: nuget-${{ runner.os }}-${{ hashFiles('**/packages.config') }}
         restore-keys: |
           nuget-${{ runner.os }}-
     ```
  3. **Artifact Upload**: Sử dụng `actions/upload-artifact@v4` trỏ thẳng vào thư mục `${{ github.workspace }}\PublishOutput` đã được WPP xuất ra.
  4. **Kiểm thử đơn vị**: Dùng lệnh `dotnet test` trực tiếp trên assembly release thay vì gọi `vstest.console.exe` không tồn tại trong biến môi trường PATH.

---

### 4. An ninh ứng dụng theo chuẩn OWASP ASVS v4.0 (Mục 4.4 & Mục 4.13)
- **Tài liệu đối chiếu**: [owasp-asvs-v4-authentication.md](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/tai_lieu_chuan_2026/owasp-asvs-v4-authentication.md) & [owasp-asvs-v4-cryptography.md](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/tai_lieu_chuan_2026/owasp-asvs-v4-cryptography.md).
- **Chuẩn hóa lỗi User Enumeration (Mục 4.4)**:
  - Mẫu nhận xét code review trong `main.pdf` hướng dẫn: *"thông báo lỗi nên phân biệt rõ tên đăng nhập sai hay mật khẩu sai trong môi trường học tập"*.
  - *Kết luận thẩm định lần 2*: Vi phạm trực tiếp OWASP ASVS V2.2 & MITRE CWE-204 (Observable Response Discrepancy). Hệ thống bắt buộc phải trả về thông báo lỗi chung: `"Invalid username or password."` (Tên đăng nhập hoặc mật khẩu không chính xác). Mọi chi tiết phân biệt phải được ghi vào log bảo mật máy chủ, không được gửi về giao diện client.
- **Chuẩn hóa lỗi Timing Attack (Mục 4.13)**:
  - Đoạn mã so sánh chuỗi băm trong `main.pdf`: `return hashLuu == hashNhap;`.
  - *Kết luận thẩm định lần 2*: Toán tử so sánh chuỗi `==` trong .NET có tính chất "ngắt sớm" (short-circuit execution) ngay khi gặp ký tự khác biệt đầu tiên. Kẻ tấn công có thể đo độ trễ nano-giây để suy đoán từng byte mã băm mật khẩu (MITRE CWE-208).
  - *Giải pháp chuẩn*:
    ```csharp
    using System.Security.Cryptography;

    public static bool KiemTraMatKhau(string hashLuu, string hashNhap)
    {
        byte[] bLuu = Convert.FromBase64String(hashLuu);
        byte[] bNhap = Convert.FromBase64String(hashNhap);
        return CryptographicOperations.FixedTimeEquals(bLuu, bNhap);
    }
    ```

---

### 5. Cập nhật hệ sinh thái AI: Định danh GitHub Copilot (Mục 4.13)
- **Tài liệu đối chiếu**: GitHub Product Catalog & Copilot Enterprise Documentation.
- **Kết luận thẩm định lần 2**:
  - Toàn bộ Mục 4.13 trong `main.pdf` sử dụng tên gọi **"Muse"** (ví dụ: *"Muse là trợ lý lập trình..."*). "Muse" là một tên hoàn toàn không có thực trong danh mục sản phẩm của GitHub.
  - Tên gọi chuẩn mực 100% là **GitHub Copilot**.
  - Bổ sung tính năng kiểm soát bản quyền: **"Suggestions matching public code" (Block)** để ngăn trợ lý AI đề xuất các đoạn mã sao chép y nguyên từ mã nguồn mở dính giấy phép copyleft (GPL v3).

---

## III. MA TRẬN ĐỐI CHIẾU TOÀN DIỆN 3 NGUỒN CHUẨN

Bảng dưới đây cung cấp liên kết đối sánh đồng thời giữa:
1. Vị trí trong báo cáo [main.pdf](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/BaoCao_LaTeX/main.pdf).
2. Số trang chính xác trong [progit.pdf](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/progit.pdf) (cả Trang PDF và Trang in).
3. Tài liệu kỹ thuật chuẩn mới nhất tại [tai_lieu_chuan_2026/](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/tai_lieu_chuan_2026/).

| Mã vấn đề | main.pdf (Trang/Mục) | Pro Git Trang PDF (Trang in) | Tài liệu kỹ thuật mới nhất (2024–2026) | Tóm tắt sai lệch & Hướng xử lý chuẩn |
| :--- | :---: | :---: | :--- | :--- |
| **FIND-S1-01** | Tr.55 (4.1) | *Không áp dụng* | `microsoft-learn-webforms-msbuild-nuget.md` (Mục 1) | Ghi `App-Data`/`App-Code` $\rightarrow$ Đổi thành `App_Data` (IIS chặn) và `App_Code` (biên dịch động). |
| **FIND-S1-02** | Tr.56 (4.2) | **218–223 (212–217)** | `progit-ch06-5-scripting.asc` & Projects v2 Specs | Thẻ Projects ánh xạ 1:1, không phải 1 thẻ chứa nhiều Issue/PR. |
| **FIND-S1-03** | Tr.56 (4.2) | **218–223 (212–217)** | GitHub Docs: Projects v2 Built-in Workflows | Bổ sung Workflow tự động hóa chuyển thẻ và chế độ xem Roadmap/Table. |
| **FIND-S1-04** | Tr.56 (4.2) | **188–190 (182–184)** | `progit-ch06-2-contributing.asc` (References) | Bổ sung từ khóa đóng Issue (`Fixes #ID`) và điều kiện merge vào nhánh mặc định. |
| **FIND-S1-05** | Tr.55–56 (4.1) | **197–199 (191–193)** | `progit-ch06-3-maintaining.asc` | Bổ sung hướng dẫn tạo kho Private và mời Collaborators có quyền Write. |
| **FIND-S1-06** | Tr.55 (4.1) | **173–176 (167–170)** | `progit-ch06-1-setting-up-account.asc` & GitHub PAT Docs | Hướng dẫn PAT Classic thay cho password và cấu hình khóa SSH Ed25519. |
| **FIND-S1-07** | Tr.56 (4.2) | **172 (166)** | GitHub Docs: *About Wikis* | Wiki là kho Git độc lập `.wiki.git`, không hỗ trợ nhánh/PR. |
| **S2-AGG-CRIT-01**| Tr.59 (4.4) | *Không áp dụng* | `owasp-asvs-v4-authentication.md` (CWE-204) | Sửa mẫu review: dùng thông báo lỗi chung chống User Enumeration. |
| **S2-AGG-CRIT-02**| Tr.56–57 (4.3) | **177–181 & 187–188** | `progit-ch06-2-contributing.asc` | Viết lại toàn bộ khối lệnh Forking Workflow (remote kép `origin`/`upstream`). |
| **S2-AGG-MAJ-01** | Tr.57 (4.3) | **178–188 (172–182)** | `progit-ch06-2-contributing.asc` (The GitHub Flow) | Đảo lại Hình 8: CI phải chạy trước Review; vẽ thêm nhánh phản hồi lỗi. |
| **S2-AGG-MAJ-02** | Tr.58 (4.4) | **190–196 (184–190)** | `progit-ch06-2-contributing.asc` (GFM) | Bổ sung cú pháp Suggestion và Batch Suggestion trong review. |
| **S2-AGG-MAJ-03** | Tr.57 (4.3) | **132–135 (126–129)** | `progit-ch05-distributed-workflows.asc` | Đổi trích dẫn `\cite{gitflow}` thành Integration-Manager Workflow trong Pro Git Ch.5. |
| **Finding 1** | Tr.61 (4.5) | *Ra mắt sau 2014* | `github-about-code-owners.md` | Bật tường minh "Require review from Code Owners" trong Branch Protection. |
| **Finding 2** | Tr.61 (4.5) | *Ra mắt sau 2014* | `github-about-code-owners.md` (Order is important) | Sắp xếp lại thứ tự CODEOWNERS: wildcard ở trên, `/Admin/` ở dưới cùng. |
| **Finding 3** | Tr.61 (4.5) | *Ra mắt sau 2014* | `github-about-code-owners.md` (Multiple owners OR) | Nhiều owner là logic OR; muốn 2 người phải đặt Require approvals = 2. |
| **Finding 4–6** | Tr.60–61 (4.5) | *Ra mắt sau 2014* | `github-about-rulesets.md` | Giới thiệu Repository Rulesets, Block force push, Linear History. |
| **Issue 1** | Tr.64–65 (4.7) | *Không áp dụng* | `microsoft-learn-webforms-msbuild-nuget.md` (Mục 2) | Bổ sung `/p:DeployOnBuild=true` để WPP tạo thư mục artifact web. |
| **Issue 2 & S5-01**| Tr.64, 67 (4.7, 4.9)| *Không áp dụng* | `microsoft-learn-webforms-msbuild-nuget.md` (Mục 3) | Sửa path cache NuGet thành `packages` và băm `packages.config`. |
| **Issue 3** | Tr.64–65 (4.7) | *Không áp dụng* | GitHub Actions Runner Images (Windows-latest) | Thay `vstest.console.exe` bằng `dotnet test` sẵn có trong PATH. |
| **Issue 4** | Tr.64 (4.7) | *Không áp dụng* | PowerShell Core Argument Parsing Rules | Bọc nháy đơn đối số `'/p:Platform="Any CPU"'` tránh lỗi MSB1008. |
| **S5-02** | Tr.66 (4.8) | *Không áp dụng* | `github-actions-deployments-environments.md` | Chuyển secret từ đối số dòng lệnh sang khối biến môi trường `env:`. |
| **F-01** | Tr.72 (4.13) | *Không áp dụng* | GitHub Product Catalog | Thay thế toàn bộ định danh hư cấu "Muse" bằng "GitHub Copilot". |
| **F-02** | Tr.72–73 (4.13)| *Không áp dụng* | `owasp-asvs-v4-cryptography.md` (CWE-208) | Sửa phép so sánh băm mật khẩu: dùng `FixedTimeEquals` chống Timing Attack. |
| **F-03** | Tr.69–70 (4.11)| *Không áp dụng* | `github-actions-workflow-syntax.md` | Phân biệt rõ `GITHUB_TOKEN` (trong Actions) và PAT (dùng trên máy local). |
| **S7-01** | Tr.74 (4.14) | **257–266 (251–260)** | `github-push-protection-on-the-command-line.md` | Thay quy trình reset sai bằng `git commit --amend --all`; đổi mã lỗi sang GH009. |
| **S7-04** | Tr.74 (4.14) | *Không áp dụng* | GitHub CodeQL C# Runner Specs | Hướng dẫn CodeQL cho .NET Framework: chạy `windows-latest` + build thủ công. |

---

## IV. KẾT LUẬN VÀ TRẠNG THÁI HIỆN TẠI

1. **Kiến thức chuẩn mới nhất**: Đã được đồng bộ và xác thực bằng tài liệu chính thức từ 3 nguồn uy tín cao nhất (Git SCM, GitHub Docs 2024–2026, Microsoft Learn và OWASP).
2. **Cơ sở dữ liệu tài liệu**: Đầy đủ 18 tệp nguồn tải về tại [tai_lieu_chuan_2026/](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/tai_lieu_chuan_2026/) phục vụ việc bảo vệ đồ án và giải trình hội đồng phản biện.
3. **Mã nguồn báo cáo LaTeX**: Tiếp tục tuân thủ nghiêm ngặt chỉ đạo của bạn — **giữ nguyên vẹn 100% các file `.tex`**, sẵn sàng áp dụng các bản vá ngay khi bạn duyệt.
